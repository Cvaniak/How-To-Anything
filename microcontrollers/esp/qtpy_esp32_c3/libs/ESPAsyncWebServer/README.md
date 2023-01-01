# ESPAsyncWebServer

In this library for ESP32-C3 there is error in file like writen here [Issue](https://github.com/me-no-dev/ESPAsyncWebServer/issues/1101).  
To fix this replace in `.pio/libdeps/adafruit_qtpy_esp32c3/ESP Async WebServer/src/AsyncWebSocket.cpp` in line `832`:

```cpp

IPAddress AsyncWebSocketClient::remoteIP() {
    if(!_client) {
        /* return IPAddress(0U); */ delete this
        return IPAddress((uint32_t)0); // and replace with that
    }
    return _client->remoteIP();
}
```
