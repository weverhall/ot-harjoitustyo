import socket
from uuid import getnode
from urllib.request import urlopen
from urllib.error import URLError
from dns.resolver import resolve
from dns.resolver import NXDOMAIN
import validators


class NetworkLookup:
    def domain_lookup(self, url):
        if validators.domain(url) is not True:
            return "Invalid domain name"
        try:
            resolve(url)
        except NXDOMAIN:
            return "Domain is available!"
        else:
            site_ip = resolve(url)[0]
            return f"Domain is already taken (host/proxy IP: {site_ip})"

    def find_own_public_ip(self):
        try:
            with urlopen("https://checkip.amazonaws.com/") as response:
                public_ip = str(response.read())[2:-3]
                response.close()
        except URLError:
            try:
                with urlopen("https://ipv4.icanhazip.com/") as response:
                    public_ip = str(response.read())[2:-3]
                    response.close()
            except URLError:
                public_ip = "127.0.0.1"

        if public_ip == "127.0.0.1" or\
            [validators.ipv6(public_ip), validators.ipv4(public_ip)].count(True) == 0:
            return "Failed to fetch public IP address, please try again"
        if validators.ipv4(public_ip) is True:
            return f"Public IP: {public_ip} (IPv4)"
        return f"Public IP: {public_ip} (IPv6)"

    def find_local_ip(self):
        try:
            own_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            own_socket.connect(("10.255.255.255", 1))
            local_ip = own_socket.getsockname()[0]
        except OSError:
            local_ip = "127.0.0.1"
        own_socket.close()

        if local_ip == "127.0.0.1" or validators.ipv4(local_ip) is not True:
            return "Failed to fetch local IP address, please try again"
        return f"Local IP: {local_ip} (IPv4)"

    def find_own_mac(self):
        formatted_mac = "".join(c + ":" if i % 2 else c for i,
        c in enumerate(hex(getnode())[2:].zfill(12)))[:-1]

        if validators.mac_address(formatted_mac) is not True:
            return "Failed to fetch MAC address, please try again"

        second_least_significant_bit = str(bin(int(formatted_mac[:2], 16)))[2:].zfill(8)[-2]
        if second_least_significant_bit == "0":
            mac_type = "UAA"
        elif second_least_significant_bit == "1":
            mac_type = "LAA"
        return f"MAC: {formatted_mac} ({mac_type})"
