# 1. Define the current array
current_array = [1,2,3]  # Example array, adjust as needed

# 2. Create an empty, new array
new_array = []

# 3. Loop through elements in the current array
for i, a in enumerate(current_array):
    for j, b in enumerate(current_array):
        for k, c in enumerate(current_array):
            # Skip if using the same index
            if i == j or j == k or i == k:
                continue

            # 4. If condition: Check if `a` is below `b` and `c`
            if a < b and a < c:
                # Check if `b` is above `c` and `c` is above `a`
                if b > c and c > a:
                    # Add to new array and break if condition met
                    new_array.append((a, b, c))
                    break

# 5. Print the path (sequence) along with a floor indicator
for path in new_array:
    print("Path:", path, "Floor:", current_array.index(path[0]))

