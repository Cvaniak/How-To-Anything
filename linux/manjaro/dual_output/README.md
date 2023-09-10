# How to enable dual output on Manjaro

If you want to listen from two Bluetooth devices at the same time:

## Pair and Connect Devices:

Pair and connect your Bluetooth devices via the Bluetooth settings in Manjaro.

## Install paprefs:

This is a PulseAudio Preferences utility that provides an easy way to enable simultaneous output.

```bash
yay -S paprefs
```

## Launch paprefs:

You can launch it by typing paprefs in the terminal or searching for it in the application menu.

## Enable Simultaneous Output:

Once paprefs is open, go to the "Simultaneous Output" tab and check the option to add a virtual output device for simultaneous output.

## Restart PulseAudio: 
To apply changes. (may not be needed)

```bash
pulseaudio -k
pulseaudio --start
```

## Select the New Virtual Output:

Open the sound settings and select the new virtual device as the output device.

## Adjust Volume Levels for Each Device:

You can fine-tune the volume levels for each Bluetooth device individually via pavucontrol.

```bash
yay -S pavucontrol
pavucontrol
```

Now you should be able to play audio through multiple Bluetooth devices simultaneously.

