from random import randint as rndm

class Player:

    def __init__(self, player, playerBoard, enemyBoard):
        self.player = player
        self.playerBoard = []
        self.enemyBoard = []

    def makePlayerBoardFunc(self):
        playersBoard = [[0 for x in range(10)] for y in range(10)]
        return playersBoard

    def makeEnemyBoard(self):
        enemyBoard = [[0 for x in range(10)] for y in range(10)]
        return enemyBoard

    def outputFunc(self):
        self.playerBoard = self.makePlayerBoardFunc()
        self.enemyBoard = self.makeEnemyBoard()
        return self.playerBoard, self.enemyBoard

    def shootFunc(self, firstInt, secondInt):

        if self.playerBoard[firstInt][secondInt] == 1:
            print("Есть попадание, о мой адмирал")
            self.enemyBoard[firstInt].insert(secondInt, 'x')
            self.enemyBoard[firstInt].pop(secondInt + 1)
            print(*self.enemyBoard, sep = '\n')
            print('Ваш ход, о мой адмирал')
            print(*self.playerBoard, sep = '\n')
            # inputFunc(player, list)

        else:
            print('Промах')
            self.enemyBoard[firstInt].insert(secondInt, '.')
            self.enemyBoard[firstInt].pop(secondInt + 1)
            print(*self.enemyBoard, sep='\n')
            print('Ваш ход, о мой адмирал')
            print(*self.playerBoard, sep = '\n')
            # inputFunc()


class Ship:
    
    def __init__(self, player, type, number):
        self.player = player.playerBoard
        self.type = type
        self.number = number

    def horizontalBooleanFunc(self):
        horizontal = rndm(0, 1) # должно стоять от нуля до единицы
        print('Random boolean is ' + str(horizontal))
        return horizontal

    def placeShipsFunc(self):

        def placeHorizontal(self):
            print('ставим  корабль горизонтально')

            ship = [1 for i in range(self.type)]
            print('Ship is - ' + str(ship))

            x = rndm(0, 9)
            print('rndm x = ' + str(x))
            y = rndm(0, 9)
            print('rndm y = ' + str(y))

            del self.player[y][x:9]
            for digits in ship:
                self.player[y].insert(x, digits)
                 

            if len(self.player[y]) > 10:
                print('Длина больше 10 символов')
                howMuChDel = len(self.player[y]) - 10
                del self.player[y][0:howMuChDel]

            elif len(self.player[y]) < 10:
                print('Длина меньше десяти символов')
                howMuchAdd = 10 - len(self.player[y])

                for i in range(howMuchAdd):
                    self.player[y].append(0)

            else:
                print('В самый раз')
                                        
            # print(*self.player, sep = '\n')

        
        def placeVertical(self):
            print('ставим  корабль вертикально')
            print(self.type)
            print(self.number)

            ship = [1 for i in range(self.type)]
            print('Ship is - ' + str(self))

            x = rndm(0, 9)
            print('x = ' + str(x))
            y = rndm(0, 9)
            print('y = ' + str(y))

            counter = 0
            for i in range(self.type):
                self.player[y + counter].insert(x, 1)
                counter -= 1

            for rows in self.player:
                if len(rows) > 10:
                    rows.pop(-1)



        for ships in range(self.number):
            
            if Ship.horizontalBooleanFunc(self) == 1:
                placeHorizontal(self)

            else:
                placeVertical(self)

        print(*self.player, sep = '\n')


# playerOne = Player('playerOne', 'playerOneBoard', 'playerOneEnemyBoard')
# playerOne.outputFunc()

# ship = Ship(playerOne, 2, 3)
# ship.placeShipsFunc()

# def inputFunc():
#     coords = []
#     coords = input('введите две координаты через запятую, чтобы произвести выстрел ')

#     print(*coords, sep='\n')
#     playerOne.shootFunc(int(coords[0]), int(coords[2]))


