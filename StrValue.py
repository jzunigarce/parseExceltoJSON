from ValueTypeInterface import ValueTypeInterface

class StrValue(ValueTypeInterface):
    def parse(self, value):
        return value.strip()
