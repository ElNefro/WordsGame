import random


class WordPicker:
    def __init__(self, words):
        self.words = words

    def choose_word(self):
        return random.choice(self.words)


class Player:
    def __init__(self, max_attempts):
        self.guessed_letters = set()
        self.max_attempts = max_attempts
        self.remaining_attempts = max_attempts

    def make_guess(self, letter):
        if letter in self.guessed_letters:
            print("Вы уже угадали эту букву.")
            return False

        self.guessed_letters.add(letter)
        return True

    def guess_is_correct(self, letter, secret_word):
        return letter in secret_word

    def decrement_attempts(self):
        self.remaining_attempts -= 1

    def is_alive(self):
        return self.remaining_attempts > 0

    def display_status(self):
        print("Угаданные буквы: {}".format(", ".join(sorted(self.guessed_letters))))
        print("Оставшиеся попытки: {}".format(self.remaining_attempts))


class WordGame:
    def __init__(self, words, max_attempts):
        self.word_picker = WordPicker(words)
        self.secret_word = self.word_picker.choose_word()
        self.player = Player(max_attempts)

    def display_word(self):
        displayed_word = ''.join(
            [letter if letter in self.player.guessed_letters else '_' for letter in self.secret_word])
        print("Текущее слово: {}".format(displayed_word))

    def check_win(self):
        return all(letter in self.player.guessed_letters for letter in self.secret_word)

    def play(self):
        print(" ")
        print("Добро пожаловать в игру 'Угадай слово'!")
        print("Загаданное слово состоит из {} букв.".format(len(self.secret_word)))

        while self.player.is_alive():
            self.display_word()
            self.player.display_status()

            guess = input("Введите букву: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Пожалуйста, вводите только одну букву.")
                continue

            if not self.player.make_guess(guess):
                continue

            if self.player.guess_is_correct(guess, self.secret_word):
                print(" ")
                print("Правильный ответ!")
                print(" ")
            else:
                print(" ")
                print("Неправильный ответ.")
                print(" ")
                self.player.decrement_attempts()

            if self.check_win():
                print(" ")
                print("Поздравляем! Вы угадали слово: {}".format(self.secret_word))
                break
        else:
            print(" ")
            print("Вы проиграли! Загаданное слово было: {}".format(self.secret_word))


if __name__ == "__main__":
    words = ["программа", "машина", "автомобиль", "светофор", "друзья", "роза", "компьютер", "программирование"]
    max_attempts = 6
    game = WordGame(words, max_attempts)
    game.play()