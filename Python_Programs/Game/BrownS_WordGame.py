#!/usr/bin/env python3
#
# Problem: Word Game
# Files:
# Game_Engine.py
# images.jpg
# Emptiness.jpeg
#
# Author: Samuel Brown
# Date: 5-May-2026

#Import modules
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Game_Engine import Back_End
#This module handles other kinds of image files
from PIL import Image, ImageTk


#Instance of object containing data from Game_Engine
my_game_engine = Back_End()


#Function that executes the player login method and the transition function
def login_frame_functions():
    #Get the data from the entry box
    player_name = name_entry.get()
    
    #Method for logging the player in
    my_game_engine.player_login(player_name)

    #Function for closing the login frame and moving to the game frame
    player_login_frame.pack_forget()

    load_game_word()

    # Shows the game frame
    game_frame.pack()         


#Function to show meme image
def show_player_meme():
    #Create the Toplevel window
    top = tk.Toplevel(root)
    
    
    #Dynamically add meme with if statement
    if my_game_engine.good_meme == True:
        #Good meme image
        pil_image = Image.open("images.jpg")
        
        # Convert it to a Tkinter-compatible image
        meme_image = ImageTk.PhotoImage(pil_image)
        
        # Create a label to hold the image
        meme_label = ttk.Label(top, image=meme_image)
        meme_label.pack()
        
        # IMPORTANT: Keep a reference to the image!
        # If you don't do this, Python's garbage collector will delete 
        # the image object and your label will appear blank.
        meme_label.image = meme_image
        #meme = tk.PhotoImage(file="images.jpg")
        #tk.Label(top, image=meme).pack(padx=20, pady=20)

    else:
        #Bad meme image
        pil_image = Image.open("Emptiness.jpeg")
        
        # Convert it to a Tkinter-compatible image
        meme_image = ImageTk.PhotoImage(pil_image)
        
        # Create a label to hold the image
        meme_label = ttk.Label(top, image=meme_image)
        meme_label.pack()
        
        # IMPORTANT: Keep a reference to the image!
        # If you don't do this, Python's garbage collector will delete 
        # the image object and your label will appear blank.
        meme_label.image = meme_image
        #meme = tk.PhotoImage(file="Emptiness.jpeg")
        #tk.Label(top, image=meme).pack(padx=20, pady=20)
    
    #Creating popup meme image
    top.title(meme_label)

    #Meme image gets destroyed after 3 sec
    top.after(3000, top.destroy)


#Function that retrieves the user's answer
def get_user_answer(guess):
    #Error handling if user doesn't type a word
    try:
        #Gets user's text
        guess = word_answer.get()

        #Error handling if user inputs anything other than letters
        assert guess.isalpha()

        #The data in the entry box to be used in multiple_functions
        return guess
    #If the user doesn't enter a word then show error
    except AssertionError as invalid:
        invalid("Invalid Input", "Please only enter letters.") 

#This function configures the game word for the player after the login process is complete
def load_game_word():
    # Update the game engine
    new_word = my_game_engine.start_game()
    
    # Update the label specifically using .config()
    game_word.config(text=f"THE WORD IS {new_word}")

    #Test to see if the word list loaded properly
    print(my_game_engine.list_of_words)

def refresh_high_score_display():
    # Get data from Game_Engine
    top_five_data = my_game_engine.top_high_scores()
    
    #Format it into a string
    display_string = "TOP 5 HIGH SCORES:\n"
    for name, score in top_five_data:
        display_string += f"{name}: {score} \n"
    
    #Update the VarString
    highscore_text.set(display_string)

#Function for button to check player guess and show meme
def multiple_functions():
    #Is this function running when player submits answer?
    print("Testing if the multiple_functions executed in GUI after button click")

    #Obtaining the get_user_answer argument
    guess = word_answer.get()
    #Retrieving the player's guess
    current_guess = get_user_answer(guess)

    #Evaluate the player's guess
    my_game_engine.submit_answer(current_guess)

    #Update the HIGH SCORES
    refresh_high_score_display()

    #This presents the meme after the player's answer has been evaluated
    show_player_meme()

    #This will update the player's current score and future high score list
    current_player_score_label.config(text=f"YOUR CURRENT SCORE IS: {my_game_engine.current_player_score}")

    #This will announce the evaluation of the submitted answer
    response_text.set(my_game_engine.response)

    #Announce to player if they won the HIGH SCORE
    if my_game_engine.announce_winner() > my_game_engine.highscore:
        messagebox.showinfo("High Score Alert", f"Congratulations! You earned the HIGH SCORE!")


#Function to display the player's current score in a label
def display_score():
    #retrieving the score
    new_score = my_game_engine.get_player_score()

    #Configuration of the player's score
    current_player_score_label.config(text=f"YOUR SCORE: {new_score}")



def save_and_quit():
    #Save the player's score to Score_Card
    my_game_engine.save_progress()
    
    #Close the game
    root.destroy()

#Create window
root = tk.Tk()

#Title of program
root.title("Word Game")

#Window size
root.geometry("800x400")

#Frame containers for the login window and the game window
player_login_frame = ttk.Frame(root)
game_frame = ttk.Frame(root)

#Pack the login frame (show it first)
player_login_frame.pack()


"""WIDGETS FOR GETTING PLAYER NAME AND SCORE CARD"""
#Prompt widget requesting player name
name_prompt = ttk.Label (player_login_frame, text=f"Enter Player Name: ")
name_prompt.grid (padx=5, pady=5, column=0, row=0)

#Entry box widget for player to enter his/her player name
name_entry = ttk.Entry (player_login_frame, width=25)
name_entry.grid (padx=5, pady=5, column=1, row=0)

#Button widget to either add new player name to Score_Card or find player name in Score_Card
button_one = ttk.Button (player_login_frame, text="Add Player Name", command=login_frame_functions)
button_one.grid (padx=5, pady=5, column=2, row=0)


"""This section of code presents the main game in play"""


#Label of this game's word
game_word = ttk.Label (game_frame, text=f"THE WORD IS: ")
game_word.grid (padx=5, pady=5, column=0, row=0)

#IN THE FUTURE - possibly add a high score label of the top 5 players?


#Entry box widget for player to enter his/her word
word_answer = ttk.Entry (game_frame, width=25)
word_answer.grid (padx=5, pady=5, column=1, row=0)

#button for user to enter his/her answer
answer_button = ttk.Button (game_frame, text="Enter Answer", command=multiple_functions)
answer_button.grid (padx=5, pady=5, column=2, row=0)



#Displays the player's current score
current_player_score_label = ttk.Label(game_frame, text=f"YOUR CURRENT SCORE IS: {my_game_engine.current_player_score}", font=("Arial", 12))
current_player_score_label.grid(padx=5, pady=10, column=0, row=2, columnspan=3)



# Create a StringVar to hold the response
response_text = tk.StringVar()
response_text.set("Waiting for your guess...")

#Response if user answers correctly or not
announce_answer = ttk.Label(game_frame, textvariable=response_text, font=("Arial", 12), background="red")
announce_answer.grid(row=3, columnspan=3)



#StringVar that can be updated
highscore_text = tk.StringVar()
highscore_text.set("TOP FIVE HIGH SCORES: Loading...")


#Label linked to the StringVar
high_score_label = ttk.Label(game_frame, textvariable=highscore_text, font=("Arial", 10))
high_score_label.grid(row=4, column=0, columnspan=3)





#Add a Save and Quit button
save_quit_button = ttk.Button(game_frame, text="Save & Quit", command=save_and_quit)

save_quit_button.grid(padx=5, pady=20, column=0, columnspan=3, row=10)

if __name__=="__main__":

    root.mainloop()
