import serial
conexao = ""
for porta in range(10):
    try:
        conexao = serial.Serial("COM"+str(porta), 115200, timeout=0.5)
        print("Conectado na porta ", conexao.portstr)
        break
    except serial.SerialException:
        pass
if conexao != "":
    acao=input("Digite:\n<L> Para Ligar\n<D> Para Desligar: ").upper()
    while acao == "L" or acao == "D":
      if acao == "L":
        conexao.write(b'1')
      else:
        conexao.write(b'0')
      acao=input("Digite:\n<L> Para Ligar\n<D> Para Desligar: ").upper()
    conexao.close()
    print("Conexão encerrada!")
else:
  print("Sem portas disponíveis!?")


''' Código Arduino Sketch
void setup() 
{
  pinMode(10, OUTPUT);
  Serial.begin(115200)
}

void loop() 
{
  int interalo_pisca = 4000;
  digitalWrite(10, LOW);
  Serial.write('0');
  delay(interalo_pisca);
  digitalWrite(10, HIGH);
  Serial.write('1');
  delay(interalo_pisca);
}
'''
