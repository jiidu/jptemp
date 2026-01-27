#include <LiquidCrystal.h>

// DFRobot LCD Shield
LiquidCrystal lcd(8, 9, 4, 5, 6, 7);

void setup() {
    Serial.begin(9600); 
    lcd.begin(16, 2);  // Set LCD size (16 x 2)
    lcd.print("JP Temp 1.0:");
    lcd.setCursor(0,2);
    lcd.print("NO DATA"); // Show this when there is no serial data
}

void loop() {
    if (Serial.available()) {
        String temperature = Serial.readStringUntil('\n');

        // Debugging
        Serial.print("Received: ");
        Serial.println(temperature);

        lcd.setCursor(0, 1); 
        lcd.clear(); 
        lcd.print ("JP Temp 1.0");
        lcd.setCursor(0, 2);
        
        if(temperature != 0){
          lcd.print(temperature);
        }
        else{
          lcd.print("NO DATA");
        }
    }
    
}
