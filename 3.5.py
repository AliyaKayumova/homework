def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[:1])
    if len(str_number) == 1 and number > 0:
        return first
    if int(str_number[1:]) == 0 and len(str_number) > 1:
        return first
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))

result = get_multiplied_digits(40203)
print(result)