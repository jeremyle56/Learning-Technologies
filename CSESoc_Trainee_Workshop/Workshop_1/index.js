
// Document Object
console.log(window);
console.log(window.location);
console.log(document);

// Creating an element
const newDiv = document.createElement("div");
const newP = document.createElement("p");
newP.innerText = "Hello";
newDiv.appendChild(newP);
document.body.appendChild(newDiv);

// Deleting an element
// newP.remove();

// Grab element
const h1 = document.querySelector(".title");
// console.log(h1);
// h1.remove();

// Mutating an element
h1.style.backgroundColor = "red";
h1.style.height = "100px";
h1.innerText = "red sus";

// Button
console.log(document.querySelector("button").click());
console.log(document.querySelector("button").onclick);

// susy is sus
const sussyButton = document.querySelector("button");

sussyButton.addEventListener("click", () => {
    console.log("sus");
    window.alert("sus");
});