from datetime import datetime as dt
from random import randint

from access_control import access_control
from constants import UNKNOWN_COMMAND, ADMIN_USERNAME


class GuessNumberGame():
    def __init__(self):
        self.username = self.get_username()
        self.total_games = 0
        self.number = randint(1, 100)
        self.start_time = dt.now()

    @access_control
    def get_statistics(self, **kwargs) -> None:
        game_time = dt.now() - self.start_time
        print(f"Общее время игры: {game_time}, "
              f"текущая игра - №{self.total_games}")

    @access_control
    def get_right_answer(self, **kwargs) -> None:
        print(f"Правильный ответ: {self.number}")

    def check_number(self, guess: int) -> bool:
        # Если число угадано...
        if guess == self.number:
            print(f"Отличная интуиция, {self.username}! Вы угадали число :)")
            # ...возвращаем True
            return True

        if guess < self.number:
            print("Ваше число меньше того, что загадано.")
        else:
            print("Ваше число больше того, что загадано.")
        return False

    @staticmethod
    def get_username() -> str:
        username = input('Представьтесь, пожалуйста, как Вас зовут?\n').strip()
        if username == ADMIN_USERNAME:
            print(
                '\nДобро пожаловать, создатель! '
                'Во время игры вам доступны команды "stat", "answer"'
            )
        else:
            print(f'\n{username}, добро пожаловать в игру!')
        return username

    def guess_number(self):
        while True:
            self.total_games += 1
            self.game()
            play_again = input("\nХотите сыграть ещё? (yes/no) ")
            if play_again.strip().lower() not in ("y", "yes"):
                break

    def game(self):
        print(
            "\nУгадайте число от 1 до 100.\n"
            'Для выхода из текущей игры введите команду "stop"'
        )
        while True:
            user_input = input("Введите число или команду: ").strip().lower()
            match user_input:
                case "stop":
                    break
                case "stat":
                    self.get_statistics(username=self.username)
                case "answer":
                    self.get_right_answer(username=self.username)
                case _:
                    try:
                        guess = int(user_input)
                    except ValueError:
                        print(UNKNOWN_COMMAND)
                        continue

                    if self.check_number(guess):
                        break


if __name__ == '__main__':
    game = GuessNumberGame()
    game.game()
