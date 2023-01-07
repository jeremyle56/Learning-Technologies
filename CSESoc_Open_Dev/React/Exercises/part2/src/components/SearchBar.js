import { useState } from "react";

const SearchBar = ({ fetchCountryData }) => {
  const [input, setInput] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();
    fetchCountryData(input);
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>Input Field</label>
        <input type="text" onChange={(event) => setInput(event.target.value)} />
      </form>
    </div>
  );
};

export default SearchBar;
