import React, { useState } from "react";
import "./App.css";
import "../css/style.css";
import facultad_ingenieria from "../images/facultad-ingenieria.png";
import { Button, Card, Accordion, Table } from "react-bootstrap";
import { Enunciado } from "./Enunciado";
import { Loader } from "./Loader";
import { default as textos } from "./strings.json";
import AceEditor from "react-ace";
import "ace-builds/src-noconflict/mode-java";
import "ace-builds/src-noconflict/theme-textmate";
import { useAlert } from "react-alert";
import axios from "axios";

const App = (props) => {
  const alert = useAlert();
  const [cadena, setCadena] = useState({
    secuencia: "",
  });
  const [tokens, setTokens] = useState({
    loading: false,
    error: null,
    data: [],
  });

  const onChange = (newValue) => {
    setCadena({
      secuencia: newValue,
    });
  };

  const createCadena = () => {
    if (cadena.secuencia) {
      axios.post(`/api/cadena-create/`, cadena).then((res) => {
        getTokens();
        alert.success(textos.exito_cadena);
      });
    } else {
      alert.error(textos.error_cadena);
      setTokens({
        loading: false,
        data: [],
        error: null,
      });
    }
  };

  const getTokens = () => {
    setTokens({
      loading: true,
      error: null,
    });

    try {
      axios.get(`/api/token-array/`).then((res) => {
        const tokens = res.data;
        setTokens({
          loading: false,
          data: tokens,
        });

        deleteCadena();
      });
    } catch (error) {
      setTokens({
        loading: false,
        error: error,
      });
    }
  };

  const deleteCadena = () => {
    axios.delete(`/api/cadena-delete-all/`).then((res) => {
      console.log(res.data);
    });
  };

  return (
    <div id="recuadro">
      <div id="logo">
        <img src={facultad_ingenieria} width="20%" />
      </div>
      <h1>{textos.titulo}</h1>
      <br />
      <h5 id="nombres">{textos.nombres}</h5>
      <Accordion>
        <Card>
          <Accordion.Toggle
            as={Card.Header}
            eventKey="0"
            style={{ cursor: "pointer" }}
          >
            {textos.problema}
          </Accordion.Toggle>
          <Accordion.Collapse eventKey="0">
            <Card.Body>
              <Enunciado {...textos} />
            </Card.Body>
          </Accordion.Collapse>
        </Card>
        <Card>
          <Accordion.Toggle
            as={Card.Header}
            eventKey="1"
            style={{ cursor: "pointer" }}
          >
            {textos.solucion}
          </Accordion.Toggle>
          <Accordion.Collapse eventKey="1">
            <Card.Body>
              <div className="container">
                <div className="row">
                  <div className="col-12 col-lg-8 espaciado_abajo">
                    <h4 className="fw-bold border border-secondary">
                      {textos.secuencia}
                    </h4>
                    <AceEditor
                      mode="java"
                      theme="textmate"
                      onChange={onChange}
                      name="code_editor"
                      fontSize={14}
                      showPrintMargin={true}
                      showGutter={true}
                      highlightActiveLine={true}
                      width={`100%`}
                      height={`400px`}
                      value={cadena.secuencia}
                      setOptions={{
                        showLineNumbers: true,
                        tabSize: 4,
                      }}
                    />
                    <Button
                      variant="success"
                      className="Button-padding"
                      onClick={createCadena}
                    >
                      {textos.tokenizar}
                    </Button>
                  </div>
                  <div className="col-12 col-lg-4">
                    {tokens.loading && (
                      <div className="text-center">
                        <Loader mensaje={textos.cargando} />
                      </div>
                    )}

                    {!tokens.loading && tokens.data.length !== 0 && (
                      <>
                        <h4 className="fw-bold border border-secondary">
                          {textos.tokens}
                        </h4>
                        <Table striped bordered hover>
                          <thead>
                            <tr>
                              <th>VALOR</th>
                              <th>TIPO</th>
                            </tr>
                          </thead>
                          <tbody>
                            {tokens.data.map((token, index) => (
                              <tr key={index}>
                                <td>{token[0]}</td>
                                <td>{token[1]}</td>
                              </tr>
                            ))}
                          </tbody>
                        </Table>
                      </>
                    )}
                  </div>
                </div>
              </div>
            </Card.Body>
          </Accordion.Collapse>
        </Card>
      </Accordion>
    </div>
  );
};

export default App;
