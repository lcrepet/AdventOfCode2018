class Polymer:
    """
    Represents a molecule made of several units.
    """

    def __init__(self, units):
        self.units = units

    def reduce(self, avoided_type = ''):
        """
        Reduce the sequence of units by removing units that react together.
        An unit can react with an adjacent unit if they are different byt have the same type.

        :param avoided_type: units of this type won't react
        :type avoided_type: str
        :rtype: list(str)
        """

        remaining_units = []

        for unit in self.units:
            if self.__same_type(avoided_type, unit):
                continue

            if len(remaining_units) > 0 and self.__should_react(remaining_units[-1], unit):
                remaining_units.pop()
            else:
                remaining_units.append(unit)

        return remaining_units


    def __should_react(self, first_unit, second_unit):
        return not(first_unit == second_unit) and self.__same_type(first_unit, second_unit)


    def __same_type(self, first_unit, second_unit):
        return first_unit.lower() == second_unit.lower()
