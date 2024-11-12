import os
import subprocess

def setup_wifi(ssid, password):
    # Define the path to the wpa_supplicant configuration file
    wpa_supplicant_conf = "/etc/wpa_supplicant/wpa_supplicant.conf"

    # Prepare the Wi-Fi configuration content
    wifi_config = f"""
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=US

network={{
    ssid="{ssid}"
    psk="{password}"
}}
"""

    # Write the Wi-Fi configuration to wpa_supplicant.conf
    try:
        with open(wpa_supplicant_conf, "w") as file:  # Overwrite the file
            file.write(wifi_config)
        print("Wi-Fi credentials written successfully.")
    except Exception as e:
        print(f"Error writing Wi-Fi credentials: {e}")
        return

    # Restart the network interface to apply changes
    try:
        # Restarting the wpa_supplicant service to apply changes
        subprocess.run(["sudo", "systemctl", "restart", "wpa_supplicant"], check=True)
        # Restart the dhcpcd service to obtain an IP address
        subprocess.run(["sudo", "systemctl", "restart", "dhcpcd"], check=True)
        print("Network services restarted. Attempting to connect...")
    except subprocess.CalledProcessError as e:
        print(f"Error restarting network services: {e}")

# Usage example
if __name__ == "__main__":
    ssid = input("Enter the Wi-Fi SSID: ")
    password = input("Enter the Wi-Fi password: ")
    setup_wifi(ssid, password)