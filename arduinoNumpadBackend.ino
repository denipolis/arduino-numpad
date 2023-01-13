#include <Keypad.h>

// CONFIGURATION

#define ROWS 4
#define COLS 4


char keys[ROWS][COLS] = {
  {'1', '2', '3', 'A'},
  {'4', '5', '6', 'B'},
  {'7', '8', '9', 'C'},
  {'*', '0', '#', 'D'}
};

const byte rowPins[ROWS] = {9, 8, 7, 6};
const byte colPins[COLS] = {5, 4, 3, 2};

// CONFIGURATION

Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

void setup() {
  Serial.begin(9600);
}

void loop() {
  char key = keypad.getKey();

  char lastKey = ' ';

  if(key){
    Serial.write("pressed.");
    Serial.write(key);
    lastKey = key;
    Serial.write("\n");
  }
}

