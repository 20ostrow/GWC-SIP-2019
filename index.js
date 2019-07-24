/*
console.log("Hello World!");

// sets i to 0, adds 2 to i each time, runs when i < 20
var i = 0;
for (i = 0; i < 21; i += 2) {
  console.log(i);
}

// sets i to 0, runs when i <= 20, adds 2 to each iteration
i = 0
while (i <= 20) {
  console.log(i);
  i += 2
}

i = 0 // sets i to 0
while (i <= 20) { //runs when i <= 20
  if(i % 2 == 0) { //runs when i is even
    console.log(i);
  }
  i ++ //adds 1
}
*/

// function getTemp() {
//   return 22.5;
// }
//
// var temperature = getTemp();
// console.log(temperature);
//
//
// function getTemp2(type) {
//   if (type == "c") {
//     alert("It is really rainy today!")
//     return 22.5;
//   }
//   if (type == "f") {
//     alert("It is really hot today!")
//     return 100;
//   }
// }
//
// console.log(getTemp2("c"));
// console.log(getTemp2("f"));

var adjs = ["nice", "amazing", "smart", "happy"];

var pos = 0;

var loc = document.getElementById("madj");

var font = ["Geostar", "Bonbon", "Fascinate", "Muli"]

function changeMadj() {
  loc.innerHTML = adjs[pos];
  loc.setAttribute("style", `font-family:${font[pos]}`)
  pos ++;
  if (pos >= adjs.length) {
    pos = 0;
  }
}

// when click on name (heading), grow in size by 10px each time

var size = 32
var x = document.getElementById("name")
var delta = 10

function bigText(){
  x.style.fontSize = `${size}px`
  size += delta;
  if (size > 92 || size < 32) {
    delta = delta * -1;
  }
}

document.getElementById("name").addEventListener("click",
function() {
  bigText();
  x.style.color = `rgb(${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)})`;
});


document.getElementById("back").addEventListener("click",
  function () {
    alert("hi");
  }
)
