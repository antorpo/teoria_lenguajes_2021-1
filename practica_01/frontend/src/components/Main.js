import React from "react";
import { render } from "react-dom";
import App from "./App";
import Main from "./Main";
import "./Main.css";
import "bootstrap/dist/css/bootstrap.min.css";
import { positions, Provider } from "react-alert";
import AlertTemplate from "react-alert-template-basic";

const options = {
  timeout: 5000,
  position: positions.BOTTOM_CENTER,
};

const container = document.getElementById("app");
render(
  <Provider template={AlertTemplate} {...options}>
    <App />
  </Provider>,
  container
);

export default Main;

/* 
Exportar por defecto
import mod from 'mod';
export default mod;
*/
