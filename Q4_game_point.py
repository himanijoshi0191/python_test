def game_point(point):
    team1_point_1 = 0
    team1_point_2 = 0



team1 = { "name": "Manchester United", "wins": 30, "loss": 3, "draws": 5, "scored": 88,
"conceded": 20 }
team2 = { "name": "FC Barcilona", "wins": 31, "loss": 3, "draws": 5, "scored": 88,
"conceded": 20 }
team3 = { "name": "Madrid", "wins": 35, "loss": 2, "draws": 5, "scored": 90,
"conceded": 25 }
teamList= [team1,team3,team2]
team_dict= {}


for team in teamList:
    team_name = team['name']
    wins = team['wins']
    loss = team['loss']
    draws = team['draws']

    total_points = 3 * wins + 0 * loss + 1 * draws
    team_dict[team_name] = total_points

team_dict =dict(sorted(team_dict.items(), key=lambda item: item[1]))
print(team_dict)
list = [(k, v) for k, v in team_dict.items()]
print(list[-1])
