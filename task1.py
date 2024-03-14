import random

def total_production(lemonade, fruit_juice):
    return lemonade + fruit_juice

def satisfies_constraints(lemonade, fruit_juice):
    water_for_lemonade = 2 * lemonade
    sugar_for_lemonade = lemonade
    lemon_juice_for_lemonade = lemonade
    water_for_juice = fruit_juice
    fruit_puree_for_juice = 2 * fruit_juice
    
    if (water_for_lemonade <= 100 and sugar_for_lemonade <= 50 and 
        lemon_juice_for_lemonade <= 30 and water_for_juice <= 100 and 
        fruit_puree_for_juice <= 40):
        return True
    else:
        return False

num_trials = 100000

optimal_lemonade = 0
optimal_fruit_juice = 0
max_total_production = 0

for _ in range(num_trials):
    lemonade = random.randint(0, 50)
    fruit_juice = random.randint(0, 40)
    
    if satisfies_constraints(lemonade, fruit_juice):
        current_total_production = total_production(lemonade, fruit_juice)
        if current_total_production > max_total_production:
            optimal_lemonade = lemonade
            optimal_fruit_juice = fruit_juice
            max_total_production = current_total_production

print("Optimal Production:")
print(f"Lemonade: {optimal_lemonade} units")
print(f"Fruit Juice: {optimal_fruit_juice} units")
print("Total Production (Lemonade + Fruit Juice):", max_total_production, "units")