import json

def main():
    with open('data.json') as f:
        data = json.load(f)
    
    num_games_played = 0
    wins = 0
    losses = 0
    w_l_ratio = 0
    best_w_l_ratio = ["", 0]
    worst_w_l_ratio = ["", 1]
    most_played = ["", 0]
    most_kills_total = ["", 0]
    most_kills_in_a_game = ["", 0]
    most_deaths_total = ["", 0]
    most_deaths_in_a_game = ["", 0]
    best_kda = ["", 0]
    worst_kda = ["", 0]
    most_double_kills = ["", 0]
    most_double_kills_in_a_game = ["", 0]
    most_triple_kills = ["", 0]
    most_triple_kills_in_a_game = ["", 0]
    most_quadra_kills = ["", 0]
    most_quadra_kills_in_a_game = ["", 0]
    most_penta_kills = ["", 0]
    most_penta_kills_in_a_game = ["", 0]

    for champion in data:
        champ_data = data[champion]
        num_games_played += champ_data['games_played']
        wins += champ_data['wins']
        losses += champ_data['losses']
        ratio = champ_data['wins'] / max(1, champ_data['losses'])
        if ratio > best_w_l_ratio[1]:
            best_w_l_ratio = [champion, ratio]
        if ratio < worst_w_l_ratio[1]:
            worst_w_l_ratio = [champion, ratio]
        if champ_data['games_played'] > most_played[1]:
            most_played = [champion, champ_data['games_played']]
        if champ_data['total_kills'] > most_kills_total[1]:
            most_kills_total = [champion, champ_data['total_kills']]
        if champ_data['most_kills'] > most_kills_in_a_game[1]:
            most_kills_in_a_game = [champion, champ_data['most_kills']]
        if champ_data['total_deaths'] > most_deaths_total[1]:
            most_deaths_total = [champion, champ_data['total_deaths']]
        if champ_data['most_deaths'] > most_deaths_in_a_game[1]:
            most_deaths_in_a_game = [champion, champ_data['most_deaths']]
        kda = (champ_data['total_kills'] + champ_data['total_assists']) / champ_data['total_deaths']
        if kda > best_kda[1]:
            best_kda = [champion, kda]
        if kda < worst_kda[1]:
            worst_kda = [champion, kda]
        if champ_data['total_double_kills'] > most_double_kills[1]:
            most_double_kills = [champion, champ_data['total_double_kills']]
        if champ_data['most_double_kills'] > most_double_kills_in_a_game[1]:
            most_double_kills_in_a_game = [champion, champ_data['most_double_kills']]
        if champ_data['total_triple_kills'] > most_triple_kills[1]:
            most_triple_kills = [champion, champ_data['total_triple_kills']]
        if champ_data['most_triple_kills'] > most_triple_kills_in_a_game[1]:
            most_triple_kills_in_a_game = [champion, champ_data['most_triple_kills']]
        if champ_data['total_quadra_kills'] > most_quadra_kills[1]:
            most_quadra_kills = [champion, champ_data['total_quadra_kills']]
        if champ_data['most_quadra_kills'] > most_quadra_kills_in_a_game[1]:
            most_quadra_kills_in_a_game = [champion, champ_data['most_quadra_kills']]
        if champ_data['total_penta_kills'] > most_penta_kills[1]:
            most_penta_kills = [champion, champ_data['total_penta_kills']]
        if champ_data['most_penta_kills'] > most_penta_kills_in_a_game[1]:
            most_penta_kills_in_a_game = [champion, champ_data['most_penta_kills']]
    
    w_l_ratio = wins/losses
    print("num_games_played: ", num_games_played)
    print("wins: ", wins)
    print("losses: ", losses)
    print("w_l_ratio: ", w_l_ratio)
    print("best_w_l_ratio: ", best_w_l_ratio)
    print("worst_w_l_ratio: ", worst_w_l_ratio)
    print("most_played: ", most_played)
    print("most_kills_total: ", most_kills_total)
    print("most_kills_in_a_game: ", most_kills_in_a_game)
    print("most_deaths_total: ", most_deaths_total)
    print("most_deaths_in_a_game: ", most_deaths_in_a_game)
    print("best_kda: ", best_kda)
    print("worst_kda: ", worst_kda)
    print("most_double_kills: ", most_double_kills)
    print("most_double_kills_in_a_game: ", most_double_kills_in_a_game)
    print("most_triple_kills: ", most_triple_kills)
    print("most_triple_kills_in_a_game: ", most_triple_kills_in_a_game)
    print("most_quadra_kills: ", most_quadra_kills)
    print("most_quadra_kills_in_a_game: ", most_quadra_kills_in_a_game)
    print("most_penta_kills: ", most_penta_kills)
    print("most_penta_kills_in_a_game: ", most_penta_kills_in_a_game)


if __name__ == "__main__":
    main()