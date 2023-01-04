// const fav_bowl = {
//   noodles: 'Ramen noodles',
//   broth: 'Chicken Stock',
//   toppings: 'eggs, green onion, corn, nori, sesame seeds, chili oil',
// };

const construct_bowl = (noodles, broth, toppings) => {
  return {
    noodles: noodles,
    broth: broth,
    toppings: toppings,
  };
};

// console.log(
//   construct_bowl(
//     "Ramen noodles",
//     "Chicken Stock",
//     "eggs, green onion, corn, nori, sesame seeds, chili oil"
//   )
// );

let currShop = 0;

const getShops = async () => {
  // Sets up the div
  const div = document.createElement("div");
  div.style.backgroundColor = "#dbf1e8";
  div.style.margin = "15px";
  div.style.padding = "15px";
  document.body.append(div);

  // Creates a header named Ramen Shops
  const header = document.createElement("h1");
  header.innerHTML = "Ramen Shops";
  div.append(header);

  // Creates a subheading for the Ramen Shop Name
  const newContent = document.createElement("h2");
  div.append(newContent);

  // Creates the Ramen Shop Image
  const img = document.createElement("img");
  div.append(img);

  // Get Ramen shops from online
  const res = await fetch(
    "https://ramen-api.dev/shops?pretty&page=1&perPage=10"
  );
  const data = await res.json();
  const shops = data.shops.map((s) => ({ id: s.id, photo: s.photos[0] }));

  // Set the first shop name and image pair
  newContent.innerHTML =
    shops[0].id.charAt(0).toUpperCase() + shops[0].id.slice(1);
  img.setAttribute("src", shops[0].photo.url);
  img.setAttribute("alt", shops[0].id);
  img.setAttribute("width", "300px");

  // Creates previous and next buttons
  const prevButton = document.createElement("button");
  prevButton.setAttribute("type", "button");
  const nextButton = document.createElement("button");
  nextButton.setAttribute("type", "button");

  // Function to change displayed shop name and image pair
  const changeShop = (direction) => {
    if (currShop >= shops.length - 1 && direction === "next") {
      currShop = 0;
    } else if (currShop <= 0 && direction === "prev") {
      currShop = shops.length - 1;
    } else if (direction === "prev") {
      currShop--;
    } else {
      currShop++;
    }

    const shop = shops[currShop];
    newContent.innerHTML = shop.id.charAt(0).toUpperCase() + shop.id.slice(1);

    img.setAttribute("src", shop.photo.url);
    img.setAttribute("alt", shop.id);
    img.setAttribute("width", "300px");
  };

  // Configure the previous and next buttons
  prevButton.onclick = () => changeShop("prev");
  nextButton.onclick = () => changeShop("next");
  prevButton.append("Previous");
  nextButton.append("Next");

  div.append(document.createElement("br"));
  div.append(prevButton);
  div.append(nextButton);
};

getShops();
