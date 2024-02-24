import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.bgpic(image)

data = pandas.read_csv("50_states.csv")
guessed_states = []

# Upon exiting by typing Exit, file with non-guessed states will be generated in the project folder
def non_guessed_states():
    rest = []
    for state in data.state:
        if state not in guessed_states:
            rest.append(state)
    new_dict = {
        "states": rest
    }
    pandas.DataFrame(new_dict).to_csv("non_guessed_states.csv")

def game_start():
    total_num_states = len(data)
    is_game_over = False
    while not is_game_over:
        answer_state = screen.textinput(title=f"{len(guessed_states)}/{total_num_states} States Correct", prompt="What's another state's name?").title()
        if answer_state == "Exit":
            non_guessed_states()
            break
        for (index, row) in data.iterrows():
            if row.state == answer_state:
                guessed_states.append(answer_state)
                turtle.penup()
                turtle.hideturtle()
                turtle.goto(row.x, row.y)
                turtle.write(f"{row.state}", align="center", font=("Arial", 7, "normal"))
                if guessed_states == 50:
                    is_game_over = True
game_start()
