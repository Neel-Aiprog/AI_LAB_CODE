def forward_chaining(rules, facts, goal):
    inferred = set(facts)   # known facts
    print("Initial Facts:", inferred)

    changed = True

    while changed:
        changed = False

        for premises, conclusion in rules:
            # if all premises are known and conclusion not yet inferred
            if set(premises).issubset(inferred) and conclusion not in inferred:
                print(f"Applying rule: {premises} -> {conclusion}")
                inferred.add(conclusion)
                changed = True

                print("Updated Facts:", inferred)

                if conclusion == goal:
                    print("\nGoal reached:", goal)
                    return True

    print("\nGoal not reached")
    return False
print("CASE (a)")
rules_a = [
    (["P"], "Q"),
    (["L", "M"], "P"),
    (["A", "B"], "L")
]

facts_a = ["A", "B", "M"]
goal_a = "Q"

forward_chaining(rules_a, facts_a, goal_a)
print("\nCASE (b)")
rules_b = [
    (["A"], "B"),
    (["B"], "C"),
    (["C"], "D"),
    (["D", "E"], "F")
]

facts_b = ["A", "E"]
goal_b = "F"

forward_chaining(rules_b, facts_b, goal_b)