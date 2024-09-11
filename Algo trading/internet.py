import requests
import time
import subprocess

def is_internet_connected(url='https://www.google.com/', timeout=5):
    try:
        # Make a request to a reliable website
        response = requests.get(url, timeout=timeout)
        # If the response status code is 200, return True

        return response.status_code == 200
    except requests.RequestException as e:
        # If there is any exception, return False
        print(f"Internet check failed: {e}")
        return False
    
def search_and_connect_to_wifi(target_ssid):
    try:
        # List available Wi-Fi networks
        result = subprocess.run(['netsh', 'wlan', 'show', 'networks'], capture_output=True, text=True)
        networks = result.stdout
        
        # Check if the target SSID is in the list of available networks
        if target_ssid in networks:
            print(f"Network '{target_ssid}' found. Attempting to connect.")
            # Connect to the target SSID
            connect_result = subprocess.run(['netsh', 'wlan', 'connect', f'name={target_ssid}'], capture_output=True, text=True)
            if connect_result.returncode == 0:
                print(f"Successfully connected to '{target_ssid}'.")
                return True
            else:
                print(f"Failed to connect to '{target_ssid}': {connect_result.stderr}")
                return False
        else:
            print(f"Network '{target_ssid}' not found.")
            return False
    except Exception as e:
        print(f"An error occurred while trying to connect to Wi-Fi: {e}")
        return False
    

