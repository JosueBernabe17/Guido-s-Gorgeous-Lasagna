"""
This program calculates the preparation and bake time for lasagna.
It includes three key functions:
1. preparation_time_in_minutes: Calculates the time needed for preparing the layers.
2. bake_time_remaining: Calculates how much time is left for baking.
3. elapsed_time_in_minutes: Summarizes the total time spent for preparation and baking.

Each function provides helpful print statements to visualize the calculation process.
"""

# Define the expected bake time constant (in minutes)
EXPECTED_BAKE_TIME = 40


def preparation_time_in_minutes(layers):
    """
    Calculates the preparation time based on the number of layers of lasagna.

    :param layers: int - The number of layers in the lasagna.
    :return: int - Preparation time (in minutes) calculated as 2 minutes per layer.
    """
    print(f"Calculating preparation time for {layers} layers of lasagna.")
    preparation_time = layers * 2  # Each layer takes 2 minutes to prepare
    print(f"Preparation time for {layers} layers: {preparation_time} minutes.")
    return preparation_time


def bake_time_remaining(elapsed_bake_time):
    """
    Calculates how much time is left for baking the lasagna based on the elapsed time.

    :param elapsed_bake_time: int - The time already spent baking the lasagna.
    :return: int - Remaining bake time (in minutes) based on the expected bake time.
    """
    remaining_time = EXPECTED_BAKE_TIME - elapsed_bake_time
    print(f"Elapsed bake time: {elapsed_bake_time} minutes.")
    print(f"Remaining bake time: {remaining_time} minutes.")
    return remaining_time


def elapsed_time_in_minutes(preparation_time, elapsed_bake_time):
    """
    Calculates the total time spent on both preparation and baking the lasagna.

    :param preparation_time: int - Time spent on preparation (in minutes).
    :param elapsed_bake_time: int - Time already spent baking (in minutes).
    :return: int - Total time spent (in minutes).
    """
    total_time = preparation_time + elapsed_bake_time
    print(f"Total time spent (preparation + baking): {total_time} minutes.")
    return total_time


# Main program to calculate the cooking time for lasagna
print("Starting the Lasagna cooking process:")

# Example inputs
layers = 3  # Number of layers in the lasagna
elapsed_bake_time = 10  # Time already spent baking

# Step 1: Calculate preparation time
preparation_time = preparation_time_in_minutes(layers)

# Step 2: Calculate remaining bake time
bake_time_remaining(elapsed_bake_time)

# Step 3: Calculate total time spent (preparation + baking)
elapsed_time_in_minutes(preparation_time, elapsed_bake_time)


