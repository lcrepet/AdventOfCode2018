class Polymer:
    def __init__(self, units):
        self.units = units

    def reduce(self, avoided_type = ''):
        remaining_units = []

        for unit in self.units:
            if self.same_type(avoided_type, unit):
                continue

            if len(remaining_units) > 0 and self.should_react(remaining_units[-1], unit):
                remaining_units.pop()
            else:
                remaining_units.append(unit)

        return remaining_units


    def should_react(self, first_unit, second_unit):
        return not(first_unit == second_unit) and self.same_type(first_unit, second_unit)


    def same_type(self, first_unit, second_unit):
        return first_unit.lower() == second_unit.lower()
