const canvas = document.getElementById("jsCanvas");
const ctx = canvas.getContext("2d");
const colors = document.getElementsByClassName("jsColor");
const range = document.getElementById("jsRange");
const mode = document.getElementById("jsMode");
const saveBtn = document.getElementById("jsSave");

ctx.strokeStyle = "#000000";
ctx.lineWidth = 5.0; /* 라인 굵기 */

canvas.width = 1000;
canvas.height = 400;

CANVAS_SIZEW =1000;
CANVAS_SIZEH =400;

ctx.fillStyle = "#FFFFFF";
ctx.fillRect(0,0,CANVAS_SIZEW,CANVAS_SIZEH);

let painting = false;
let filling = false;

function stopPainting() {
    painting = false;
}

function startPainting() {
    painting = true;
}

function onMouseMove(event) {
    const x = event.offsetX;
    const y = event.offsetY;
    if (!painting) {
        ctx.beginPath();
        ctx.moveTo(x, y);
    } else{
        ctx.lineTo(x, y);
        ctx.stroke();
    }
}

if (canvas) {
    canvas.addEventListener("mousemove", onMouseMove);
    canvas.addEventListener("mousedown", startPainting);
    canvas.addEventListener("mouseup", stopPainting);
    canvas.addEventListener("mouseleave", stopPainting);
}

function handleColorClick(event){
    const color = event.target.style.backgroundColor;
    ctx.strokeStyle = color;
}

Array.from(colors).forEach(color => color.addEventListener("click", handleColorClick));

function handleRangeChange(event){
    const size = event.target.value;
    ctx.lineWidth = size
}

function removeall(event){
    filling = true
    ctx.fillStyle = "#FFFFFF";
    ctx.fillRect(0,0,CANVAS_SIZEW,CANVAS_SIZEH);
    filling = false;
}

function handleSaveClick(){
    const image = canvas.toDataURL("image/jpg");
    const link = document.createElement("a");
    link.href = image;
    link.download = "Paint.jpg";
    link.click();
}

if (mode) {
    mode.addEventListener("click",removeall)
}

if (range) {
    range.addEventListener("click",handleRangeChange);
}

if(saveBtn){
    saveBtn.addEventListener("click",handleSaveClick)
}
