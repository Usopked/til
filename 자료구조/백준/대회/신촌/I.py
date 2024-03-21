from collections import defaultdict
def team_value(K, players):
    grouped_players = defaultdict(list)
    for P, W in players:
        grouped_players[P].append(W)
    
    for P in grouped_players:
        grouped_players[P].sort(reverse=True)
    
    total_value = 0
    for _ in range(K):
        for P in grouped_players:
            if grouped_players[P]:
                total_value += grouped_players[P][0]
                grouped_players[P][0] -= 1 
                if grouped_players[P][0] <= 0:
                    grouped_players[P].pop(0)  
        for P in grouped_players:
            if grouped_players[P]:
                total_value += grouped_players[P][0]
                grouped_players[P][0] -= 1  
                if grouped_players[P][0] <= 0:
                    grouped_players[P].pop(0)  
    return total_value
def solve_fifa_problem():
    N, K = map(int, input().split())
    players = [tuple(map(int, input().split())) for _ in range(N)]
    
    return team_value(K, players)

print(solve_fifa_problem())
