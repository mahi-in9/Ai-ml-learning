# Default Parameter and multiple returns

def power(base, exponent=2):
    return base ** exponent;

print(power(2));
print(power(2, 5))

def get_stats(numbers):
    total = sum(numbers)
    average = total/len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    return total, average, minimum, maximum;

t, avg, mn, mx = get_stats([23, 16, 1, 1996, 9, 6, 2004])

print(f"Total = {t}, Average = {avg}, minimum = {mn}, maxmimum = {mx}")


