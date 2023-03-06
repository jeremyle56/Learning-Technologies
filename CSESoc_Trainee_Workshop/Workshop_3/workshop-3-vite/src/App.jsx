import { useState } from 'react'
import isOdd from 'is-odd' 
import sussy from './assets/sussy.png'
import './App.css'

function App() {
  const [count, setCount] = useState(0);

  const handleChange = (event) => {
    setCount(event.target.value);
  };

  return (
    <div className="App">
      <div>
        <a href="https://reactjs.org" target="_blank">
          <img src={sussy} className="logo react" alt="Sus logo" />
        </a>
      </div>
      <h1>Is it odd?</h1>
      <input type="number" name="my-number" id="my-number" onChange={handleChange}/>
      <p>{isOdd(count) ? "It's odd": "Is even"}</p>
    </div>
  )
}

export default App
