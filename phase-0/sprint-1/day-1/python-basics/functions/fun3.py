# Lamda and Higher Order Functions

# Lamda -> A tiny, anonymous function

square = lambda x: x**2;
print(square(5));

# HOF - function that take fn as an argument

numbers = [32, 15, 16, 83, 50, 7]

# sorted()
sorted_numbers = sorted(numbers);

print(sorted_numbers)

# map();
doubled = list(map(lambda x: x*2, numbers));

print(doubled);

# filter()

evens = list(filter(lambda x: x%2 == 0, numbers));

print(evens);

# Nested functions and closures

def make_multiplier(factor):
    def multiplier(x):
        return x*factor
    return multiplier

triple = make_multiplier(3)
print(triple(10))
print(triple(7))


