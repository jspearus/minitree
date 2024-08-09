import os
import argparse

def setup_wifi(ssid, password):
    # Path to the wpa_supplicant.conf file
    wpa_supplicant_conf = '/etc/wpa_supplicant/wpa_supplicant.conf'
    
    # Check if the script is run with superuser privileges
    if os.geteuid() != 0:
        raise PermissionError("This script must be run with superuser privileges.")
    
    # Network configuration to be added
    network_config = f"""
network={{
    ssid="{ssid}"
    psk="{password}"
    key_mgmt=WPA-PSK
}}
"""
    
    try:
        # Read the current configuration
        with open(wpa_supplicant_conf, 'r') as file:
            current_config = file.read()
        
        # Append the new network configuration if not already present
        if network_config.strip() not in current_config:
            with open(wpa_supplicant_conf, 'a') as file:
                file.write(network_config)
            
            print("Network configuration added. Restarting networking service...")
            
            # Restart the dhcpcd service to apply changes
            os.system('sudo systemctl restart dhcpcd')
        else:
            print("Network configuration already present.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Setup Wi-Fi configuration on Raspberry Pi.')
    parser.add_argument('ssid', type=str, help='SSID of the Wi-Fi network')
    parser.add_argument('password', type=str, help='Password of the Wi-Fi network')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Setup Wi-Fi with the provided arguments
    setup_wifi(args.ssid, args.password)

if __name__ == "__main__":
    main()