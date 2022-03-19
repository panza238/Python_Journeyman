"""SortedSet module. here I will implement MY OWN collection"""


class SortedSet(object):

    def __init__(self, iterable=None):
        if iterable is None:
            iterable = []
        self._items = sorted(iterable)

    def __iter__(self):
        """If we implement the iterable protocol, the container protocol is automatically implemented"""
        for item in self._items:
            yield item

    def __contains__(self, item):
        return item in self._items

    def __getitem__(self, item):
        return_value = self._items[item]
        if isinstance(item, slice):
            return SortedSet(return_value)
        else:
            return return_value

    def __eq__(self, rhs):
        """I have to override equality! Just like lists.
        otherwise, == and 'is' are the same. it checks whether if the object IS the other object."""
        if not isinstance(rhs, SortedSet):
            return NotImplemented
        return self._items == rhs._items
