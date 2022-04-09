import uuid, socket, sys, whois, validators
from iplookup import iplookup


class NetworkLookup:
    def domain_lookup(self, url):
        if validators.domain(url) != True:
            return "Invalid domain name, try again"
        else:
            try:
                if whois.whois(url).domain_name == None:
                    sys.exit()  
            except:
                return "Domain is available!"
            else:
                try:
                    site_ip = str(iplookup.iplookup(url)[0])
                    return f"Domain is already taken (host/proxy IP: {site_ip})"
                except:
                    return "Domain is already taken"

    def find_own_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:       
            s.connect(("10.255.255.255", 1))
            ip = s.getsockname()[0]
        except:
            ip = "127.0.0.1"
        s.close()

        if ip[:8] == "192.168." or ip[:7] == "172.16."\
        or ip[:7] == "172.17." or ip[:7] == "172.18."\
        or ip[:7] == "172.19." or ip[:7] == "172.30."\
        or ip[:7] == "172.31." or ip[:5] == "172.2"\
        or ip[:3] == "10.":            
            return f"IP: {ip} (private)"
        elif ip == "127.0.0.1":
            return "Failed to fetch IP address"
        else:
            return f"IP: {ip} (public)"

    def find_own_mac(self):
        formatted_mac = ":".join(['{:02x}'.format((uuid.getnode() >> i) & 0xff)
        for i in range(0,8*6,8)][::-1])

        if validators.mac_address(formatted_mac) != True:
            return "Failed to fetch MAC address"
        else:
            return f"MAC: {formatted_mac}"