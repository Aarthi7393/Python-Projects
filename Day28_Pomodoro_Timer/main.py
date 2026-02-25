from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# WORK_MIN = 25
# SHORT_BREAK_MIN = 5
# LONG_BREAK_MIN = 20

WORK_MIN = 0.5
SHORT_BREAK_MIN = 0.25
LONG_BREAK_MIN = 1


reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps, timer
    window.after_cancel(timer)

    reps = 0
    timer_label.config(text="Timer", fg= GREEN)
    check_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_time():
    global reps
    reps += 1

    work_sec = math.floor(WORK_MIN * 60)
    short_break_sec = math.floor(SHORT_BREAK_MIN * 60)
    long_break_sec = math.floor(LONG_BREAK_MIN * 60)

    if reps %8 == 0:
        timer_label.config(text= "Long Break ⏰", fg= RED)
        count_down(long_break_sec)
    elif reps %2 == 0:
        timer_label.config(text="Short Break ☕", fg= PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work Mode 👩🏻‍💻 ", fg= GREEN)
        count_down(work_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    if count_min < 10:
        count_min = "0" + str(count_min)

    #to change anything in canvas
    canvas.itemconfig(timer_text, text =f"{count_min}:{count_sec}")
    if count > 0:
       global timer
       timer = window.after(1000, count_down, count-1)
    # after 1000ms, call count_down function and pass the count-1 value
    else:
        # When the countdown is over:
        window.bell()  # Play a system sound
        window.attributes('-topmost', 1)  # Bring the window to the front

        # Schedule to remove the topmost attribute after 3 seconds (3000 milliseconds)
        # This will allow other windows to cover it again after a brief moment.
        window.after(3000, lambda: window.attributes('-topmost', 0))

        start_time()
        global reps
        marks = ""
        for x in range(math.floor(reps/2)):
            marks +="✔"
        check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=25,bg = YELLOW)

timer_label = Label(text="Timer", fg= GREEN, bg= YELLOW, font= (FONT_NAME,40))
timer_label.grid(row=0, column=1)

#------------------------------
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
#highlightthickness is remove the board line fo the canvas

tomato_image = PhotoImage(file = "tomato.png")
#image is taken only through the PhotoImage function
canvas.create_image(100, 112, image = tomato_image )

#create text
timer_text = canvas.create_text(100, 130, text= "00:00", fill="white", font = (FONT_NAME,35, "bold"))


canvas.grid(row=1, column=1)
#-------------------------------------

start_button = Button(text= "Start", bg= "white", highlightthickness=0, command=start_time)
start_button.grid(row=2, column=0)


reset_button = Button(text= "Reset", bg= "white", highlightthickness=0, command= reset_timer)
reset_button.grid(row=2, column=2)

check_mark = "✔"
check_label = Label(fg= GREEN, bg= YELLOW)
check_label.grid(row=3, column=1)








window.mainloop()