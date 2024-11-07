# Define initial and goal states
initial_state = {
    "on": [("a", "b"), ("b", "c"), ("c", "Floor1")],
    "clear": ["a", "Floor2", "Floor3"]
}
goal_state = {
    "on": [("a", "b"), ("b", "c"), ("c", "Floor3")],
    "clear": []  # Ensuring "clear" key is present, even if empty in goal state
}

# Define possible moves with preconditions and effects
def move(x, y, z, state):
    """Move block x from y to z if preconditions are met."""
    if (x, y) in state["on"] and z in state["clear"]:
        # Create a copy of the state to avoid modifying the original
        new_state = {
            "on": state["on"][:],  # Copy the list of 'on' relationships
            "clear": state["clear"][:]  # Copy the list of 'clear' locations
        }
        
        # Apply the effects of the move
        new_state["on"].remove((x, y))  # Remove the old "on" relationship
        new_state["on"].append((x, z))  # Add the new "on" relationship
        new_state["clear"].remove(z)    # Mark the destination as not clear
        new_state["clear"].append(y)    # Mark the origin as clear
        
        return new_state  # Return the updated state
    return None  # Return None if the move is not valid

# Define function to get possible actions based on the current state
def get_possible_actions(state):
    """Generate all valid actions based on the current state."""
    actions = []
    
    # Possible moves we could try (from source to destination)
    moves = [
        ("a", "b", "Floor1"), ("a", "Floor1", "b"),
        ("b", "Floor1", "c"), ("b", "c", "Floor1"),
        ("c", "Floor1", "Floor3"), ("c", "Floor3", "Floor1")
    ]
    
    for x, y, z in moves:
        # Check if the move is valid by applying it
        new_state = move(x, y, z, state)
        if new_state:
            actions.append((x, y, z))  # Add valid actions to the list
    return actions

# Apply an action to the current state and get the new state
def apply_action(action, state):
    """Apply an action to the state to get a new state."""
    x, y, z = action
    return move(x, y, z, state)  # Use the move function to get the new state

# Helper function to convert a state to a tuple for hashing
def state_to_tuple(state):
    # Ensure both "on" and "clear" lists are converted to tuples for consistent hashing
    return (tuple(state["on"]), tuple(state.get("clear", [])))

# Initialize search for the goal state
current_state = initial_state
path = []  # Record the path of actions taken
visited = set()  # To keep track of visited states

# Loop until we reach the goal state
while state_to_tuple(current_state) != state_to_tuple(goal_state):
    visited.add(state_to_tuple(current_state))  # Mark current state as visited

    # Get possible actions based on the current state
    possible_actions = get_possible_actions(current_state)
    
    # Apply the first valid action
    found_new_state = False
    for action in possible_actions:
        new_state = apply_action(action, current_state)
        if new_state and state_to_tuple(new_state) not in visited:
            path.append(action)  # Record the action
            current_state = new_state  # Update the current state
            found_new_state = True
            break  # Move to the next state

    # If no new state found, break to avoid infinite loop
    if not found_new_state:
        print("No further moves available. Goal not reachable.")
        break

# Output the path taken to reach the goal
if state_to_tuple(current_state) == state_to_tuple(goal_state):
    print("Goal reached!")
else:
    print("Failed to reach goal.")
print("Path to goal:", path)
