
void setup() {
  Serial.begin(9600);
  Serial.setTimeout(1);
}

void loop() {
  Serial.println("Begin");
  delay(5000);
  Serial.println("Processing data...");
  delay(5000);
  Serial.println("Finished");
  delay(5000);
}
