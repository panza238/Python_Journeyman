"""Implement the DNS resolver
Also, I might implement some of the things I learned before!"""

import socket


class DNSResolver(object):
    """The DNS Resolver instance template"""

    def __init__(self):
        self._cache = dict()

    def __call__(self, host):
        """by implementing this method, I am allowing the object itself to be a callable object"""
        return self.resolve(host)

    def resolve(self, hostname):
        """resolve hostname"""
        ip = self._cache.get(hostname, None)
        if not ip:
            ip = socket.gethostbyname(hostname)
        return ip
