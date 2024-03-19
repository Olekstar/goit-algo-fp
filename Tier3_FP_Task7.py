import numpy as np
import matplotlib.pyplot as plt

n_rolls = 1000000
rolls = np.random.randint(1, 7, size=(n_rolls, 2))
sums = np.sum(rolls, axis=1)
sum_counts = np.bincount(sums)[2:] 

# Обчислення ймовірностей
probabilities = sum_counts / n_rolls

sums_range = np.arange(2, 13)
probabilities_analytical = np.array([1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36])

# Порівняння з аналітичними розрахунками
plt.figure(figsize=(10, 6))
plt.plot(sums_range, probabilities * 100, 'o-', label='Monte Carlo')
plt.plot(sums_range, probabilities_analytical * 100, 's--', label='Analytical')
plt.title('Probability of Dice Roll Sums')
plt.xlabel('Sum')
plt.ylabel('Probability (%)')
plt.xticks(sums_range)
plt.grid(True)
plt.legend()
plt.show(), probabilities * 100
