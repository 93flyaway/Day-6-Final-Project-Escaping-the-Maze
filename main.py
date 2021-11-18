# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# code is for Reeborg's world maze solution

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_right_at_next_exit():
    #if wall on the right, move forward until you can turn right.
    while wall_on_right():
        if front_is_clear():
            move()
    #if you can't move forward, turn left
        else:
            turn_left()
    # once while loop breaks, robot can turn right. If not already at the goal, turn right and move.
    if not at_goal():
        turn_right()
        move() 
        # if the robot isn't at the goal and does not have a wall on the right after turning right (i.e. single wall sticking out), turn right and move so that the robot has a wall on the right again.
        if not wall_on_right() and not at_goal():
            turn_right()
            move()

while not wall_on_right():
    if front_is_clear():
        move()
    else:
        turn_left()

# my solution using turn_right_at_next_exit() function      
while not at_goal():
    turn_right_at_next_exit()

#simpler solution than using turn_right_at_next_exit():
#while not at_goal():
#    if right_is_clear():
#        turn_right()
#        move()
#    elif front_is_clear():
#        move()
#    else:
#        turn_left()