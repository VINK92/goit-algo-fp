def greedy_algorithm(foods, budget):
    sorted_foods = sorted(foods.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    total_calories = 0
    selected_foods = []

    for food, properties in sorted_foods:
        if properties['cost'] <= budget:
            selected_foods.append(food)
            total_calories += properties['calories']
            budget -= properties['cost']

    return selected_foods, total_calories

def dynamic_programming(foods, budget):
    dp = [[0] * (budget + 1) for _ in range(len(foods) + 1)]

    for i, (food, properties) in enumerate(foods.items(), 1):
        for j in range(1, budget + 1):
            if properties['cost'] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - properties['cost']] + properties['calories'])
            else:
                dp[i][j] = dp[i - 1][j]

    selected_foods = []
    total_calories = dp[len(foods)][budget]

    for i in range(len(foods), 0, -1):
        if dp[i][budget] != dp[i - 1][budget]:
            selected_foods.append(list(foods.keys())[i - 1])
            budget -= foods[list(foods.keys())[i - 1]]['cost']

    return selected_foods, total_calories

foods = {
    'pizza': {'cost': 5, 'calories': 800},
    'burger': {'cost': 4, 'calories': 600},
    'salad': {'cost': 2, 'calories': 300},
    'sandwich': {'cost': 3, 'calories': 400},
    'soup': {'cost': 2, 'calories': 200}
}

budget = 10

# Виклик жадібного алгоритму
greedy_selection, greedy_calories = greedy_algorithm(foods, budget)
print("Greedy Algorithm:")
print("Selected Foods:", greedy_selection)
print("Total Calories:", greedy_calories)

# Виклик алгоритму динамічного програмування
dp_selection, dp_calories = dynamic_programming(foods, budget)
print("\nDynamic Programming Algorithm:")
print("Selected Foods:", dp_selection)
print("Total Calories:", dp_calories)
