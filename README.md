# Data Collection Device WebGUI (Notes)

## Streaming & Recording
To stream preview and record from one camera at the same time it is necessary to generate two ```v4l2loopback``` virtual cameras. This could be ahived in three steps:

> [!IMPORTANT]
> **OS used for installation:**
> ```bash
> hwuser@hwdev22:~ $ cat /etc/os-release
> PRETTY_NAME="Debian GNU/Linux 12 (bookworm)"
> NAME="Debian GNU/Linux"
> VERSION_ID="12"
> VERSION="12 (bookworm)"
> VERSION_CODENAME=bookworm
> ID=debian
> HOME_URL="https://www.debian.org/"
> SUPPORT_URL="https://www.debian.org/support"
> BUG_REPORT_URL="https://bugs.debian.org/"
> 
> hwuser@hwdev22:~ $ uname -a
> Linux hwdev22 6.6.74+rpt-rpi-2712 #1 SMP PREEMPT Debian 1:6.6.74-1+rpt1 (2025-01-27) aarch64 GNU/Linux
> 
> hwuser@hwdev22:~ $ /etc/rpi-issue
> Raspberry Pi reference 2024-11-19
> Generated using pi-gen, https://github.com/RPi-Distro/pi-gen, 891df1e21ed2b6099a2e6a13e26c91dea44b34d4, stage4
> ```

**1. Install ```v4l2loopback``` Kernel Module and Utils - [https://github.com/v4l2loopback/v4l2loopback](https://github.com/v4l2loopback/v4l2loopback)**
```bash
sudo apt install v4l2loopback-dkms v4l2loopback-utils
Official Repository - 
```

**2. Load ```v4l2loopback``` Module at Boot.**
```bash
Create the following file:
/etc/modules-load.d/v4l2loopback.conf

Add the following line to the file:
v4l2loopback
```

**3. Specify Settings and Devices.**
```bash
Create the following file:
/etc/modprobe.d/v4l2loopback.conf

Add the following line to the file:
options v4l2loopback devices=2 video_nr=100,101 exclusive_caps=1,1 buffers=4
```
