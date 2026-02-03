from rich.console import Console
from rich.live import Live
from rich.table import Table
import psutil
import time

console = Console()

def get_table():
    table = Table()
    table.add_column("Metric")
    table.add_column("Value")

    # CPU
    table.add_row("CPU Usage", f"{psutil.cpu_percent()} %")
    table.add_row("CPU Freq", f"{psutil.cpu_freq().current:.2f} MHz")

    # RAM
    ram = psutil.virtual_memory()
    table.add_row("RAM Usage", f"{ram.percent} % ({ram.used/1024**3:.2f}/{ram.total/1024**3:.2f} GB)")

    # Battery
    battery = psutil.sensors_battery()
    battery_status = f"{battery.percent}% Plugged:{battery.power_plugged}" if battery else "Not Available"
    table.add_row("Battery", battery_status)

    return table

with Live(get_table(), refresh_per_second=1) as live:
    while True:
        time.sleep(1)
        live.update(get_table())
