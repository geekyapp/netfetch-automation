from netmiko import ConnectHandler

def get_device_info(ip):
    device = {
        'device_type': 'cisco_ios',
        'host': ip,
        'username': 'sa_atm_cisco',
        'password': "(E''h9d?Hn\\[\"}+g",
    }

    try:
        conn = ConnectHandler(**device)
        ospf = conn.send_command("show ip ospf neighbor")
        ospf2 = conn.send_command("show ip ospf interface brief")
        ospf3 = conn.send_command("sh ip ospf neighbor detail")
        arp = conn.send_command("show ip arp")
        cdp = conn.send_command("show cdp neighbors detail")
        bgp = conn.send_command("show ip bgp summary")
        interfaces = conn.send_command("show ip interface brief")
        interfaces02 = conn.send_command("show int desc")
        hostname = conn.send_command("show runn | i hostname")
        version = conn.send_command("show version | i Version")
        reloadtime =  conn.send_command("show version  | i restarted")
        reloadreason = conn.send_command("show version  | i reload")
        uptime = conn.send_command("show version | i uptime")
        cpu = conn.send_command("show processes cpu history")
        memory = conn.send_command("show memory statistics")
        pdu = conn.send_command("show power")
        conn.disconnect()
    except Exception as e:
        return {"error": str(e)}

    return {
        "arp": arp,
        "cdp": cdp,
        "bgp": bgp,
        "hostname": hostname,
        "ospf": ospf,
        "ospf2": ospf2,
        "ospf3": ospf3,
        "intdesc": interfaces02,
        "version": version,
        "reloadtime": reloadtime,
        "reloadreason": reloadreason,
        "uptime": uptime,
        "cpu": cpu,
        "memory": memory,
        "pdu": pdu,
        "interfaces": interfaces
    }

