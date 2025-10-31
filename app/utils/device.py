import threading
import pyudev

devices = []

def add_device(dev):
    props = dict(dev.properties)
    info = {
        "node": dev.device_node,
        "model": props.get("ID_MODEL", "n/a"),
        "vendor": props.get("ID_VENDOR", "n/a"),
        "serial": props.get("ID_SERIAL", "n/a"),
        "job": None
    }

    if not any(d["node"] == info["node"] for d in devices):
        devices.append(info)

def assign(node, job):
    for d in devices:
        if d["node"] != node:
            continue
    
        d["job"] = job
        break

def is_busy(node):
    for d in devices:
        if d["node"] != node:
            continue
        
        if d["job"] is not None:
            return True
        
        break

    return False

def remove_device(dev):
    node = dev.device_node
    for d in devices:
        if d["node"] == node:
            devices.remove(d)
            break

def check():
    global devices
    ctx = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(ctx)
    monitor.filter_by(subsystem="block")

    for d in ctx.list_devices(subsystem="block", DEVTYPE="disk"):
        if d.get("ID_CDROM") == "1":
            add_device(d)

    for action, dev in monitor:
        if dev.get("DEVTYPE") != "disk" or dev.get("ID_CDROM") != "1":
            continue

        if action == "add":
            add_device(dev)
        elif action == "remove":
            remove_device(dev)

def watch():
    t = threading.Thread(target=check, daemon=True)
    t.start()
