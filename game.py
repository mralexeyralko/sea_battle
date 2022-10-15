from classes import *

playerOne = Player('playerOne', 'playerOneBoard', 'playerOneEnemyBoard')
playerOne.outputFunc()

ship = Ship(playerOne, 2, 3)
ship.placeShipsFunc()

def inputFunc():
    coords = []
    coords = input('введите две координаты через запятую, чтобы произвести выстрел ')

    print(*coords, sep='\n')
    playerOne.shootFunc(int(coords[0]), int(coords[2]))

inputFunc()

