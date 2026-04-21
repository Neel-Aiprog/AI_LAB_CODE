# so basically we try to reduce the time to search the solution by reducing the number of options from which we choose and that 
# we do by reducing the domains and for that 
# we use AC-3 algorithm which works on arc consistency and basically 
# we reduce variables that arent useful using AC-3 
# we prune them and if in the end 
# we empty any variables domain we say that it returns a failure otherwise 
# so this is a kind of a preprocessing step we do before going to  backtracking search...
# we try to impose arc consistency using ac3 ,two variables are arc consistent when one of the values in the variables has atleast
#one supporting variable in the other domain..
class Deque:
    def __init__(self):
        self.data = []
        self.front = 0   
    def append(self, item):
        self.data.append(item)
    def popleft(self):
        if self.is_empty():
            return None
        item = self.data[self.front]
        self.front += 1
        return item
    def is_empty(self):
        return self.front >= len(self.data)


variables = ["P1", "P2", "P3", "P4", "P5", "P6"]
def reset_domains():
    return {v: ["R1", "R2", "R3"] for v in variables}
neighbors = {
    "P1": ["P2", "P3", "P6"],
    "P2": ["P1", "P3", "P4"],
    "P3": ["P1", "P2", "P5"],
    "P4": ["P2", "P6"],
    "P5": ["P3", "P6"],
    "P6": ["P1", "P4", "P5"]
}
def constraint(x, y):
    return x != y
def revise(domains, Xi, Xj):
    revised = False
    new_domain = []

    for x in domains[Xi]:
        if any(constraint(x, y) for y in domains[Xj]):
            new_domain.append(x)
        else:
            revised = True

    domains[Xi] = new_domain
    return revised


def ac3(domains):
    queue = Deque()
    for Xi in variables:
        for Xj in neighbors[Xi]:
            queue.append((Xi, Xj))

    step = 1

    while not queue.is_empty():
        Xi, Xj = queue.popleft()
        print(f"Step {step}: Checking ({Xi}, {Xj})")
        step += 1

        if revise(domains, Xi, Xj):
            print(f"  Reduced: {Xi} -> {domains[Xi]}")

            if len(domains[Xi]) == 0:
                print("Failure: Empty domain")
                return False

            for Xk in neighbors[Xi]:
                if Xk != Xj:
                    queue.append((Xk, Xi))
        else:
            print("  No change")

    return True


print("Without Assignment")
domains = reset_domains()
ac3(domains)

print("\nFinal Domains:")
for v in domains:
    print(v, domains[v])


print("\nWith P1 = R1 ")
domains = reset_domains()
domains["P1"] = ["R1"]

ac3(domains)

print("\nFinal Domains:")
for v in domains:
    print(v, domains[v])