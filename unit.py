# a list of units base on their categories
units = (
    ("length", (
        "kilometer", "meter", "centimeter", "mile",
        "feet", "yard", "inch"
    )),

    ("currency", (
        "dollar", "euro", "rial", "lira",
    )),

    ("speed", (
        "km/h", "m/s", "mile/h",
        "knot", "speed of light",
    )),

    ("temperature", (
        "celsius", "fahrenheit", "kelvin",
    )),

    ("weight", (
        "kg", "gram", "pound", "ounce",
    )),
    ("volume", (
        "cubic meter", "liter", "cc", "gallon",
    )),
)

def main():
    while True:
        print("Let's CONVERT IT!\n")

        # show categories
        print(*(f"{i+1}. {c[0]}" for i, c in enumerate(units)),
              sep='\n', end='\n\n')

        selected_cat_index = int(input("which category? ")) - 1
        units_of_cat = [
            f"{i+1}. {u}" for i, u in enumerate(units[selected_cat_index][1])]

        print(*units_of_cat, sep='\n', end='\n\n')
        from_unit_index = int(input("what is your input unit? ")) - 1

        print(*units_of_cat, sep='\n', end='\n\n')
        to_unit_index = int(input("what is your output unit? ")) - 1

        from_value = float(input("ok . what is your value ? "))

        answer = convert_it(units[selected_cat_index][0],
                            units[selected_cat_index][1][from_unit_index],
                            from_value,
                            units[selected_cat_index][1][to_unit_index])

        print(f'answer: {answer}')

        choise_to_continue = int(input(
            "would you like to continue ?\n" "1.  Yes\n" "2.  No\n"
        ))

        if choise_to_continue != 1:
            break


def convert_it(category_name: str, from_unit: str, from_value: float, to_unit: str):
    """
    this function knows what category relates to which function,
    in order to convert it
    """

    if category_name == 'length':
        func = length_conv
    elif category_name == 'currency':
        func = currency_conv
    elif category_name == "speed":
        func = speed_conv
    elif category_name == "temperature":
        func = temperature_conv
    elif category_name == "weight":
        func = weight_conv
    elif category_name == "volume":
        func = volume_conv

    return func(from_unit, from_value, to_unit)


"""
this is how these convert functions work:
    they convert your value to a [base unit]
    and then they convert that [base unit] to given unit
"""


def length_conv(from_unit: str, from_value: float, to_unit: str) -> float:

    def kilometer_to_unit(unit, value) -> float:
        if unit == "kilometer":
            return (value)
        elif unit == "meter":
            return (value * 1000)
        elif unit == "centimeter":
            return (value * 100000)
        elif unit == "mile":
            return (value * 0.62137)
        elif unit == "feet":
            return (value * 3280.839)
        elif unit == "yard":
            return (value * 1093.61)
        elif unit == "inch":
            return (value * 39370.07)

    def unit_to_kilometer(unit, value) -> float:
        if unit == "kilometer":
            return (value)
        elif unit == "meter":
            return (value / 1000)
        elif unit == "centimeter":
            return (value / 100000)
        elif unit == "mile":
            return (value / 0.62137)
        elif unit == "feet":
            return (value / 3280.839)
        elif unit == "yard":
            return (value / 1093.61)
        elif unit == "inch":
            return (value / 39370.07)

    return kilometer_to_unit(to_unit, unit_to_kilometer(from_unit, from_value))


def currency_conv(from_unit: str, from_value: float, to_unit: str) -> float:
    def unit_to_dollar(unit, value):
        if unit == "dollar":
            return (value)
        elif unit == "euro":
            return (value / 0.85)
        elif unit == "rial":
            return (value / 230000)
        elif unit == "lira":
            return (value / 7.83)

    def dollar_to_unit(unit, value):
        if unit == "dollar":
            return (value)
        elif unit == "euro":
            return (value * 0.85)
        elif unit == "rial":
            return (value * 230000)
        elif unit == "lira":
            return (value * 7.83)

    return dollar_to_unit(to_unit, unit_to_dollar(from_unit, from_value))


def speed_conv(from_unit: str, from_value: float, to_unit: str) -> float:
    def kmh_to_unit(unit, value):
        if unit == "km/h":
            return (value)
        elif unit == "m/s":
            return (value*0.27777)
        elif unit == "mile/h":
            return (value * 0.62137)
        elif unit == "knot":
            return (value * 0.539956)
        elif unit == "speed of light":
            return (value * 0.000000000926566)

    def unit_to_kmh(unit, value):
        if unit == "km/h":
            return (value)
        elif unit == "m/s":
            return (value / 0.27777)
        elif unit == "mile/h":
            return (value / 0.62137)
        elif unit == "knot":
            return (value/0.539956)
        elif unit == "speed of light":
            return (value / 0.000000000926566)

    return kmh_to_unit(to_unit, unit_to_kmh(from_unit, from_value))


def temperature_conv(from_unit: str, from_value: float, to_unit: str) -> float:

    def celsius_to_unit(unit, value):
        if from_unit == "celsius":
            return (from_value)
        elif from_unit == "fahrenheit":
            return (from_value * 1.8) + 32
        elif from_unit == "kelvin":
            return (from_value + 273)

    def unit_to_celsius(unit, value):
        if from_unit == "celsius":
            return (from_value)
        elif from_unit == "fahrenheit":
            return (from_value - 32) / 1.8
        elif from_unit == "kelvin":
            return (from_value - 273)

    return celsius_to_unit(to_unit, unit_to_celsius(from_unit, from_value))


def weight_conv(from_unit: str, from_value: float, to_unit: str) -> float:
    def kg_to_unit(unit, value):
        if from_unit == "kg":
            return (from_value)
        elif from_unit == "gram":
            return (from_value * 1000)
        elif from_unit == "pound":
            return (from_value * 2.2046)
        elif from_unit == "ounce":
            return (from_value * 35.2739)

    def unit_to_kg(unit, value):
        if from_unit == "kg":
            return (from_value)
        elif from_unit == "gram":
            return (from_value / 1000)
        elif from_unit == "pound":
            return (from_value / 2.2046)
        elif from_unit == "ounce":
            return (from_value / 35.2739)

    return kg_to_unit(to_unit, unit_to_kg(from_unit, from_value))


def volume_conv(from_unit: str, from_value: float, to_unit: str) -> float:
    def cubicmeter_to_unit(unit, value):
        if from_unit == "cubic meter":
            return (from_value)
        elif from_unit == "liter":
            return (from_value * 1000)
        elif from_unit == "cc":
            return (from_value * 1000000)
        elif from_unit == "gallon":
            return (from_value * 264.172052)

    def unit_to_cubicmeter(unit, value):
        if from_unit == "cubic meter":
            return (from_value)
        elif from_unit == "liter":
            return (from_value / 1000)
        elif from_unit == "cc":
            return (from_value / 1000000)
        elif from_unit == "gallon":
            return (from_value / 264.172052)

    return cubicmeter_to_unit(to_unit, unit_to_cubicmeter(from_unit, from_value))


if __name__ == "__main__":
    main()
