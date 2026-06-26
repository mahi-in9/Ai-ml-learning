# *args and *kwargs

def add_all(*numbers): #numbers collect all args into a TUPLE
    return sum(numbers);

print(add_all(3, 34, 64));
print(add_all(34, 12, 16, 9, 24, 96))


def print_info(**details): #details collect all args into a DICT
    for key, value in details.items():
        print(f"{key}: {value}");

print_info(name="Mahi", age=21, city="Bangalore");
print_info(name="Jennie", age=30, city="Korea");
