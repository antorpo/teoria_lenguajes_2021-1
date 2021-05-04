import React from 'react'
import "../css/style.css";
//import { default as textos } from './strings.json';

export const Enunciado = (props) => {

    const {enunciado, numerales, entregables} = props;

    return(
        <div>
        <p>{enunciado}</p><br/>
        <p className="enunciado">{entregables}</p>
        <ol>
            <li>
                {numerales.primero.enunciado}
                <ol type="a">
                    <li>{numerales.primero.opciones.a}</li>
                    <li>{numerales.primero.opciones.b}</li>
                    <li>{numerales.primero.opciones.c}</li>
                    <li>{numerales.primero.opciones.d}</li>
                </ol>
                
            </li>
            <li>{numerales.segundo.enunciado}</li>
            <li>{numerales.tercero.enunciado}</li>     
        </ol>
      </div>
    )
}