# TextBasedAdventureGame

This python program allows the user to navigate through the game, where they will discover doors. This is one of the first
python projects that I have worked on and I am definitely planning to exapnd it even further by adding items that the user can 
collect while navigating through the game. (Maybe keys where user need to collect to unlock doors. 

In this game, the user will be asked to input the direction and the number of steps to take. The user will then be told of the
location, he/she is in. There will be walls and doors. The game layout is created based on x and y axis, and the position of 
the rooms, walls and hallway in the game is classified into lists according to their location with respect to the x and y axis.

The user will be updated of the location they are in each time they input the location and the number of steps to take. 


At this first stage of the game, the user will be required to navigate all the 6 doors in the game under a certain amount of
time. 

The basic code is as follows: 

1) The layout of the game is created based on the x and y axis. And the coordinates of the rooms, its dimensions is made into a set: 

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
        
2) Initializing the variables that we need for later use:

        direction= ''
        steps = 0
        user_posx = {5}
        user_posy = {0}

        x = 5
        y = 0
        
        found_room1 = 0
        found_room2 = 0
        found_room3 = 0
        found_room4 = 0
        found_room5 = 0
        found_room6 = 0
        total_rooms_found = 0
        
3) 2 functions are created: the instructions and the movement functions to be called later:


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
                
 4) As the game's objective is to find the rooms within a certain period of time, we have to import the time module, and time can be set according to your preference: 
 
        import time
        timeout = time.time() + 300
        
        
 5) The main execution of the code is done with a while loop as follows, where the input of the user ie the user's location is constantly being checked with the coordinates of the hallway and the rooms. If the location of the user, which is made into a set intersects the set of coordinates of the rooms and the hallway, the user will be notified of the location. And while the time does not run out, the user will be able to continue searching for the rooms. 
 
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






