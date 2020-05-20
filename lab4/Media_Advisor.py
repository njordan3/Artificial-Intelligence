# Lab4 Media Advisor
# 2/25/20

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
        temp = ""
        if goal[-3] == "ing":
            temp = input("Is '{}' a job in the medium?(Y/N) ".format(goal))
        elif goal[-1] == "s":
            temp = input("Are '{}' an environment in the medium?(Y/N) ".format(goal))
        else:
            temp = input("Is '{}' included in the medium?(Y/N) ".format(goal))
        if temp == "Y" or temp == "y":
            KB.append(goal)
            return True
    print( "Did NOT find '{}' in KB".format(goal) )
    return False

# main code starts here
# rules formatted as ([antecedents],consequent)
rules = [(["papers"],"verbal"), (["manuals"],"verbal"), (["documents"],"verbal"), (["textbooks"],"verbal"), #4
        (["pictures"],"visual"), (["illustrations"],"visual"), (["photographs"],"visual"), (["diagrams"],"visual"),#4
        (["machines"],"physical object"), (["buildings"],"physical object"), (["tools"],"physical object"), #3
        (["numbers"],"symbolic"), (["formulas"],"symbolic"), (["computer programs"],"symbolic"), #3
        (["lecturing"],"oral"), (["advising"],"oral"), (["counselling"],"oral"), #3
        (["building"],"hands-on"), (["repairing"],"hands-on"), (["troubleshooting"],"hands-on"), #3
        (["writing"],"documented"), (["typing"],"documented"), (["drawing"],"documented"), #3
        (["evaluating"],"analytical"), (["reasoning"],"analytical"), (["investigating"],"analytical"), #3
        (["physical object","hands-on","required"],"workshop"), #1
        (["symbolic","analytical","required"],"lecture-tutorial"), #1
        (["visual","documented","not required"],"videocassette"), #1
        (["visual","oral","required"],"lecture-tutorial"), #1
        (["verbal","analytical","required"],"lecture-tutorial"), #1
        (["verbal","oral","required"],"role-play exercises")] #1

# from looking at the rules I reasoned that the mediums can be differenciated from the others by looking at
# how many antecedents the rule has, so if it has more than one antecedent then it is considered a medium
mediums = []
for i in rules:
    antecedent, consequent = i
    if len(antecedent) > 1 and consequent not in mediums:
        mediums.append(consequent)
print("{}".format(mediums))
KB = []
goal = input("What is the medium? ")
feedback = input("Is feedback required?(Y/N) ")
if feedback == "Y" or feedback == "y":
    KB.append("required")
else:
    KB.append("not required")

if (backward_chaining(KB, rules, goal)):
    print( "Inference Success! Medium is {}.".format(goal) )
else:
    print( "Inference Failed... Medium could not be inferred." )
