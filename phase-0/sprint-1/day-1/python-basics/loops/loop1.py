fruits = ["apple", "guava", "kiwis"];

for index, fruit in enumerate(fruits):
    print(f"{index} fruit is {fruit}");

names = ["Mahi", "Jennie", "Aman"]
scores = [84, 100, 93];

for name, score in zip(names, scores): 
    print(f"{name}'s score is {score}");
    