#!/usr/bin/env python3
#
# Problem: Word Game
# Files:
#Score_Card.csv
#study_word_combinations.csv
#grade_word_combinations.csv
#learn_word_combinations.csv
#
# Author: Samuel Brown
# Date: 5-May-2026

#Imported modules
import csv
import random
#Word list files
SCORE_CARD = "Score_Card.csv"
STUDY_WORD = "study_word_combinations.csv"
GRADE_WORD = "grade_word_combinations.csv"
LEARN_WORD = "learn_word_combinations.csv"

#Randomly select a file for the player
filename = random.choice([STUDY_WORD, GRADE_WORD, LEARN_WORD])

class Back_End:
    def __init__(self):
        #Getting the user's text so it can be easily reused
        self.user_guess = ""
        #Getting the first word in the word list for the user to play with
        self.main_word = ""
        #Storing all of the current player names:scores from the csv in a dictionary
        self.player_list = {}
        #Populate player_list to update old player scores
        self.load_scores()
        #Getting the player's name
        self.current_player_name = ""
        #Storing the current player's score
        self.current_player_score = 0
        #The player with the highest score
        self.highscore = 0
        #List of words the player successfully guessed so they don't reused guessed words
        self.already_guessed = []
        #Total list of correct words the player can guess
        self.list_of_words = []
        #Populates the self.list_of_words
        self.load_word_list()
        #True False statement to decide to give the player a good or bad meme
        self.good_meme = True
        #This is the player's response after they submit his/her answer
        self.response = ""

    #Method that retrieves the player's name and adds it and their score to the Score_Card
    def player_login(self, player_name):
        #First, read the CSV file and upload data to a dictionary

        #Fetch player's name from entry box and assign it to the attribute
        self.current_player_name = player_name

        #Reset list to avoid old data
        self.player_list = {}

        #Reads CSV file
        with open(SCORE_CARD, newline="", mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Store the Player name as the key, and convert the Score to an Integer
                self.player_list[row["Player"]] = int(row["Score"])

        #Ask if the name is in the dictionary. IF PLAYER IS ALREADY IN LIST, SKIP THIS PART 
        if self.current_player_name not in self.player_list:
            #Write to Score_Card csv file
            with open(SCORE_CARD, "a", newline="") as file:
                    writer = csv.DictWriter(file, fieldnames=["Player", "Score"])
                    #Saves the new player and his/her score to the Score_Card
                    writer.writerow({"Player": self.current_player_name, "Score": 0})
                    #Adds new Player Name and Score to dictionary
                    self.player_list[self.current_player_name] = 0


    def load_scores(self):
        with open(SCORE_CARD, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.player_list[row["Player"]] = int(row["Score"])
            #Populate scores in player_list attribute
        if self.player_list:
            self.highscore = max(self.player_list.values())



            

    #Method that writes the word list once to the list_of_words attribute. Makes it faster and easier to apprehend.
    def load_word_list(self):
        # Ensures it's empty before populating
        self.list_of_words = [] 

        with open(filename, newline="", encoding="utf-8") as file:
            contents_of_file = csv.reader(file)
            for row in contents_of_file:
                #Make sure row is not empty
                if row:
                    #Iterate through each row and append each word
                    self.list_of_words.append(row[0].strip().lower())
        return self.list_of_words
        #Test to make sure function executed
        print(f"Executed load_word_list from Game_Engine\n. Loaded {len(self.list_of_words)} words from {filename}")

    #Method for updating the word prompt in the game_frame with the main word
    def start_game(self):
        #Executes the load_word_list method to populate the list_of_words attribute
        self.list_of_words = self.load_word_list() 
        #Assigning the game word to play with
        self.main_word = self.list_of_words[0]
        #This part feeds into the start_game function to appear in the GUI label
        return self.main_word

    #Method for displaying the player's current score and save it in the save_progress method
    def get_player_score(self):
        #Assigning the current player's score to the player_score class attribute
        self.current_player_score = self.player_list[self.current_player_name]
        return self.current_player_score

    def announce_winner(self):
        #Takes dictionary of players and scores, the self.current_player_score attribute, and evaluates
        #which player has the highest score. Then, announce if they won the high score.
        #This is faster and more efficient than constantly searching the csv file every time the player makes a guess.
        #At the end of the game, the data will be saved to the CSV file with the save_progress method.


        #Get all scores from the list EXCEPT the current player's
        other_scores = [score for name, score in self.player_list.items() if name != self.current_player_name]
        
        #If there are no other scores yet, they are the winner by default
        if not other_scores:
            return True
            
        #Get the highest score currently in the list
        highest = max(other_scores)
        
        #If the player's score is equal to or greater than high score, then True. If not, then they are still a loser
        #and the value is False.
        return self.current_player_score > highest
        


    #Method that compares user's answer with word list
    def submit_answer(self, player_guess):
            #Makes player's guess proper case no matter what
            player_guess = player_guess.lower().strip()

            #Test if function ran
            print("Testing if submit_answer executed in Game_Engine\n")
            
            #List of already answered words so the user can't get more points by guessing the same word
            if player_guess in self.already_guessed:
                #Text to screen
                self.response = f"You already guessed {player_guess}! Guess again"
            
            #Correctly answered word response
            elif player_guess in self.list_of_words:
                #Add to player's score and check to see if the player won the high score
                self.current_player_score += 1

                #Update the highscore
                self.player_list[self.current_player_name] = self.current_player_score

                #Add answer to list of guessed words
                self.already_guessed.append(player_guess)

                #Text to screen
                self.response = f"CONGRAGULATIONS! {player_guess} IS A WORD! 1 point has been added to your score"

                
                #Reward with meme image
                self.good_meme = True

            #Incorrectly answered word response
            else:
                self.response = f"BZZZZZ!!! {player_guess} IS NOT A WORD! try again"

                #Punish with meme image
                self.good_meme = False


    #Method that shows the top five high scores
    def top_high_scores(self):
        #Store the hightest 5 entries 
        top_five = sorted(self.player_list.items(), key=lambda x: x[1], reverse=True)
    
        #Test to see if the method executed
        print(f"Testing if top_high_scores in Game_Engine executed.\nThe top five high scores are {top_five}")

        #return values
        return top_five[:5]

                
    #Method that saves the player's score at the end of the game
    def save_progress(self):
        #Add score to Score_Card.
        with open(SCORE_CARD, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            #Overwrite header
            writer.writerow(["Player", "Score"])
            #Replace player names and scores
            for name, score in self.player_list.items():
                writer.writerow([name, score])
        #Test
        print(f"Saved {self.current_player_name}'s score of {self.current_player_score} to file.")

