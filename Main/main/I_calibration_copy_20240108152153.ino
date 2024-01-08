// AC & DC Current Sensor 

// Note Summary
// Note :  Safety is very important when dealing with electricity. We take no responsibilities while you do it at your own risk.
// Note :  This AC & DC  Current Sensor Code is for HSTS016L Hall effect split core current transformer use.
// Note :  The value shown in Serial Monitor / LCD Display is refreshed every second and measurement value is the average value of 4000 sample readings for nearly a second.
// Note :  The current measured is the Root Mean Square (RMS) value.
// Note :  The analog value per sample is squared and accumulated for every 4000 samples before being averaged. The averaged value is then getting square-rooted.
// Note :  The unit provides reasonable accuracy and may not be comparable with other expensive branded and commercial product.
// Note :  All credit shall be given to Solarduino.

/*/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////*/////////////*/

        /* 0- General */

                        

        /* 1- AC Current Measurement */

        int currentAnalogInputPin = A1;             // Which pin to measure Current Value (A0 is reserved for LCD Display Shield Button function)
        int calibrationPin = A2;                    // Which pin to calibrate offset middle value
        float manualOffset = 0.00;                  // Key in value to manually offset the initial value
        float mVperAmpValue = 31.25;                 // If using "Hall-Effect" Current Transformer, key in value using this formula: mVperAmp = maximum voltage range (in milli volt) / current rating of CT
                                                    // For example, a 20A Hall-Effect Current Transformer rated at 20A, 2.5V +/- 0.625V, mVperAmp will be 625 mV / 20A = 31.25mV/A 
                                                    // For example, a 50A Hall-Effect Current Transformer rated at 50A, 2.5V +/- 0.625V, mVperAmp will be 625 mV / 50A = 12.5 mV/A
        float supplyVoltage = 5000;                 // Analog input pin maximum supply voltage, Arduino Uno or Mega is 5000mV while Arduino Nano or Node MCU is 3300mV
        float offsetSampleRead = 0;                 /* to read the value of a sample for offset purpose later */
        float currentSampleRead  = 0;               /* to read the value of a sample including currentOffset1 value*/
        float currentLastSample  = 0;               /* to count time for each sample. Technically 1 milli second 1 sample is taken */
        float currentSampleSum   = 0;               /* accumulation of sample readings */
        float currentSampleCount = 0;               /* to count number of sample. */
        float currentMean ;                         /* to calculate the average value from all samples, in analog values*/ 
        float RMSCurrentMean ;                      /* square roof of currentMean, in analog values */   
        float FinalRMSCurrent ;                     /* the final RMS current reading*/
        
    



void setup()                                              /*codes to run once */

{                                      

        /* 0- General */
        
        Serial.begin(9600);                               /* to display readings in Serial Monitor at 9600 baud rates */

 

}






float a =0.844 /* Calculé à partir des lectures de calibrage */;
float b =0.496 /* Calculé à partir des lectures de calibrage */;

void loop() {
    // ...

    if(micros() >= currentLastSample + 20) {
        currentSampleRead = a * (analogRead(currentAnalogInputPin) - analogRead(calibrationPin)) + b;
        currentSampleSum = currentSampleSum + sq(currentSampleRead);
        currentSampleCount = currentSampleCount + 1;
        currentLastSample = micros();
    }

    if(currentSampleCount == 100) {
        currentMean = currentSampleSum / currentSampleCount;
        RMSCurrentMean = sqrt(currentMean);
        FinalRMSCurrent = RMSCurrentMean;
        //FinalRMSCurrent = (((RMSCurrentMean / 1023) * supplyVoltage) / mVperAmpValue) - manualOffset;

        // Appliquer la correction de calibration
        FinalRMSCurrent = a * FinalRMSCurrent + b;

        if(FinalRMSCurrent <= (625 / mVperAmpValue / 100)) {
            FinalRMSCurrent = 0;
        }

          Serial.print(" The Current RMS value is: ");
            Serial.print(FinalRMSCurrent);
            Serial.println(" A ");
            currentSampleSum =0;                                                                              /* to reset accumulate sample values for the next cycle */
            currentSampleCount=0;  
    }

    // ...
}

