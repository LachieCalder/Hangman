# Simple hangman game in python
# Lachie Calder

import random
import sys

stages = [["___   "],

          ["_|_   "],
          
          [" |    ",
           "_|_   "],
           
          [" |    ",
           " |    ",
           "_|_   "],
           
          [" |    ",
           " |    ",
           " |    ",
           "_|_   "],
           
          [" ____ ",
           " |    ",
           " |    ",
           " |    ",
           " |    ",
           "_|_   "],
           
          [" ____ ",
           " |  | ",
           " |    ",
           " |    ",
           " |    ",
           "_|_   "],
           
          [" ____ ",
           " |  | ",
           " |  O ",
           " |    ",
           " |    ",
           "_|_   "],
           
          [" ____ ",
           " |  | ",
           " |  O ",
           " | /|\\",
           " |    ",
           "_|_   "],
           
          [" ____ ",
           " |  | ",
           " |  O ",
           " | /|\\",
           " | / \\",
           "_|_   "]]
           
class HangmanGame:
    
    def __init__(self, games):
        """
            games - the number of games to be played
            words_used = the secret words used during the game
                         (ensures no repeats are used)
        """
        self.games = games
        self.words_used = []
        self.start_game()
        
    def start_game(self):
        """Main game function containing game loop"""
        while self.games > 0:
            print("New game started. " + str(self.games) + " game/s remaining")
            self.games -= 1
            self.guessed_letters = []
            self.get_new_word()
            self.guesses = 0
            while True:
                self.display_status()
                if self.word.guessed(self.guessed_letters):
                    print("You won!")
                    break
                if self.guesses == 9:
                    self.display_game_over()
                    break
                self.get_guess()
            
    def display_game_over(self):
        print("You failed!")
        print("The word was " + self.word.word)

    def get_new_word(self):
        """Gets a new secret word to guess"""
        while True:
            self.word = SecretWord()
            if self.word.word not in self.words_used:
                self.words_used.append(self.word.word)
                break

    def display_status(self):
        """Prints hangman ASCII and game status"""
        print('\n')
        for line in stages[self.guesses]: print(line)
        for c in self.word.get_word_guessed(self.guessed_letters): 
            print(c, end=" ")
        print("\nLetters Used:")
        for letter in self.guessed_letters: 
            print(letter, end=", ")
        print("\nGuesses Remaining:")
        print(9 - self.guesses)
        
    def get_guess(self):
        """Gets and validates guess from player"""
        while True:
            letter = input("Guess a letter: ").lower()
            if letter in self.guessed_letters:
                print("You've already guessed that letter")
            elif letter.isalpha():
                self.guessed_letters.append(letter)
                if letter not in self.word.word:
                    self.guesses += 1
                return
        
class SecretWord:
    
    def __init__(self):
        """word - the word being guessed by the player"""
        self.word = self.random_word().lower()
    
    def get_word_guessed(self, guessed_letters):
        """Returns a string of the word with letters guessed filled in"""
        return [c if c in guessed_letters else '_' for c in self.word]
    
    def guessed(self, guessed_letters):
        return not '_' in self.get_word_guessed(guessed_letters)
    
    def random_word(self, source="words.txt"):
        """Returns a random word from source file in current directory"""
        # slice to remove newlines
        return random.choice(open(source, 'r').readlines())[:-1]
        
def main():
    print("Hello! Would you like to play a game of hangman?")
    if input("Y/N: ").lower() == 'n': return
    print("How many games do you want to play?")
    
    while True:
        games = int(input("A number 1-3 (inclusive): "))
        if games > 0 and games < 4:
            break
        print("Invalid number")
    
    game = HangmanGame(games)
    
main()