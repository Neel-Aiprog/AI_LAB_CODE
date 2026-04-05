ACTIONS = ["CLEAN", "LEFT", "RIGHT"]
def is_goal(state):
    _, A, B = state
    return A == 'C' and B == 'C'

# this is the transition model
def results(state, action):
    loc, A, B = state

    outcomes = []

    if action == "CLEAN":
        if loc == 'A':
            if A == 'D':
                outcomes.append(('A', 'C', B))      # only A cleaned
                outcomes.append(('A', 'C', 'C'))    # both cleaned
            else:
                outcomes.append(('A', 'C', B))      # no change
                outcomes.append(('A', 'D', B))      # dirt added
        else:  
            if B == 'D':
                outcomes.append(('B', A, 'C'))
                outcomes.append(('B', 'C', 'C'))
            else:
                outcomes.append(('B', A, 'C'))
                outcomes.append(('B', A, 'D'))

    elif action == "RIGHT":
        if loc == 'A':
            outcomes.append(('B', A, B))
    elif action == "LEFT":
        if loc == 'B':
            outcomes.append(('A', A, B))

    return outcomes


def and_or_search(state):
    return OR_search(state, [])
 

def OR_search(state, path):
    if is_goal(state):
        return []

    if state in path:
        return None  

    for action in ACTIONS:
        result_states = results(state, action)

        if not result_states:
            continue

        plan = AND_search(result_states, path + [state])

        if plan is not None:
            return (action, plan)

    return None


def AND_search(states, path):
    plan = {}

    for s in states:
        subplan = OR_search(s, path)

        if subplan is None:
            return None

        plan[s] = subplan

    return plan
initial_state = ('A', 'D', 'D')

solution = and_or_search(initial_state)

print(solution)