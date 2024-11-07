
initial_state = {
    ["on" :[("a", "b"), ("b", "c"), ("c", "Floor1")]],
    ["clear": ["a", "Floor2", "Floor3"]]
}
goal = {
    ["on": [("a", "b"), ("b", "c"), ("c", "Floor3")]],
   ["clear": []]  # Ensuring "clear" key is present, even if empty in goal state
}


initial_state = {"position": "Floor1"}
goal  = {"position": "Floor3"}

def possible_moves(state):
    actions = []
    if state["position"] == "Floor1":
        actions.append("move_to_Floor2")
    elif state["position"] == "Floor2":
        actions.append("move_to_Floor3")
    return actions

def apply_move(action, state):
    new_state = state.copy()
    if action == "move_to_Floor2":
        new_state["position"] = "Floor2"
    elif action == "move_to_Floor3":
        new_state["position"] = "Floor3"
    return new_state

# Initialize the current state
current = initial_state
path = []  # Record the path of actions

while current != goal:
    possibleMoves = possible_moves(current)
    if not possible_moves: 
        print("No further moves available.")
        break

    action = possible_moves[0]
    current = apply_move(action, current)
    path.append(action)

if current == goal: 
    print("Goal reached!")
else:
    print("Failed to reach goal.")
print("Path to goal:", path)