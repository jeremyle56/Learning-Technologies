/**
 * Uses fetch to get information about countries from the REST Countries API.
 * Returns the first country matching the given name.
 */
export const fetchCountryInfo = async (name) => {
  const url = `https://restcountries.com/v3/name/${name}`;
  const response = await fetch(url);
  const data = await response.json(); // list of matching countries
  return data[0]; // first country in that list
};
