import random
import copy
class initialState:

    def __init__(self, grid, wor):
        #self._words=[]
        self._words=wor
        self._matrix = grid
        self._rows=12
        self._cols=12
        # for i in range(m):
        #     self._matrix.append([])
        #     for j in range(m):
        #         self._matrix[i].append("0")

    def getWord(self, n):
        return self._words[n]

    def getLength(self):
        f=len(self._words)
        return f

    # remove a word wor from the list
    def removeWord(self, word):
        self._words.remove(word)

    # add a letter l to the grid at position (a,b)
    def addLetter(self, l, a, b):
        self._matrix[b][a] = l

    # get a letter from the grid at position (a,b)
    def getl(self, a, b):
        return self._matrix[a][b]

    # display the grid
    def displayMatrix(self):
        a = ""
        for i in range(0, self._rows):
            for j in range(0, self._cols):
                a = a + str(self._matrix[i][j]) + " "
            a = a + "\n"
        return a

    # display the list of words
    def displayList(self):
        r = ""
        for i in range(0, len(self._words)):
            r = r + str(self._words[i]) + " "
        return r

    # get the whole grid
    def getMatrix(self):
        return self._matrix

    # get the value of the words list
    def getList(self):
        return self._words

    # get the no. of rows and cols in the matrix
    def getlenMatrix(self):
        return (self._rows, self._cols)

class finalState:

    def __init__(self, grid, wor):
        #self._words=[]
        self._words=wor
        self._matrix = grid
        self._rows=12
        self._cols=12
        # for i in range(m):
        #     self._matrix.append([])
        #     for j in range(m):
        #         self._matrix[i].append("0")

    def getWord(self, n):
        return self._words[n]

    def getLength(self):
        f=len(self._words)
        return f

    # remove a word wor from the list
    def removeWord(self, word):
        self._words.remove(word)

    # add a letter l to the grid at position (a,b)
    def addLetter(self, l, a, b):
        self._matrix[b][a] = l

    # get a letter from the grid at position (a,b)
    def getl(self, a, b):
        return self._matrix[a][b]

    # display the grid
    def displayMatrix(self):
        a = ""
        for i in range(0, self._rows):
            for j in range(0, self._cols):
                a = a + str(self._matrix[i][j]) + " "
            a = a + "\n"
        return a

    # display the list of words
    def displayList(self):
        r = ""
        for i in range(0, len(self._words)):
            r = r + str(self._words[i]) + " "
        return r

    # get the whole grid
    def getMatrix(self):
        return self._matrix

    # get the value of the words list
    def getList(self):
        return self._words

    # get the no. of rows and cols in the matrix
    def getlenMatrix(self):
        return (self._rows, self._cols)

def generateMat(m,n):
    mat =[]
    for i in range(m):
        mat.append([])
        for j in range(m):
            mat[i].append("0")
    return mat


def goal(state):
    if (state.getLength() == 0):
        return True
    else:
        return False

def applyRule(rule, state2):

    state = copy.deepcopy(state2)
    g = state.getMatrix()
    f = state.getList()


    word = rule[0]
    row = rule[1]
    col = rule[2]
    dh = rule[3]
    dv = rule[4]

    # (1,0)
    if ((dh == 1) and (dv == 0)):
        for i in range(0, len(word)):
            g[row][col] = word[i]
            col = col + 1

    # (-1,0)
    elif ((dh == -1) and (dv == 0)):
        for i in range(0, len(word)):
            g[row][col] = word[i]
            col = col - 1

    # (1,-1)
    elif ((dh == 1) and (dv == -1)):
        for i in range(0, len(word)):
            g[row][col] = word[i]
            row = row - 1
            col = col + 1

    # (-1,1)
    elif ((dh == -1) and (dv == 1)):
        for i in range(0, len(word)):
            g[row][col] = word[i]
            row = row + 1
            col = col - 1
    # (-1,-1)
    elif ((dh == -1) and (dv == -1)):
        for i in range(0, len(word)):
            g[row][col] = word[i]
            row = row - 1
            col = col - 1
    # (1,1)
    elif ((dh == 1) and (dv == 1)):
        for i in range(0, len(word)):
            g[row][col] = word[i]
            row = row + 1
            col = col + 1
    # (0,-1)
    elif ((dh == 0) and (dv == -1)):
        for i in range(0, len(word)):
            g[row][col] = word[i]
            row = row - 1
    # (0,1)
    elif ((dh == 0) and (dv == 1)):
        for i in range(0, len(word)):
            g[row][col] = word[i]
            row = row + 1

    f.remove(word)
    # value of words
    r = ""
    for i in range(0, len(f)):
        r = r + str(f[i]) + " "

    # value of grids
    a = ""
    for i in range(0, len(g)):
        for j in range(0, len(g)):
            a = a + str(g[i][j]) + " "
        a = a + "\n"


    return finalState(g,f)

def checkOverlap(initial, desired):
    if (initial == "0" or initial == desired):
        return True
    else:
        return False


def precondition(rule, state):
    g = state.getMatrix()
    f = state.getList()
    word = rule[0]
    row = rule[1]
    col = rule[2]
    dh = rule[3]
    dv = rule[4]

    m = state.getlenMatrix()[0]
    n = state.getlenMatrix()[1]
    Length = len(word)

    if ((dh == 1) and (dv == 0)):
        if (col + Length) <= n:
            flag = True
            for i in range(0, len(word)):
                if not (checkOverlap(g[row][col], word[i])):
                    flag = False
                col = col + 1
            return flag
        else:
            return False

    elif ((dh == -1) and (dv == 0)):
        if (col - Length + 1) >= 0:
            flag = True
            for i in range(0, len(word)):
                if not (checkOverlap(g[row][col], word[i])):
                    flag = False
                col = col - 1
            return flag
        else:
            return False

    elif ((dh == 1) and (dv == -1)):
        if (((row - Length + 1) >= 0) and ((col + Length) <= n)):
            flag = True
            for i in range(0, len(word)):
                if not (checkOverlap(g[row][col], word[i])):
                    flag = False
                col = col + 1
                row = row - 1
            return flag
        else:
            return False

    elif ((dh == -1) and (dv == 1)):
        if (((row + Length) <= m) and ((col - Length + 1) >= 0)):
            flag = True
            for i in range(0, len(word)):
                if not (checkOverlap(g[row][col], word[i])):
                    flag = False
                col = col - 1
                row = row + 1
            return flag
        else:
            return False

    elif ((dh == -1) and (dv == -1)):
        if (((row - Length + 1) >= 0) and ((col - Length + 1) >= 0)):
            flag = True
            for i in range(0, len(word)):
                if not (checkOverlap(g[row][col], word[i])):
                    flag = False
                col = col - 1
                row = row - 1
            return flag
        else:
            return False

    elif ((dh == 1) and (dv == 1)):
        if (((row + Length) <= m) and ((col + Length) <= n)):
            flag = True
            for i in range(0, len(word)):
                if not (checkOverlap(g[row][col], word[i])):
                    flag = False
                col = col + 1
                row = row + 1
            return flag
        else:
            return False

    elif ((dh == 0) and (dv == -1)):
        if ((row - Length + 1) >= 0):
            flag = True
            for i in range(0, len(word)):
                if not (checkOverlap(g[row][col], word[i])):
                    flag = False
                row = row - 1
            return flag
        else:
            return False

    elif ((dh == 0) and (dv == 1)):
        if ((row + Length + 1) <= m):
            flag = True
            for i in range(0, len(word)):
                if not (checkOverlap(g[row][col], word[i])):
                    flag = False
                row = row + 1
            return flag
        else:
            return False


    else:
        return False

def generateRules(state):
    Lis = state.getList()
    b = state.getMatrix()
    a = []
    random = []
    for i in range(0, 8):
        a.append(None)
    a[0] = [1, 0]
    a[1] = [-1, 0]
    a[2] = [1, -1]
    a[3] = [-1, 1]
    a[4] = [-1, -1]
    a[5] = [1, 1]
    a[6] = [0, 1]
    a[7] = [0, -1]

    for f in range(0, len(Lis)):
        for i in range(0, len(b)):
            for j in range(0, len(b)):
                for k in range(0, len(a)):
                    if (precondition([Lis[f], i, j, a[k][0], a[k][1]], state)):
                        # print("word "+str(Lis[f])+" row "+str(i)+" col "+str(j)+" dh "+str(a[k][0])+" dv "+str(a[k][1]))
                        random.append([str(Lis[f]), i, j, a[k][0], a[k][1]])
                        # print()

    return random

def describeState(state):
    print("- - - - - - - - Describe state - - - - - - - - ")
    print()
    print(state.displayMatrix())
    print(state.displayList())
    print()


def describeRule(rule):
    word = rule[0]
    row = rule[1]
    col = rule[2]
    dh = rule[3]
    dv = rule[4]
    explain = "Place the word " + str(word) + " in the grid starting at position ( " + str(row) + " , " + str(col)
    explain = explain + ") and proceeding in the direction [ " + str(dh) + " , " + str(dv) + " ]"
    return explain

def flailWildly(state):
    f=""
    while not (goal(state)):

        # generating the applicable rules
        d = generateRules(state)

        if (len(d) == 0):
            print("No more Rules are left to be applied")
            return

        # optional(d)

        # randomly choosing a rule

        t = int(round(random.random(), 1) * len(d)) - 1

        # applying the Rule
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print()
        print("We are applying Rule: ", d[t])
        #print("Rule Descrition: ", describeRule(d[t]))
        f = applyRule(d[t], state)
        d1=f.getMatrix()
        d2=f.getList()
        state=finalState(d1,d2)
        print(f.displayMatrix())
        print(f.displayList())
        print()
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

def backtracking(state,count):
    print("Number of backtrack called: ",count)
    if(not goal(state)):
        d=generateRules(state)
        a=[]
        for i in range(len(d)):
            if d[i][0] not in a:
                a.append(d[i][0])

        index=0
        i=0
        b=[]
        c=[]
        count1=0
        if(index<len(a)):
            for j in range(len(d)):
                if (a[index] == d[j][0]):
                    b.append(d[j])
            t = int(round(random.random(), 1) * len(b)) - 1
            if d[t] not in c:
                c.append(d[t])
                print(
                    "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                print()
                print("We are applying Rule: ", d[t])
                # print("Rule Descrition: ", describeRule(d[t]))
                f = applyRule(d[t], state)
                d1 = f.getMatrix()
                d2 = f.getList()
                state = finalState(d1, d2)
                print(f.displayMatrix())
                print(f.displayList())
                print()
                print(
                    "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                index = index + 1
                count=count+1
                backtracking(state,count)
            else:
                count1=count1+1
                print("Failure occurs we are backtracked", count1)
                backtracking(state,count1)


def deadEnd(state):
    f = generateRules(state)
    if len(f) == 0:
        return False


def addToFront(newState, stateList):
    stateList.insert(0, newState)
    return stateList


def append1(path, rule):
    path.append(rule)
    return path


words = ["Admissible", "Agent", "Backtrack", "Cannibal", "Deadend", "Global", "Graphsearch", "Heuristic", "Hill",
              "LISP", "Local", "Missionary", "Optimum", "Search", "Symmetry"]
mat = generateMat(12,12)
state = initialState(mat, words)
a=0
backtracking(state,a)

def optional2(state):
    print("state")
    print(state.displayMatrix())
    print(state.getList())

#optional2(state)


