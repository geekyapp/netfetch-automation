from netmiko import ConnectHandler
 
def get_fortinet_info(ip):
    device = {
        'device_type': 'fortinet',
        'host': ip,
        'username': 'sa_atm_cisco',  # update if needed
        'password': "(E''h9d?Hn\\[\"}+g",
    }
 
    try:
        conn = ConnectHandler(**device)
        policy = conn.send_command("show firewall policy")
        hostname = conn.send_command("get system status | grep Hostname")
        bgp = conn.send_command("get router info bgp summary")
        ha = conn.send_command("get system ha status")
        arp = conn.send_command("get system arp")
        vpn_detail = conn.send_command("get vpn ipsec tunnel details")
        vpn_summary = conn.send_command("get vpn ipsec tunnel summary")
        sdwan = conn.send_command("diagnose sys sdwan health-check")
        sdwanservice = conn.send_command("diagnose sys sdwan service")
        sdwanmember = conn.send_command("diagnose sys sdwan member")
        conn.disconnect()
    except Exception as e:
        return {"error": str(e)}
 
    return {
        "hostname": hostname,
        "policy": policy,
        "sdwanservice": sdwanservice,
        "sdwanmember": sdwanmember,
        "bgp": bgp,
        "ha": ha,
        "arp": arp,
        "vpn_detail": vpn_detail,
        "vpn_summary": vpn_summary,
        "sdwan": sdwan
    }
