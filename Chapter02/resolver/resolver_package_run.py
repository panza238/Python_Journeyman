"""run the resolver"""
# Is the PYTHONPATH correctly set?
# If not, can we set it up with subprocess?
from resolver import DNSResolver
from timeit import timeit  # Very useful package to measure performance!

resolver = DNSResolver()
first_run_performance = timeit(setup="from __main__.py import resolver",
                               stmt="resolver('google.com')",
                               number=1)
second_run_performance = timeit(setup="from __main__.py import resolver",
                                stmt="resolver('google.com')",
                                number=1)
# Not much explanation about how timeit works... But a glimpse at this tool

print(f"First Run: {first_run_performance:<.7f}\n"
      f"Second Run: {second_run_performance:<.7f}")
# Second run is much faster, because 'google.com' is cached
# Getting data from memory is 2000 times faster than getting it over HTTP
