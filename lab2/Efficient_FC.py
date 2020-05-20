#Lab2 Efficient Forward Chaining
#2/11/20

# rules formatted as ([antecedents],consequent)
KB = [(["looks","swims","quacks"],"duck"), (["barks"],"dog"), (["hoots","flies"],"owl")]
# goal
q = "duck"
# number of antecedents in each rule
count = [3, 1, 2]
# inferred symbols (initially false)
inferred = []
# list of symbols known to be true initially
#agenda = ["barks", "hoots", "looks", "swims", "quacks"]
#agenda = []
#agenda = ["looks", "swims", "quacks"]

# prints the initial table
print ( "-------------" )
print ( "| {} | {} | {} |".format(count[0], count[1], count[2]) )
print ( "-------------" )

# loop while agenda is not empty
while agenda:
    # agenda is properly a list, but in Python can be treated as a stack/queue
    # pop(0) takes the left-most element, while pop(-1) would be right-most. defaults to -1
    p = agenda.pop(0)
    # check if the goal is already inferred
    if p == q:
        print( "Goal is entailed!" )
        break
    if p not in inferred:
        # add p to the list of inferred symbols
        inferred.append(p)
        for c in range(0, len(KB)):
            premise, consequent = KB[c]
            if p in premise:
                # decrement count[c]
                count[c] -= 1
                # if count[c]=0 push the consequent into agenda
                if count[c] == 0:
                    agenda.append(consequent)
    # prints the table for each iteration of the loop
    print ( "| {} | {} | {} |".format(count[0], count[1], count[2]) )
    print ( "-------------" )
