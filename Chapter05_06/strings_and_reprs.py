"""This module shows the difference between str and repr methods"""


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """str method is more for the client: brief, concise"""
        return '({}, {})'.format(self.x, self.y)

    def __repr__(self):
        """repr method is more for the developer: as accurate an descriptive as possible
        It is what the developer will see in a debugger!"""
        return 'Point2D(x={}, y={})'.format(self.x, self.y)


# Rule of thumb: str should be brief, but descriptive.
# repr should give a very accurate description of the object!
