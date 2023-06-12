import tkinter as tk
from tkinter import ttk
import os, random, json

# Encode/decode msgs with Deaconification
# scramble game
# spongebob textify
# translate into Randolang no, the language of Laadren
# Rubibuark??????????????? Whats this

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
    main_label = tk.Label(root, text="To encrypt text", bg=mc, fg=oc)
    main_label.pack()

    main_input = tk.Entry(root, bg=oc, fg=mc)
    main_input.pack()

def spongebob():
    #example: turn "Hi guys welcome to this video" into "hI gUyS wElCoMe To ThIs ViDeO"
    clear_window()

    main_label = tk.Label(root, text="To spongebob text", bg=mc, fg=oc)
    main_label.pack()
    
    main_input = tk.Entry(root, bg=oc, fg=mc)
    main_input.pack()

    sponge = main_input.get()
    new = ""
    for i in range(0, len(sponge)-1):
        #check if even or odd position
        if i%2 == 0:
            new.append(sponge[i].lower())
        else:
            new.append(sponge[i].upper())# Upload to git
    #Bye
    new_var = tk.StringVar()
    spongebob_label = tk.Label(text="iM a SpOnGe", textvariable = new_var)


    #You can close it, I copied the code to IDLE
    #I can do that 
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

#That means we need to use global And it solves a lot of problems
#How?