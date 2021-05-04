class Automata_Java():
  def __init__(self):
    self.public = [0, "RECHAZO", "KEYWORD"]
    self.static = [0, "RECHAZO", "KEYWORD"]
    self.void = [0, "RECHAZO", "KEYWORD"]
    self.sout = [0, "RECHAZO", "KEYWORD"]
    self.string = [0, "RECHAZO", "KEYWORD"]
    self.clase = [0, "RECHAZO", "KEYWORD"]
    self.else2 = [0, "RECHAZO", "KEYWORD"]
    self.char = [0, "RECHAZO", "KEYWORD"]
    self.int2 = [0, "RECHAZO", "KEYWORD"]
    self.for2 = [0, "RECHAZO", "KEYWORD"]
    self.if2 = [0, "RECHAZO", "KEYWORD"]
    self.string2 = [0, "RECHAZO", "KEYWORD"]

    self.numConst = [0, "RECHAZO", "numConst"]

    self.operator = [0, "RECHAZO", "OPERATOR"]

    self.separator = [0, "RECHAZO", "SEPARATOR"]

    self.identificador = [0, "RECHAZO", "IDENTIFICADOR"]

    self.charConst = [0, "RECHAZO", "charConst"]

    self.numbers = list(map(str, list(range(0,10)))) #'0','1',...,
    self.abecedario = list(map(chr,range(65,91))) + list(map(chr,range(97,123)))
    self.A=['t','b','n','r','f']

  def automata_Java(self, c):
    #AGREGAR CADA NUEVO AUTÓMATA
    self.automata_public(c)
    self.automata_static(c)
    self.automata_void(c)
    self.automata_sout(c)
    self.automata_string(c)
    self.automata_string2(c)
    self.automata_clase(c)
    self.automata_else2(c)
    self.automata_char(c)
    self.automata_int2(c)
    self.automata_for2(c)
    self.automata_if2(c)

    self.automata_operator(c)

    self.automata_separator(c)

    self.automata_numConst(c)

    self.automata_identificador(c)

    self.automata_charConst(c)

  def estado_actual(self):
    #AGREGAR CADA NUEVO TIPO DE TOKEN RECONOCIBLE
    if self.public[1]=="ACEPTACIÓN" or self.static[1]=="ACEPTACIÓN" or self.void[1]=="ACEPTACIÓN" or self.sout[1]=="ACEPTACIÓN" or self.string[1]=="ACEPTACIÓN" or self.string2[1]=="ACEPTACIÓN" or self.clase[1]=="ACEPTACIÓN" or self.else2[1]=='ACEPTACIÓN' or self.char[1]=='ACEPTACIÓN' or self.int2[1]=='ACEPTACIÓN' or self.for2[1]=='ACEPTACIÓN' or self.if2[1]=='ACEPTACIÓN':
      return "ACEPTACIÓN", "KEYWORD"
    elif self.numConst[1]=='ACEPTACIÓN':
      return "ACEPTACIÓN", "numConst"
    elif self.operator[1]=='ACEPTACIÓN':
        return "ACEPTACIÓN", "OPERATOR"
    elif self.separator[1]=='ACEPTACIÓN':
        return "ACEPTACIÓN", "SEPARATOR"
    elif self.identificador[1]=='ACEPTACIÓN':
        return "ACEPTACIÓN", "IDENTIFICADOR"
    elif self.charConst[1]=='ACEPTACIÓN':
      return "ACEPTACIÓN", "charConst"
    else:
      return "RECHAZO", "NINGUNO"
    
  def caracter_invalido(self,c):
    #AGREGAR CADA NUEVA VARIABLE QUE SE AGREGUE AL CONSTRUCTOR
    if self.public[0]==1 and self.static[0]==1 and self.void[0]==1 and self.sout[0]==1 and self.string[0]==1 and self.string2[0]==1 and self.clase[0]==1 and self.else2[0]==1 and self.char[0]==1 and self.int2[0]==1 and self.for2[0]==1 and self.if2[0]==1 and self.numConst[0]==1 and self.operator[0]==1 and self.separator[0]==1 and self.identificador[0]==1 and self.charConst[0]==1:
      return True
    return False
    
  
  #PRIMER AUTÓMATA DE KEYWORD
  def automata_public(self, c):
    if self.public[0]==0:
      if c=='p':
        self.public[0]='P'
      else:
        self.public[0]=1
    elif self.public[0]=='P':
      if c=='u':
        self.public[0]='U'
      else:
        self.public[0]=1
    elif self.public[0]=='U':
      if c=='b':
        self.public[0]='B'
      else:
        self.public[0]=1
    elif self.public[0]=='B':
      if c=='l':
        self.public[0]='L'
      else:
        self.public[0]=1
    elif self.public[0]=='L':
      if c=='i':
        self.public[0]='I'
      else:
        self.public[0]=1
    elif self.public[0]=='I':
      if c=='c':
        self.public[0]='C'
        self.public[1]="ACEPTACIÓN"
      else:
        self.public[0]=1
    elif self.public[0]=='C':
      self.public[0]=1
      self.public[1]="RECHAZO"
    elif self.public[0]=='1':
      self.public[0]=1

  #SEGUNDO AUTÓMATA DE KEYWORD
  def automata_static(self, c):
    if self.static[0]==0:
      if c=='s':
        self.static[0]='S'
      else:
        self.static[0]=1
    elif self.static[0]=='S':
      if c=='t':
        self.static[0]='T1'
      else:
        self.static[0]=1
    elif self.static[0]=='T1':
      if c=='a':
        self.static[0]='A'
      else:
        self.static[0]=1
    elif self.static[0]=='A':
      if c=='t':
        self.static[0]='T2'
      else:
        self.static[0]=1
    elif self.static[0]=='T2':
      if c=='i':
        self.static[0]='I'
      else:
        self.static[0]=1
    elif self.static[0]=='I':
      if c=='c':
        self.static[0]='C'
        self.static[1]="ACEPTACIÓN"
      else:
        self.static[0]=1
    elif self.static[0]=='C':
      self.static[0]=1
      self.static[1]="RECHAZO"
    elif self.static[0]=='1':
      self.static[0]=1

  #TERCER AUTÓMATA DE KEYWORD
  def automata_void(self, c):
    if self.void[0]==0:
      if c=='v':
        self.void[0]='V'
      else:
        self.void[0]=1
    elif self.void[0]=='V':
      if c=='o':
        self.void[0]='O'
      else:
        self.void[0]=1
    elif self.void[0]=='O':
      if c=='i':
        self.void[0]='I'
      else:
        self.void[0]=1
    elif self.void[0]=='I':
      if c=='d':
        self.void[0]='D'
        self.void[1]='ACEPTACIÓN'
      else:
        self.void[0]=1
    elif self.void[0]=='D':
      self.void[0]=1
      self.void[1]="RECHAZO"
    elif self.void[0]=='1':
      self.void[0]=1

  #CUARTO AUTÓMATA DE KEYWORD  
  def automata_sout(self,c):
    if self.sout[0]==0:
      if c=='S':
        self.sout[0]='S1'
      else:
        self.sout[0]=1
    elif self.sout[0]=='S1':
      if c=='y':
        self.sout[0]='Y'
      else:
        self.sout[0]=1
    elif self.sout[0]=='Y':
      if c=='s':
        self.sout[0]='S2'
      else:
        self.sout[0]=1
    elif self.sout[0]=='S2':
      if c=='t':
        self.sout[0]='T1'
      else:
        self.sout[0]=1
    elif self.sout[0]=='T1':
      if c=='e':
        self.sout[0]='E'
      else:
        self.sout[0]=1
    elif self.sout[0]=='E':
      if c=='m':
        self.sout[0]='M'
      else:
        self.sout[0]=1
    elif self.sout[0]=='M':
      if c=='.':
        self.sout[0]='P1'
      else:
        self.sout[0]=1
    elif self.sout[0]=='P1':
      if c=='o':
        self.sout[0]='O'
      else:
        self.sout[0]=1
    elif self.sout[0]=='O':
      if c=='u':
        self.sout[0]='U'
      else:
        self.sout[0]=1
    elif self.sout[0]=='U':
      if c=='t':
        self.sout[0]='T2'
      else:
        self.sout[0]=1
    elif self.sout[0]=='T2':
      if c=='.':
        self.sout[0]='P2'
      else:
        self.sout[0]=1
    elif self.sout[0]=='P2':
      if c=='p':
        self.sout[0]='P'
      else:
        self.sout[0]=1
    elif self.sout[0]=='P':
      if c=='r':
        self.sout[0]='R'
      else:
        self.sout[0]=1
    elif self.sout[0]=='R':
      if c=='i':
        self.sout[0]='I'
      else:
        self.sout[0]=1
    elif self.sout[0]=='I':
      if c=='n':
        self.sout[0]='N'
      else:
        self.sout[0]=1
    elif self.sout[0]=='N':
      if c=='t':
        self.sout[0]='T3'
        self.sout[1]="ACEPTACIÓN"
      else:
        self.sout[0]=1
    elif self.sout[0]=="T3":
      self.sout[0]=1
      self.sout[1]="RECHAZO"
    elif self.sout[0]==1:
      self.sout[0]=1

  #QUINTO AUTÓMATA DE KEYWORD
  def automata_string(self, c):
    if self.string[0]==0:
      if c=='S':
        self.string[0]='S'
      else:
        self.string[0]=1
    elif self.string[0]=='S':
      if c=='t':
        self.string[0]='T'
      else:
        self.string[0]=1
    elif self.string[0]=='T':
      if c=='r':
        self.string[0]='R'
      else:
        self.string[0]=1
    elif self.string[0]=='R':
      if c=='i':
        self.string[0]='I'
      else:
        self.string[0]=1
    elif self.string[0]=='I':
      if c=='n':
        self.string[0]='N'
      else:
        self.string[0]=1
    elif self.string[0]=='N':
      if c=='g':
        self.string[0]='G'
        self.string[1]="ACEPTACIÓN"
      else:
        self.string[0]=1
    elif self.string[0]=='G':
      self.string[0]=1
      self.string[1]="RECHAZO"
    elif self.string[0]==1:
      self.string[0]=1

  #SEXTO AUTÓMATA DE KEYWORD
  def automata_clase(self, c):
    if self.clase[0]==0:
      if c=='c':
        self.clase[0]='C'
      else:
        self.clase[0]=1
    elif self.clase[0]=='C':
      if c=='l':
        self.clase[0]='L'
      else:
        self.clase[0]=1
    elif self.clase[0]=='L':
      if c=='a':
        self.clase[0]='A'
      else:
        self.clase[0]=1
    elif self.clase[0]=='A':
      if c=='s':
        self.clase[0]='S1'
      else:
        self.clase[0]=1
    elif self.clase[0]=='S1':
      if c=='s':
        self.clase[0]='S2'
        self.clase[1]='ACEPTACIÓN'
      else:
        self.clase[0]=1
    elif self.clase[0]=='S2':
      self.clase[0]=1
      self.clase[1]='RECHAZO'
    elif self.clase[0]==1:
      self.clase[0]=1
    
  #SEPTIMO AUTÓMATA DE KEYWORD
  def automata_else2(self, c):
    if self.else2[0]==0:
      if c=='e':
        self.else2[0]='E1'
      else:
        self.else2[0]=1
    elif self.else2[0]=='E1':
      if c=='l':
        self.else2[0]='L'
      else:
        self.else2[0]=1
    elif self.else2[0]=='L':
      if c=='s':
        self.else2[0]='S'
      else:
        self.else2[0]=1
    elif self.else2[0]=='S':
      if c=='e':
        self.else2[0]='E2'
        self.else2[1]="ACEPTACIÓN"
      else:
        self.else2[0]=1
    elif self.else2[0]=='E2':
      self.else2[0]=1
      self.else2[1]='RECHAZO'
    elif self.else2[0]==1:
      self.else2[0]=1

  #OCTAVO AUTÓMATA DE KEYWORD
  def automata_char(self, c):
    if self.char[0]==0:
      if c=='c':
        self.char[0]='C'
      else:
        self.char[0]=1
    elif self.char[0]=='C':
      if c=='h':
        self.char[0]='H'
      else:
        self.char[0]=1
    elif self.char[0]=='H':
      if c=='a':
        self.char[0]='A'
      else:
        self.char[0]=1
    elif self.char[0]=='A':
      if c=='r':
        self.char[0]='R'
        self.char[1]='ACEPTACIÓN'
      else:
        self.char[0]=1
    elif self.char[0]=='R':
      self.char[0]=1
      self.char[1]='RECHAZO'
    elif self.char[0]==1:
      self.char[0]=1

  #NOVENO AUTÓMATA DE KEYWORD
  def automata_int2(self, c):
    if self.int2[0]==0:
      if c=='i':
        self.int2[0]='I'
      else:
        self.int2[0]=1
    elif self.int2[0]=='I':
      if c=='n':
        self.int2[0]='N'
      else:
        self.int2[0]=1
    elif self.int2[0]=='N':
      if c=='t':
        self.int2[0]='T'
        self.int2[1]='ACEPTACIÓN'
      else:
        self.int2[0]=1
    elif self.int2[0]=='T':
      self.int2[0]=1
      self.int2[1]='RECHAZO'
    elif self.int2[0]==1:
      self.int2[0]=1

  #DÉCIMO AUTÓMATA DE KEYWORD
  def automata_for2(self, c):
    if self.for2[0]==0:
      if c=='f':
        self.for2[0]='F'
      else:
        self.for2[0]=1
    elif self.for2[0]=='F':
      if c=='o':
        self.for2[0]='O'
      else:
        self.for2[0]=1
    elif self.for2[0]=='O':
      if c=='r':
        self.for2[0]='R'
        self.for2[1]='ACEPTACIÓN'
      else:
        self.for2[0]=1
    elif self.for2[0]=='R':
      self.for2[0]=1
      self.for2[1]='RECHAZO'
    elif self.for2[0]==1:
      self.for2[0]=1

  #UNDÉCIMO AUTÓMATA DE KEYWORD
  def automata_if2(self, c):
    if self.if2[0]==0:
      if c=='i':
        self.if2[0]='I'
      else:
        self.if2[0]=1
    elif self.if2[0]=='I':
      if c=='f':
        self.if2[0]='F'
        self.if2[1]='ACEPTACIÓN'
      else:
        self.if2[0]=1
    elif self.if2[0]=='F':
      self.if2[0]=1
      self.if2[1]='RECHAZO'
    elif self.if2[0]==1:
      self.if2[0]=1

  #DUODÉCIMO AUTÓMATA DE KEYWORD
  def automata_string2(self, c):
    if self.string2[0]==0:
      if c=='S':
        self.string2[0]='S'
      else:
        self.string2[0]=1
    elif self.string2[0]=='S':
      if c=='t':
        self.string2[0]='T'
      else:
        self.string2[0]=1
    elif self.string2[0]=='T':
      if c=='r':
        self.string2[0]='R'
      else:
        self.string2[0]=1
    elif self.string2[0]=='R':
      if c=='i':
        self.string2[0]='I'
      else:
        self.string2[0]=1
    elif self.string2[0]=='I':
      if c=='n':
        self.string2[0]='N'
      else:
        self.string2[0]=1
    elif self.string2[0]=='N':
      if c=='g':
        self.string2[0]='G'
      else:
        self.string2[0]=1
    elif self.string2[0]=='G':
      if c=='[':
        self.string2[0]='C1'
      else:
        self.string2[0]=1
    elif self.string2[0]=='C1':
      if c==']':
        self.string2[0]='C2'
        self.string2[1]='ACEPTACIÓN'
      else:
        self.string2[0]=1
    elif self.string2[0]=='C2':
      self.string2[0]=1
      self.string2[1]="RECHAZO"
    elif self.string2[0]==1:
      self.string2[0]=1


  #AUTÓMATA NUMCONST
  def automata_numConst(self, c):
    if self.numConst[0]==0:
      if c=='+':
        self.numConst[0]='S+'
      elif c=='-':
        self.numConst[0]='S-'
      elif c in self.numbers:
        self.numConst[0]='E'
        self.numConst[1]='ACEPTACIÓN'
      elif c=='.':
        self.numConst[0]='P1'
      else:
        self.numConst[0]=1

    elif self.numConst[0]=='S+':
      if c=='-':
        self.numConst[0]='S-'
      elif c in self.numbers:
        self.numConst[0]='E'
        self.numConst[1]='ACEPTACIÓN'
      elif c=='.':
        self.numConst[0]='P1'
      else:
        self.numConst[0]=1
        
    elif self.numConst[0]=='S-':
      if c=='+':
        self.numConst[0]='S+'
      elif c in self.numbers:
        self.numConst[0]='E'
        self.numConst[1]='ACEPTACIÓN'
      elif c=='.':
        self.numConst[0]='P1'
      else:
        self.numConst[0]=1
        
    elif self.numConst[0]=='E':
      if c in self.numbers:
        self.numConst[0]='E'
      elif c=='.':
        self.numConst[0]='P2'
        self.numConst[1]='ACEPTACIÓN'
      else:
        self.numConst[0]=1
        self.numConst[1]='RECHAZO'

    elif self.numConst[0]=='P1' or self.numConst[0]=='P2' or self.numConst[0]=='D':
      if c in self.numbers:
        self.numConst[0]='D'
        self.numConst[1]='ACEPTACIÓN'
      else:
        self.numConst[0]=1
        self.numConst[1]='RECHAZO'

  #AUTÓMATA OPERATOR
  def automata_operator(self, c):
    if self.operator[0]==0:
      if c=='!':
        self.operator[0]='N'
        self.operator[1]='ACEPTACIÓN'
      elif c in ['%','*','+','-','/']:
        self.operator[0]='A1'
        self.operator[1]='ACEPTACIÓN'
      elif c in ['<','>']:
        self.operator[0]='C1'
        self.operator[1]='ACEPTACIÓN'
      elif c=='=':
        self.operator[0]='A2'
        self.operator[1]='ACEPTACIÓN'
      else:
        self.operator[0]=1
    elif self.operator[0]=='N':
      if c=='=':
        self.operator[0]='C2'
      else:
        self.operator[0]=1
        self.operator[1]='RECHAZO'
    elif self.operator[0]=='A1':
      self.operator[0]=1
      self.operator[1]='RECHAZO'
    elif self.operator[0]=='A2':
      if c=='=':
        self.operator[0]='C2'
      else:
        self.operator[0]=1
        self.operator[1]='RECHAZO'
    elif self.operator[0]=='C1':
      if c=='=':
        self.operator[0]='C2'
      else:
        self.operator[0]=1
        self.operator[1]='RECHAZO'
    elif self.operator[0]=='C2':
      self.operator[0]=1
      self.operator[1]='RECHAZO'
    elif self.operator[0]==1:
      self.operator[0]=1

  #AUTÓMATA SEPARATOR
  def automata_separator(self,c):
    if self.separator[0]==0:
      if c in ['(', ')', '{', '}', ';']:
        self.separator[0]='S'
        self.separator[1]='ACEPTACIÓN'
      else:
        self.separator[0]=1
    elif self.separator[0]=='S':
      self.separator[0]=1
      self.separator[1]='RECHAZO'
    elif self.separator[0]==1:
      self.separator[0]=1

  #AUTÓMATA IDENTIFICADOR
  def automata_identificador(self,c):
    if self.identificador[0]==0:
      if c=='_':
        self.identificador[0]='G'
      elif c in self.abecedario:
        self.identificador[0]='A'
        self.identificador[1]='ACEPTACIÓN'
      else:
        self.identificador[0]=1
    elif self.identificador[0]=='G':
      if c=='_' or c in self.abecedario or c in self.numbers:
        self.identificador[0]='A'
        self.identificador[1]='ACEPTACIÓN'
      else:
        self.identificador[0]=1
    elif self.identificador[0]=='A':
      if c=='_' or c in self.abecedario or c in self.numbers:
        self.identificador[0]='A'
      else:
        self.identificador[0]=1
        self.identificador[1]='RECHAZO'
    elif self.identificador[0]==1:
      self.identificador[0]=1

  #AUTÓMATA CHARCONST
  def automata_charConst(self,c):
    if self.charConst[0]==0:
      if c=='"':
        self.charConst[0]='A'
      else:
        self.charConst[0]=1
    elif self.charConst[0]=='A':
      if c=='"':
        self.charConst[0]='B'
        self.charConst[1]='ACEPTACIÓN'
      else:
        self.charConst[0]='A'
    elif self.charConst[0]=='B':
      self.charConst[0]=1
      self.charConst[1]='RECHAZO'
    elif self.charConst[0]==1:
      self.charConst[0]=1
