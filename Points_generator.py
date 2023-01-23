import random
import tkinter as tk
import pyautogui
import time

words = ["dog", "cat", "house", "car", "book", "tree", "sun", "moon", "flower", "sky", "pen", "pencil", "paper", "desk", "chair", "computer", "mouse", "keyboard", "monitor", "apple","banana","orange","grapes","strawberry","watermelon","kiwi","mango","pear","peach","pineapple","lemon","lime","blackberry","blueberry","raspberry","cranberry","plum","apricot","avocado","broccoli","cabbage","carrot","cauliflower","celery","corn","cucumber","eggplant","green pepper","lettuce","olive","onion","pepper","potato","pumpkin","spinach","tomato","watercress","zucchini"]

used_words = []

def generate_words():
    global count, remaining_time
    if count < 30:
        random_word = random.choice(words)
        while random_word in used_words:  # check if the word has already been used
            random_word = random.choice(words)
        used_words.append(random_word)  # add the used word to the list
        pyautogui.typewrite(random_word)  # types the random word
        pyautogui.press("enter")  # presses enter
        pyautogui.doubleClick()  # double clicks
        count += 1
        remaining_time -= 1
        root.after(2000, generate_words)
    else:
        stop_button.config(state="disabled")

def stop_generating():
    global count
    count = 3

def start_generating():
    global count, remaining_time
    count = 0
    remaining_time = 30
    stop_button.config(state="normal")
    time.sleep(1)
    update_time()
    generate_words()

def update_time():
    global remaining_time
    if remaining_time > 0:
        time_label.config(text="Words remaining: {} Words".format(remaining_time))
        root.after(1000, update_time)
    else:
        time_label.config(text="Words remaining: 0 words")

def on_closing():
    if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root = tk.Tk()
root.title("Bing Word Generator")

count = 0
remaining_time = 0
used_words = []

label = tk.Label(root, text="Press Start to generate random words...")
label.pack()

start_button = tk.Button(root, text="Start", command=start_generating)
start_button.pack()

stop_button = tk.Button(root, text="Stop", command=stop_generating, state="disabled")
stop_button.pack()

time_label = tk.Label(root, text="Words remaining: ")
time_label.pack()

root.bind("<Escape>", lambda e: on_closing())
root.mainloop()
