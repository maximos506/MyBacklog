import os
from steam_web_api import Steam

class SteamGameFinder():
    def __init__(self):
        KEY = os.environ.get("STEAM_API_KEY")
        self.steam = Steam(KEY)

    def getGameData(self,gameName):
        user = self.steam.apps.search_games(gameName)
        game = user.get('apps')
        game_id = game[0].get('id')[0]
        detailedGame = self.steam.apps.get_app_details(game_id)
        detailedGame_dict_id = detailedGame.get(str(game_id))
        detailedGame_dict_data = detailedGame_dict_id.get('data')
        print(detailedGame_dict_data)

    def getDetailedImageData(self,gameName):
        user = self.steam.apps.search_games(gameName)
        game = user.get('apps')
        game_id = game[0].get('id')[0]
        detailedGame = self.steam.apps.get_app_details(game_id)
        detailedGame_dict_id = detailedGame.get(str(game_id))
        detailedGame_dict_data = detailedGame_dict_id.get('data')
        detailedGame_image = detailedGame_dict_data.get('header_image')
        print(detailedGame_image)


    def FindGamePrice(self,gameName):
        user = self.steam.apps.search_games(gameName, "RU")
        game = user.get('apps')
        if(game[0] is not None):
            game_price = game[0].get('price')
            return game_price

    def FindGameLink(self,gameName):
        user = self.steam.apps.search_games(gameName)
        game = user.get('apps')
        if(game[0] is not None):
            game_link = game[0].get('link')
            return game_link

    def FindGameImage(self,gameName):
        user = self.steam.apps.search_games(gameName)
        game = user.get('apps')
        game_id = game[0].get('id')[0]
        detailedGame = self.steam.apps.get_app_details(game_id)
        detailedGame_dict_id = detailedGame.get(str(game_id))
        detailedGame_dict_data = detailedGame_dict_id.get('data')
        detailedGame_image = detailedGame_dict_data.get('header_image')
        return(detailedGame_image)

    def FindGameImageOld(self,gameName):
        user = self.steam.apps.search_games(gameName)
        game = user.get('apps')
        if(game[0] is not None):
            game_image = game[0].get('img')
            return game_image

    def FindGameAge(self,gameName):
        user = self.steam.apps.search_games(gameName, "RU")
        game = user.get('apps')
        game_id = game[0].get('id')[0]
        detailedGame = self.steam.apps.get_app_details(game_id)
        detailedGame_dict_id = detailedGame.get(str(game_id))
        detailedGame_dict_data = detailedGame_dict_id.get('data')
        detailedGame_age = detailedGame_dict_data.get('required_age')
        return(detailedGame_age)


steam = SteamGameFinder()
steam.FindGameAge('Hotline Miami')
#steam.getDetailedImageData('Grand Theft Auto 5')