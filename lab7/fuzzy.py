def membership(inputValue, fuzzySet):
    # Fuzzy set should be a set of two tuples, with the first element being fuzzy
    # value and the second element being the crisp value that corresponds to it.
    #
    # Do a single/linear pass to determine the nearest crisp value.
    closestCrispValue = 10000000 # distance of the nearest crisp value
    bestReturnValue = fuzzySet[0][0]
    for i in fuzzySet:
        fuzzy, crisp = i
        if crisp == inputValue:
            return fuzzy
        # Calculate distance of the crisp value to
        # the input value to find the closest one
        distance = abs(crisp - inputValue)
        if distance < closestCrispValue:
            closestCrispValue = distance
            bestReturnValue = fuzzy
    return bestReturnValue

def inverseMembership(inputValue, fuzzySet):
    # Fuzzy set should be a set of two tuples, with the first element being fuzzy
    # value and the second element being the crisp value that corresponds to it.
    #
    # Do a single/linear pass to determine the nearest fuzzy value.
    closestFuzzyValue = 10000000 # distance of the nearest fuzzy value
    bestReturnValue = fuzzySet[0][1]
    for i in fuzzySet:
        fuzzy, crisp = i
        if fuzzy == inputValue:
            return crisp
        # Calculate distance of the crisp value to
        # the input value to find the closest one
        distance = abs(fuzzy - inputValue)
        if distance < closestFuzzyValue:
            closestFuzzyValue = distance
            bestReturnValue = crisp
    return bestReturnValue

# Below are fuzzy sets that are formatted as (Fuzzy Value, Crisp Value)
# Empty is interpreted as ( Empty, Mostly Empty, Getting There, Not Empty )
Empty = ( (1.0,1), (0.8,2), (0.2,7), (0.0,10) )
# Crowded is interpreted as ( Crowded, Mostly Crowded, Mosty Empty, Not Crowded )
Crowded = ( (1.0,15), (0.8,10), (0.2,5), (0.0,2) )

# Idle is interpreted as ( Idle, Mostly Idle, Not Idle, High )
Idle = ( (1.0,0.0), (0.95,0.25), (0.2,0.5), (0.0,1.0) )
# High is interpreted as ( High, Mostly High, Not High, Idle )
High = ( (1.0,0.80), (0.75,0.65), (0.45,0.5), (0.0,0.20) )

# Cold and Hot are in Fahrenheit
Cold = ( (1.0,32), (0.75,69), (0.50,75), (0.2,80) )
Hot = ( (1.0,90), (0.75,80), (0.25,75), (0.0,70) )

print ("If temperature is hot, then cooling is high: {}".format(inverseMembership(membership(32,Hot), High)))
print ("If occupancy is empty, then cooling is idle: {}".format(inverseMembership(membership(3,Empty), Idle)))
print ("If temperature is cold, then occupancy is empty: {}".format(inverseMembership(membership(72,Cold), Empty)))
