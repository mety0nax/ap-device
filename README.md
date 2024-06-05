# apDevice

> [!IMPORTANT]
> After successfull installation, do not forget to manually:
> * Reset crontab by executing and saving crontab file : ``` sudo crontab -e ```
> * Rename the data folder ```./apDevice/data_<MAC_ADDRESS>``` :
> ```bash
> mv ./apDevice/data_XX-XX-XX-XX-XX ./apDevice/data_$(cat /sys/class/net/wlan0/address | tr ':' '-')
> ```

Global TODOs:
- [x] File transfer functionality via Rsync (do not add keys or any credentials)
- [x] Create a script that simulates data generation (testing)
- [x] Create separate installation script
- [ ] Restart cron and load new config after installation
- [ ] Add functionality to verify that current data folder is using the device MAC (maybe on each boot)
