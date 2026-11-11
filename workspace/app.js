/* Thinking Workspace — vanilla JS, no build, no deps
 * Data: workspace/boards/<id>.json  (JSON schema in boards/_schema.json)
 * Persistence: localStorage  +  file drop (import/export)
 * Agents: read/write boards/<id>.json directly (or POST via future server)
 */
const LS_PREFIX = "thinking-workspace:board:";
const el = (s) => document.querySelector(s);
const boardEl = el("#board");
const lanesEl = el("#lanes");
const notesLayer = el("#notesLayer");
const canvas = el("#drawCanvas");
const ctx = canvas.getContext("2d");
let drawing = false, drawActive = false, strokes = [];
let drag = null;
let board = null;
let timerInt = null, timerSec = 300, timerRunning = false;

const TEMPLATES = {
  blank: { title: "Blank", lanes: ["Inbox"] },
  "six-hats": { title: "Six Hats", lanes: ["White — facts","Red — feelings","Yellow — benefits","Black — caution","Green — creativity","Blue — synthesis"]},
  brainwriting: { title: "Brainwriting", lanes: ["P1","P2","P3"] },
  scamper: { title: "SCAMPER", lanes: ["S Substitute","C Combine","A Adapt","M Modify","P Put to other use","E Eliminate","R Reverse"]},
  "crazy-eights": { title: "Crazy 8s", lanes: ["1","2","3","4","5","6","7","8"]},
  backcasting: { title: "Backcasting", lanes: ["2030 — future","2028","2027","2026 — today"]},
  "morph-box": { title: "Morph Box", lanes: ["D1 Trigger","D2 Channel","D3 Timing","D4 Owner"]},
  sit: { title: "SIT (5 operators)", lanes: ["S Subtraction","M Multiplication","D Division","T Task Unification","A Attribute Dependency"]},
  "c-k-theory": { title: "C-K Theory", lanes: ["C0 initial concept","C partitions","K pockets","Learning agenda"]},
  bodystorming: { title: "Bodystorming", lanes: ["Before","During","After","Friction clusters"]},
  "rich-picture-catwoe": { title: "Rich Picture + CATWOE", lanes: ["Actors","Flows","Tensions","CATWOE","Root definition"]},
  "causal-loop": { title: "Causal Loop Diagram", lanes: ["Variables","R loops","B loops","Delays","Leverage"]},
  synectics: { title: "Synectics", lanes: ["Personal","Direct","Symbolic","Fantasy","Excursion","Springboards"]},
  "liberating-structures": { title: "Liberating Structures", lanes: ["1-2-4-All","Impromptu Networking","15% Solutions","TRIZ","Wicked Q","Ecocycle"]},
  "nominal-group": { title: "NGT / Delphi", lanes: ["Silent ideas","Round-robin","Clarify","Vote 5-4-3-2-1","Dissent log"]},
  "lotus-blossom": { title: "Lotus Blossom", lanes: ["Centre","P1","P2","P3","P4","P5","P6","P7","P8"]},
  "dot-voting": { title: "Dot Voting + Impact–Effort", lanes: ["Dots N/3","Quick wins","Strategic","Fill-ins","Avoid","Keep/Pivot/Kill"]},
};

const COLORS = { fact: "#ffeb3b", assumption: "#81d4fa", speculation: "#ef9a9a", action: "#c8e6c9", question: "#ffe0b2" };

function uid(){ return Math.random().toString(36).slice(2,8); }
function nowISO(){ return new Date().toISOString(); }

function defaultBoard(id="default"){
  return {
    id,
    title: "Untitled board",
    template: "blank",
    lanes: [{id:"lane-1", title:"Inbox"}],
    notes: [],
    drawings: [],
    createdAt: nowISO(),
    updatedAt: nowISO(),
    schema: "boards/_schema.json"
  };
}

function loadBoard(id){
  const key = LS_PREFIX + id;
  const raw = localStorage.getItem(key);
  if(raw){ try{ return JSON.parse(raw);}catch(e){}}
  return null;
}

async function loadBoardFromFile(id){
  try{
    const r = await fetch(`boards/${encodeURIComponent(id)}.json`, {cache:"no-store"});
    if(r.ok) return await r.json();
  }catch(e){}
  return null;
}

function saveBoard(){
  if(!board) return;
  board.updatedAt = nowISO();
  localStorage.setItem(LS_PREFIX + board.id, JSON.stringify(board));
  // also keep canvas strokes
  board.drawings = strokes;
}

function renderLanes(){
  lanesEl.innerHTML = "";
  el("#noteLane").innerHTML = "";
  board.lanes.forEach(lane=>{
    const div = document.createElement("div");
    div.className = "lane";
    div.dataset.laneId = lane.id;
    const head = document.createElement("div");
    head.className = "laneHead";
    head.innerHTML = `<span>${escapeHtml(lane.title)}</span><button data-add="${lane.id}" title="add note">+ </button>`;
    const body = document.createElement("div");
    body.className = "laneBody";
    body.dataset.laneId = lane.id;
    head.querySelector("button").onclick = ()=> addNote(lane.id);
    div.append(head, body);
    lanesEl.append(div);
    const opt = document.createElement("option");
    opt.value = lane.id; opt.textContent = lane.title;
    el("#noteLane").append(opt);
  });
}

function escapeHtml(s){ return s.replace(/[&<>"']/g, c=>({ "&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;" }[c])); }

function laneIndex(laneId){
  return board.lanes.findIndex(l=>l.id===laneId);
}

function renderNotes(){
  notesLayer.innerHTML = "";
  // place notes roughly in lanes columns
  const laneEls = [...document.querySelectorAll(".lane")];
  const laneRects = laneEls.map(le=>le.getBoundingClientRect());
  const boardRect = boardEl.getBoundingClientRect();
  board.notes.forEach(n=>{
    const note = document.createElement("div");
    note.className = "note";
    note.dataset.id = n.id;
    note.style.background = n.color || COLORS[n.tag] || "#ffeb3b";
    // position: if note has x/y use it else stack in lane
    if(n.x != null && n.y != null){
      note.style.left = n.x + "px";
      note.style.top = (n.y) + "px";
    } else {
      const idx = Math.max(0, laneIndex(n.laneId));
      const col = laneEls[idx] || laneEls[0];
      const r = col ? col.getBoundingClientRect() : boardRect;
      const x = (r.left - boardRect.left) + 10 + Math.random()*20;
      const y = 60 + Math.random()*80;
      n.x = Math.round(x); n.y = Math.round(y);
      note.style.left = n.x + "px";
      note.style.top = n.y + "px";
    }
    note.innerHTML = `<div class="text">${escapeHtml(n.text||"")}</div><div class="meta"><span>${escapeHtml(n.tag||"")}</span><span class="votes">● ${n.votes||0}</span></div>`;
    note.addEventListener("dblclick", ()=> openDialog(n.id));
    note.addEventListener("mousedown", startDrag);
    note.addEventListener("touchstart", startDrag, {passive:false});
    notesLayer.append(note);
  });
}

function addNote(laneId){
  const lane = laneId || board.lanes[0]?.id || "lane-1";
  const note = {
    id: uid(),
    text: "New note — double-click to edit",
    laneId: lane,
    color: el("#noteColor").value || "#ffeb3b",
    votes: 0,
    tag: "fact",
    x: null, y: null
  };
  board.notes.push(note);
  saveBoard(); renderNotes();
  openDialog(note.id);
}

let editingId = null;
function openDialog(id){
  editingId = id;
  const n = board.notes.find(x=>x.id===id);
  if(!n) return;
  el("#dialogTitle").textContent = "Edit note";
  el("#noteText").value = n.text;
  el("#noteLane").value = n.laneId;
  el("#noteColor2").value = n.color || "#ffeb3b";
  el("#noteVotes").value = n.votes || 0;
  el("#noteTag").value = n.tag || "fact";
  el("#noteDialog").showModal();
}
el("#saveNote").addEventListener("click", (e)=>{
  e.preventDefault();
  if(!editingId) return;
  const n = board.notes.find(x=>x.id===editingId);
  n.text = el("#noteText").value.trim() || n.text;
  n.laneId = el("#noteLane").value;
  n.color = el("#noteColor2").value;
  n.votes = parseInt(el("#noteVotes").value,10)||0;
  n.tag = el("#noteTag").value;
  saveBoard(); renderNotes();
  el("#noteDialog").close();
});
el("#deleteNote").addEventListener("click", ()=>{
  if(!editingId) return;
  board.notes = board.notes.filter(x=>x.id!==editingId);
  saveBoard(); renderNotes();
  el("#noteDialog").close();
});

notesLayer.addEventListener("click", (e)=>{
  const note = e.target.closest(".note");
  if(!note) return;
  // vote with + key is handled globally; click vote badge
  if(e.target.classList.contains("votes")){
    const n = board.notes.find(x=>x.id===note.dataset.id);
    n.votes = (n.votes||0)+1; saveBoard(); renderNotes();
  }
});

/* Drag */
function startDrag(e){
  const note = e.currentTarget;
  const n = board.notes.find(x=>x.id===note.dataset.id);
  const startX = (e.touches ? e.touches[0].clientX : e.clientX);
  const startY = (e.touches ? e.touches[0].clientY : e.clientY);
  const orig = { x: n.x||0, y: n.y||0 };
  drag = { id: n.id, sx: startX, sy: startY, ox: orig.x, oy: orig.y };
  function move(ev){
    const cx = (ev.touches ? ev.touches[0].clientX : ev.clientX);
    const cy = (ev.touches ? ev.touches[0].clientY : ev.clientY);
    n.x = Math.round(drag.ox + (cx - drag.sx));
    n.y = Math.round(drag.oy + (cy - drag.sy));
    note.style.left = n.x + "px";
    note.style.top = n.y + "px";
    // update lane by x position
    const boardRect = boardEl.getBoundingClientRect();
    const laneEls = [...document.querySelectorAll(".lane")];
    const centerX = (n.x + 70);
    for(let i=0;i<laneEls.length;i++){
      const r = laneEls[i].getBoundingClientRect();
      const rel = r.left - boardRect.left;
      if(centerX >= rel && centerX < rel + r.width){ n.laneId = board.lanes[i].id; break; }
    }
    ev.preventDefault();
  }
  function up(){
    document.removeEventListener("mousemove", move);
    document.removeEventListener("mouseup", up);
    document.removeEventListener("touchmove", move);
    document.removeEventListener("touchend", up);
    saveBoard();
    drag = null;
  }
  document.addEventListener("mousemove", move);
  document.addEventListener("mouseup", up);
  document.addEventListener("touchmove", move, {passive:false});
  document.addEventListener("touchend", up);
  e.preventDefault();
}

document.addEventListener("keydown", (e)=>{
  if(e.key==="+" || e.key==="="){
    const sel = document.querySelector(".note:last-child");
    // actual vote via note hover — find note under mouse? easier: focus last edited
    if(editingId){
      const n = board.notes.find(x=>x.id===editingId);
      if(n){ n.votes = (n.votes||0)+1; saveBoard(); renderNotes(); }
    }
  }
  if(e.key==="x" || e.key==="X"){
    if(editingId && el("#noteDialog").open){
      // delete via dialog
    }
  }
  if(e.key==="n" && (e.metaKey||e.ctrlKey)){
    e.preventDefault(); addNote();
  }
});

/* Drawing */
el("#toggleDraw").addEventListener("click", ()=>{
  drawActive = !drawActive;
  canvas.classList.toggle("active", drawActive);
  el("#toggleDraw").textContent = drawActive ? "✎ drawing" : "✎ draw";
  if(drawActive) resizeCanvas();
});
function resizeCanvas(){
  const rect = boardEl.getBoundingClientRect();
  const dpr = window.devicePixelRatio || 1;
  canvas.width = Math.round(rect.width * dpr);
  canvas.height = Math.round(rect.height * dpr);
  canvas.style.width = rect.width + "px";
  canvas.style.height = rect.height + "px";
  ctx.setTransform(dpr,0,0,dpr,0,0);
  redrawStrokes();
}
function redrawStrokes(){
  ctx.clearRect(0,0,canvas.width, canvas.height);
  ctx.lineCap="round"; ctx.lineJoin="round";
  for(const s of strokes){
    ctx.strokeStyle = s.color || "#1a1a1a";
    ctx.lineWidth = s.width || 2;
    ctx.beginPath();
    s.points.forEach((pt,i)=> i?ctx.lineTo(pt.x,pt.y):ctx.moveTo(pt.x,pt.y));
    ctx.stroke();
  }
}
let curStroke = null;
canvas.addEventListener("pointerdown", (e)=>{
  if(!drawActive) return;
  canvas.setPointerCapture(e.pointerId);
  drawing = true;
  const rect = canvas.getBoundingClientRect();
  curStroke = { color: "#1a1a1a", width: 2, points: [{x:e.clientX-rect.left, y:e.clientY-rect.top}] };
  strokes.push(curStroke);
});
canvas.addEventListener("pointermove", (e)=>{
  if(!drawing || !curStroke) return;
  const rect = canvas.getBoundingClientRect();
  curStroke.points.push({x:e.clientX-rect.left, y:e.clientY-rect.top});
  redrawStrokes();
});
canvas.addEventListener("pointerup", ()=>{
  drawing=false; curStroke=null; saveBoard();
});
window.addEventListener("resize", ()=>{ if(drawActive) resizeCanvas(); });

/* Template */
el("#applyTemplate").addEventListener("click", ()=>{
  const key = el("#template").value;
  const t = TEMPLATES[key];
  if(!t) return;
  board.template = key;
  board.title = t.title;
  el("#boardTitle").value = t.title;
  board.lanes = t.lanes.map((title,i)=>({id:`lane-${i+1}`, title}));
  renderLanes(); saveBoard(); renderNotes();
});

/* Board switching */
async function initBoard(){
  const params = new URLSearchParams(location.search);
  const id = params.get("board") || el("#boardId").value.trim() || "demo";
  el("#boardId").value = id;
  let loaded = loadBoard(id);
  const fileBoard = await loadBoardFromFile(id);
  if(fileBoard && fileBoard.notes) loaded = fileBoard;
  board = loaded || defaultBoard(id);
  board.id = id;
  // ensure at least one lane
  if(!board.lanes || !board.lanes.length) board.lanes = [{id:"lane-1", title:"Inbox"}];
  el("#boardTitle").value = board.title || "";
  renderLanes();
  strokes = board.drawings || [];
  if(strokes.length) { resizeCanvas(); redrawStrokes(); }
  renderNotes();
  el("#boardTitle").addEventListener("change", ()=>{ board.title = el("#boardTitle").value.trim()||board.title; saveBoard(); });
  el("#boardId").addEventListener("change", ()=>{
    saveBoard();
    const nid = el("#boardId").value.trim()||"demo";
    const u = new URL(location.href); u.searchParams.set("board", nid); history.replaceState(null,"",u);
    initBoard();
  });
}
el("#addNote").addEventListener("click", ()=> addNote());
el("#clearBoard").addEventListener("click", ()=>{
  if(!confirm("Clear this board's notes and drawings?")) return;
  board.notes = []; strokes = []; board.drawings = [];
  saveBoard(); renderNotes(); redrawStrokes();
});
el("#exportJson").addEventListener("click", ()=>{
  saveBoard();
  const data = JSON.stringify(board, null, 2);
  const blob = new Blob([data], {type:"application/json"});
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href=url; a.download = `${board.id}.json`; a.click();
  URL.revokeObjectURL(url);
});
el("#exportPng").addEventListener("click", ()=>{
  // export board as PNG via canvas + notes rasterization (simple: board screenshot via draw + notes)
  const off = document.createElement("canvas");
  const rect = boardEl.getBoundingClientRect();
  const dpr = 2;
  off.width = rect.width * dpr; off.height = rect.height * dpr;
  const octx = off.getContext("2d");
  octx.scale(dpr,dpr);
  octx.fillStyle = "#f9fafb"; octx.fillRect(0,0,rect.width, rect.height);
  // draw strokes scaled
  for(const s of strokes){
    octx.strokeStyle = s.color || "#1a1a1a"; octx.lineWidth = s.width||2;
    octx.beginPath(); s.points.forEach((pt,i)=> i?octx.lineTo(pt.x,pt.y):octx.moveTo(pt.x,pt.y)); octx.stroke();
  }
  octx.fillStyle="#1a1a1a"; octx.font="12px system-ui";
  board.notes.forEach(n=>{
    octx.fillStyle = n.color || "#ffeb3b";
    const x = n.x||10, y=n.y||10;
    octx.fillRect(x,y,170,64);
    octx.fillStyle="#1a1a1a";
    const words = (n.text||"").slice(0,60);
    octx.fillText(words, x+6, y+16, 158);
    octx.fillText(`● ${n.votes||0}  ${n.tag||""}`, x+6, y+52);
  });
  const url = off.toDataURL("image/png");
  const a = document.createElement("a"); a.href=url; a.download = `${board.id}.png`; a.click();
});
el("#importFile").addEventListener("change", async (e)=>{
  const f = e.target.files[0]; if(!f) return;
  const text = await f.text();
  try{
    const data = JSON.parse(text);
    if(!data.id || !Array.isArray(data.notes)) throw new Error("invalid board json");
    board = data; saveBoard(); renderLanes(); strokes = board.drawings||[]; renderNotes(); redrawStrokes();
    el("#boardId").value = board.id; el("#boardTitle").value = board.title||"";
    const u = new URL(location.href); u.searchParams.set("board", board.id); history.replaceState(null,"",u);
  }catch(err){ alert("Import failed: " + err.message); }
});

/* Timer: toggles 5/10/15 min */
let timerPreset = 300;
el("#timerBtn").addEventListener("click", ()=>{
  if(timerRunning){
    clearInterval(timerInt); timerRunning=false; el("#timerBtn").textContent = `⏱ ${fmt(timerSec)} ▶`;
    return;
  }
  const choices = [300,600,900];
  const idx = choices.indexOf(timerPreset);
  timerPreset = choices[(idx+1)%choices.length];
  timerSec = timerPreset;
  el("#timerBtn").textContent = `⏱ ${fmt(timerSec)} ▶`;
});
let fmt = s=> `${Math.floor(s/60)}:${String(s%60).padStart(2,"0")}`;
function tick(){
  if(!timerRunning) return;
  timerSec = Math.max(0, timerSec-1);
  el("#timerBtn").textContent = `⏱ ${fmt(timerSec)}`;
  if(timerSec===0){ clearInterval(timerInt); timerRunning=false; el("#timerBtn").textContent="⏱ 0:00 ✓"; try{ new Audio("data:audio/wav;base64,UklGRigAAABXQVZFZm10IBAAAAABAAEARKwAAIhYAQACABAAZGF0YQQAAAAA").play(); }catch(e){} }
}
el("#timerBtn").addEventListener("dblclick", ()=>{
  timerSec = timerPreset;
  timerRunning = true;
  el("#timerBtn").textContent = `⏱ ${fmt(timerSec)}`;
  clearInterval(timerInt);
  timerInt = setInterval(tick,1000);
});
el("#timerBtn").addEventListener("contextmenu", (e)=>{ e.preventDefault(); timerSec = timerPreset; el("#timerBtn").textContent = `⏱ ${fmt(timerSec)} ▶`; });

initBoard();
