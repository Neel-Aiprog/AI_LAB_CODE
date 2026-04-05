letters=["E","S","N","D","M","O","R","Y"] #all the letters we need
def is_valid(assign):
    if 'S' in assign  and assign['S']==0:
        return False
    if 'M' in assign  and assign['M']==0:
        return False
        # check for leading digits they cant be 0
    if(len(assign)==8):
        S,E,N,D,M,O,R,Y=[assign[l] for l in letters]
        SEND=1000*S+100*E+10*N+D
        MORE=1000*M+100*O+10*R+E
        MONEY=10000*M+1000*O+100*N+10*E+Y
        
        return SEND+MORE==MONEY #checks if assignment is valid or not
    return True #allows partial assignment
def backtrack(assign,used):
    if len(assign)==8:
        return assign #if all letters are assigned then return solution
    for letter in letters:
        if letter not in assign:
            break #find an unassigned letter
    for d in range(10):
        if d not in used:
            assign[letter]=d
            used.add(d) #assign it a digit which is not used
            
            if is_valid(assign):
                result=backtrack(assign,used) #call recursively 
                if result:
                    return result #if result found return it
            del assign[letter] #backtracking if encountered conflict at any stage
            used.remove(d) #freeing the digit and going back
    return None
solution = backtrack({}, set()) #at first no digits assigned and no letters assigned

print("Solution:", solution)