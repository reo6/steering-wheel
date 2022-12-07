#include <TimedAction.h>
#include <IRremote.hpp>
#define RV_PIN 7
#define PEDAL1_PIN 9
#define PEDAL2_PIN 8
#define IR_DELAY 10
#define PEDAL_DELAY 5


void logIRMessages() {
    if (IrReceiver.decode()) {
        if (IrReceiver.decodedIRData.decodedRawData != 0) {
            Serial.println(IrReceiver.decodedIRData.decodedRawData);
        }
        IrReceiver.resume();
    }
}

int pedal1State = HIGH;
int pedal2State = HIGH;
int currentPedal1 = HIGH;
int currentPedal2 = HIGH;

void logPedalStates() {
    currentPedal1 = digitalRead(PEDAL1_PIN);
    currentPedal2 = digitalRead(PEDAL2_PIN);

    if(currentPedal1 != pedal1State) {
        if(currentPedal1 == HIGH) {
            Serial.println("-10");
        } else {
            Serial.println("-11");
        }
    }

    pedal1State = currentPedal1;

    if(currentPedal2 != pedal2State) {
        if(currentPedal2 == HIGH) {
            Serial.println("-20");
        } else {
            Serial.println("-21");
        }
    }

    pedal2State = currentPedal2;

}



TimedAction irAction = TimedAction(IR_DELAY, logIRMessages);
TimedAction pedalAction = TimedAction(PEDAL_DELAY, logPedalStates);

void setup() {
    pinMode(PEDAL1_PIN, INPUT_PULLUP);
    pinMode(PEDAL2_PIN, INPUT_PULLUP);
    
    Serial.begin(9600);
    IrReceiver.begin(RV_PIN, ENABLE_LED_FEEDBACK);
}

void loop() {
    irAction.check();
    pedalAction.check();
}
