#Written by Professor Cruz
#Modified ever so slightly by Nicholas Jordan
#Lab1 Forward Chaining
#2/4/20

#array of facts
KB = ["barks"]
#array of rules in ([antecedent(s)], consequent) format
rules = [(["looks","swims","quacks"],"duck"),(["barks"],"dog"),(["hoots","flies"],"owl")]

#Number of times we have iterated over the whole rule set
count = 1
#flag to keep track if any new knowledge was generated
changes = True

while changes:
    #Set the flag that there have been no changes
    changes = False

    print( "Starting iteration " + str(count) )
    print( "====================" )

    #For each rule in the set of rules...
    for p in rules:
        #p is the current rule for this iteration which has two parts
        #p gets split and the first part goes into antecedent and the second into consequent
        antecedent, consequent = p

        print( "Consider a rule where {} implies {}".format(antecedent, consequent))

        #Flag for the antecedent in the KB
        anteInKB = True

        #Determine if all literals in antecedent are also in KB
        for q in antecedent:
            #q will be a string
            #KB is a list of strings
            if q not in KB:
                #Flag as false, all clauses must be implied
                anteInKB = False
        #If it passes the above, then antecedent is satisfied
        #...and consequent should be entailed
        if anteInKB and consequent not in KB:
            KB.append( consequent )
            changes = True
            print( "Antecedent is in KB, consequent is implied, KB is now: " )
            print(KB)
        elif anteInKB and consequent in KB:
            print( "Consequent is implied, but was already in KB")
        else:
            print( "Consequent is not implied" )
    count = count + 1
    #prints a newline
    print()
print( "No more changes. KB is: " )
print(KB)
