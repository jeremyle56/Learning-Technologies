// Objects 

let person = {
    name: "Bob",
    age: 20,
    eyeColour: "black",
    greeting: function() {
        return "Hi my name is " + this.name;
    }
};

let nameVar = person.name;
let greetingName = person.greeting();
console.log(nameVar);
console.log(greetingName);

// let getMovies = async () => {
//     let response = await fetch('https://fake-movie-database-api.herokuapp.com/api?s=batman');
//     let movies = await response.json();
//     console.log(movies);
// }
// getMovies();

// let button = document.getElementById("button");
// let text = document.getElementById("text");
// let clickCount = 0;
// button.addEventListener('click', () => {
//     clickCount++;
//     text.innerText = `You clicked this button ${clickCount} times`
// })

// let currMovie = 0;

// let moviesCycle = async () => {
//     let div = document.createElement('div');
//     document.body.append(div);
//     let img = document.createElement('img');
//     div.append(img);
    


//     let response = await fetch('https://fake-movie-database-api.herokuapp.com/api?s=batman');
//     let movies = await response.json();
//     // console.log(movies);
//     let movieData = movies.Search;
//     console.log(movieData);

//     let incrementButton = document.createElement('button');
//     div.append(incrementButton);

//     let imgSrc = movieData[currMovie].Poster;
//     img.setAttribute('src', imgSrc);



//     const incrementMovie = () => {
//         if (currMovie >= 8) {
//             currMovie = 0;
//         } else {
//             currMovie++;
//         }

//         let imgSrc = movieData[currMovie].Poster;
//         img.setAttribute('src', imgSrc);
//         div.append(img);
//     }

//     incrementButton.onclick = incrementMovie;
//     incrementButton.append("Next")
// }

// moviesCycle();

// Good website to learn more about JavaScript
// https://javascript.info/

// JavaScript Documentation
// https://developer.mozilla.org/en-US/docs/Web/JavaScript