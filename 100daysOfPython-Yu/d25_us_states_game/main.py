import turtle
import pop_up
'''
https://www.sporcle.com/games/g/states
'''

screen = turtle.Screen()

screen.setup(width=730, height=495)
screen.bgpic('blank_states_img.gif')
screen.tracer(0)

pop_up = pop_up.PopUp()

is_game_on = True
while is_game_on:
    user_input = pop_up.user_input()

    is_state_correct = pop_up.evaluate_answer(user_input)

    if is_state_correct:
        coordinates = pop_up.return_coordinates(user_input)
        print(pop_up.print_coordinates(coordinates))
    else:
        print('Try again!')

    pop_up.terminate_game()

screen.mainloop()
