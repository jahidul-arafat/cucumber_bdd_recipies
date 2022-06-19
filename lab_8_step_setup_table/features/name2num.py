class NamedNumber(object):
    """Map named number into numbers."""
    # Class Variable
    MAP ={
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6
    }
    
    @classmethod
    def from_string(cls,named_number):
        name = named_number.strip().lower() # to strip the white space and convert the string to lowercase letter
        return cls.MAP[name]
