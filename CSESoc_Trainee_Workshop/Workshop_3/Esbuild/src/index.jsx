import React from "react";
import { createRoot } from 'react-dom/client'

const MyEpicButton = (props) => {
    const coolText = "I'm a cool button!";
    return (
        <button>
            {coolText} {5 + 5}
        </button>
    );
}

const App = () => {
    return (
        <div>
          <MyEpicButton />  
        </div>
    );
};

const appRoot = document.querySelector('#root');

const virtualDOMRoot = createRoot(appRoot);
virtualDOMRoot.render(<App />); 