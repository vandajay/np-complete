import itertools

def factorial(n): # positive integers only n>=0
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

# Python function is_proper(g,c) passes two parameters, a graph in the form of a
# dictionary (g) and a colo# dictionary (g) and a coloring of this graphs vertices, also in the form of aring of this graphs vertices, also in the form of a
# dictionary (c). This function transcribes the LETTERS of the given
# graph into their corresponding COLORS/NUMBERS using a nested FOR loop. One
# for accessing each individual vertex-string (keys) and the adjacent-list of
# vertices they are paired with (values). An IF statement checks to see if
# the vertex exists in the given coloring. If so, the next FOR loop opens up
# each list of adjacent edges and looks at the individual vertex strings.
# Again an IF statement checks to see if the vertex exists in the given
# coloring. If so, it builds a temporary list of these adjacent vertices as
# their color/number list newAdj. Once looped through all adjacents, we index
# this list with the color/number of the vertex they are adjacent for.
#
# The last FOR loop simply uses the same logic as above opening up lists etc.
# to compare each vertex/color with their list of adjacent colors to make
# sure there isn't any equality. If there is not, the function returns TRUE
# meaning the graph passed through is indeed colored properly using given
# coloring. Otherwise is_proper() returns false.

def is_proper(g, c):
    colored = {}
    if len(g) is len(c):
        for x, y in g.items():
            newAdj = []
            if x in c.keys():
                for k in y:
                    if k in c.keys():
                        newAdj.append(c[k])
            colored[c[x]] = newAdj

        for x, y in colored.items():
            if x in y:
                return False
        return True
    else:
        return False

# Python function greedy(g,o) passes two parameters, a graph as a dictionary
# (g), and list in order of the vertices that will be colored (o). First, the
# function builds a temporary dictionary, using the ordered list of vertices as
# the dictionary's keys (c), no values are assigned to these ordered
# vertices/keys.
#
# Next we do a simple check to see if both the given graph and ordered list
# have the same length. The main for loop opens the ordered list and uses the
# vertex strings (x) to search c to see if they have been given a color yet.
# The first vertex is given one since nothing has a color yet with the IF
# statement. The else statement handles the 2nd coloring on, under the
# condition that boolean the variable "first" is false. Again we set set
# value/color of the key/vertex to 1, but this time we need to begin worrying
# about adjacent vertices and their colors. The WHILE loop handles this.
# Another boolean variable "loop" is used here to tell whether the WHILE
# loops inner FOR loop should iterate through the adjacent vertices again if
# coloring is ever changed. This is necessary because if the second
# vertex/color in the adjacent list is conflicting, we increment the parent
# vertices color up one, we then need to know if it the adjacent
# vertex/color preceding the conflicting one doesn't now conflict. When we
# increment this is where the "loop" variable is set back to TRUE.
#
# Once all greedy coloring is set for the graph is set in temporary
# dictionary c, we reorder it by its vertices into a new dictionary
# "greedyColoring" with yet another FOR loop. For good measure we check to
# see if the resulting coloring passes our other function is_proper(),
# if so we return the completed dictionary greedyColoring, if not we return
# an empty dictionary.

def greedy(g, o):
    c = {}
    c = dict.fromkeys(o)
    first = True

    if len(g) is len(o):
        for x in o:
            loop = True
            if first:
                c[x] = 1
                first = False
            else:
                c[x] = 1
                while loop is True:
                    loop = False
                    for y in g[x]:
                        if c[y] == c[x]:
                            c[x] = c[y] + 1
                            loop = True
        greedyColoring = {}
        for key in sorted(c):
            greedyColoring[key] = c[key]
        if is_proper(g, greedyColoring):
            return greedyColoring
        else:
            return {}
    else:
        return {}



# properGraph = {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}
#
# greedyGraph1 = {"A": ["B", "C"], "B": ["A"], "C": ["A"]}
# greedyGraph2 = {"A": ["B"], "B": ["A", "C","D"], "C": ["B", "D"], "D": ["C","B"]}
greedyGraph3 = {"A": ["B", "E"], "B": ["A", "C", "E"], "C": ["B", "D", "E"], "D": ["C"], "E" : ["A", "B", "C"]}

# properColor1 = {"A": 1, "B": 2, "C": 3}
# properColor2 = {"A": 1, "B": 1, "C": 2}

# greedyOrder1 = ["A", "B", "C"]
# greedyOrder2 = ["A","B", "C", "D"]
greedyOrder3 = ["A", "D", "B", "E", "C"]

# print(is_proper(properGraph,properColor1))
# print(greedy(greedyGraph2, greedyOrder2))
permutations = list(itertools.permutations(greedyOrder3))

for order in permutations:
    coloring = greedy(greedyGraph3,order)
    chromatic_num = coloring[max(coloring,key=coloring.get)]
    print(chromatic_num, coloring, order)
# for list in results:
#     chromatic_numbers = max(list, key=list.get)
