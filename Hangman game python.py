import random

class HangmanGame:
    def __init__(self):
        self.words = {
            "python": "Programming language",
            "keyboard": "Input device",
            "internet": "Global network",
            "algorithm": "Step-by-step solution",
            "database": "Stores structured data"
        }
        self.word, self.hint = random.choice(list(self.words.items()))
        self.display = ["_"] * len(self.word)
        self.attempts = 6
        self.score = 0
        self.used = set()

    def show_status(self):
        print("\nWord:", " ".join(self.display))
        print("Attempts left:", self.attempts)
        print("Used letters:", " ".join(sorted(self.used)))
        print("Score:", self.score)

    def guess_letter(self, letter):
        if letter in self.used:
            print("⚠️ Already used!")
            return

        self.used.add(letter)

        if letter in self.word:
            print("✅ Correct!")
            for i, ch in enumerate(self.word):
                if ch == letter:
                    self.display[i] = letter
                    self.score += 10
        else:
            print("❌ Wrong!")
            self.attempts -= 1
            self.score -= 5

    def play(self):
        print("🎮 Welcome to Advanced Hangman!")
        print("💡 Hint:", self.hint)

        while self.attempts > 0 and "_" in self.display:
            self.show_status()
            letter = input("Enter a letter: ").lower()

            if len(letter) != 1 or not letter.isalpha():
                print("⚠️ Enter a valid single letter!")
                continue

            self.guess_letter(letter)

        if "_" not in self.display:
            print("\n🎉 You Won!")
        else:
            print("\n💀 You Lost!")

        print("Word was:", self.word)
        print("Final Score:", self.score)


# Run game
game = HangmanGame()
game.play()
