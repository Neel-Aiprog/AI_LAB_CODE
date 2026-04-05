# this is the graph visualising the CSP graph of the gujarat state and its districts
graph = {
    "Kachchh": ["Banaskantha", "Patan", "Surendranagar", "Jamnagar"],
    "Banaskantha": ["Kachchh", "Patan", "Sabarkantha"],
    "Patan": ["Kachchh", "Banaskantha", "Mehsana", "Surendranagar"],
    "Mehsana": ["Patan", "Sabarkantha", "Gandhinagar", "Ahmedabad"],
    "Sabarkantha": ["Banaskantha", "Mehsana", "Gandhinagar", "Panchmahal"],
    "Gandhinagar": ["Mehsana", "Sabarkantha", "Ahmedabad", "Kheda"],
    "Ahmedabad": ["Mehsana", "Gandhinagar", "Kheda", "Anand", "Surendranagar"],
    "Kheda": ["Gandhinagar", "Ahmedabad", "Anand", "Panchmahal"],
    "Panchmahal": ["Sabarkantha", "Kheda", "Dahod", "Vadodara"],
    "Dahod": ["Panchmahal"],
    "Vadodara": ["Panchmahal", "Anand", "Bharuch", "Narmada"],
    "Anand": ["Ahmedabad", "Kheda", "Vadodara", "Bharuch"],
    "Bharuch": ["Vadodara", "Anand", "Narmada", "Surat"],
    "Narmada": ["Vadodara", "Bharuch", "Surat"],
    "Surat": ["Bharuch", "Narmada", "Navsari"],
    "Navsari": ["Surat", "Valsad"],
    "Valsad": ["Navsari", "Dang"],
    "Dang": ["Valsad"],
    "Surendranagar": ["Kachchh", "Patan", "Ahmedabad", "Rajkot"],
    "Rajkot": ["Surendranagar", "Jamnagar", "Amreli"],
    "Jamnagar": ["Kachchh", "Rajkot"],
    "Amreli": ["Rajkot", "Bhavnagar", "Junagadh"],
    "Bhavnagar": ["Amreli", "Ahmedabad"],
    "Junagadh": ["Amreli"]
}
# now lets try to solve it using backtracking search
colors=["Blue","Green","Red","Yellow"]
# lets try with 4 colours and try to distribute the colors into the districts
def is_valid(node,color,assignment):
    for neighbor in graph[node]:
        if neighbor in assignment  and assignment[neighbor]==color: #if a neighbour and current node have same colour return false 
            return False
    return True
def backtrack(assignment):
    if(len(assignment)==len(graph)):
        return assignment #if all nodes are assigned return the solution
    for node in graph:
        if node not in assignment: #the node that is not assigned select it 
            break
    for color in colors:
        if(is_valid(node,color,assignment)): #check which color we can assign to the node
            assignment[node]=color
            result=backtrack(assignment) #call recursively to fill the colours in the nodes
            if result:
                return result
            del assignment[node] #if we cant get result in any case that means we cant assign any colour so we backtrack and change the colour and exlpore some other path
    return None

solution = backtrack({}) #at first no nodes are coloured so we pass an empty list

if solution:
    print("Solution Found:\n")
    for district in solution:
        print(f"{district} → {solution[district]}")
else:
    print("No solution exists") #if solution doesnt exist then it will print this