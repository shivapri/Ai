import numpy as np
import random
#
p=[]
for i in range(0,3,1):
    c=[]
    for j in range(0,3,1):
       c.append('_')
    p.append(c)
for i in range(0,3,1):
    for j in range(0,3,1):
        print(p[i][j],end=" ")
    print('\n')
def checkRows(board):
    for row in board:
        if len(set(row)) == 1:
            return row[0]
    return 0

def checkDiagonals(board):
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0]
    if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
        return board[0][len(board)-1]
    return 0

def checkWin(board):
    #transposition to check rows, then columns
    for newBoard in [board, np.transpose(board)]:
        result = checkRows(newBoard)
        if result:
            return result
    return checkDiagonals(board)


row,col =input("The location where you want the 0")
# print(row," ",col)
p[int(row)][int(col)]='O'
row,col =input("The location where you want the 0")
# print(row," ",col)
p[int(row)][int(col)]='O'
row,col =input("The location where you want the 0")
# print(row," ",col)
p[int(row)][int(col)]='X'
for i in range(0,3,1):
    for j in range(0,3,1):
        print(p[i][j],end=" ")
    print('\n')
# global eva
def utility(node):
    cost = 0
    goal = np.array(node)
    row,col = np.where(goal=='X')
    # print("row is ",row," and col is ",col)
    for i in range(0, len(row), 1):
        if row[i] + 1 in row and col[i] - 1 in col:
            cost = cost + 1
            continue
            # return "Not same"
            # break

        if row[i] + 1 in row and col[i] + 1 in col:
            cost = cost + 1
            continue

        if row[i] - 1 in row and col[i] + 1 in col:
            cost = cost + 1
            continue

        if row[i] - 1 in row and col[i] - 1 in col:
            cost = cost + 1
            continue

        if row[i] + 1 in row and col[i] in col:
            cost = cost + 1
            continue
        if row[i] - 1 in row and col[i] in col:
            cost = cost + 1
            continue
        if col[i] + 1 in col and row[i] in row:
            cost = cost + 1
            continue
        if col[i] - 1 in col and row[i] in row:
            cost = cost + 1
            continue
    if cost == 0:
        cost = -1
        return cost
    return cost
# print(utility(p))

# def terminal(node):


def checkpos(node):
        # self.state = state
        arr = np.array(node)
        # print(arr)
        dim = np.where(arr == '_')
        row,col =dim
        # print(row)
        str = []
        pos = []
        for i in range(0, len(row), 1):
            if row[i] == 1 and col[i] == 1:
                s ="centre"
                str.append(s)
                pos.append(row[i])
                pos.append(col[i])
            elif row[i] == 0 and col[i] == 0:
                s = "extreme up left"
                str.append(s)
                pos.append(row[i])
                pos.append(col[i])
            elif row[i] == 0 and col[i] == 2:
                s =  "extreme up right"
                str.append(s)
                pos.append(row[i])
                pos.append(col[i])
            elif row[i] == 2 and col[i] == 0:
                s= "extreme down left"
                str.append(s)
                pos.append(row[i])
                pos.append(col[i])
            elif row[i] == 2 and col[i] == 2:
                s = "extreme down right"
                str.append(s)
                pos.append(row[i])
                pos.append(col[i])
            elif col[i] == 0:
                s =  "extreme left"
                str.append(s)
                pos.append(row[i])
                pos.append(col[i])
            elif col[i] == 2:
                s = "extreme right"
                str.append(s)
                pos.append(row[i])
                pos.append(col[i])

            elif row[i] == 0:
                s = "up"
                str.append(s)
                pos.append(row[i])
                pos.append(col[i])
            elif row[i] == 2:
                s = "down"
                str.append(s)
                pos.append(row[i])
                pos.append(col[i])
        return str,pos
def checkstate(self,node):
        self.node=node
        arr =np.array(node)
        row1, col1 = np.where(arr == '_')
        if (len(row1) == 0):
            state = 'terminal'
        else:
            state = 'non-terminal'
    # @staticmethod


class Node(object):
    def __init__(self,value,state):
            self.value = value
            self.state = state
            self.left = None
            self.right = None
            self.middle = None
            # return value

class BinaryTree(object):
        def __init__(self,root,state):
            self.root = Node(root,"non-terminal")
            self.state = state
            # return root

        def Dfs_print(self,start,depth,traversal):
            depth +=1

            if depth<4:
                traversal = start
                traversal = self.Dfs_print(left(start),depth,traversal)
                traversal = self.Dfs_print(mid(start),depth,traversal)
                traversal = self.Dfs_print(right(start),depth,traversal)
            return traversal
def left(node):
    s,p = checkpos(node)
    cond = ["extreme up left","extreme down left","extreme left"]
    t = [word for word in s if word in cond]
    if len(t)>0:
       node[p[0]][p[1]] = 'X'



    return node
def mid(node):
    s, p = checkpos(node)
    cond = ["up", "down", "center"]
    t = [word for word in s if word in cond]
    if len(t) > 0:
        node[p[0]][p[1]] = 'X'

    return node



def right (node):
    s,p= checkpos(node)
    cond = ["extreme up right", "extreme down right", "extreme right"]
    t = [word for word in s if word in cond]
    if len(t) > 0:
        node[p[0]][p[1]] = 'X'
    return node

p = np.array(p)
row1,col1= np.where(p=='_')
print(row1,"-",col1)
def minimax(node,depth,state,maximizing,acc):
    node1 = np.array(node)
    depth = depth+1
    if depth>5:
        return utility(node),acc
    if len(np.where(node1=='_'))==0:
        return utility(node),acc
    if state == 'terminal':
        return utility(node),acc

    if maximizing:
        maxeva = -99999
        child=left(node)
        if (node== child).all():
            state = 'terminal'
        evalef,temp= minimax(child,depth,state,False,acc)
        maxeva = max(maxeva,evalef)
        if (maxeva == evalef).all():
            acc.append('left')
        child = mid(node)
        if (node == child).all():
            state = 'terminal'
        evamid,temp = minimax(child,depth, state, False,acc)
        maxeva = max(maxeva,evamid)
        if maxeva == evamid:
            acc.append('mid')
        child =right(node)
        if (node == child).all():
            state ='terminal'
        evarig,temp = minimax(child,depth,state,False,acc)
        maxeva=max(maxeva,evarig)
        if maxeva == evarig:
            acc.append('right')


        return utility(node),acc
    else:
        mineva = 9999
        child = left(node)
        if (node == child).all():
            state = 'terminal'
        # if child == node:
        #     state = 'terminal'
        evalef,temp= minimax(child,depth,state,True,acc)
        mineva = min(mineva,evalef)
        if mineva== evalef:
            acc.append('left')
        child = mid(node)
        if (node == child).all():
            state = 'terminal'
        # if child == node:
        #     state = 'terminal'
        evamid,temp= minimax(child, depth,state, True,acc)
        mineva = min(mineva, evamid)
        if mineva == evamid:
            acc.append('mid')
        child = right(node)
        if (node == child).all():
            state = 'terminal'
        # if child == node:
        #     state = 'terminal'
        evarig,temp = minimax(child, depth,state, True,acc)
        mineva = min(mineva, evarig)
        if mineva == evarig:
            acc.append('right')

        return utility(node),acc


# print(tree.Dfs_print(tree.root.value,0,""))
# print(tree.root.right)

# print(tree.root.right.state)
# tree.root.left = Node(2)
# tree.root.right = Node(3)
# tree.root.left.left = Node(4)
# tree.root.left.right = Node(5)
# print(tree.print_tree('yes'))
# acc = []
# depth = 0
# value,result = minimax(p,depth,'non-terminal',False,acc)
# print(result)
node = p
while(True):
    node = np.array(node)

    row, col = input("The location where you want the 0")
    # print(row," ",col)
    if node[int(row)][int(col)]=='_':
        node[int(row)][int(col)] = 'O'
        print(node)
    else:
        print("wrong choice")

    if len(np.where(node=='_'))==0:
        if checkWin(np.array(node)) == 0:
            print('losecondition')
            print(node)
            break
        if checkWin(np.array(node) )== 1:
            print('wincondition')
            print(node)
            break
    acc = []
    score,dir = minimax(node,5,'non-terminal',False,acc)
    if dir == 'left':
        node = left(node)
        print(node)
    if dir=='mid':
        node = mid(node)
        print(node)
    if dir == 'right':
        node = right(node)
        print(node)

# sh = states(p)
# print(sh.checkpos(p))
# print(sh.minimax(p,True))
