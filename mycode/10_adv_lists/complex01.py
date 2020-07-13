#!/user/bin/env python3

#creating list number 1
players = ["kohli", "dhoni", "agarwal", "vihari"]
print(players)
print(players[1])
scores = [39, 74, 52, 104]
print(scores)

players.extend(["yadav", "sharma"])
print(players)
players.append(scores)
print(players)
print(players[0] , " has scored", players[6][1], " runs")

