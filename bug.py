def function_with_uncommon_error(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return a / b

# This will cause a ZeroDivisionError if a and b are 0, but the if statements above do not cover it
result = function_with_uncommon_error(0,0)