// Exercise 1
import { useState } from "react";

/**
 * Displays a counter that increments by 1 whenever a button is clicked.
 */
const Counter = () => {
  // TODO: Declare a new state variable for the counter with useState
  const [counter, setCounter] = useState(0)
  
  // gets called when the button is clicked
  const handleOnClick = () => {
    // TODO: Increment the counter by 1
    setCounter((counter) => counter + 1);
  };

  return (
    <div>
      <p>Counter: {counter}</p>
      <button onClick={handleOnClick}>Increment</button>
    </div>
  );
};

export default Counter;
