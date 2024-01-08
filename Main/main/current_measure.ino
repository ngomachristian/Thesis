void read_current(){
  int meas = analogRead(A1)-analogRead(A0);
  //Serial.print(millis());Serial.print(" # ");
  Serial.println(meas);
  delay(10);
}