// ...

float a = /* Calculé à partir des lectures de calibrage */;
float b = /* Calculé à partir des lectures de calibrage */;

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
        FinalRMSCurrent = (((RMSCurrentMean / 1023) * supplyVoltage) / mVperAmpValue) - manualOffset;

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

