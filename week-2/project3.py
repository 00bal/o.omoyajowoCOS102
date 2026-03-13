girls_names = ["Evelyn", "Jessica", "Somto", "Edith", "Liza", "Madonna", "Waje", "Tola", "Aisha", "Latifa"]
girls_ages = [17, 16, 17, 18, 16, 18, 17, 20, 19, 17]
girls_heights = [5.5, 6.0, 5.4, 5.9, 5.6, 5.5, 6.1, 6.0, 5.7, 5.5]
girls_scores = [80, 85, 70, 60, 76, 66, 87, 95, 50, 49]

boys_names = ["Chinedu", "Liam", "Wale", "Gbenga", "Abiola", "Kola", "Kunle", "George", "Thomas", "Wesley"]
boys_ages = [19, 16, 18, 17, 20, 19, 16, 18, 17, 19]
boys_heights = [5.7, 5.9, 5.8, 6.1, 5.9, 5.5, 6.1, 5.4, 5.8, 5.7]
boys_scores = [74, 87, 75, 68, 66, 78, 87, 98, 54, 60]

all_names = girls_names + boys_names
all_ages = girls_ages + boys_ages
all_heights = girls_heights + boys_heights
all_scores = girls_scores + boys_scores

print(f"{'NAME':<12} | {'AGE':<5} | {'HEIGHT':<8} | {'SCORE':<5}")
print("-" * 45)

for name, age, height, score in zip(all_names, all_ages, all_heights, all_scores):
    print(f"{name:<12} | {age:<5} | {height:<8} | {score:<5}")