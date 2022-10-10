from scorboard import Scoreboard
import turtle
import pandas
# # Todo:Get x, y coordinate on click python turtle
# # have been done and save to file "50 states"
# def get_mouse_click_co(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_co)
# # Can keep the windows open
# turtle.mainloop()


def write_guessed_name(state_name, x_cor, y_cor):
    pencil.hideturtle()
    pencil.color("black")
    pencil.penup()
    pencil.goto(x_cor, y_cor)
    pencil.write(state_name)


def write_learn_name(state_name, x_cor, y_cor):
    pencil.hideturtle()
    pencil.color("salmon")
    pencil.penup()
    pencil.goto(x_cor, y_cor)
    pencil.write(state_name)


pencil = turtle.Turtle()
screen = turtle.Screen()
screen.title("U.S. States Game")
# image = "blank_states_img.gif"
# screen.addshape(image)
# turtle.shape(image)
# no different
screen.bgpic("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()

guessed_stated = []
scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    ask = screen.textinput(title=f"{scoreboard.score}/50 States Correct",
                           prompt="What's another state name? Exit to end the game")

    if ask == "exit" and scoreboard.score < 50:
        game_is_on = False
        scoreboard.game_over()

    answer = ask.title()
    if answer in states_list:
        guessed_stated.append(answer)
        target_row = data[data.state == answer]
        x = int(target_row.x)
        y = int(target_row.y)
        write_guessed_name(answer, x, y)
        scoreboard.count()

    if scoreboard.score == 50:
        game_is_on = False
        scoreboard.win_the_game()

# Todo: list comprehension
missing_states = [state for state in states_list if state not in guessed_stated]
# missing_states = []
# for state in states_list:
#     if state not in guessed_stated:
#         missing_states.append(state)

pandas.DataFrame(missing_states).to_csv("to learn state.csv")

for item in missing_states:
    learn_row = data[data.state == item]
    x = int(learn_row.x)
    y = int(learn_row.y)
    write_learn_name(item, x, y)

screen.exitonclick()
