class InvalidInput(Exception):
    pass

class EmptyInput(Exception):
    pass

class NegativeInput(Exception):
    pass

class RestrictedInput(Exception):
    pass

class InvalidRangeInput(Exception):
    def __init__(self, rangeMin, rangeMax):
        self.rangeMin = rangeMin
        self.rangeMax = rangeMax
        self.message = f"Input not in ({rangeMin}, {rangeMax}) range"
        super().__init__(self.message)

class GameRulesViolation(Exception):
    pass
