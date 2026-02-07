import pandas as pd
import matplotlib.pyplot as plt
# INDUSTRIAL ENERGY OPTIMIZER
def optimize_energy_cost():
    prices = [0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.4, 0.5, 0.5, 0.4, 0.3, 0.3, 0.3, 0.3, 0.4, 0.5, 0.6, 0.6, 0.5, 0.4, 0.2, 0.1, 0.1, 0.1]
    load = [20, 20, 20, 25, 30, 50, 80, 100, 120, 110, 100, 90, 90, 95, 100, 110, 130, 125, 100, 80, 60, 40, 30, 20]
    battery_capacity = 200
    current_charge = 0
    max_rate = 50
    grid_power = []
    battery_action = []
    avg_price = sum(prices) / len(prices)
    for i in range(24):
        price = prices[i]
        demand = load[i]
        if price > avg_price and current_charge > 0:
            discharge = min(demand, max_rate, current_charge)
            current_charge -= discharge
            grid_power.append(demand - discharge)
            battery_action.append(-discharge)
        elif price < avg_price and current_charge < battery_capacity:
            charge = min(max_rate, battery_capacity - current_charge)
            current_charge += charge
            grid_power.append(demand + charge)
            battery_action.append(charge)
        else:
            grid_power.append(demand)
            battery_action.append(0)
    cost_without = sum([p * l for p, l in zip(prices, load)])
    cost_with = sum([p * g for p, g in zip(prices, grid_power)])
    savings = cost_without - cost_with
    print(f"Total Cost WITHOUT Battery: ${cost_without:.2f}")
    print(f"Total Cost WITH Battery: ${cost_with:.2f}")
    print(f"SAVINGS: ${savings:.2f}")
    plt.figure(figsize=(10, 6))
    plt.plot(prices, 'r--', label='Price ($)')
    plt.bar(range(24), battery_action, color='green', alpha=0.6, label='Battery')
    plt.plot(load, 'k', label='Load (kW)')
    plt.legend()
    plt.grid(True)
    plt.show()
if __name__ == "__main__":
    optimize_energy_cost()
