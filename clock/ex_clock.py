class Clock:
    'Clock that displays 24 hour clock that rollsover properly'

    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.cleanup()

    def __repr__(self):
        return "%02d:%02d" % (self.hour, self.minute)

    #__eq__ seems to customize what the comparison operator will do.
    # by default, when the object is compared to another object, python
    # will compare the objects' identities. this compares their return values
    # instead. i think. 
    def __eq__(self, other):
        return repr(self) == repr(other)

    def add(self, minutes):
        self.minute += minutes
        return self.cleanup()

    def cleanup(self):
        self.hour += self.minute // 60
        self.hour %= 24
        self.minute %= 60
        return self