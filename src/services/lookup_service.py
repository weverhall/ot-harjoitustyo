import socket
import subprocess
from platform import system as platform_os
from uuid import getnode
from urllib.request import urlopen
from urllib.error import URLError
import validators

from repositories.history_repository import(
    history_repository as default_history_repository)


class NetworkLookup:
    def __init__(self, history_repository=default_history_repository):
        self._history_repository = history_repository

    def domain_lookup(self, host):
        if [validators.domain(host), validators.ipv4(host),
                validators.ipv6(host)].count(True) == 0:
            return "Invalid domain name or IP"

        try:
            if validators.domain(host):
                address = str(socket.gethostbyname(host))
                ping = str(NetworkLookup._domain_ping(host))

                self._history_repository.insert(host, address, ping)

                return f"Domain is taken (IPv4: {address})"\
                       f"\n{ping}"

            address = str(socket.gethostbyaddr(host)[0])
            ping = str(NetworkLookup._domain_ping(host))

            self._history_repository.insert(host, address, ping)

            return f"Domain is taken (FQDN: {address})"\
                   f"\n{ping}"

        except socket.gaierror:
            return "Domain is available!"
        except socket.herror:
            return "Domain is available (or PTR record is invalid)"

    def _domain_ping(host):
        try:
            if platform_os().lower() == "windows":
                popen_args = ["ping", "-n", "1", host]
                pinging = subprocess.Popen((popen_args), stdout=subprocess.PIPE)
                output = str(pinging.communicate(timeout=0.85)[0])
                pinging.terminate()
                if "unreachable" in output or "100%" in output:
                    return "Pinging process failed (destination port unreachable)"
                parsed_output = output.split("Minimum = ", 1)[1]
                return f'Latency: {parsed_output.split("ms", 1)[0]} ms'

            popen_args = ["ping", "-c", "1", host]
            pinging = subprocess.Popen((popen_args), stdout=subprocess.PIPE)
            output = str(pinging.communicate(timeout=0.85)[0])
            pinging.terminate()
            if "unreachable" in output or "100%" in output:
                return "Pinging process failed (destination port unreachable)"
            parsed_output = output.split("mdev = ", 1)[1]
            return f'Latency: {parsed_output.split("/", 3)[1]} ms'

        except subprocess.TimeoutExpired:
            pinging.terminate()
            return "Pinging process timed out (severe latency or packet loss)"

    def find_own_public_ip(self):
        try:
            with urlopen("https://checkip.amazonaws.com/") as response:
                public_ip = str(response.read())[2:-3]
        except URLError:
            try:
                with urlopen("https://ipv4.icanhazip.com/") as response:
                    public_ip = str(response.read())[2:-3]
            except URLError:
                public_ip = "127.0.0.1"

        if public_ip == "127.0.0.1" or [validators.ipv6(public_ip),
           validators.ipv4(public_ip)].count(True) == 0:
            return "Failed to fetch public IP address"

        if validators.ipv4(public_ip) is True:
            return f"Public IP: {public_ip} (IPv4)"
        return f"Public IP: {public_ip} (IPv6)"

    def find_local_ip(self):
        try:
            own_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            own_socket.connect(("10.255.255.255", 1))
            local_ip = own_socket.getsockname()[0]
            own_socket.close()
        except OSError:
            local_ip = "127.0.0.1"

        if local_ip == "127.0.0.1" or validators.ipv4(local_ip) is not True:
            return "Failed to fetch local IP address"
        return f"Local IP: {local_ip} (IPv4)"

    def find_mac(self):
        formatted_mac = "".join(c + ":" if i % 2 else c for i,
                                c in enumerate(hex(getnode())[2:].zfill(12)))[:-1]

        if validators.mac_address(formatted_mac) is not True:
            return "Failed to fetch MAC address"

        second_least_significant_bit = str(bin(int(formatted_mac[:2], 16)))[
            2:].zfill(8)[-2]
        if second_least_significant_bit == "0":
            mac_type = "UAA"
        elif second_least_significant_bit == "1":
            mac_type = "LAA"
        return f"MAC: {formatted_mac} ({mac_type})"

    def fetch_history(self):
        return self._history_repository.fetch_all()

    def clear_history(self):
        self._history_repository.clear_all()
