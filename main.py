from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#FFE2E2"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLUE = "#16325B"
NAVY = "#213555"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps =0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text = "00:00")
    timer_title.config(text = "Timer")
    check_marks.config(text= "")
    global reps
    reps =0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN *60
    long_break_sec = LONG_BREAK_MIN
    # if it's the 1st/3rd/5th/7th rep:
    if reps  %  8 ==0:
        timer_title.config(text="BREAK", fg=GREEN, bg=PINK, font=(FONT_NAME, 30, "bold"))
        count_down(long_break_sec)
    # if it's the 8th rep
    elif reps % 2==0:
        timer_title.config(text = "BREAK",fg = RED, bg=PINK ,font = (FONT_NAME,30,"bold"))
        count_down(short_break_sec)
    #if it's 2nd/4th/6th rep:
    else:
        timer_title.config(text="WORK", fg=NAVY, bg=PINK, font=(FONT_NAME, 30, "bold"))
        count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_minutes = math.floor(count / 60)
    count_sec = count % 60
    if count_sec <10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text = f"{count_minutes}:{count_sec}")
    if count >0:
        global  timer
        timer =window.after(1000, count_down,count-1)
    else:
        start_timer()
        marks =""
        work_sesstions = math.floor(reps/2)
        for _ in range(work_sesstions):
            marks ="✓"
            check_marks.config(text = marks)

# ---------------------------- UI SETUP --------------- ---------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady =100,bg =PINK)
# Timer
timer_title = Label(text = "TIMER",fg = GREEN, bg=PINK ,font = (FONT_NAME,30,"bold"))
timer_title.grid(column = 1, row = 0)

# Canvas
tomato_img = PhotoImage(file = "tomato.png")
canvas = Canvas(width =200,height = 224,bg = PINK, highlightthickness= 0)
canvas.create_image(100,112, image = tomato_img)
timer_text = canvas.create_text(100,130, text = "00:00",fill = "white",font = (FONT_NAME, 50,"bold"))
canvas.grid(column =1, row =1)

start_button =Button(text = "start",command= start_timer,  highlightthickness= 0,  font=(FONT_NAME,12,"bold"))
start_button.grid(column = 0, row =3)

reset_button = Button(text = "reset",command= reset_timer,highlightthickness= 0 ,font=(FONT_NAME,12,"bold"))
reset_button.grid(column =3, row = 3)

check_marks = Label(text = "✓", fg= GREEN ,bg = PINK, font=30)
check_marks.grid(column = 1, row =4)
window.mainloop()