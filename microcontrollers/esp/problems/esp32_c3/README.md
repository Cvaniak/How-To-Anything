# Problems with ESP32 C3

When you are not connect with ESP32 C3 with Serial Port but you have any
`Serial.print` statement then it slows down.
[Here is issue](https://github.com/espressif/arduino-esp32/issues/6983)

To solve this:

```cpp
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.setTxTimeoutMs(0);   // <<<====== solves this issue of delay
}
```
