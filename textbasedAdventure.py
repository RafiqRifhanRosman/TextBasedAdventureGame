Room1_x = {0, 1, 2, 3, 4}
Room1_y = {3, 4, 5, 6, 7}

Room2_x = {9, 10, 11, 12, 13}
Room2_y = {3, 4, 5, 6, 7}

Room3_x = {0, 1, 2, 3, 4}
Room3_y = {10, 11, 12, 13, 14}

Room4_x = {9, 10, 11, 12, 13}
Room4_y = {10, 11, 12, 13, 14}

Room5_x = {0, 1, 2, 3, 4}
Room5_y = {17, 18, 19, 20, 21}

Room6_x = {9, 10, 11, 12, 13}
Room6_y = {17, 18, 19, 20, 21}

Hallway_x = {4, 5, 6, 7, 8, 9}
Hallway_y = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21}


direction= ''
steps = 0
user_posx = {5}
user_posy = {0}

found_room1 = 0
found_room2 = 0
found_room3 = 0
found_room4 = 0
found_room5 = 0
found_room6 = 0
total_rooms_found = 0

x = 5
y = 0

def instructions ():
        print (' Welcome to Adventure!. In this game you will search for rooms.\n')
        print ('There is a total of 6 rooms in this game and hallways where you can\n')
        print ('navigate yourself. You have 30 minutes to find the rooms.\n\n')
        print ('Instructions: \n')
        print ('1) When prompted with \'Enter the directions you wanna go: \', \n')
        print ('   Enter \'U\' to go up, \'D\' to go down, \'L\' to go left and \'R\' to go right.\n')
        print ('')
               

def movement ():
        # This function allows user to input the direction and the number of steps they want to take, the number of steps taken is also updated 
        global steps
        direction = input('Enter the direction you wanna go: ') 
        steps = int(input('Enter the number of steps you want to take: '))
        
        global x
        global y
        
        if direction == 'U':
                y += steps
        
        if direction == 'D':
                y -= steps
        
        if direction == 'R':
                x += steps
                
        if direction == 'L':
                x -= steps
                
        user_posx.clear()
        user_posx.add(x) #updates the postion of the user in the x axis 
        
        user_posy.clear()
        user_posy.add(y) #updates the position of the user in the y axis 
        
        print (user_posx)
        print (user_posy)

        return (direction)
        return (steps)
        
        
# def undo_movement ():

        # global x
        #global y
        
        
       # if direction == 'U':
               # y -= steps
        
        #if direction == 'D':
                #y += steps
        
        #if direction == 'R':
                #x -= steps
                
        #if direction == 'L':
              #  x += steps
                
       # user_posx.clear()
        #user_posx.add(x)
        
        #user_posy.clear()
        #user_posy.add(y)
        
       # print (user_posx)
        #print (user_posy
import time
timeout = time.time() + 350

instructions ()
while True:
        
        
        movement()
        if time.time () > timeout:
            break
        
        if (user_posx.intersection(Hallway_x) != set() and user_posy.intersection(Hallway_y) != set()):
                print ('You are still in the Hallway')
        
        elif (user_posx.intersection(Room1_x)!= set() and user_posy.intersection(Room1_y)!= set()):
                print ('You are in Room 1')
                if (found_room1) == 0:
                     found_room1 +=1
                    
                  
        elif (user_posx.intersection(Room2_x) != set() and user_posy.intersection(Room2_y)!= set()):
                print ('You are in Room 2')
                if  found_room2 == 0:
                     found_room2 +=1
                
        elif (user_posx.intersection(Room3_x)!= set() and user_posy.intersection(Room3_y)!= set()):
                print ('You are in Room 3')
                if found_room3 == 0:
                     found_room3 +=1
                 
        elif (user_posx.intersection(Room4_x)!= set() and user_posy.intersection(Room4_y)!= set()):
                print ('You are in Room 4')
                if found_room4 == 0:
                     found_room4 +=1
                 
        elif (user_posx.intersection(Room5_x)!= set() and user_posy.intersection(Room5_y)!= set()):
                print ('You are in Room 5')
                if  found_room5 == 0:
                     found_room5 +=1
                 
        elif (user_posx.intersection(Room6_x)!= set() and user_posy.intersection(Room6_y)!= set()):
                print ('You are in Room 6')
                if  found_room6 == 0:
                     found_room6 +=1
        
        else:
                print ('You are walking against the wall! Go back!')
                
        
        total_rooms_found = found_room1 + found_room2 + found_room3 + found_room4 + found_room5 + found_room6
        if (total_rooms_found) == 6:
            break
        print (total_rooms_found)
                
                
        


print ('Time\'s up!')
print ("The number of rooms you have found is: " + str(total_rooms_found))

                


                

