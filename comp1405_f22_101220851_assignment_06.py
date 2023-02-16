

###Limitations

#In game if the space before the end is landed on you automatically lose
#The lowest roll is  a 2 which becomes impossible to roll '


### Another big limitation is I am on a Mac because the pygame
###window will not display until all the code is executed


#Player 1 is in Red
#Player 2 is green


#My two game features are exact ending and,
#if same space landed on reset the landed on player

#Imports
import pygame
import random


###Exact Ending 
def check_end(column, pos, roll, break_val):
    
    
    if (column == 6 and pos == 8) or (column == 5 and pos == 16):
        print("You win Player 1")
        break_val = 1
        return column, pos, roll, break_val
    

    #This is the code to say if you lose when you land on the space 1 before the end 
    elif (column == 6 and pos ==7) or (column == 5 and pos == 15):
        print("You Lose Player 1 ")
        break_val = 1
        return column, pos, roll, break_val

    elif (column >= 6 and pos > 8):
        pos = pos - roll 
        print("Too High try again")
        if column == 7:
            column = column - 1

        elif column == 8:
            column = column - 2
            
        return column, pos, roll, break_val
    
    else:
        return column, pos, roll, break_val



#Player 2's end check 

def P2_check_end(P2_column, P2_pos, P2_roll, break_val):
    
    
    if (P2_column == 6 and P2_pos == 8) or (P2_column == 5 and P2_pos == 16):
        print("You win Player 2 ")
        break_val = 1
        return P2_column, P2_pos, P2_roll, break_val
    

    #This is the same lose code but for player 2 
    elif (P2_column == 6 and P2_pos ==7) or (P2_column == 5 and P2_pos == 15):
        print("You Lose Player 2 ")
        break_val = 1
        return P2_column, P2_pos, P2_roll, break_val

    elif P2_column >= 6 and P2_pos > 8:
        P2_pos = P2_pos - P2_roll 
        print("Too High try again")
        
        if P2_column == 7:
            P2_column = P2_column - 1
            
        elif P2_column == 8:
            p2_column = P2_column - 2

            
        return P2_column, P2_pos, P2_roll, break_val
    
    else:
        return P2_column, P2_pos, P2_roll, break_val



#Player 1 reseting Player 2 Sorry Reset function 
def sorry_reset(P1_col, P1, P2, P2_col):
    if P1_col == P2_col:
        if P1 == P2:
            P2 = 0
            P2_col = 0
            print("SOOOOOOORRRRYYYYYY")
            return P1_col, P1, P2, P2_col
        
        else:
            return P1_col, P1, P2, P2_col
    else:
        return P1_col, P1, P2, P2_col


            

#Player 2 reseting Player 1 Sorry Reset function 
def P2_sorry_reset(P1_col, P1, P2, P2_col):
    if P1_col == P2_col:
        if P1 == P2:
            P1 = 0
            P1_col = 0
            print("SOOOOOOORRRRYYYYYY")
            return P1_col, P1, P2, P2_col
        
        else:
            return P1_col, P1, P2, P2_col
    else:
        return P1_col, P1, P2, P2_col
    



##Initialization of all of my variables


column = 0
player1_x = 0
player2_x = 0
endval = 0
P2_column = 0



#Making of the board
#The board is in the loop in order to make it so the old movements get covered

while endval == 0:
    width_squares = 8
    height_squares = 7


    size = 50

    window = pygame.display.set_mode((width_squares * size ,height_squares * size))
    window.fill((127,127,127))


    black = ( 0, 0, 0)
    white = (255, 255, 255)

    current = white 
    for i in range(0, height_squares):
        for j in range(0, width_squares):
            pygame.draw.rect(window, current, (j * size, i * size, size, size))
            
            if current == white:
                current = black
            else:
                current = white
        if current == white:
            current = black

        else:
            current = white


 

                         
    
    

    #Dice Rolls
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    total_roll = roll1 + roll2
    print("Player 1 rolled a, ", total_roll)
    print('')
    player1_x = total_roll + player1_x 

    #Exact Ending Check
    if column >= 5:
        column, player1_x, total_roll, endval = check_end(column, player1_x, total_roll, endval)
        
       
        

    

            
    #Going down 2 rows
    if player1_x > 16:
        player1_x = player1_x - 16
        realX = (player1_x * 50) - 25
        column = column + 2
        realY = (column * 50) +25
        pygame.draw.circle(window, (255, 0, 0), (realX, realY), 15)


    elif player1_x >= 8:
        #For the first row if an eight is rolled 
        if column == 0 and player1_x == 8:
            realX = (player1_x * 50) - 25
            realY = (column * 50) +25
            pygame.draw.circle(window, (255, 0, 0), (realX, realY), 15)
            
        #To go to the last square without going down a row 
        elif player1_x == 8:
            realX = (player1_x * 50) - 25
            realY = (column * 50) +25
            pygame.draw.circle(window, (255, 0, 0), (realX, realY), 15)
    
        #Basic move down 1 row 
        else:
            player1_x = player1_x - 8
            realX = (player1_x * 50) - 25
            column = column + 1
            realY = (column * 50) +25
            pygame.draw.circle(window, (255, 0, 0), (realX, realY), 15)

    
        #Rolling a value to move on the same row 
    if player1_x < 8 or player1_x >= 1:
        realX = (player1_x * 50) - 25
        realY = (column * 50) +25
        pygame.draw.circle(window, (255, 0, 0), (realX, realY), 15)



        
    #killing the program after player1's turn if player 1 wins or loses  
    if endval == 1:
        pygame.display.update()
        pygame.time.delay(2000)
        break
    
    


        
    #This is the function for the sorry condition
    #Checks to see if the players are on the same space
    #Sees if player 1 landed on player 2 and resets player 2

    column, player1_x, player2_x, P2_column = sorry_reset(column, player1_x, player2_x, P2_column)

    
    
    
    
#ALL FOR PLAYER 2

    #Very structurally simalar to player 1  
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    total_roll = roll1 + roll2
    print("Player 2 rolled a, ", total_roll)
    print('')
    player2_x = total_roll + player2_x 

    #Exact Ending Check
    if P2_column >= 5:
        P2_column, player2_x, total_roll, endval = P2_check_end(P2_column, player2_x, total_roll, endval)
        #For if you roll perfectly on the end to draw the circle on the finish line


    #Going down 2 row
    if player2_x > 16:
        player2_x = player2_x - 16
        P2_realX = (player2_x * 50) - 25
        P2_column = P2_column + 2
        P2_realY = (P2_column * 50) +25
        pygame.draw.circle(window, (0, 200, 0), (P2_realX, P2_realY), 12)


    elif player2_x >= 8:
        #For the first row if an eight is rolled 
        if P2_column == 0 and player2_x == 8:
            P2_realX = (player2_x * 50) - 25
            P2_realY = (P2_column * 50) +25
            pygame.draw.circle(window, (0, 200, 0), (P2_realX, P2_realY), 12)
            
        #To go to the eighth spot without moving down a row 
        elif player2_x == 8:
            P2_realX = (player2_x * 50) - 25
            P2_realY = (P2_column * 50) +25
            pygame.draw.circle(window, (0, 200, 0), (P2_realX, P2_realY), 12)
            

        #move down 1 row 
        else:
            player2_x = player2_x - 8
            P2_realX = (player2_x * 50) - 25
            P2_column = P2_column + 1
            P2_realY = (P2_column * 50) +25
            pygame.draw.circle(window, (0, 200, 0), (P2_realX, P2_realY), 12)
            


    
        #Rolling a value to move on the same row 
    if player2_x < 8 or player2_x >= 1:
        P2_realX = (player2_x * 50) - 25
        P2_realY = (P2_column * 50) +25
        pygame.draw.circle(window, (0, 200, 0), (P2_realX, P2_realY), 12)

        

    #This is the function for the sorry condition
    #Checks to see if the players are on the same space
    #Sees if player 2 landed on player 1  and resets player 1
    column, player1_x, player2_x, P2_column = P2_sorry_reset(column, player1_x, player2_x, P2_column)


    #statement to break the loop immediately after player2 either wins or loses 
    if endval == 1:
        pygame.display.update()
        pygame.time.delay(3000)
        break 




    pygame.display.update()
    pygame.event.pump()
    pygame.time.delay(3000)

    
print("Thank you for playing")







    
    

#Mac issue 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

















##
##
##
##
