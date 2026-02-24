import pandas as pd
import turtle
FONT = ("Courier", 8, "bold")

screen = turtle.Screen()
screen.title("Name the States Game")
bg_image = "india.gif"
screen.addshape(bg_image)
turtle.shape(bg_image)

# def get_mouse_click_coor(x,y):
#      print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pd.read_csv("States.csv")
state_list = data["state"].tolist()
print(state_list)


def missed_states(guessed_states):
    print(guessed_states)
    missed_states = []
    for state in state_list:
        if state.lower() not in guessed_states:
            missed_states.append(state)
    #print(missed_states)
    create_csv(missed_states)

def create_csv(missed_states):
    # with open("missed_states.csv", "w") as file:
    #     for state in missed_states:
    #         file.write(state + "\n")
    new_data = pd.DataFrame(missed_states)
    new_data.to_csv("missed_states.csv")




guessed_state =[]
while len(guessed_state) < 31:
    screen.listen()
    user_answer = screen.textinput(title=f"{len(guessed_state)} / 31 State ",prompt="State Name of this country?").lower()

    if user_answer == "exit":
        missed_states(guessed_state)
        break

    #TODO Check if the user guess matches the states
    for index, row in data.iterrows():
        if row["state"].lower() == user_answer and user_answer not in guessed_state:
            guessed_state.append(user_answer)
            t = turtle.Turtle()
            t.penup()
            t.hideturtle()
            t.color("black")
            x_cor = row["x"]
            y_cor = row["y"]
            t.goto(x_cor, y_cor)
            t.write(row["state"], align="left", font=FONT)







