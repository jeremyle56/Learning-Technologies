// Exercises 2 and 3

import { useEffect, useState } from 'react';
import { fetchCountryInfo } from '../utils';

/**
 * Displays the capital city of a given country.
 */
const CapitalFinder = () => {
  const [query, setQuery] = useState('australia');
  const [country, setCountry] = useState(null);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);

  // FIXME: Prevent the infinite render loop with useEffect
  useEffect(() => {
    setLoading(true);
    const updateInfo = async () => {
      const countryInfo = await fetchCountryInfo(query);
      setCountry(countryInfo);
      setLoading(false);
    };
    updateInfo();
  }, [query]);

  const handleOnSubmit = (event) => {
    event.preventDefault();
    setQuery(input);
  }

  const renderMessage = () => {
    if (loading) {
      return <p>Loading...</p>
    }

    if (country == null) {
      return <p>No country found.</p>;
    }

    return <p>The capital city of {country.name.common} is {country.capital}.</p>
  }

  return (
    <div>
      <h2>Capital Finder</h2>
      <button onClick={() => setQuery('australia')}>Australia</button>
      <button onClick={() => setQuery('canada')}>Canada</button>
      <button onClick={() => setQuery('new zealand')}>New Zealand</button>
      {renderMessage()}
      
      <form onSubmit={handleOnSubmit}>
        <input onChange={(event) => setInput(event.target.value)} />
        <button>Search</button>
      </form>
    </div>
  );
};

export default CapitalFinder;
