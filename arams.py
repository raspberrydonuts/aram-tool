import  requests, time, json

def process_champion_data():
    all_champion_data_response = requests.get("http://ddragon.leagueoflegends.com/cdn/11.2.1/data/en_US/champion.json").json()
    champion_table = dict()
    for champion in all_champion_data_response['data']:
        # print(all_champion_data_response['data'][champion])
        champion_name = all_champion_data_response['data'][champion]['id']
        champion_key =  all_champion_data_response['data'][champion]['key']
        champion_table[champion_key] = champion_name
    return champion_table

def main():

    data = {}

    # to run virtual environment: source aram_tool/bin/activate 
    # key = "RGAPI-fcd52462-de11-44de-b8a5-985913607996"
    get_account_url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/Wrangler%20Jeans?api_key=RGAPI-ab827109-ce88-453a-b23c-e26e89a081b0"
    get_account_response = requests.get(get_account_url)
    if get_account_response.status_code != 200:
        print("Get account failed. Status code: ", get_account_response.status_code)
        return
    account_id = get_account_response.json()['accountId']

    beginIndex = 100
    get_matches_url = f"https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/{account_id}?beginIndex={beginIndex}&api_key=RGAPI-ab827109-ce88-453a-b23c-e26e89a081b0"
    get_matches_response = requests.get(get_matches_url)
    num_games = 0
    champion_table = process_champion_data()
    print(get_matches_response.status_code)
    while get_matches_response.status_code == 200:
        # for every game in games played
        for match in get_matches_response.json()['matches']:
            game_id = match['gameId']
            print(num_games)
            get_game_url = f"https://na1.api.riotgames.com/lol/match/v4/matches/{game_id}?api_key=RGAPI-ab827109-ce88-453a-b23c-e26e89a081b0"
            get_game_response = requests.get(get_game_url).json()

            # if the game is ARAM
            if 'gameMode' in get_game_response and get_game_response['gameMode'] == "ARAM":
                participant_id = 0
                num_games += 1
                for participant in get_game_response['participantIdentities']:
                    if account_id == participant['player']['accountId']:
                        participant_id = participant['participantId']
                        break
                if participant_id != 0:
                    for participant in get_game_response['participants']:
                        if participant['participantId'] == participant_id:
                            champion_id = str(participant['championId'])
                            champion_name = champion_table[champion_id]

                            if champion_name not in data:
                                data[champion_name] = {}
                                champion_details = data[champion_name]
                                champion_details["games_played"] = 0 
                                champion_details["wins"] = 0
                                champion_details["losses"] = 0
                                champion_details["total_kills"] = 0 
                                champion_details["most_kills"] = 0 
                                champion_details["total_deaths"] = 0 
                                champion_details["most_deaths"] = 0 
                                champion_details["total_assists"] = 0 
                                champion_details["most_assists"] = 0 
                                champion_details["total_damage_dealt"] = 0 
                                champion_details["most_damage_dealt"] = 0 
                                champion_details["total_double_kills"] = 0 
                                champion_details["most_double_kills"] = 0 
                                champion_details["total_triple_kills"] = 0 
                                champion_details["most_triple_kills"] = 0 
                                champion_details["total_quadra_kills"] = 0 
                                champion_details["most_quadra_kills"] = 0 
                                champion_details["total_penta_kills"] = 0 
                                champion_details["most_penta_kills"] = 0 
                                champion_details["total_unreal_kills"] = 0 
                                champion_details["most_unreal_kills"] = 0 
                                champion_details["total_minions_killed"] = 0 
                                champion_details["most_minions_killed"] = 0 
                            champion_details = data[champion_name]

                            champion_details["games_played"] += 1
                            game_result = participant['stats']['win']
                            
                            if game_result:
                                champion_details["wins"] += 1 
                            else: 
                                champion_details["losses"]  += 1

                            kills = participant['stats']['kills']
                            champion_details["total_kills"] += kills
                            champion_details["most_kills"] = max(kills, champion_details["most_kills"])

                            deaths = participant['stats']['deaths']
                            champion_details["total_deaths"] += deaths
                            champion_details["most_deaths"] = max(deaths, champion_details["most_deaths"])

                            assists = participant['stats']['assists']
                            champion_details["total_assists"] += assists
                            champion_details["most_assists"] = max(assists, champion_details["most_assists"])

                            total_damage_dealt = participant['stats']['totalDamageDealt']
                            champion_details["total_damage_dealt"] += total_damage_dealt
                            champion_details["most_damage_dealt"] = max(total_damage_dealt, champion_details["most_damage_dealt"])
                            
                            double_kills = participant['stats']['doubleKills']
                            champion_details["total_double_kills"] += double_kills
                            champion_details["most_double_kills"] = max(double_kills, champion_details["most_double_kills"])

                            triple_kills = participant['stats']['tripleKills']
                            champion_details["total_triple_kills"] += triple_kills
                            champion_details["most_triple_kills"] = max(triple_kills, champion_details["most_triple_kills"])

                            quadra_kills = participant['stats']['quadraKills']
                            champion_details["total_quadra_kills"] += quadra_kills
                            champion_details["most_quadra_kills"] = max(quadra_kills, champion_details["total_quadra_kills"])

                            penta_kills = participant['stats']['pentaKills']
                            champion_details["total_penta_kills"] += penta_kills
                            champion_details["most_penta_kills"] = max(penta_kills, champion_details["most_penta_kills"])

                            unreal_kills = participant['stats']['unrealKills']
                            champion_details["total_unreal_kills"] += unreal_kills
                            champion_details["most_unreal_kills"] = max(unreal_kills, champion_details["most_unreal_kills"])

                            total_minions_killed = participant['stats']['totalMinionsKilled']
                            champion_details["total_minions_killed"] += total_minions_killed
                            champion_details["most_total_minions_killed"] = max(total_minions_killed, champion_details["most_minions_killed"])
                            break
        beginIndex += 100
        if len(get_matches_response.json()['matches']) < 100:
            break
        time.sleep(120)
        get_matches_url = f"https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/{account_id}?beginIndex={beginIndex}&api_key=RGAPI-ab827109-ce88-453a-b23c-e26e89a081b0"
        get_matches_response = requests.get(get_matches_url)
        print(get_matches_response.status_code)

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    


if __name__ == "__main__":
    main()
