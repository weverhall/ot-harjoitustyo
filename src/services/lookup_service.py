import uuid
import socket
import sys
import whois
import validators
import dns.resolver


class NetworkLookup:
    def domain_lookup(self, url):
        if validators.domain(url) is not True:
            return "Invalid domain name, try again"
        try:
            if whois.whois(url).domain_name is None:
                sys.exit()
        except:
            return "Domain is available!"
        try:
            site_ip = str(dns.resolver.resolve(url)[0])
            return f"Domain is already taken (host/proxy IP: {site_ip})"
        except:
            return "Domain is already taken"

    def find_own_ip(self):
        own_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            own_socket.connect(("10.255.255.255", 1))
            own_ip = own_socket.getsockname()[0]
        except:
            own_ip = "127.0.0.1"
        own_socket.close()

        if own_ip == "127.0.0.1" or\
        [validators.ipv6(own_ip), validators.ipv4(own_ip)].count(True) == 0:
            return "Failed to fetch IP address"
        if own_ip[:8] == "192.168." or own_ip[:7] == "172.16."\
        or own_ip[:7] == "172.17." or own_ip[:7] == "172.18."\
        or own_ip[:7] == "172.19." or own_ip[:7] == "172.30."\
        or own_ip[:7] == "172.31." or own_ip[:5] == "172.2"\
        or own_ip[:3] == "10.":
            return f"IP: {own_ip} (private)"
        return f"IP: {own_ip} (public)"

    def find_own_mac(self):
        formatted_mac = ":".join(['{:02x}'.format((uuid.getnode() >> i) & 0xff)
        for i in range(0,8*6,8)][::-1])

        if validators.mac_address(formatted_mac) is not True:
            return "Failed to fetch MAC address"
        return f"MAC: {formatted_mac}"
