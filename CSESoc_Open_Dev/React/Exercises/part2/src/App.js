import SearchBar from "./components/SearchBar";
import CountryCard from "./components/CountryCard";
import { useState } from "react";

function App() {
  const [countryData, setCountryData] = useState(null);

  const fetchCountryData = async (country) => {
    console.log(`fetchCountryData function is called with ${country}`)
    const url = `https://restcountries.com/v3/name/${country}`;
    const response = await fetch(url);
    const countryData = await response.json();
    setCountryData(countryData[0]);
  }

  if (!countryData) {
    return (
      <div>
        <CountryCard country={"something"} area={"something"} population={"something"}/>
        <SearchBar fetchCountryData={fetchCountryData}/>
      </div>
    )
  };

  return (
    <div>
      <CountryCard country={countryData.name.common} area={countryData.area} population={countryData.population}/>
      <SearchBar fetchCountryData={fetchCountryData}/>
    </div>
  );
}

export default App;
