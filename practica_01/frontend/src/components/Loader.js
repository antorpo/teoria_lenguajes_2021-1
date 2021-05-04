import React from "react";
import "../css/Loader.css";

export const Loader = (props) => {
  const { mensaje } = props;

  return (
    <div className="spinner-container">
      <div className="spinner">
        <div className="sk-chase ">
          <div className="sk-chase-dot" />
          <div className="sk-chase-dot" />
          <div className="sk-chase-dot" />
          <div className="sk-chase-dot" />
          <div className="sk-chase-dot" />
          <div className="sk-chase-dot" />
        </div>

        <h4>{mensaje}</h4>
      </div>
    </div>
  );
};
