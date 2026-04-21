def backward_chaining(rules, facts, goal, visited=None):
    if visited is None:
        visited = set()

    print(f"Trying to prove: {goal}")
    # If goal already a known fact
    if goal in facts:
        print(f" {goal} is a known fact")
        return True
    # Avoid infinite loops
    if goal in visited:
        return False
    visited.add(goal)
    # Find rules that conclude the goal
    for premises, conclusion in rules:
        if conclusion == goal:
            print(f"Checking rule: {premises} -> {conclusion}")

            # Try to prove all premises
            all_proved = True
            for p in premises:
                if not backward_chaining(rules, facts, p, visited):
                    all_proved = False
                    break

            if all_proved:
                print(f"Rule satisfied: {premises} -> {goal}")
                return True

    print(f"Cannot prove: {goal}")
    return False
print("CASE (a)")
rules_a = [
    (["P"], "Q"),
    (["R"], "Q"),
    (["A"], "P"),
    (["B"], "R")
]
facts_a = ["A", "B"]
goal_a = "Q"
result_a = backward_chaining(rules_a, facts_a, goal_a)
if result_a:
    print("\n Goal Q is PROVED")
else:
    print("\n Goal Q cannot be proved")
print("\n CASE (b) ")
rules_b = [
    (["A"], "B"),
    (["B", "C"], "D"),
    (["E"], "C")
]
facts_b = ["A", "E"]
goal_b = "D"
result_b = backward_chaining(rules_b, facts_b, goal_b)
if result_b:
    print("\n Goal D is PROVED")
else:
    print("\n Goal D cannot be proved")