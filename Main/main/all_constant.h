#include <Filters.h> //Easy library to do the calculations


//___________Via Filters.h_________//
float testFrequency = 50;                     // test signal frequency (Hz)
float windowLength = 40.0/testFrequency;     // how long to average the signal, for statistist

int Sensor = 0; //Sensor analog input, here it's A0

float intercept = -0.04; // to be adjusted based on calibration testing
float slope = 0.0405; // to be adjusted based on calibration testing
float current_Volts; // Voltage

unsigned long printPeriod = 100; //Refresh rate
unsigned long previousMillis = 0;

unsigned long max_time = 20000;
unsigned long current_time = millis();


int constant_value = 220;

//___________Via Polynomial Regression_________//

int voltagePin = A1;
float V2 = 0;
float Vsquare = 0;
int N = 1000;

float V = 0;
float Vmin = 0;
float Vmax = 0;
float x = 0;

bool to_reinitialise = false;
int sensorValue = 0;
int sensorValue1 = 0;
int sensorValue2 = 0;


