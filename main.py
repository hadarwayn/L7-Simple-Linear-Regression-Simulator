# Import the tools we need: NumPy for math and Matplotlib for plotting
import numpy as np
import matplotlib.pyplot as plt

# --- Step a: Generate the random data points ---
# We'll create points that follow a "secret" line, but with some randomness (noise)
# Our secret line will be Y = 2.5*X + 0.5 (but the program doesn't know this!)
TRUE_a = 2.5
TRUE_b = 0.5

# Ask the user how many points they want to create
try:
    n_points_str = input("Enter the number of points to generate (default is 1000): ")
    if n_points_str == "":
        n_points = 1000
    else:
        n_points = int(n_points_str)
except ValueError:
    print("Invalid input. Using default of 1000 points.")
    n_points = 1000

# Generate n random X values between 0 and 1
X = np.random.rand(n_points)

# Generate some random noise to make the data look more realistic
noise = np.random.randn(n_points) * 0.1  # Smaller number means less noise

# Calculate the Y values based on our secret line and add the noise
Y_raw = TRUE_a * X + TRUE_b + noise

# Normalize the Y values to be between 0 and 1, just like X
Y = (Y_raw - np.min(Y_raw)) / (np.max(Y_raw) - np.min(Y_raw))

print(f"\nGenerated {n_points} data points.")

# --- This is a good place for Step b, but we will plot everything at the end ---

# --- Steps c, d, e, f: The Guessing Game ---
# We'll make a user-defined number of random guesses for 'a' and 'b' and find the best one.

# --- NEW CODE BLOCK STARTS HERE ---
# Ask the user how many experiments (guesses) to run
try:
    num_experiments_str = input("Enter the number of experiments to run (default is 100): ")
    if num_experiments_str == "":
        num_experiments = 100
    else:
        num_experiments = int(num_experiments_str)
except ValueError:
    print("Invalid input. Using default of 100 experiments.")
    num_experiments = 100
# --- NEW CODE BLOCK ENDS HERE ---


min_avg_error = float('inf')  # Start with an infinitely high error
best_a = None
best_b = None

print(f"Running {num_experiments} experiments to find the best line...")

for i in range(num_experiments):
    # Step c (part 1): Guess a random 'a' and 'b'
    # We'll guess 'a' from -5 to 5 and 'b' from -1 to 1
    a_guess = np.random.uniform(-5, 5)
    b_guess = np.random.uniform(-1, 1)

    # Step c (part 2): Calculate the predicted Y for our guess
    Y_predicted = a_guess * X + b_guess

    # Step c (part 3): Calculate the squared error for each point
    errors = (Y - Y_predicted)**2

    # Step d: Calculate the average of all the errors for this guess
    avg_error = np.mean(errors)

    # Step e & f: Check if this guess is the best one so far
    if avg_error < min_avg_error:
        min_avg_error = avg_error
        best_a = a_guess
        best_b = b_guess

# --- Step f: Announce the winner! ---
print("\n--- Results ---")
print(f"The best guess found was:")
print(f"  a = {best_a:.4f}")
print(f"  b = {best_b:.4f}")
print(f"This guess had the lowest average error: {min_avg_error:.4f}")

# --- Step b & g: Draw the Graph ---
print("\nDisplaying the graph. Close the graph window to exit the program.")

# Step b: Display the original n-points on a graph
plt.scatter(X, Y, label='Random Data Points', alpha=0.6)

# Step g: Draw the line using the best 'a' and 'b' we found
best_fit_line = best_a * X + best_b
plt.plot(X, best_fit_line, color='red', linewidth=3, label='Best Guessed Line')

# Add some nice labels to the graph
plt.title('Machine Learning Guessing Game')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.legend()  # Shows the labels for the points and the line
plt.grid(True) # Adds a grid for easier viewing

# Show the final plot
plt.show()