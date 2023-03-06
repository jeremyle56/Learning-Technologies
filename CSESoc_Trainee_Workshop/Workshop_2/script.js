
const elem = document.getElementById("btn")
// elem.addEventListener("click", () => {
//     fetch("https://randomuser.me/api")
//         .then((resp) => resp.json())
//         .then((data) => {
//             const results = data.results;
//             console.log(results);
//         });
// });

elem.addEventListener("click", async () => {
    const resp = await fetch("https://randomuser.me/api");
    const data = await resp.json();

    const user = data.results[0];

    const nameElem = document.getElementById("name");
    const emailElem = document.getElementById("email");

    nameElem.innerText = user.name.first + " " + user.name.last;
    emailElem.innerText = user.email;
});