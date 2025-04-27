import random


class WordGame:
    def __init__(self):
        self.words = ["программа", "машина", "автомобиль", "светофор", "друзья", "роза", "компьютер", "программирование"]
        self.secret_word = ""
        self.guesses = []
        self.max_attempts = 6
        self.attempts_left = self.max_attempts

    def choose_word(self):
        self.secret_word = random.choice(self.words)
        print(" ")
        print(" ")
        print("Загадано слово из {} букв.".format(len(self.secret_word)))

    def display_status(self):
        word_display = "".join([letter if letter in self.guesses else "_" for letter in self.secret_word])
        print(" ")
        print("=========================================================================================")
        print(" ")
        print("Слово: ", word_display)
        print("Попыток осталось: ", self.attempts_left)
        print("Угаданные буквы: ", " ".join(sorted(self.guesses)))

    def make_guess(self, guess):
        if guess in self.guesses:
            print("Вы уже угадали эту букву. Попробуйте еще раз!")
            return

        self.guesses.append(guess)

        if guess not in self.secret_word:
            self.attempts_left -= 1
            print("Неправильно! Буква отсутствует в слове.")
        else:

            print("Правильно! Буква '{}' есть в слове.".format(guess))

    def check_win(self):
        return set(self.secret_word).issubset(set(self.guesses))

    def play(self):
        self.choose_word()
        while self.attempts_left > 0:
            self.display_status()
            guess = input("Введите букву: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Пожалуйста, вводите только одну букву.")
                continue

            self.make_guess(guess)

            if self.check_win():
                print("Поздравляем! Вы угадали слово: {}".format(self.secret_word))
                break
        else:
            print("Вы проиграли! Загаданное слово было: {}".format(self.secret_word))


if __name__ == "__main__":
    game = WordGame()
    game.play()