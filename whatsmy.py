import socket
import uuid

try:
    import psutil
except ImportError:
    print("Missing module 'psutil'. Install it with: pip install psutil")
    input("\nPress ENTER to exit...")
    exit()

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

def get_mac():
    mac = uuid.getnode()
    mac_address = ':'.join(('%012X' % mac)[i:i+2] for i in range(0, 12, 2))
    return mac_address

def get_dns():
    dns_servers = []
    try:
        for nic, addrs in psutil.net_if_addrs().items():
            for addr in addrs:
                if addr.family == socket.AF_INET and addr.address != '127.0.0.1':
                    dns_servers.append(addr.address)
    except Exception as e:
        print(f"Error getting DNS: {e}")
    return dns_servers

# Main Output
try:
    print(f"IP Address: {get_ip()}")
    print(f"MAC Address: {get_mac()}")

    print("DNS Servers:")
    dns_servers = get_dns()
    if dns_servers:
        for dns in dns_servers:
            print(f" - {dns}")
    else:
        print(" - No DNS servers found.")
except Exception as e:
    print(f"An error occurred: {e}")

input("\nPress ENTER to exit...")
