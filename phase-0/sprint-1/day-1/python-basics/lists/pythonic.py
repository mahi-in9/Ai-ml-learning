
# squares = [];

# for n in range (1,6):
#     squares.append(n**2);


squares = [n**2 for n in range(1,6)]
print(squares);

evens = [n for n in range(1,20) if n%2 == 0]
print(evens);
