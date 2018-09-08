'''Magic Square from Pickover p. 147-8
Sept 7, 2018'''


from random import sample, shuffle

nums = [3,3,2,2,1,1,1,1,0,0,0,0,0,0,0,0]
#the sums of the rows and columns
s = [2,5,1,6,4,4,3,2,5]


##function not used##
def renderList(a):
    '''Turns 16x1 list into 4x4 matrix'''
    output = []
    index = 0
    for i in range(4):
        row = []
        for j in range(4):
            row.append(a[index])
            index += 1
        output.append(row)
    return output
#####################

def printList(a):
    '''prints a 16x1 list out
    all pretty'''
    index = 0
    for i in range(4):
        for j in range(4):
            print(a[index],end=' ')
            index += 1
        print()

def shuffleList(a):
    output = list(a)
    shuffle(output)
    return output

def checkList(a):
    '''checks whether the list is the
    solution to the square'''
     
    if sum(a[:4]) == s[0] and \ #row 1
       sum(a[4:8]) == s[1] and \ #row 2
       sum(a[8:12]) == s[2] and \ #row 3
       sum(a[12:]) == s[3] and \ #row 4
       sum([a[0],a[5],a[10],a[15]])== s[4] and \ #diagonal
       sum([a[3],a[7],a[11],a[15]]) == s[5] and \ #column 4
       sum([a[2],a[6],a[10],a[14]]) == s[6] and \ #column 3
       sum([a[1],a[5],a[9],a[13]]) == s[7] and \ #column 2
       sum([a[0],a[4],a[8],a[12]]) == s[8]: #column 1
        return True
    return False

#infinite loop to shuffle the nums list then check it
while True:
    newList = shuffleList(nums)
    if checkList(newList):
        printList(newList)
        print()

'''Some solutions:
       
0 1 0 1 
3 0 2 0 
0 0 1 0 
2 1 0 3 

1 0 0 1 
3 0 2 0 
1 0 0 0 
0 2 1 3 

0 0 2 0 
3 1 0 1 
0 1 0 0 
2 0 1 3

2 0 0 0 
1 1 0 3 
0 1 0 0 
2 0 3 1 

1 0 0 1 
2 0 3 0 
1 0 0 0 
1 2 0 3

1 0 0 1 
2 0 3 0 
0 1 0 0 
2 1 0 3

0 2 0 0 
3 0 1 1 
0 0 1 0 
2 0 1 3
'''
