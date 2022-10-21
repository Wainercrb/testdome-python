'''
The LeagueTable class tracks the score of each player in a league. After each game, the player records their score with the record_result function. 

The player's rank in the league is calculated using the following logic:

    1. The player with the highest score is ranked first (rank 1). The player with the lowest score is ranked last.
    2. If two players are tied on score, then the player who has played the fewest games is ranked higher.
    3. If two players are tied on score and number of games played, then the player who was first in the list of players is ranked higher.

Implement the player_rank function that returns the player at the given rank.

For example:

    table = LeagueTable(['Mike', 'Chris', 'Arnold'])
    table.record_result('Mike', 2)
    table.record_result('Mike', 3)
    table.record_result('Arnold', 5)
    table.record_result('Chris', 5)
    print(table.player_rank(1))

All players have the same score. However, Arnold and Chris have played fewer games than Mike, and as Chris is before Arnold in the list of players, he is ranked first. Therefore, the code above should display "Chris".

--------------|------------------

Difficulty: Hard
Duration: 20 min

Python 3.7.4, Base Test:

from collections import Counter
from collections import OrderedDict

class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])
       
    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score
      
    def player_rank(self, rank):
        return None

if __name__ == "__main__":
    table = LeagueTable(['Mike', 'Chris', 'Arnold'])
    table.record_result('Mike', 2)
    table.record_result('Mike', 3)
    table.record_result('Arnold', 5)
    table.record_result('Chris', 5)
    print(table.player_rank(1))
'''


from collections import Counter
from collections import OrderedDict

class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])
       
    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score

    def player_rank(self, rank):
        map_items = []
        for p in self.standings:
            map_items.append({
                'player': p,
                'score': self.standings[p]['score'],
                'games_played': self.standings[p]['games_played']
            })

        sorted_by_score = sorted(map_items, key=lambda i: i['score'])
        current_player = sorted_by_score[0]
        filter_by_score = list(i for i in sorted_by_score if i['score'] == current_player['score'])

        if len(filter_by_score) == 1:
            return current_player['player']

        sorted_by_play_times = sorted(map_items, key=lambda i: i['games_played'])
        current_player = sorted_by_play_times[0]
        filter_by_games_played = list(i for i in sorted_by_play_times if i['games_played'] == current_player['games_played'])
        sorted_by_name = sorted(filter_by_games_played, key=lambda i: i['player'], reverse=True)

        result = []
        if rank <= 1:
            return sorted_by_name[0]['player']
        else:
            for i in range(rank):
                result.append(sorted_by_name[i]['player']) 
        return result

if __name__ == "__main__":
    table = LeagueTable(['Mike', 'Chris', 'Arnold'])
    table.record_result('Mike', 2)
    table.record_result('Mike', 3)
    table.record_result('Arnold', 5)
    table.record_result('Chris', 5)
    print(table.player_rank(2))