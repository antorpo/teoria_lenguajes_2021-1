import json
from .automata_java import Automata_Java


def splitter(cadena):
    l = []
    aux = []
    abierto = False
    for c in cadena+' ':
        if ord(c) == 10 and not abierto:
            continue
        if c == '"' and abierto:
            aux.append(c)
            abierto = False
        elif c == '"' and not abierto:
            aux.append(c)
            abierto = True
        elif abierto or (not abierto and c != ' '):
            aux.append(c)
        elif c == ' ' and len(aux) != 0:
            l.append("".join(aux))
            aux = []
    return l


def tokenizador(secuencia):

    tokensAcumulados = []
    tokensIteracion = []

    for cadena in splitter(secuencia):
        reconocedor = Automata_Java()
        reconocedor2 = Automata_Java()
        l_char_token = []
        tokensIteracion = []
        for c in cadena+" ":
            reconocedor2.automata_Java(c)
            if reconocedor2.estado_actual()[0] == 'RECHAZO' and reconocedor.estado_actual()[0] == 'ACEPTACIÓN' and not c in ['.', '['] and reconocedor2.numConst[0] == 1:

                if len(tokensIteracion) == 0:
                    tokensIteracion.append(
                        ("".join(l_char_token), reconocedor.estado_actual()[1]))
                    l_char_token = [c]
                    reconocedor, reconocedor2 = Automata_Java(), Automata_Java()
                    reconocedor.automata_Java(c)
                    reconocedor2.automata_Java(c)
                    continue

                elif reconocedor.estado_actual()[1] == 'KEYWORD':

                    if tokensIteracion[-1][0] in [';', '{', '}'] and not "".join(l_char_token) in ['static', 'void', 'String[]']:
                        tokensIteracion.append(
                            ("".join(l_char_token), reconocedor.estado_actual()[1]))
                        l_char_token = [c]
                        reconocedor, reconocedor2 = Automata_Java(), Automata_Java()
                        reconocedor.automata_Java(c)
                        reconocedor2.automata_Java(c)
                        continue
                    elif tokensIteracion[-1][0] == '(' and "".join(l_char_token) == 'String[]':

                        tokensIteracion.append(
                            ("".join(l_char_token), reconocedor.estado_actual()[1]))
                        l_char_token = [c]
                        reconocedor, reconocedor2 = Automata_Java(), Automata_Java()
                        reconocedor.automata_Java(c)
                        reconocedor2.automata_Java(c)
                        continue
                    else:
                        tokensIteracion = []
                        break

                elif reconocedor.estado_actual()[1] == 'numConst':
                    if (((tokensIteracion[-1][0] == '(') or (tokensIteracion[-1][1] == 'numConst' and l_char_token[0] in ['+', '-'])) and c != ' '):
                        tokensIteracion.append(
                            ("".join(l_char_token[0]), 'OPERATOR'))
                        tokensIteracion.append(
                            ("".join(l_char_token[1:]), 'numConst'))
                        l_char_token = [c]
                        reconocedor, reconocedor2 = Automata_Java(), Automata_Java()
                        reconocedor.automata_Java(c)
                        reconocedor2.automata_Java(c)
                        continue
                    elif tokensIteracion[-1][1] == 'OPERATOR' or c == ' ':
                        tokensIteracion.append(
                            ("".join(l_char_token), 'numConst'))
                        l_char_token = [c]
                        reconocedor, reconocedor2 = Automata_Java(), Automata_Java()
                        reconocedor.automata_Java(c)
                        reconocedor2.automata_Java(c)
                        continue
                    else:
                        tokensIteracion = []
                        break

                elif reconocedor.estado_actual()[1] == 'charConst':
                    if tokensIteracion[-1][0] in ['(', '=']:
                        tokensIteracion.append(
                            ("".join(l_char_token), reconocedor.estado_actual()[1]))
                        l_char_token = [c]
                        reconocedor, reconocedor2 = Automata_Java(), Automata_Java()
                        reconocedor.automata_Java(c)
                        reconocedor2.automata_Java(c)
                        continue
                    else:
                        tokensIteracion = []
                        break

                elif reconocedor.estado_actual()[1] == 'SEPARATOR':
                    if l_char_token[-1] == '(' and (tokensIteracion[-1][0] in ['System.out.print', 'for', 'if', '('] or tokensIteracion[-1][1] == 'OPERATOR' or tokensIteracion[-1][1] == 'IDENTIFICADOR'):
                        tokensIteracion.append(
                            ("".join(l_char_token), reconocedor.estado_actual()[1]))
                        l_char_token = [c]
                        reconocedor, reconocedor2 = Automata_Java(), Automata_Java()
                        reconocedor.automata_Java(c)
                        reconocedor2.automata_Java(c)
                        continue
                    elif l_char_token[-1] == ')' and (tokensIteracion[-1][0] == '(' or tokensIteracion[-1][0] == ')' or tokensIteracion[-1][1] == 'numConst' or tokensIteracion[-1][1] == 'charConst' or tokensIteracion[-1][1] == 'IDENTIFICADOR'):
                        tokensIteracion.append(
                            ("".join(l_char_token), reconocedor.estado_actual()[1]))
                        l_char_token = [c]
                        reconocedor, reconocedor2 = Automata_Java(), Automata_Java()
                        reconocedor.automata_Java(c)
                        reconocedor2.automata_Java(c)
                        continue
                    elif l_char_token[-1] == '{' and (tokensIteracion[-1][0] in [')', ';'] or tokensIteracion[-1][1] == 'IDENTIFICADOR'):
                        tokensIteracion.append(
                            ("".join(l_char_token), reconocedor.estado_actual()[1]))
                        l_char_token = [c]
                        reconocedor, reconocedor2 = Automata_Java(), Automata_Java()
                        reconocedor.automata_Java(c)
                        reconocedor2.automata_Java(c)
                        continue
                    elif l_char_token[-1] == '}' and tokensIteracion[-1][0] in [';', '{', ')']:
                        tokensIteracion.append(
                            ("".join(l_char_token), reconocedor.estado_actual()[1]))
                        l_char_token = [c]
                        reconocedor, reconocedor2 = Automata_Java(), Automata_Java()
                        reconocedor.automata_Java(c)
                        reconocedor2.automata_Java(c)
                        continue
                    elif l_char_token[-1] == ';' and (tokensIteracion[-1][0] == ')' or tokensIteracion[-1][1] == 'numConst' or tokensIteracion[-1][1] == 'charConst' or tokensIteracion[-1][1] == 'IDENTIFICADOR'):
                        tokensIteracion.append(
                            ("".join(l_char_token), reconocedor.estado_actual()[1]))
                        l_char_token = [c]
                        reconocedor, reconocedor2 = Automata_Java(), Automata_Java()
                        reconocedor.automata_Java(c)
                        reconocedor2.automata_Java(c)
                        continue
                    else:
                        #print(c, tokensIteracion)
                        tokensIteracion = []
                        break

                elif reconocedor.estado_actual()[1] == 'OPERATOR':
                    if (tokensIteracion[-1][1] == 'numConst' or tokensIteracion[-1][1] == 'IDENTIFICADOR') and l_char_token[-1] != '!':
                        tokensIteracion.append(
                            ("".join(l_char_token), reconocedor.estado_actual()[1]))
                        l_char_token = [c]
                        reconocedor, reconocedor2 = Automata_Java(), Automata_Java()
                        reconocedor.automata_Java(c)
                        reconocedor2.automata_Java(c)
                        continue
                    elif l_char_token[-1] == '!' and (tokensIteracion[-1][0] in ['!', '(']):
                        tokensIteracion.append(
                            ("".join(l_char_token), reconocedor.estado_actual()[1]))
                        l_char_token = [c]
                        reconocedor, reconocedor2 = Automata_Java(), Automata_Java()
                        reconocedor.automata_Java(c)
                        reconocedor2.automata_Java(c)
                        continue
                    else:
                        # print(c)
                        tokensIteracion = []
                        break

                elif reconocedor.estado_actual()[1] == 'IDENTIFICADOR':
                    if tokensIteracion[-1][1] == 'OPERATOR' or tokensIteracion[-1][0] == '(':
                        tokensIteracion.append(
                            ("".join(l_char_token), reconocedor.estado_actual()[1]))
                        l_char_token = [c]
                        reconocedor, reconocedor2 = Automata_Java(), Automata_Java()
                        reconocedor.automata_Java(c)
                        reconocedor2.automata_Java(c)
                        continue
                    else:
                        tokensIteracion = []
                        break

            else:
                reconocedor.automata_Java(c)
                l_char_token.append(c)

        if len(tokensIteracion) != 0:
            tokensAcumulados += tokensIteracion
    return tokensAcumulados


def tokens_to_Json(secuencia):
    procesado = tokenizador(secuencia)
    json_secuencia = json.dumps(procesado)
    json_array = json.loads(json_secuencia)
    return json_array
