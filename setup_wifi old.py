import os
import argparse

import os

def configure_wifi(ssid, password):
    config_lines = [
        'ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev',
        'update_config=1',
        'country=US',
        '\n',
        'network={',
        '\tssid="{}"'.format(ssid),
        '\tpsk="{}"'.format(password),
        '}'
        ]
    config = '\n'.join(config_lines)
    
    #give access and writing. may have to do this manually beforehand
    os.popen("sudo chmod a+w /etc/wpa_supplicant/wpa_supplicant.conf")
    
    #writing to file
    with open("/etc/wpa_supplicant/wpa_supplicant.conf", "w") as wifi:
        wifi.write(config)
    
    print("Wifi config added. Refreshing configs")
    ## refresh configs
    os.popen("sudo wpa_cli -i wlan0 reconfigure")

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Setup Wi-Fi configuration on Raspberry Pi.')
    parser.add_argument('ssid', type=str, help='SSID of the Wi-Fi network')
    parser.add_argument('password', type=str, help='Password of the Wi-Fi network')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Setup Wi-Fi with the provided arguments
    configure_wifi(args.ssid, args.password)

if __name__ == "__main__":
    main()