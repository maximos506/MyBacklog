from ast import IsNot
import main_project
import steam_api
import sys
import urllib
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt


class MyApp(QWidget,):
    def __init__(self,Gamebase, steamApi):
        super().__init__()
        frame = QFrame()
        self.getMainWindow()
        self.gamebase = Gamebase
        self.steamApi = steamApi

        self.addGameWidgets()
        for widget in self.addGameWidgets:
            widget.hide()

        self.lookGameList()
        for widget in self.lookGameListObjs:
            widget.hide()

        self.editGameList()
        for widget in self.editGameListObjs:
            widget.hide()

        self.deleteGameList()
        for widget in self.deleteGameListObjs:
            widget.hide()

        self.lookGameWidgets()
        for widget in self.lookgameWidgets:
            widget.hide()

    def getMainWindow(self):
        # Установка заголовка и размера окна
        self.setWindowTitle('My BackLog')
        self.setFixedSize(1000, 500)
        self.mainWindowWidgets = []

        # Создание вертикального компоновщика
        self.layout = QVBoxLayout()

        # Создание метки с текстом
        self.title_label = QLabel('My BackLog - создайте собственный бэклог игр!')
        self.title_label.setFont(QFont('Arial', 20))
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Создание метки для изображения
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.update_image('static\img\Logo.png')  # Укажите путь к изображению


        self.layout.addWidget(self.image_label)
        self.mainWindowWidgets.append(self.image_label)
        self.layout.addWidget(self.title_label)
        self.mainWindowWidgets.append(self.title_label)

        # Создание горизонтального компоновщика для кнопок
        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # Создание кнопок
        buttonSizeH = int(200)
        buttonSizeV = int(100)

        # кнопка создать игру (открыть меню)
        self.AddGameWindowButton = QPushButton('Добавить игру')
        self.AddGameWindowButton.setFont(QFont('Arial', 20))
        self.AddGameWindowButton.clicked.connect(self.AddGameButtonWindow_clicked) 
        self.AddGameWindowButton.setFixedSize(buttonSizeH, buttonSizeV)

        # кнопка изменить игру
        self.EditGameWindowButton = QPushButton('Изменить игру')
        self.EditGameWindowButton.setFixedSize(buttonSizeH, buttonSizeV)
        self.EditGameWindowButton.setFont(QFont('Arial', 20))
        self.EditGameWindowButton.clicked.connect(self.EditGameButtonWindow_clicked)

        # кнопка удалить игру
        self.DeleteGameWindowButton = QPushButton('Удалить игру')
        self.DeleteGameWindowButton.setFixedSize(buttonSizeH,buttonSizeV)
        self.DeleteGameWindowButton.setFont(QFont('Arial', 20))
        self.DeleteGameWindowButton.clicked.connect(self.DeleteGameButtonWindow_clicked)

        # кнопка просмотр игр
        self.WatchGamesWindowButton = QPushButton('Просмотр игр')
        self.WatchGamesWindowButton.setFixedSize(buttonSizeH,buttonSizeV)
        self.WatchGamesWindowButton.setFont(QFont('Arial', 20))
        self.WatchGamesWindowButton.clicked.connect(self.LookGameButtonWindow_clicked)

        # Добавление кнопок в горизонтальный компоновщик
        button_layout.addWidget(self.AddGameWindowButton)
        button_layout.addWidget(self.EditGameWindowButton)
        button_layout.addWidget(self.DeleteGameWindowButton)
        button_layout.addWidget(self.WatchGamesWindowButton)
        self.mainWindowWidgets.append(self.AddGameWindowButton)
        self.mainWindowWidgets.append(self.EditGameWindowButton)
        self.mainWindowWidgets.append(self.DeleteGameWindowButton)
        self.mainWindowWidgets.append(self.WatchGamesWindowButton)

        # Добавление горизонтального компоновщика в вертикальный
        self.layout.addLayout(button_layout)

        # Установка основного компоновщика
        self.setLayout(self.layout)

    def addGameWidgets(self):
        self.addGameWidgets = []

        self.add_game_title = QLabel('Добавление новой игры')
        self.add_game_title.setFont(QFont('Arial', 20))
        self.add_game_title.setFixedHeight(35)
        self.add_game_title.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.addGameWidgets.append(self.add_game_title)
        self.layout.addWidget(self.add_game_title)

        self.addGameForms = QVBoxLayout()

        self.gameNameLine = QHBoxLayout()
        self.gameInfoLine = QHBoxLayout()
        self.gamePlatformLine = QHBoxLayout()
        self.gameIsPassedLine = QHBoxLayout()

        self.inputTitlesFontSize = int(15)

        self.gameName_form = QLabel('Название игры:')
        self.gameName_form.setFont(QFont('Arial', self.inputTitlesFontSize))

        self.gameNameInputForm = QLineEdit(parent=self)
        self.gameNameInputForm.setFixedHeight(40)

        self.gameInfo_form = QLabel('Описание игры:')
        self.gameInfo_form.setFont(QFont('Arial', self.inputTitlesFontSize))

        self.gameInfoInputForm = QLineEdit(parent=self)

        self.gamePlatform_form = QLabel('Доступна на:')
        self.gamePlatform_form.setFont(QFont('Arial', self.inputTitlesFontSize))

        self.gamePlatformInputForm = QLineEdit(parent=self)

        self.gameIsPassed_form = QLabel('Игра пройдена:')
        self.gameIsPassed_form.setFont(QFont('Arial', self.inputTitlesFontSize))
        self.gameIsPassed_form.setFixedWidth(155)

        self.gameIsPassedInputForm = QCheckBox(parent=self)

        #self.gameIsPassedInputForm.setFixedWidth(55)

        self.gameNameLine.addWidget(self.gameName_form)
        self.gameNameLine.addWidget(self.gameNameInputForm)


        self.gameInfoLine.addWidget(self.gameInfo_form)
        self.gameInfoLine.addWidget(self.gameInfoInputForm)


        self.gamePlatformLine.addWidget(self.gamePlatform_form)
        self.gamePlatformLine.addWidget(self.gamePlatformInputForm)

        self.gameIsPassedLine.addWidget(self.gameIsPassed_form)
        self.gameIsPassedLine.addWidget(self.gameIsPassedInputForm)


        self.addGameForms.addLayout(self.gameNameLine)
        self.addGameForms.addLayout(self.gameInfoLine)
        self.addGameForms.addLayout(self.gamePlatformLine)
        self.addGameForms.addLayout(self.gameIsPassedLine)

        self.addGameForms.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.layout.addLayout(self.addGameForms)

        AddGame_button_layout = QHBoxLayout()
        AddGame_button_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        buttonSizeH = int(200)
        buttonSizeV = int(100)

        self.AddGameButton = QPushButton('Добавить игру')
        self.AddGameButton.setFont(QFont('Arial', 20))
        self.AddGameButton.clicked.connect(self.AddGameButton_clicked) 
        self.AddGameButton.setFixedSize(buttonSizeH, buttonSizeV)
        AddGame_button_layout.addWidget(self.AddGameButton)


        self.GetBackButton1 = QPushButton('Назад')
        self.GetBackButton1.setFont(QFont('Arial', 20))
        self.GetBackButton1.clicked.connect(self.getFromAddGame_ToMainWindow) 
        self.GetBackButton1.setFixedSize(buttonSizeH, buttonSizeV)
        AddGame_button_layout.addWidget(self.GetBackButton1)
        self.layout.addLayout(AddGame_button_layout)

        self.addGameWidgets.append(self.gameName_form)
        self.addGameWidgets.append(self.gameNameInputForm)
        self.addGameWidgets.append(self.gameInfo_form)
        self.addGameWidgets.append(self.gameInfoInputForm)
        self.addGameWidgets.append(self.gamePlatform_form)
        self.addGameWidgets.append(self.gamePlatformInputForm)
        self.addGameWidgets.append(self.gameIsPassed_form)
        self.addGameWidgets.append(self.gameIsPassedInputForm)
        self.addGameWidgets.append(self.GetBackButton1)
        self.addGameWidgets.append(self.AddGameButton)

    def lookGameList(self):
        self.lookGameListObjs = []
        self.listWidget = QListWidget();

        self.look_game_title = QLabel('Просмотр добавленных игр')
        self.look_game_title.setFont(QFont('Arial', 20))
        self.look_game_title.setFixedHeight(35)
        self.look_game_title.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.layout.addWidget(self.look_game_title)
        self.layout.addWidget(self.listWidget)

        LookGame_button_layout = QHBoxLayout()
        LookGame_button_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        buttonSizeH = int(200)
        buttonSizeV = int(100)

        self.LookGameButton = QPushButton('Просмотр игры')
        self.LookGameButton.setFont(QFont('Arial', 20))
        self.LookGameButton.clicked.connect(self.LookGameButton_clicked) 
        self.LookGameButton.setFixedSize(buttonSizeH, buttonSizeV)
        LookGame_button_layout.addWidget(self.LookGameButton)

        self.GetBackButton2 = QPushButton('Назад')
        self.GetBackButton2.setFont(QFont('Arial', 20))
        self.GetBackButton2.clicked.connect(self.fromLookGame_ToMainWindow) 
        self.GetBackButton2.setFixedSize(buttonSizeH, buttonSizeV)
        LookGame_button_layout.addWidget(self.GetBackButton2)

        self.layout.addLayout(LookGame_button_layout)

        self.lookGameListObjs.append(self.look_game_title)
        self.lookGameListObjs.append(self.listWidget)
        self.lookGameListObjs.append(self.LookGameButton)
        self.lookGameListObjs.append(self.GetBackButton2)

    def editGameList(self):
        self.editGameListObjs = []

        self.edit_game_title = QLabel('Изменение данных о игре')
        self.edit_game_title.setFont(QFont('Arial', 20))
        self.edit_game_title.setFixedHeight(35)
        self.edit_game_title.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.layout.addWidget(self.edit_game_title)

        self.EditlistWidget = QListWidget();

        self.layout.addWidget(self.EditlistWidget)


        EditGame_button_layout = QHBoxLayout()
        EditGame_button_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        buttonSizeH = int(200)
        buttonSizeV = int(100)

        self.EditGameButton = QPushButton('Изменить игру')
        self.EditGameButton.setFont(QFont('Arial', 20))
        self.EditGameButton.clicked.connect(self.EditGameButton_clicked) 
        self.EditGameButton.setFixedSize(buttonSizeH, buttonSizeV)
        EditGame_button_layout.addWidget(self.EditGameButton)

        self.GetBackButton3 = QPushButton('Назад')
        self.GetBackButton3.setFont(QFont('Arial', 20))
        self.GetBackButton3.clicked.connect(self.fromeditGame_ToMainWindow) 
        self.GetBackButton3.setFixedSize(buttonSizeH, buttonSizeV)
        EditGame_button_layout.addWidget(self.GetBackButton3)

        self.layout.addLayout(EditGame_button_layout)

        self.editGameListObjs.append(self.edit_game_title)
        self.editGameListObjs.append(self.EditlistWidget)
        self.editGameListObjs.append(self.EditGameButton)
        self.editGameListObjs.append(self.GetBackButton3)

    def deleteGameList(self):
        self.deleteGameListObjs = []
        self.deleteGameslistWidget = QListWidget();

        self.delete_game_title = QLabel('Удаление игры')
        self.delete_game_title.setFont(QFont('Arial', 20))
        self.delete_game_title.setFixedHeight(35)
        self.delete_game_title.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.layout.addWidget(self.delete_game_title)
        self.layout.addWidget(self.deleteGameslistWidget)

        deleteGame_button_layout = QHBoxLayout()
        deleteGame_button_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        buttonSizeH = int(200)
        buttonSizeV = int(100)

        self.DeleteGameButton = QPushButton('Удалить игру')
        self.DeleteGameButton.setFont(QFont('Arial', 20))
        self.DeleteGameButton.clicked.connect(self.DeleteGameButton_clicked) 
        self.DeleteGameButton.setFixedSize(buttonSizeH, buttonSizeV)
        deleteGame_button_layout.addWidget(self.DeleteGameButton)

        self.GetBackButton3 = QPushButton('Назад')
        self.GetBackButton3.setFont(QFont('Arial', 20))
        self.GetBackButton3.clicked.connect(self.fromDeleteGame_ToMainWindow) 
        self.GetBackButton3.setFixedSize(buttonSizeH, buttonSizeV)
        deleteGame_button_layout.addWidget(self.GetBackButton3)

        self.layout.addLayout(deleteGame_button_layout)

        self.deleteGameListObjs.append(self.delete_game_title)
        self.deleteGameListObjs.append(self.deleteGameslistWidget)
        self.deleteGameListObjs.append(self.DeleteGameButton)
        self.deleteGameListObjs.append(self.GetBackButton3)

    def getURLImage(self, imageURL):
        self.data = urllib.request.urlopen(imageURL).read()
        return self.data
    def lookGameWidgets(self):
        self.lookgameWidgets = []
        self.lookGame_image_label = QLabel(self)
        self.LookGame_pixmap = QPixmap(u'static\img\gameStandartIcon.png')
        self.lookGame_image_label.setPixmap(self.LookGame_pixmap.scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio))

        self.lookGame_gameName = QLabel('Название игры')
        self.lookGame_gameName.setFont(QFont('Arial', 25))
        self.lookGame_gameName.setFixedHeight(35)

        self.lookGame_gamePlatform = QLabel('ПК')
        self.lookGame_gamePlatform.setFont(QFont('Arial', 20))
        self.lookGame_gamePlatform.setFixedHeight(25)

        self.lookGame_gameInfo = QLabel('Grand Theft Auto V — компьютерная игра в жанре action-adventure с открытым миром, разработанная компанией Rockstar North и изданная компанией Rockstar Games.')
        self.lookGame_gameInfo.setFont(QFont('Arial', 15))
        self.lookGame_gameInfo.setFixedHeight(75)
        self.lookGame_gameInfo.setWordWrap(True)


        self.lookGame_gameIsPassed = QLabel('Игра пройдена')
        self.lookGame_gameIsPassed.setFont(QFont('Arial', 15))
        self.lookGame_gameIsPassed.setFixedHeight(35)

        self.SteamGameLink = 'Google.com'

        self.lookGame_gameLink = QLabel(f"Нет ссылки")
        self.lookGame_gameLink.setFont(QFont('Arial', 15))
        self.lookGame_gameLink.setFixedHeight(35)
        self.lookGame_gameLink.setOpenExternalLinks(True)

        self.lookGame_gamePrice = QLabel('Цена игры - 10$')
        self.lookGame_gamePrice.setFont(QFont('Arial', 15))
        self.lookGame_gamePrice.setFixedHeight(35)

        self.lookGame_gameAge = QLabel('Возрастной рейтинг - 18')
        self.lookGame_gameAge.setFont(QFont('Arial', 15))
        self.lookGame_gameAge.setFixedHeight(35)


        self.layout.addWidget(self.lookGame_image_label)
        self.layout.addWidget(self.lookGame_gameName)
        self.layout.addWidget(self.lookGame_gamePlatform)
        self.layout.addWidget(self.lookGame_gameInfo)
        self.layout.addWidget(self.lookGame_gameIsPassed)
        self.layout.addWidget(self.lookGame_gameLink)
        self.layout.addWidget(self.lookGame_gamePrice)
        self.layout.addWidget(self.lookGame_gameAge)

        lookGame_button_layout = QHBoxLayout()
        lookGame_button_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        buttonSizeH = int(200)
        buttonSizeV = int(100)

        self.GetBackButton4 = QPushButton('Назад')
        self.GetBackButton4.setFont(QFont('Arial', 20))
        self.GetBackButton4.clicked.connect(self.fromLookGameWidgets_toLookGameWindow) 
        self.GetBackButton4.setFixedSize(buttonSizeH, buttonSizeV)
        lookGame_button_layout.addWidget(self.GetBackButton4)

        self.layout.addLayout(lookGame_button_layout)
        
        self.lookgameWidgets.append(self.lookGame_image_label)
        self.lookgameWidgets.append(self.lookGame_gameName)
        self.lookgameWidgets.append(self.lookGame_gameInfo)
        self.lookgameWidgets.append(self.lookGame_gamePlatform)
        self.lookgameWidgets.append(self.lookGame_gameIsPassed)
        self.lookgameWidgets.append(self.GetBackButton4)
        self.lookgameWidgets.append(self.lookGame_gameLink)
        self.lookgameWidgets.append(self.lookGame_gamePrice)
        self.lookgameWidgets.append(self.lookGame_gameAge)


    def AddGameButtonWindow_clicked(self):
        try: self.AddGameButton.clicked.disconnect(self.AddGameButton_clicked)
        except Exception: pass
        try: self.AddGameButton.clicked.disconnect(self.editGameApply_clicked)
        except Exception: pass
        self.AddGameButton.clicked.connect(self.AddGameButton_clicked)
        self.add_game_title.setText('Добавление новой игры')
        self.AddGameButton.setText('Добавить игру')
        self.gameNameInputForm.setText('')
        self.gameInfoInputForm.setText('')
        self.gamePlatformInputForm.setText('')
        self.gameIsPassedInputForm.setChecked(False)
        for widget in self.mainWindowWidgets:
            widget.hide()
        for widget in self.addGameWidgets:
            widget.show()
        print('Opened AddGame Window')

    def EditGameButtonWindow_clicked(self):
        for widget in self.mainWindowWidgets:
            widget.hide()
        for widget in self.editGameListObjs:
            widget.show()
        self.updateEditGameList()

    def LookGameButtonWindow_clicked(self):
        for widget in self.mainWindowWidgets:
            widget.hide()
        for widget in self.lookGameListObjs:
            widget.show()
        self.updateLookGameList()

    def DeleteGameButtonWindow_clicked(self):
        for widget in self.mainWindowWidgets:
            widget.hide()
        for widget in self.deleteGameListObjs:
            widget.show()
        self.updateDeleteGameList()

    def updateEditGameList(self):
        self.EditlistWidget.clear()
        gameNames_list = self.gamebase.getAllGamesName()
        for game in gameNames_list:
            QListWidgetItem(game, self.EditlistWidget)

    def updateLookGameList(self):
        self.listWidget.clear()
        gameNames_list = self.gamebase.getAllGamesName()
        for game in gameNames_list:
            QListWidgetItem(game, self.listWidget)

    def updateDeleteGameList(self):
        self.deleteGameslistWidget.clear()
        gameNames_list = self.gamebase.getAllGamesName()
        for game in gameNames_list:
            QListWidgetItem(game, self.deleteGameslistWidget)



    def getFromAddGame_ToMainWindow(self):
        for widget in self.addGameWidgets:
            widget.hide()
        for widget in self.mainWindowWidgets:
            widget.show() # из добавления игры на главный экран
    
    def fromLookGame_ToMainWindow(self):
        for widget in self.lookGameListObjs:
            widget.hide()
        for widget in self.mainWindowWidgets:
            widget.show() # из просмотра игры на главный экран

    def fromeditGame_ToMainWindow(self):
        for widget in self.editGameListObjs:
            widget.hide()
        for widget in self.mainWindowWidgets:
            widget.show() # из изменения игры на главный экран

    def fromDeleteGame_ToMainWindow(self):
        for widget in self.deleteGameListObjs:
            widget.hide()
        for widget in self.mainWindowWidgets:
            widget.show() # из удаления игры на главный экран


    def AddGameButton_clicked(self):
        if(self.gameNameInputForm.text() == ''):
            self.showErrorMessage('Не введено название игры!')
            print('no game name')
            return
            
        gameNameText = self.gameNameInputForm.text()
        gameInfoText = self.gameInfoInputForm.text()
        gamePlatformText = self.gamePlatformInputForm.text()
        if(self.gameIsPassedInputForm.isChecked()):
            gameIsPassedInfo = "Да"
        else:
            gameIsPassedInfo = "Нет"
        if(self.gamebase.FindGame(gameNameText) == []):
            self.gamebase.createNewGame(gameNameText,gameInfoText,gamePlatformText,gameIsPassedInfo)
            print('GameAdded')
            self.gameNameInputForm.clear()
            self.gameInfoInputForm.clear()
            self.gamePlatformInputForm.clear()
            self.getFromAddGame_ToMainWindow() # добавить игру
        else:
            self.showErrorMessage('Данная игра уже существует!')

    def fromLookGameWidgets_toLookGameWindow(self):
        for widget in self.lookGameListObjs:
            widget.show()
        for widget in self.lookgameWidgets:
            widget.hide()

    def LookGameButton_clicked(self):
        try: selectedGameName = self.listWidget.currentItem().text()
        except Exception:
            self.showErrorMessage('Не выбрана игра!')
            return
        SQL_gameObject = self.gamebase.FindGame(selectedGameName)
        self.lookGame_gameName.setText(selectedGameName)
        self.lookGame_gameInfo.setText(SQL_gameObject[0][2])
        self.lookGame_gamePlatform.setText('Игра доступна на : ' + SQL_gameObject[0][3])
        self.lookGame_gameIsPassed.setText('Игра пройдена: ' + SQL_gameObject[0][4])
        try:
            self.SteamGameLink = self.steamApi.FindGameLink(selectedGameName)
            self.lookGame_gameLink.setText(f"<a style='color:black;' href='{self.SteamGameLink}' target='_blank'>Ссылка на страницу в Steam</a>")
        except Exception:
            self.lookGame_gameLink.setText('Ссылка на игру не найдена')
        try:
            self.SteamGamePrice = self.steamApi.FindGamePrice(selectedGameName)
            self.lookGame_gamePrice.setText('Цена игры : ' + self.SteamGamePrice)
        except Exception:
            self.lookGame_gamePrice.setText('Цена на игру не найдена')
        try:
            self.SteamGameAge = self.steamApi.FindGameAge(selectedGameName)
            self.lookGame_gameAge.setText('Возрастной рейтинг : ' + self.SteamGameAge + "+")
        except Exception:
            self.lookGame_gameAge.setText('Возрастной рейтинг не найден')
        try:
            self.SteamImageURL = self.steamApi.FindGameImage(selectedGameName)
            self.LookGame_pixmap.loadFromData(self.getURLImage(self.SteamImageURL))
            self.lookGame_image_label.setPixmap(self.LookGame_pixmap.scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio))
            print(self.SteamImageURL)
        except Exception:
            self.LookGame_pixmap = QPixmap('static\img\gameStandartIcon.png')
            self.lookGame_image_label.setPixmap(self.LookGame_pixmap.scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio))
            pass
        for widget in self.lookGameListObjs:
            widget.hide()
        for widget in self.lookgameWidgets:
            widget.show()
        print('Look selected game')

    def EditGameButton_clicked(self):
        try: self.GameNameForEdit = self.EditlistWidget.currentItem().text()
        except Exception:
            self.showErrorMessage('Не выбрана игра!')
            return
        SQL_gameObject = self.gamebase.FindGame(self.GameNameForEdit)
        try: self.AddGameButton.clicked.disconnect(self.AddGameButton_clicked)
        except Exception : pass
        try: self.AddGameButton.clicked.disconnect(self.editGameApply_clicked)
        except Exception: pass
        self.AddGameButton.clicked.connect(self.editGameApply_clicked) 
        self.add_game_title.setText('Изменение данных игры')
        self.AddGameButton.setText('Изменить игру')
        self.gameNameInputForm.setText(self.GameNameForEdit)
        self.gameInfoInputForm.setText(SQL_gameObject[0][2])
        self.gamePlatformInputForm.setText(SQL_gameObject[0][3])
        if(SQL_gameObject[0][4] == 'Да'):
            self.gameIsPassedInputForm.setChecked(True)
        else:
            self.gameIsPassedInputForm.setChecked(False)
        
        for widget in self.addGameWidgets:
            widget.show()
        for widget in self.editGameListObjs:
            widget.hide()

        print('Edit selected game')

    def editGameApply_clicked(self):
        newGameName = self.gameNameInputForm.text()
        newGameInfo = self.gameInfoInputForm.text()
        newGamePlatfrom = self.gamePlatformInputForm.text()
        if(self.gameIsPassedInputForm.isChecked()):
            print('yes')
            newGameIsPassed = 'Да'
        else:
            print('no')
            newGameIsPassed = 'Нет'
        self.gamebase.editGame(self.GameNameForEdit,newGameName,newGameInfo,newGamePlatfrom,newGameIsPassed)
        self.getFromAddGame_ToMainWindow()

    def DeleteGameButton_clicked(self):
        try: selectedGameName = self.deleteGameslistWidget.currentItem().text()
        except Exception:
            self.showErrorMessage('Не выбрана игра!')
            return
        self.gamebase.deleteGame(selectedGameName)
        self.updateDeleteGameList()
        print('Delete selected game')

    def showErrorMessage(self,errorText):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText("Ошибка!")
            msg.setInformativeText(errorText)
            msg.setWindowTitle("Ошибка!")
            msg.exec()





    def update_image(self, image_path):
        # Загрузка и отображение изображения
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap.scaled(500, 500, Qt.AspectRatioMode.KeepAspectRatio))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())