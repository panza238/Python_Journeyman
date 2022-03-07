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
        # update cache
        self._cache[hostname] = ip

        return ip

    def resolve_args(self, *hostnames):
        """Method to demonstrate positional arguments
        this method will be executed with any number of arguments
        in this case, instead of '*args', we will use '*hostnames'"""
        iter_hosts = iter(hostnames)
        for host in iter_hosts:
            ip = self.resolve(host)

    def resolve_kwargs(self, **kwargs):
        """Method to try out kwargs"""
        if host := kwargs.get('host', None):
            ip = self.resolve(host)
            return ip

        if host_list := kwargs.get('host_list', None):
            for host in host_list:
                self.resolve(host)
        # Yay! I found a way to use the walrus operator!
        # I'm guessing walrus and **kwargs get along quite well.
