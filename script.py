import datetime

net_iface = 'wlan0'

def main( ):
  mac_addr = open(f'/sys/class/net/{net_iface}/address').readline( ).strip( ).replace(':', '-')
  device_id = open('/home/pi/apDevice/deviceID').readline( ).strip( )
  time = datetime.datetime.now( ).strftime('%d-%m-%Y_%H-%M-%S')
  f_desc = open('/home/pi/apDevice/data/' + f'{mac_addr}___{device_id}___{time}', 'w')
  f_desc.close( )

if __name__ == '__main__':
  main( )
else:
  print('This module is supposed to be run as __main__')