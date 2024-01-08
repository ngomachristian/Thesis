void instantaneous_volatage(){
  for(int i = 0; i<N; i++){
    x = (analogRead(voltagePin)-512);
    //Serial.print("x : ");Serial.println(x);
    V = (0.0000012*x*x*x-0.006457*x*x + 2.685*x - 3.198);
    //Serial.print("V : ");Serial.println(V);
    V2 = V*V;
    Vsquare = Vsquare +V2;
    delay(0.1);
  }
  float Vrms = sqrt(Vsquare/N);
  Serial.print(millis());Serial.print(" # ");
  Serial.println(Vrms);
  delay(0.01);
  Vsquare = 0;
}

void maximum_voltage_method(){
  Vmax = 0;
  Vmin = 1023; //Encodé sur 10bits
  for(int i =0; i<1000;i++){
    sensorValue1 = Vmax;
    sensorValue2 = Vmin;
    sensorValue = analogRead(voltagePin);
    if (sensorValue > sensorValue1){
      Vmax = sensorValue;
      to_reinitialise = false;
    }
    if (sensorValue < sensorValue2){
      Vmin = sensorValue;
      to_reinitialise = false;
    }
    if (to_reinitialise){
      Vmax = sensorValue1;
      Vmin = sensorValue2;
    }
    to_reinitialise = true;
    delay(0.1);
  }
  float x = (Vmax-Vmin);
  V = (0.0000012*x*x*x-0.006457*x*x + 2.685*x - 3.198);
  float Vrms = V/(2*sqrt(2));
  //Serial.print("Vrms : ");
  Serial.println(Vrms);
  delay(2000);

}