void measure_via_filter_library(){

  RunningStatistics inputStats;                //Easy life lines, actual calculation of the RMS requires a load of coding
  inputStats.setWindowSecs( windowLength );
   
  while( current_time < max_time ) {   
    Sensor = analogRead(voltagePin);  // read the analog in value:
    inputStats.input(Sensor);  // log to Stats function
        
    if((unsigned long)(millis() - previousMillis) >= printPeriod) {
      previousMillis = millis();   // update time every second

      
      current_Volts = intercept + slope * inputStats.sigma(); //Calibartions for offset and amplitude
      current_Volts= current_Volts*(190);                //Further calibrations for the amplitude
      
      //Serial.print( "Voltage: " );
      //Serial.print("Variable 1: " );
      Serial.println( current_Volts ); //Calculation and Value display is done the rest is if you're using an OLED display
      //Serial.print("Variable 2: " );
      //Serial.println( constant_value );

    }
    current_time = millis();
  }
}