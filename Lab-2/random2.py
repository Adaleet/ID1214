# Define initial positions
positions = {
    'a': 'b',       # Block A is on Block B
    'b': 'c',       # Block B is on Block C
    'c': 'Floor1'   # Block C is on Floor1
}

# Define goal state
goal = {
    'a': 'b',       # A should be on B
    'b': 'c',       # B should be on C
    'c': 'Floor3'   # C should be on Floor3
}

# Path to store each move
path = []
previous_positions = []  # Store previous states for backtracking

# Define floors
floors = ['Floor1', 'Floor2', 'Floor3']

c_move_count = 0  # Track how many times C is moved
max_c_moves = 3   # Maximum moves allowed for C

# Move a block function with constraints check
def move_block(block, destination):
    global c_move_count
    
    # Check if we're moving C and respect the move limit
    if block == 'c':
        if c_move_count >= max_c_moves:
            print("Cannot move C anymore; move limit reached.")
            return False
        c_move_count += 1
    
    # Save the current position for backtracking
    previous_positions.append(positions.copy())
    
    # Perform the move and record it in the path
    positions[block] = destination
    path.append(f"Moved {block} to {destination}")
    print(f"Moved {block} to {destination}")
    return True

def undo_move():
    """Undo the last move by restoring the last saved state."""
    global c_move_count
    if previous_positions:
        # Restore the previous position
        previous_state = previous_positions.pop()
        # Check if C was moved in the last action and adjust move count
        if positions['c'] != previous_state['c']:
            c_move_count -= 1
        # Restore state
        positions.update(previous_state)
        # Remove the last move from the path
        path.pop()
        print("Undid last move, current positions:")
        print_positions()
    else:
        print("No more moves to undo.")

def is_valid_configuration():
    if positions['a'] not in ['b', 'c', 'Floor1', 'Floor2', 'Floor3']:
        return False
    if positions['b'] == 'a' or positions['b'] not in ['c', 'Floor1', 'Floor2', 'Floor3']:
        return False
    if positions['c'] not in ['Floor1', 'Floor2', 'Floor3']:
        return False
    return True

def is_goal_state():
    return positions == goal

# Print the current positions
def print_positions():
    for block, location in positions.items():
        print(f"{block} is on {location}")

# Attempt to reach the goal state with backtracking
def solve_with_backtracking():
    # Step 1: Move C to Floor3 (goal position)
    if positions['c'] != goal['c']:
        if not move_block('c', 'Floor3'):
            undo_move()

    # Step 2: Move A to B's goal position if necessary
    if positions['a'] != goal['a'] and positions['a'] == 'b':
        move_block('a', 'Floor2')  # Intermediate move if needed
        if is_valid_configuration():
            move_block('a', 'b')  # Move A to goal position on B
        else:
            undo_move()

    # Step 3: Ensure B is on C in the goal configuration
    if positions['b'] != goal['b'] and positions['b'] in floors:
        move_block('b', 'c')

    # Final check if goal is reached
    if is_goal_state():
        print("\nGoal configuration achieved.")
    else:
        print("\nCouldn't achieve the desired configuration with the given moves.")

# Execute the backtracking solution
if __name__ == "__main__":
    print("Initial positions:")
    print_positions()
    solve_with_backtracking()

    # Print final positions
    print("\nFinal positions:")
    print_positions()

    # Print path to goal
    print("\nPath to goal:")
    for step in path:
        print(step)
