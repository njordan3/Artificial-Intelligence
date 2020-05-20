# Lab3 Backward Chaining
# 2/18/20

# backward chaining recursive function
def backward_chaining(KB, rules, goal):
    print( "Calling BC with '{}' as the goal".format(goal) )
    if goal in KB:
        print( "Found '{}' in KB".format(goal) )
        return True
    else:
        for i in rules:
            antecedent, consequent = i
            if goal in consequent:
                print( "Found rule that implies '{}'".format(goal) )
                proven = 0
                for j in antecedent:
                    if backward_chaining(KB, rules, j):
                        proven += 1
                if proven == len(antecedent):
                    return True
    print( "Did NOT find '{}' in KB".format(goal) )
    return False

# main code starts here
# rules formatted as ([antecedents],consequent)
rules = [(["looks","swims","quacks"],"duck"), (["barks"],"dog"), (["hoots","flies"],"owl")]
goal = "duck"

print( "Running Backward Chaining inference tests" )
print( "=========================================" )

# test 1
KB = []
if backward_chaining(KB, rules, goal):
    print( "Entailment SUCCESS where KB = {}".format(KB) )
else:
    print( "Entailment FAILED where KB = {}".format(KB) )

# test 2
print( "=========================================" )
KB = ["looks"]
if backward_chaining(KB, rules, goal):
    print( "Entailment SUCCESS where KB = {}".format(KB) )
else:
    print( "Entailment FAILED where KB = {}".format(KB) )

# test 3
print( "=========================================" )
KB = ["looks", "swims", "quacks"]
if backward_chaining(KB, rules, goal):
    print( "Entailment SUCCESS where KB = {}".format(KB) )
else:
    print( "Entailment FAILED where KB = {}".format(KB) )
