import turtle
import pandas

screen = turtle.Screen()
screen.title("India States Game")
screen.setup(height=700, width=614)

image = "India_map.gif"
data = pandas.read_csv("India_states.csv")
screen.addshape(image)
turtle.shape(image)

loc = turtle.Turtle()
loc.ht()
loc.penup()

ind_states = data.state.to_list()
user_states = []

while len(user_states) < 36:
    user = screen.textinput(title=f"{len(user_states)}/36 Guess State", prompt="Guess another state")
    try:
        answer = user.title()
        state = data[data.state == answer]

        if answer in str(state):
            user_states.append(answer)
            x_cor = int(state.x)
            y_cor = int(state.y)
            loc.goto(x_cor, y_cor)
            loc.write(answer, align="center", font=("Courier", 10, "bold"))

        if answer == "Exit":
            missed_states = [state for state in ind_states if state not in user_states]
            learn = pandas.DataFrame(missed_states)
            learn.to_csv("states_to_learn.csv")
            break
    except AttributeError:
        missed_states = [state for state in ind_states if state not in user_states]
        learn = pandas.DataFrame(missed_states)
        learn.to_csv("states_to_learn.csv")
        break
    except TypeError:
        pass

if len(user_states) == 36:
    screen.clear()
    loc.goto(0, 0)
    loc.write("You got it all!\nCongrats! You are a Champ!!", align='center', font=("Courier", 24, "bold"))
elif len(user_states) > 25:
    screen.clear()
    loc.goto(0, 0)
    loc.write("You guessed over 25 states.\nGreat Job!", align='center', font=("Courier", 24, "bold"))
else:
    screen.clear()
    loc.goto(0, 0)
    loc.write("Better luck next time!", align='center', font=("Courier", 24, "bold"))

screen.exitonclick()
