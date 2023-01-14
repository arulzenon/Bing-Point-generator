import random
import time
import tkinter as tk
import pyautogui

words = ["dog", "cat", "house", "car", "book", "tree", "sun", "moon", "flower", "sky", "pen", "pencil", "paper", "desk", "chair", "computer", "mouse", "keyboard", "monitor", "apple","banana","orange","grapes","strawberry","watermelon","kiwi","mango","pear","peach","pineapple","lemon","lime","blackberry","blueberry","raspberry","cranberry","plum","apricot","avocado","broccoli","cabbage","carrot","cauliflower","celery","corn","cucumber","eggplant","green pepper","lettuce","olive","onion","pepper","potato","pumpkin","spinach","tomato","watercress","zucchini"]

def generate_words():
    global count
    if count < 35:
        random_word = random.choice(words)
        pyautogui.typewrite(random_word)  # types the random word
        pyautogui.press("enter")  # presses enter
        pyautogui.doubleClick()  # double clicks
        count += 1
        root.after(1000, generate_words)
    else:
        stop_button.config(state="disabled")

def stop_generating():
    global count
    count = 35

def start_generating():
    global count
    count = 0
    stop_button.config(state="normal")
    generate_words()

root = tk.Tk()
root.title("Bing Points Generator")

count = 0

label = tk.Label(root, text="Press Start to generate random words...")
label.pack()

start_button = tk.Button(root, text="Start", command=start_generating)
start_button.pack()

stop_button = tk.Button(root, text="Stop", command=stop_generating, state="disabled")
stop_button.pack()

root.mainloop()
