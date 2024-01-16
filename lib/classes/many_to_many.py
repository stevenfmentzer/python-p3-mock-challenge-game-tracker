class Game:

    all = []
    def __init__(self, title):
        self.title = title
        self.__class__.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if isinstance(value, str) and len(value) > 0 and not hasattr(self, 'title'):
            self._title = value
        else: 
            raise Exception("Titles must be of type str/ Titles must be longer than 0 characters/ Should not be able to change after the game is instantiated")

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list(set([player for player in Result.all if player.game == self]))

    def average_score(self, player):
        if player and isinstance(player, Player):
            player_results  = [result.score for result in Result.all if result.player == self]
            if player_results: 
                return sum(player_results) / len(player_results)
            return 0

        
class Player:

    all = []
    def __init__(self, username):
    
            self.username = username
            self.__class__.all.append(self)

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2<= len(username) <= 16:                
            self._username = username
        else:     
            raise Exception("Username must be type 'string' and between 2-16 characters long")
        
    
    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return list(set([result.game for result in Result.all if result.player == self]))

    def played_game(self, game):
        return any(result.game == game for result in Result.all if result.player == self)

    def num_times_played(self, game):
        return sum(1 for result in Result.all if result.player == self and result.game == game)

class Result:

    all = [] 
    def __init__(self, player, game, score):
    
            self.player = player
            self.game = game
            self.score = score
            self.__class__.all.append(self)

    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        if player and isinstance(player, Player):
            self._player = player
        else: 
            raise TypeError

    @property 
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if game and isinstance(game, Game):
            self._game = game
        else: 
            raise TypeError
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if score and isinstance(score, int) and 0 < score < 5001: 
            self._score = score
        else: 
            raise Exception("wrong")