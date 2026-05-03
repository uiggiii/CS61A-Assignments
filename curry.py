'''
def curry2(f):
    def curried(x):
        def curried2(y):
            return f(x, y)
        return curried2
    return curried


# Example usage:
def add(x, y):
    return x + y
curried_add = curry2(add)
add_five = curried_add(5)
print(add_five(10))  # Output: 15
def curry3(f):
    def curried(x):
        def curried2(y):
            def curried3(z):
                return f(x, y, z)
            return curried3
        return curried2
    return curried


# Example usage:
def multiply(x, y, z):
    return x * y * z
curried_multiply = curry3(multiply)
multiply_by_two = curried_multiply(2)
multiply_by_two_and_three = multiply_by_two(3)
print(multiply_by_two_and_three(4))  # Output: 24

def curry4(f):
    def curried(x):
        def curried2(y):
            def curried3(z):
                def curried4(w):
                    return f(x, y, z, w)
                return curried4
            return curried3
        return curried2
    return curried



# Example usage:
def power(x, y, z, w):
    return (x ** y) * (z ** w)
curried_power = curry4(power)
power_of_two = curried_power(2)
power_of_two_and_three = power_of_two(3)
power_of_two_and_three_and_four = power_of_two_and_three(4)
print(power_of_two_and_three_and_four(5))  # Output: 256
'''