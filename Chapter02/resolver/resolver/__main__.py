"""The executable package!
if you execute this package, you can get the ip of the corresponding website"""
import sys
from .resolver import DNSResolver


def run_package(hostname):
    """function that runs the package"""
    resolver = DNSResolver()
    ip = resolver.resolve(hostname)
    print(f"IP: {ip}")
    return ip


try:
    hostname = sys.argv[1]
except IndexError as e:
    print(str(e), file=sys.stderr)
    print("Please provide a domain", file=sys.stderr)
    raise

run_package(hostname)
