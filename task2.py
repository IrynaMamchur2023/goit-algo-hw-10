import numpy as np
import scipy.integrate as spi

def f(x):
    return x ** 2

a = 0  
b = 2  

def monte_carlo_integration(func, a, b, num_points):
    max_f = max(func(np.linspace(a, b, 1000)))
    points_under_curve = 0
    
    for _ in range(num_points):
        x = np.random.uniform(a, b)
        y = np.random.uniform(0, max_f)
        
        if y <= func(x):
            points_under_curve += 1
    
    integral_approximation = (points_under_curve / num_points) * (b - a) * max_f
    return integral_approximation

num_points = 100000
monte_carlo_result = monte_carlo_integration(f, a, b, num_points)
print("Monte Carlo Integration Result:", monte_carlo_result)

analytical_result, _ = spi.quad(f, a, b)
print("Analytical Integration Result:", analytical_result)

error = abs(monte_carlo_result - analytical_result)
print("Absolute Error:", error)