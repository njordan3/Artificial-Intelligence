#Written by Professor Cruz
#Modified by Nicholas Jordan
#Lab6 Forward Chaining with certainty factors
#2/28/20

#array of facts
KB = [("A",1.00), ("B",0.70), ("C",0.75), ("D",0.80), ("E",0.50), ("M",-1.0)]
#array of rules in ([antecedent(s)], consequent) format
rules = [(("Y","D"),"Z",0.7), (("A","B","E"),"Y",0.95), (("A"),"X",1.0), (("C"),"L",1.0), (("L","M"),"N",1.0), (("D","X"),"Y", 0.45)]
#indexes of rules that have already been acknowledged
rules_considered = []
#Number of times we have iterated over the whole rule set
count = 1
#flag to keep track if any new knowledge was generated
changes = True
while changes:
    #Set the flag that there have been no changes
    changes = False
    #count to keep track of what rule we're at in the for loop below
    rule_count = 0;

    print( "Starting iteration " + str(count) )
    print( "====================" )

    #For each rule in the set of rules...
    for p in rules:
        #p is the current rule for this iteration which has two parts
        #p gets split and the first part goes into antecedent and the second into consequent
        antecedent, consequent, certainty = p

        print( "Consider a rule where {} implies {}".format(antecedent, consequent))

        #Flag for the antecedent in the KB
        anteInKB = True
        #counter for antecedent appearance in KB
        c = 0
        #minimum certainty factor for this rule
        min_cf = 1.00
        #Check if KB contains all the antecedents
        for q in antecedent:
            #q will be a string
            #KB is a list of strings
            for i in KB:
                fact, cf = i
                if q == fact:
                    c += 1
                    if cf < min_cf:
                        min_cf = cf
                    break
        #KB did not contain all antecedents
        if c != len(antecedent):
            anteInKB = False
        
        #counter for loop iterations to get the index
        c = 0
        #certainty of the consequent in KB
        c1 = 0
        #certainty of the rule in the current iteration of the for loop
        c2 = round(min_cf*certainty,3)
        #index of the consequent in KB
        index = 0
        #list of facts in the KB
        facts = [] 
        #fill a list with facts from the KB
        for i in KB:
            fact = i[0]
            #record the index and certainty of the consequent in the KB
            if fact == consequent:
                c1 = i[1]
                index = c
            facts.append(fact)
            c += 1

        #If it passes the above, then antecedent is satisfied
        #...and consequent should be entailed
        if anteInKB and consequent not in facts:
            KB.append((consequent, c2))
            changes = True
            rules_considered.append(rule_count)
            print( "Antecedent is in KB, consequent is implied, KB is now: " )
            print(KB)
        elif rule_count in rules_considered:
            print ( "This rule has already been considered" )
        elif anteInKB and consequent in facts:
            if c2 == c1:
                print( "Consequent already in KB and they have the same certainty")
            elif c2 > 0 and c1 > 0:
                KB.remove(KB[index])
                KB.append((consequent, round(c1 + c2 * (1 - c1),3)))
                rules_considered.append(rule_count)
                print( "Consequent already in KB, but both rules have different certainty and are greater than 0, KB is now:")
                print(KB)
            elif c2 < 0 and c1 < 0:
                KB.remove(KB[index])
                KB.append((consequent, round(c1 + c2 * (1 + c1),3)))
                rules_considered.append(rule_count)
                print( "Consequent already in KB, but both rules have different certainty and are lesss than 0, KB is now:")
                print(KB)
            elif c2 < 0 or c1 < 0: 
                KB.remove(KB[index])
                KB.append((consequent, round((c1 + c2)/(1 - min(abs(c1),abs(c2)),3))))
                rules_considered.append(rule_count)
                print( "Consequent already in KB, but both rules have different certainty and at least one is less than 0, KB is now:")
                print(KB)
        else:
            print( "Consequent is not implied" )
        rule_count += 1
    count += 1
    #prints a newline
    print()
print( "No more changes. KB is: " )
print(KB)
