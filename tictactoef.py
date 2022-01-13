'''
Author: nsamba kabemba hugette
'''
print('welcome to Tic Tac Toe Game!')

thegrid  = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }
grids = []

for num in thegrid:
    grids.append(num)

def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

def main():

    player = 'X'
    count = 0
    for i in range(10):
        printBoard(thegrid)
        print("It's your turn," + player + ".Move to which place?")

        move = input()        

        if thegrid[move] == ' ':
            thegrid[move] = player
            count += 1
        else:
            print("That place is already filled.\n chose another place?")
            continue 
        if count >= 5:
            if thegrid['7'] == thegrid['8'] == thegrid['9'] != ' ': 
                printBoard(thegrid)
                print("\nGame Over.\n")                
                print(player + " is the winner!")               
                break
            elif thegrid['4'] == thegrid['5'] == thegrid['6'] != ' ': 
                printBoard(thegrid)
                print("\nGame Over.\n")                
                print(player + " is the winner!") 
                break
            elif thegrid['1'] == thegrid['2'] == thegrid['3'] != ' ': 
                printBoard(thegrid)
                print("\nGame Over.\n")                
                print(player + " is the winner!") 
                break
            elif thegrid['1'] == thegrid['4'] == thegrid['7'] != ' ': 
                printBoard(thegrid)
                print("\nGame Over.\n")                
                print(player + " is the winner!") 
                break
            elif thegrid['2'] == thegrid['5'] == thegrid['8'] != ' ': 
                printBoard(thegrid)
                print("\nGame Over.\n")                
                print(player + " is the winner!") 
                break
            elif thegrid['3'] == thegrid['6'] == thegrid['9'] != ' ': 
                printBoard(thegrid)
                print("\nGame Over.\n")                
                print(player + " is the winner!") 
                break 
            elif thegrid['7'] == thegrid['5'] == thegrid['3'] != ' ': 
                printBoard(thegrid)
                print("\nGame Over.\n")                
                print(player + " is the winner!") 
                break
            elif thegrid['1'] == thegrid['5'] == thegrid['9'] != ' ': 
                printBoard(thegrid)
                print("\nGame Over.\n")                
                print(player + " is the winner!") 
                break 
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")
        if player =='X':
            player = 'O'
        else:
            player = 'X'        
    play = input("Do you want to play Again?(y/n)")
    if play == "y" or play == "Y":  
        for num in grids:
            thegrid[num] = " "
        main()

if __name__ == "__main__":
    main()