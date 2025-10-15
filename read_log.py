#!/usr/bin/env python3
import re
import sys
import time
import subprocess

def monitor_log_for_mac(log_file_path):
    """
    Monitor a log file for MAC addresses and execute a command when found.
    
    Args:
        log_file_path: Path to the log file to monitor
    """
    # MAC address pattern (matches formats like AA:BB:CC:DD:EE:FF or AA-BB-CC-DD-EE-FF)
    mac_pattern = re.compile(r'([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})')
    
    try:
        with open(log_file_path, 'r') as log_file:
            # Move to the end of the file to start monitoring new entries
            log_file.seek(0, 2)
            
            print(f"Monitoring {log_file_path} for MAC addresses...")
            
            while True:
                line = log_file.readline()
                
                if not line:
                    # No new line, wait briefly before checking again
                    time.sleep(0.1)
                    continue
                
                # Search for MAC address in the line
                match = mac_pattern.search(line)
                
                if match:
                    mac_address = match.group(0)
                    print(f"MAC Address found: {mac_address}")
                    
                    # Execute bash command (placeholder)
                    # Replace with your actual command
                    command = f"echo 'Processing MAC: {mac_address}'"
                    
                    try:
                        result = subprocess.run(command, shell=True, capture_output=True, text=True)
                        print(f"Command output: {result.stdout.strip()}")
                    except Exception as e:
                        print(f"Error executing command: {e}")
    
    except FileNotFoundError:
        print(f"Error: Log file '{log_file_path}' not found.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <log_file_path>")
        sys.exit(1)
    
    log_file = sys.argv[1]
    monitor_log_for_mac(log_file)
