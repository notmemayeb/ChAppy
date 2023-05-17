int TRIGGER = 11;
int ECHO = 8;
int DISTANCIA;
int DURACION;
void setup() {
  // put your setup code here, to run once:
  pinMode(TRIGGER,OUTPUT);  
  pinMode(ECHO,INPUT);
  Serial.begin(9600);
  digitalWrite(TRIGGER,LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(TRIGGER, HIGH);
  delay(10);
  digitalWrite(TRIGGER,LOW);
  DURACION = pulseIn(ECHO,HIGH); //espera por un pulso alto
  //esto mide el tiempo en lo que tarda en recibir respuesta la señal ultrasonica que hemos mandado
  DISTANCIA = DURACION / 59;
  if(DISTANCIA < 20){
    //Serial.write("1");
    Serial.write('A');
  }else{
    Serial.write('Q');
  }
  delay(300);
}
