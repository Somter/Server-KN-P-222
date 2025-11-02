import statistics
import math

strategies = {
    "arithmetic": lambda data: sum(data) / len(data),
    "geometric": lambda data: math.prod(data) ** (1 / len(data)),
    "harmonic": lambda data: len(data) / sum(1 / x for x in data),
    "median": lambda data: statistics.median(data)
}

def min_strategy(strategies, data):
    results = {name: func(data) for name, func in strategies.items()}
    return min(results, key=results.get)

def max_strategy(strategies, data):
    results = {name: func(data) for name, func in strategies.items()}
    return max(results, key=results.get)

data = [2, 4, 6, 8, 10]

print("Результати стратегій:")
for name, func in strategies.items():
    print(f"{name:10s} → {func(data):.3f}")

print("\nНайменший результат дає стратегія:", min_strategy(strategies, data))
print("Найбільший результат дає стратегія:", max_strategy(strategies, data))
