import sqlite3
import sys
import main_ui
import steam_api
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt

import os
from steam_web_api import Steam

class gameBase():
    def __init__(self):
        self.connection = sqlite3.connect('gameBase.db') # создаем базу данных
        self.cursor = self.connection.cursor() # курсор для выполнения операций
        self.createGamesDBTable()

    def createGamesDBTable(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS GamesTable (
        id INTEGER PRIMARY KEY,
        gameName TEXT NOT NULL,
        gameInfo TEXT,
        gamePlatform TEXT,
        gameIsPassed BLOB
        )
        ''')
        self.connection.commit()

    def createNewGame(self,gameName,gameInfo,gamePlatform,gameIsPassed):
        self.cursor.execute('INSERT INTO GamesTable (gameName, gameInfo, gamePlatform, gameIsPassed) VALUES (?, ?, ?, ?)',
                            (gameName, gameInfo, gamePlatform,gameIsPassed))
        self.connection.commit()

    def editGame(self,gameName,newGameName,gameInfo,gamePlatform,gameIsPassed):
        self.cursor.execute('UPDATE GamesTable SET gameName = ?, gameInfo = ?, gamePlatform = ?, gameIsPassed = ? WHERE gameName = ?',
                            (newGameName, gameInfo, gamePlatform,gameIsPassed, gameName))
        self.connection.commit()

    def deleteGame(self, gameName):
        self.cursor.execute('DELETE FROM GamesTable WHERE gameName = ?', (gameName,))
        self.connection.commit()

    def FindGame(self,gameName):
        self.cursor.execute('SELECT * FROM GamesTable WHERE gameName = ?', (gameName,))
        game = self.cursor.fetchall()
        return(game)

    def getGames(self):
        self.cursor.execute('SELECT * FROM GamesTable')
        games = self.cursor.fetchall()
        games_list = []
        for game in games:
            games_dict = {
                'id': game[0],
                'gameName': game[1],
                'gameInfo': game[2],
                'gamePlatform': game[3],
                'gameIsPassed': game[4]
                }
        games_list.append(games_dict)
        for game in games_list:
            print(game)

    def getAllGamesName(self):
        gamesNamesList = [game[0] for game in self.cursor.execute("SELECT gameName FROM GamesTable")]
        return gamesNamesList


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gamebase = gameBase()
    steamApi = steam_api.SteamGameFinder()
    window = main_ui.MyApp(gamebase, steamApi)
    window.show()
    sys.exit(app.exec())

#game_base = gameBase()

#game_base.createNewGame("GTA 4","Super Game","PC",1,100,"gta3.jpg")
#game_base.getGames()

class gameObj():
    def __init__(self,gameName,gameInfo,isPassed):
        self.gameName = gameName
        self.gameInfo = gameInfo
        self.isPassed = isPassed

