import platform
import wmi
import psutil
import socket
import datetime
import yaml
from ASCII import get_logo, get_available_logos, get_logo_dimensions

def load_config():
    """Load configuration from config.yml"""
    try:
        with open('config.yml', 'r', encoding='utf-8') as file:
            cfg = yaml.safe_load(file)

        # Validate picked logo
        logo_choice = cfg.get('logo', {}).get('pick', '')
        if logo_choice not in get_available_logos():
            print(f"[warn] Logo '{logo_choice}' not found. Defaulting to windows_simple.")
            cfg['logo']['pick'] = 'windows_simple'

        return cfg

    except FileNotFoundError:
        print("No config.yml found. Using fallback settings.")
        return {
            'logo': {'pick': 'windows_simple'},
            'display': {'show_logo': True, 'logo_side': 'left', 'space_between': 2},
            'show_info': [
                {'name': 'OS', 'show': True},
                {'name': 'Uptime', 'show': True},
                {'name': 'Local IP', 'show': True},
                {'name': 'Motherboard', 'show': True},
                {'name': 'CPU', 'show': True},
                {'name': 'GPU', 'show': True},
                {'name': 'Memory', 'show': True},
                {'name': 'Disk Usage', 'show': True}
            ]
        }


# Gather various bits of system data
def get_system_info():
    details = {}

    # OS platform
    details['OS'] = f"{platform.system()} {platform.release()} {platform.version()}"

    # System uptime
    boot = datetime.datetime.fromtimestamp(psutil.boot_time())
    up_for = datetime.datetime.now() - boot
    days = up_for.days
    hrs = up_for.seconds // 3600
    mins = (up_for.seconds % 3600) // 60
    details['Uptime'] = f"{days}d {hrs}h {mins}m"

    # Local IP (hostname based)
    try:
        hostname = socket.gethostname()
        details['Local IP'] = socket.gethostbyname(hostname)
    except Exception:
        details['Local IP'] = "Not available"

    # Motherboard info (Windows only)
    try:
        board = wmi.WMI().Win32_BaseBoard()[0]
        details['Motherboard'] = f"{board.Manufacturer} {board.Product}"
    except Exception:
        details['Motherboard'] = "Not available"

    # CPU name
    try:
        cpu = wmi.WMI().Win32_Processor()[0]
        details['CPU'] = cpu.Name
    except Exception:
        details['CPU'] = "Not available"

    # GPU name(s)
    try:
        gpus = wmi.WMI().Win32_VideoController()
        details['GPU'] = ', '.join(g.Name for g in gpus if g.Name)
    except Exception:
        details['GPU'] = "Not available"

    # Memory stats
    try:
        mem = psutil.virtual_memory()
        total = mem.total / (1024 ** 3)
        available = mem.available / (1024 ** 3)
        details['Memory'] = f"{available:.1f}GiB / {total:.1f}GiB ({mem.percent:.1f}%)"
    except Exception:
        details['Memory'] = "Not available"

    # Disk usage (loop all partitions)
    try:
        partitions = psutil.disk_partitions()
        disk_lines = []
        for part in partitions:
            if not part.fstype:
                continue
            try:
                usage = psutil.disk_usage(part.mountpoint)
                used = usage.used / (1024 ** 3)
                total = usage.total / (1024 ** 3)
                disk_lines.append(f"{part.device} {used:.1f}GiB / {total:.1f}GiB ({usage.percent:.1f}%)")
            except Exception:
                disk_lines.append(f"{part.device} - inaccessible")
        details['Disk Usage'] = "\n".join(disk_lines)
    except Exception:
        details['Disk Usage'] = "Not available"

    return details

# Print the logo and system info side by side
def display_info():
    config = load_config()
    sys_info = get_system_info()

    logo_name = config['logo']['pick']
    logo_lines = get_logo(logo_name)
    gap = config.get('display', {}).get('space_between', 2)

    # Figure out what info lines to show
    info_lines = []
    for item in config.get('show_info', []):
        if item.get('show'):
            label = config.get('labels', {}).get(item['name'], item['name'])
            val = sys_info.get(item['name'], "N/A")
            info_lines.append(f"{label}: {val}")

    print("\n")  # breathing room

    max_lines = max(len(logo_lines), len(info_lines))
    for i in range(max_lines):
        line = logo_lines[i] if i < len(logo_lines) else " " * 20
        info = info_lines[i] if i < len(info_lines) else ""
        print(f"{line}{' ' * gap}{info}")

    print("\n")

# Run the whole thing
if __name__ == "__main__":
    display_info()
