def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_cost = 0
    total_calories = 0
    chosen_items = []

    for item, properties in sorted_items:
        if total_cost + properties['cost'] <= budget:
            chosen_items.append(item)
            total_cost += properties['cost']
            total_calories += properties['calories']

    return chosen_items, total_cost, total_calories


def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(budget + 1):
            if items[list(items.keys())[i - 1]]['cost'] <= j:  # Змінено індексацію тут
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - items[list(items.keys())[i - 1]]['cost']] + items[list(items.keys())[i - 1]]['calories'])  # Змінено індексацію тут
            else:
                dp[i][j] = dp[i - 1][j]

    max_calories = dp[n][budget]
    total_cost = budget
    chosen_items = []

    for i in range(n, 0, -1):
        if max_calories <= 0:
            break
        if max_calories == dp[i - 1][total_cost]:
            continue
        else:
            chosen_items.append(list(items.keys())[i - 1])
            max_calories -= items[list(items.keys())[i - 1]]['calories']
            total_cost -= items[list(items.keys())[i - 1]]['cost']

    return chosen_items, budget - total_cost, dp[n][budget]


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 70

# Використання жадібного алгоритму
greedy_items, greedy_cost, greedy_calories = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Обрані страви:", greedy_items)
print("Загальна вартість:", greedy_cost)
print("Загальна калорійність:", greedy_calories)

# Використання алгоритму динамічного програмування
dp_items, dp_cost, dp_calories = dynamic_programming(items, budget)
print("\nАлгоритм динамічного програмування:")
print("Обрані страви:", dp_items)
print("Загальна вартість:", dp_cost)
print("Загальна калорійність:", dp_calories)
