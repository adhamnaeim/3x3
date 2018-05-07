#user chooses between Single or multiplayer
from random import choice
slots=['','','','','','','','','']
demo=['1','2','3','4','5','6','7','8','9']
def SingleOrMulti():
    gametype=''
    while gametype=='':
        mode=input('are you alone? y for yes and n for no please.')
        if mode == 'y':
            gametype+='single'
            print("alright! you'll play with Ultron :)")
            return gametype
        elif mode == 'n':
            print("oh, you are with a friend. this will be interesting.")
            gametype+='multi'
            return gametype
        else:
            print('oh-oh. use y for yes and n for no. no capitalization.')
     
def demoboard():
    print('' +board[0]+ '  | ' +board[1]+ '  | '+board[2] )
    print('' +board[3]+ '  | ' +board[4]+ '  | '+board[5] )
    print('' +board[6]+ '  | ' +board[7]+ '  | '+board[8] )    

def shwBoard(board):
    print('' +board[0]+ '  | ' +board[1]+ '  | '+board[2] )
    print('' +board[3]+ '  | ' +board[4]+ '  | '+board[5] )
    print('' +board[6]+ '  | ' +board[7]+ '  | '+board[8] )

#shwBoard(slots)    
    
    
#user chooses who goes first            
def whosfirst():
    answertype=''
    while answertype=='':
        answer=input('Player 1, do you wanna go first? y for yes and n for no please.')
        if answer== 'y':
            print('okay! good luck. make your first move player.')
            answertype+='yes'
            return answertype
        elif answer == 'n':
            print('Ultron will go first. be careful from his moves.')
            answertype+='no'
            return answertype
        else:
            print('please stick with y for yes and n for no, no capitalization.')


###def multiTTT():

def emptyspace(plyr_mve):
    if slots[plyr_mve] == '':
        return True
    else:
        return False

def compmove():
    state=bool
    while state != True:    
        x =choice(list(range(8)))
        y=emptyspace(x)
        state=y     
    if state == True:
        slots[x]='Z'
        shwBoard(slots)


def player1move(symb):
    state = bool
    shwBoard(demo)
    while state !=True:
        loc=int(input("choose your move's place from 1-9 as stated in the board infront of you"))-1
        if emptyspace(loc) == True:
            slots[loc]=symb
            shwBoard(slots)
            print(slots)
            break
        
def boardfull():
    marker=0
    for i in slots:
        if i == "":
            marker+=1
            return False
    if marker == 0:
        print("oh no it's a draw.")        
        return True
        
'''
def checkwin():
    Player= ((slots[0] == slots[1] and slots[1] == slots[2]) =='X') or ((slots[3] == slots[4] and slots[4] == slots[5]) == 'X') or ((slots[6] == slots[7] and slots[7] == slots[8]) == 'X') or ((slots[0] == slots[3] and slots[3] == slots[6]) == 'X') or ((slots[1] == slots[4] and slots[4] == slots[7]) == 'X') or ((slots[2] == slots[5] and slots[5] == slots[8]) == 'X') or ((slots[0] == slots[4] and slots[4] == slots[8]) == 'X') or ((slots[2] == slots[4] and slots[4] == slots[6]) == 'X')
    Comp=   ((slots[0] == slots[1] and slots[1] == slots[2]) =='Z') or ((slots[3] == slots[4] and slots[4] == slots[5]) == 'Z') or ((slots[6] == slots[7] and slots[7] == slots[8]) == 'Z') or ((slots[0] == slots[3] and slots[3] == slots[6]) == 'Z') or ((slots[1] == slots[4] and slots[4] == slots[7]) == 'Z') or ((slots[2] == slots[5] and slots[5] == slots[8]) == 'Z') or ((slots[0] == slots[4] and slots[4] == slots[8]) == 'Z') or ((slots[2] == slots[4] and slots[4] == slots[6]) == 'Z')
    
    if Player== True:
        print('congrat! you won.')
        return True
        
    elif Comp==True:
        print('You lost to Ultron.')
        return True
        
    else:
        return False
'''
def checkwin(symb):
    index_count=0
    possible=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    outcome=[]
    
    for item in possible:
        emp_lst=[]
        for i in item:
            emp_lst.append(slots[i])
        if emp_lst[0]!='' and emp_lst[0] == emp_lst[1] and emp_lst[1] == emp_lst[2]:
            print('you won!')
            return True
    else:
        return False
                    
'''
def gameon():
    status=True
    if checkwin==False:
        status=True
        return status
    if checkwin==True:
        status=False
        return status
'''
def runGame():
    mode=SingleOrMulti()
    if mode == 'multi':
        if whosfirst() == 'yes':
            while True:
                player1move('X')
                checkwin('X')
                boardfull()
                if checkwin('X')==False:
                    player1move('Z')
                    checkwin('Z')
                    boardfull() 
        else:
            while True:
                player1move('Z')
                print(checkwin('Z'))
                if checkwin('Z')==False:
                    player1move('X')
                    print(checkwin('X'))        
    if mode == 'single':
        if whosfirst()== 'yes':
            while True:
                player1move()
                checkwin('X')
                boardfull()
                if checkwin('X')==False:
                    compmove()
                    checkwin('Z')
                    boardfull()
        else:
            while True:
                compmove()
                print(checkwin('Z'))
                if checkwin('Z')==False:
                    player1move()
                    print(checkwin('X'))
            
        

        


        
