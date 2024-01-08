/* This code works with ZMPT101B AC voltage sensor module and 128x32 OLED display
 * It permits you to measure any AC voltage up to 250V, BE CAREFUL !!!
 * The functions from Filters library permits you to calculate the True RMS of a signal
 * Refer to www.surtrTech.com or SurtrTech YouTube channel for more details
 */

#include "all_constant.h"

void setup() {
  Serial.begin(9600);    // start the serial port
  delay(1000);

}

void loop() {
  
 //measure_via_filter_library();
  //instantaneous_volatage();
  //maximum_voltage_method();
  //Serial.println(analogRead(voltagePin));

  read_current();
  //delay(500);

}
