import { useState, useEffect } from "react";

const App = () => {
  const [message, setMessage] = useState('Hello, world!');
  useEffect(() => {
    console.log('useEffect has fired')
  }, [message]);
  // gets called when the button is clicked
  const handleOnClick = () => {
    // TODO: Update message to 'Hello, Open Dev!'
    setMessage('Hello, Open Dev!');
  };

  return (
    <div>
      <p>{message}</p>
      <button onClick={handleOnClick}>Update message</button>
    </div>
  );
};

export default App;
