# How to printer in Manjaro
This is not best way probably but it works really well:
* Start with this commands:
```bash
sudo systemctl disable --now org.cups.cupsd.socket
sudo systemctl disable --now org.cups.cupsd.service
sudo systemctl disable --now org.cups.cupsd.path
sudo systemctl enable --now cups.service
sudo systemctl enable --now cups.socket
sudo systemctl enable --now cups.path

yay -S avahi
sudo systemctl enable --now avahi-daemon.service
```
* Then I install:
```bash
yay -S manjaro-printer
sudo gpasswd -a yourusername sys
```
* You may need drivers for your printer so search for them and install, for example:
```bash
yay -S brother-dcpl3550cdw
```
Then in menu I search for `HP Device Manager` and I open with it `localhost:631`. From there it is quite self explanatory:  
~[alt text](./HpManager.png)    
~[alt text](./localhost.png)  

# Scanner
If you want to scan something, add your printer with previous steps and then install:
```bash
yay -S simple-scan
```
find `Document scanner` and thats all.


