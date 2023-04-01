def print_string(component, values):
    print(component.ljust(14), values)


def get_stringified_values(values_list):
    return ' '.join(str(value) for value in values_list)
