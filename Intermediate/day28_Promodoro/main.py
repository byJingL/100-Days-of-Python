from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#FF7396"
YELLOW = "#F4E06D"
SAND = "#FFFFDE"
GREEN = "#59CE8F"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_count = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_click():
    global reps
    # 停止计时 stop Time-counting
    window.after_cancel(timer_count)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    reps = 0
    check_label.config(text="")


# ---------------------------- TIMER MECHANISM --------------------------- #
def start_click():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 8:
        count_down(long_break_sec)
        reps = 0  # reset
        title_label.config(text="Long Break", fg=PINK)
    elif reps % 2 != 0:
        count_down(work_sec)
        title_label.config(text="work", fg=GREEN)
    else:
        count_down(short_break_sec)
        title_label.config(text="Short Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------- #
def count_down(count):
    global timer_count
    minute = count // 60
    second = count % 60
    if second < 10:
        second = f"0{second}"

    canvas.itemconfig(timer_text, text=f"{minute}:{second}")

    if count > 0:
        # 开始计时 Time-counting begin
        timer_count = window.after(1000, count_down, count - 1)
    else:
        print(reps)
        if reps % 2 != 0:
            check_label["text"] += "✔"
        start_click()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=SAND)


canvas = Canvas(width=220, height=228, bg=SAND, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(112, 112, image=tomato_img)

timer_text = canvas.create_text(111, 130, text="00:00", fill="white", font=("FONT_NAME", 35, "bold"))
canvas.grid(column=2, row=2)

title_label = Label(width=11, text="Timer", font=(FONT_NAME, 40, "normal"), bg=SAND, fg=GREEN)
title_label.grid(column=2, row=1)
# count_down(5)

check_label = Label(fg=GREEN, bg=SAND)
check_label.grid(column=2, row=4)

start_button = Button(text="Start", highlightbackground=SAND, highlightthickness=0,
                      command=start_click)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", highlightbackground=SAND, command=reset_click)
reset_button.grid(column=3, row=3)

window.mainloop()

