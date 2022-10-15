from random import randint as rndm

class Player:

    def __init__(self, playersBoard, enemyBoard):
        self.playersBoard = playersBoard
        self.enemyBoard = enemyBoard
    
    def makePlayerBoardFunc(playersBoard):
        playersBoard = [[0 for x in range(10)] for y in range(10)]
        print("Player's board is:")
        print(*playersBoard, sep = '\n')
        playersBoard = list(playersBoard)
        print(playersBoard)
        return playersBoard
    
    def makeEnemyBoard(enemyBoard):
        enemyBoard = [[1  for x in range(10)] for y in range(10)]
        print("Enemy's board is:")
        print(*enemyBoard, sep = '\n')
        return enemyBoard


# myBoard = Player
# myBoard = Player.makeBoardFunc(myBoard)


playerOne = Player
# playerOne.makeEnemyBoard('playerOneBoard')
# playerOne.makePlayerBoardFunc()


# print('myboard is' + str(myBoard))

# class Board:     

#     def makeBoardFunc(playerName):
#         name = [[0 for x in range(10)] for y in range(10)]
#         return name

# myBoard = Board
# myBoard = myBoard.makeBoardFunc()


# print(type(myBoard))

class Ship:
    def __init__(self, type, number):
        self.player = Player(self.playersBoard)
        self.type = type
        self.number = number

    def horizontalBooleanFunc():
        horizontal = rndm(1, 1) # должно стоять от нуля до единицы
        print('Random boolean is ' + str(horizontal))
        return horizontal

    def placeShipsFunc(player, type, number):

        def placeHorizontal(type, number):
            print('ставим  корабль горизонтально')
            Player.makePlayerBoardFunc(player)

            ship = [1 for i in range(type)]
            print('Ship is - ' + str(ship))

            for i in range(number):
                x = rndm(0, 9)
                print('x = ' + str(x))
                y = rndm(0, 9)
                print('y = ' + str(y))


                # del Player.makePlayerBoardFunc(player[y][x:9])
                for digits in ship:
                    Player.makePlayerBoardFunc(player[y].insert(x, digits))
                 

                if len(Player.makePlayerBoardFunc(player[y])) > 10:
                    print('Длина больше 10 символов')
                    howMuChDel = len(Player.makePlayerBoardFunc(player[y])) - 10
                    # del Player.makePlayerBoardFunc(player[y][0:howMuChDel])

                elif len(Player.makePlayerBoardFunc(player[y])) < 10:
                    print('Длина меньше десяти символов')
                    howMuchAdd = 10 - len(player[y])
                    for i in range(howMuchAdd):
                        player[y].append(0)
                else:
                    print('В самый раз')
                                        
            print(*player, sep = '\n')
            print(type)
            print(number)
        
        def placeVertical(type, number):
            print('ставим  корабль вертикально')
            print(type)
            print(number)

            ship = [1 for i in range(type)]
            print('Ship is - ' + str(ship))

            x = rndm(0, 9)
            print('x = ' + str(x))
            y = rndm(0, 9)
            print('y = ' + str(y))

            counter = 0
            for i in range(type):
                player[y + counter].insert(x, 1)
                counter -= 1

            for rows in player:
                if len(rows) > 10:
                    rows.pop(-1)

            print(*player, sep = '\n')

        if ship.horizontalBooleanFunc() == 1:
            placeHorizontal(type, number)

        else:
            placeVertical(type, number)


ship = Ship
# ship2 = Ship
# ship3 = Ship
# ship4 = Ship
# ship5 = Ship

ship.placeShipsFunc(playerOne, 5, 2)
# ship2.placeShipsFunc(4, 2)
# ship3.placeShipsFunc(3, 3)
# ship4.placeShipsFunc(2, 4)
# ship5.placeShipsFunc(1, 5)

