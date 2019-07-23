// console.log("Hello, world");
//
// var h1tag = document.getElementsByTagName("h1")[0];
//
// var loc = document.getElementsByClassName("headings")[3];

var adjectives = ["nice", "stupendous", "funny", "tall", "simple", "dirty", "happy", "eloquent", "etc"];

var pos = 0;

var loc = document.getElementById("adj");

function changeAdj() {
  loc.innerHTML = adjectives[pos];
  pos ++;
  if (pos >= adjectives.length) {
    pos = 0;
  }
}

var y = document.getElementsByTagName("body")[0];

function colorfulBackground() {
  y.setAttribute("style", `background-color:rgb(${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)})`);
}

y.setAttribute("onmouseover", colorfulBackground());
