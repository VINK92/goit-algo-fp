import random

def simulate_dice_rolls(num_rolls):
    rolls = []
    for _ in range(num_rolls):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        rolls.append(roll1 + roll2)
    return rolls

def calculate_probabilities(rolls):
    probabilities = {}
    total_rolls = len(rolls)
    for i in range(2, 13):
        count = rolls.count(i)
        probabilities[i] = count / total_rolls * 100
    return probabilities

def print_probabilities(probabilities):
    print("Сума\tІмовірність")
    for key, value in probabilities.items():
        print(f"{key}\t{value:.2f}% ({rolls.count(key)}/{len(rolls)})")

# Кількість кидків кубиків для симуляції
num_rolls = 100000

# Симуляція кидків кубиків
rolls = simulate_dice_rolls(num_rolls)

# Обчислення ймовірностей
probabilities = calculate_probabilities(rolls)

# Виведення результатів
print_probabilities(probabilities)


def print_analytical_probabilities():
    print("Аналітичні ймовірності:")
    print("Сума\tІмовірність")
    analytical_probabilities = {
        2: 1 / 36 * 100,
        3: 2 / 36 * 100,
        4: 3 / 36 * 100,
        5: 4 / 36 * 100,
        6: 5 / 36 * 100,
        7: 6 / 36 * 100,
        8: 5 / 36 * 100,
        9: 4 / 36 * 100,
        10: 3 / 36 * 100,
        11: 2 / 36 * 100,
        12: 1 / 36 * 100
    }
    for key, value in analytical_probabilities.items():
        print(f"{key}\t{value:.2f}%")

print_analytical_probabilities()

print("\nЙмовірності за допомогою Методу Монте-Карло:")
print_probabilities(probabilities)
