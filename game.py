import tkinter as tk
from tkinter import ttk
import os, random, json, subprocess 

# Encode/Decode msgs with Deaconification
# Scramble game
# Spongebob textify
# Translate into Randolang, the language of Laadren
# Rubibuark

mc = "#6b75ff"
oc = "black"

perm_widgets = ['main_label', 'options_frame', 'codify_button', 'spongebob_button', 'rubibuark_button', 'scramble_button']

root = tk.Tk()

def clear_window():
    for w in root.winfo_children():
        if w.winfo_name() not in perm_widgets:
            w.destroy()
        
def codify():
    # To encrypt text
    clear_window()
    main_label = tk.Label(root, text="Encryption", bg=mc, fg=oc)
    main_label.pack()

    main_input = tk.Entry(root, bg=oc, fg=mc)
    main_input.pack()

    button_done = tk.Button(root, text="Codify!", bg=mc, fg=oc)
    button_done.pack()

def sponge_it():
    sponge = main_input.get()
    sponge = sponge.lower()

    new = ""
    for i in range(0, len(sponge)-1):
        if i%2 == 1 and sponge[i] != " ":
            new = new + sponge[i].upper()
        elif i%2 == 0 and sponge[i] != " ":
            new = new + sponge[i].lower()
        elif sponge[i] == " ":
            new = new + " "
    subprocess.run("pbcopy", text=True, input=new)
    new = new + " (Copied to clipboard)"
    spongebob_label.config(text=new)


def spongebob():
    # Example: turn "Hi guys welcome to this video" into "hI gUyS wElCoMe To ThIs ViDeO"
    clear_window()

    main_label = tk.Label(root, text="Spongebob text", bg=mc, fg=oc)
    main_label.pack()
    
    global main_input
    main_input = tk.Entry(root, bg=oc, fg=mc)
    main_input.pack()

    button_done = tk.Button(root, text="Sponge it!", bg=mc, fg=oc, command=sponge_it)
    button_done.pack()

    global spongebob_label
    spongebob_label = tk.Label(root, text="SpOnGe TeXt!")
    spongebob_label.pack()

def rubibuark():
    clear_window()

def scramble():
    clear_window()
    
    
def main():

    root.title("theBOYS Entertainment ---- Here to save your day!")
    root["bg"] = mc
    root.geometry("500x300")
    root.resizable = (False, False)
    
    main_label = tk.Label(root, name='main_label', text="theBOYS Home Entertainment System", bg=mc, fg=oc)

    options_frame = tk.Frame(name='options_frame', bg=mc)
    codify_button = tk.Button(options_frame, name='codify_button', text="Codify", command=codify)
    spongebob_button = tk.Button(options_frame, name='spongebob_button', text="sPoNgEbOb", command=spongebob)
    rubibuark_button = tk.Button(options_frame, name='rubibuark_button', text="Rubibuark", command=rubibuark)
    scramble_button = tk.Button(options_frame, name='scramble_button', text="Scramble", command=scramble)

    main_label.pack(pady=20)

    options_frame.pack(pady=20)
    codify_button.grid(row=0,column=0)
    spongebob_button.grid(row=0,column=1)
    rubibuark_button.grid(row=0,column=2)
    scramble_button.grid(row=0,column=3)


    root.mainloop()
    
main()