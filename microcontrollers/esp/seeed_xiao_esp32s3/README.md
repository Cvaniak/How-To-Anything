<!-- [Botland](https://botland.com.pl/moduly-wifi-i-bt-esp32/21080-qt-py-esp32-s2-plytka-rozwojowa-z-wifi-i-zlaczem-antenowym-ufl-stemma-qtqwiic-adafruit-5348.html)   -->
<!-- [Kamami](https://kamami.pl/en/esp32/1178261-adafruit-qt-py-esp32-s2-board-with-the-esp32-s2-wifi-module-5325.html)   -->
<!-- [Adafruit](https://learn.adafruit.com/adafruit-qt-py-esp32-s2)   -->
<!---->
<!-- <img src="./qtpy_esp32_s2_back.jpg" width="120"/> -->
<!-- <img src="./qtpy_esp32_s2_front.jpg" width="120"/> -->

# PlatformIO setup

```ini
[env:seeed_xiao_esp32s3]
platform = espressif32
board = seeed_xiao_esp32s3
framework = arduino
upload_port = /dev/ttyACM0

upload_speed = 921600
monitor_speed = 115200

board_build.mcu = esp32s3
board_build.f_cpu = 240000000L
```
