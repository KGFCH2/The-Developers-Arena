# Data Cleaning Script: Remove duplicates and filter values

# Step 1: Take user input
user_input = input("Enter numbers separated by commas (e.g., 10,20,20,30,40,25): ")

# Step 2: Convert input string to a list of integers
data = [int(x.strip()) for x in user_input.split(",")]

# Step 3: Remove duplicates
unique_data = list(set(data))

# Step 4: Ask user for filter condition
threshold = int(input("Enter a threshold value to filter (e.g., keep numbers > threshold): "))
filtered_data = [x for x in unique_data if x > threshold]

# Step 5: Print results
print("\nOriginal Data:        ", data)
print("After Removing Duplicates:", unique_data)
print("After Filtering (> {}):   {}".format(threshold, filtered_data))
