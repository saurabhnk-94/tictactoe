class Tictactoe:
    game_data = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    number_of_moves = 0

    @classmethod
    def is_game_over(cls):
        game_finished = False
        for value in range(9):
            if value == 0 or value == 3 or value == 6:
                if cls.game_data[value] == cls.game_data[value + 1] == cls.game_data[value + 2]:
                    game_finished = True
                    break
            elif value == 0 or value == 1 or value == 2:
                if cls.game_data[value] == cls.game_data[value + 3] == cls.game_data[value + 6]:
                    game_finished = True
                    break
            elif value == 0:
                if cls.game_data[value] == cls.game_data[value + 4] == cls.game_data[value + 8]:
                    game_finished = True
                    break
            elif value == 2:
                if cls.game_data[value] == cls.game_data[value + 2] == cls.game_data[value + 4]:
                    game_finished = True
                    break
            else:
                game_finished = False
        if cls.number_of_moves == 9 or game_finished:
            return True
        else:
            return False

    @classmethod
    def is_a_move(cls):
        Tictactoe.number_of_moves += 1

    @classmethod
    def update_game_data(cls, index, value):
        cls.game_data[index] = value

    @classmethod
    def check_value(cls, index):
        if cls.game_data[index] == 'X' or cls.game_data[index] == 'O' or cls.game_data[index] == 'x' or cls.game_data[index] == 'o':
            return True
        else:
            return False


class User(Tictactoe):
    def __init__(self, name):
        self.name = name

    def make_move(self):
        super().is_a_move()
        acknowledgement = super().is_game_over()
        return acknowledgement


if __name__ == '__main__':
    game_status = False
    game_obj = Tictactoe()
    first_player = User(input('First player name:\t'))
    second_player = User(input('Second player name:\t'))
    while not game_status:
        print('|----------|----------|----------|')
        print(f'|     {game_obj.game_data[0]}    |     {game_obj.game_data[1]}    |     {game_obj.game_data[2]}    |')
        print('|----------|----------|----------|')
        print(f'|     {game_obj.game_data[3]}    |     {game_obj.game_data[4]}    |     {game_obj.game_data[5]}    |')
        print('|----------|----------|----------|')
        print(f'|     {game_obj.game_data[6]}    |     {game_obj.game_data[7]}    |     {game_obj.game_data[8]}    |')
        print('|----------|----------|----------|')
        if game_obj.number_of_moves % 2 == 0:
            game_over = game_obj.is_game_over()
            if not game_over:
                selected_box = int(input(f"{first_player.name}! Enter respective box Number to mark:\t"))
                selected_box = selected_box - 1
                if selected_box < 0 or selected_box > 9 or game_obj.check_value(selected_box):
                    print('Enter Valid box number')
                else:
                    # print('Please enter O')
                    # user_value = input("Enter your character:\t")
                    user_value = 'O'
                    if user_value == 'O' or user_value == 'o':
                        game_status = first_player.make_move()
                        game_obj.update_game_data(selected_box, user_value)
                    else:
                        print('Please enter O!')
            else:
                print('Game is Over')
                print(f'{second_player.name} has won!!')
                game_status = True

        else:
            game_over = game_obj.is_game_over()
            if not game_over:
                selected_box = int(input(f"{second_player.name}! Enter respective box Number to mark:\t"))
                selected_box = selected_box - 1
                if selected_box < 0 or selected_box > 9 or game_obj.check_value(selected_box):
                    print('Enter Valid box number')
                else:
                    # print('Please enter X ')
                    # user_value = input("Enter your character:\t")
                    user_value = 'X'
                    if user_value == 'X' or user_value == 'x':
                        game_status = second_player.make_move()
                        game_obj.update_game_data(selected_box, user_value)
                    else:
                        print('Please enter X!')
            else:
                print('Game is Over')
                print(f'{first_player.name} has won!!')
                game_status = True

