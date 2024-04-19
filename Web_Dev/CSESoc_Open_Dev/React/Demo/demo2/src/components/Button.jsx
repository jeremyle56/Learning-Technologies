import React from "react";

const Button = (props) => {
  return (
    <button
      style={{
        width: "200px",
        background: props.bg,
      }}
      onClick={props.onClick}
    >
      {props.children}
    </button>
  );
};

export default Button;
