# A fatal error occurred: Could not open /dev/ttyACM0, the port doesn't exist

* In theory you should have installed [99-platformio-udev.rules](https://docs.platformio.org/en/latest/core/installation/udev-rules.html#platformio-udev-rules)

But this does not work for me.

My final solution was:

```bash
sudo chmod a+rw /dev/ttyACM0
```
