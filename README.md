# Data Collection Device WebGUI

[!Streaming & Recording]
To stream preview and record from one camera at the same time it is necessary to generate two v4l2loopback virtual cameras. This could be ahived in three steps:

1. Install v4l2loopback Kernel Module and Utils.
```bash
sudo apt install v4l2loopback-dkms v4l2loopback-utils
```

2. Load v4l2loopback Module at Boot.
```bash
Create the following file /etc/modules-load.d/v4l2loopback.conf
Add the following line to the file:
v4l2loopback
```

3. Specify Settings and Devices.
```bash
Create the following file /etc/modprobe.d/v4l2loopback.conf
Add the following line to the file:
options v4l2loopback devices=2 video_nr=100,101 exclusive_caps=1,1 buffers=4
