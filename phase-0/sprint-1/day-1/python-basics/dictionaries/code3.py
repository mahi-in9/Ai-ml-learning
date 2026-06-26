names = ["Mahi", "Jennie", "Aman"];
scores = [98, 100, 99];

result = {name: score for name, score in zip(names, scores)}
print(result);

