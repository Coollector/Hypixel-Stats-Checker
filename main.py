import requests
import keyboard
from win10toast import ToastNotifier

notifier = ToastNotifier()
hypixel_api_key = "YOUR HYPIXEL API KEY HERE"


log = []




def refresh_log():
    with open(r"C:\Users\Felix\.lunarclient\offline\multiver\logs\latest.log") as f:
        for i in f.readlines():
            log.append(i)


def notification(header, body, time:int=20):
    notifier.show_toast(
            header,
            body,
            duration = time,
            threaded = True,
        )



def get_division(wins):
    if wins == 'NICKED':
        return
    wins = int(wins)
    if wins < 50:
        division = "None"
    if wins >= 50:
        division = "Rookie"
    if wins >= 60:
        division = "Rookie II"
    if wins >= 70:
        division = "Rookie III"
    if wins >= 80:
        division = "Rookie IV"
    if wins >= 90:
        division = "Rookie V"
    if wins >= 100:
        division = "Iron"
    if wins >= 130:
        division = "Iron II"
    if wins >= 160:
        division = "Iron III"
    if wins >= 190:
        division = "Iron IV"
    if wins >= 220:
        division = "Iron V"
    if wins >= 250:
        division = "Gold"
    if wins >= 300:
        division = "Gold II"
    if wins >= 350:
        division = "Gold III"
    if wins >= 400:
        division = "Gold IV"
    if wins >= 450:
        division = "Gold V"
    if wins >= 500:
        division = "Diamond"
    if wins >= 600:
        division = "Diamond II"
    if wins >= 700:
        division = "Diamond III"
    if wins >= 800:
        division = "Diamond IV"
    if wins >= 900:
        division = "Diamond V"
    if wins >= 1000:
        division = "Master"
    if wins >= 1200:
        division = "Master II"
    if wins >= 1400:
        division = "Master III"
    if wins >= 1600:
        division = "Master IV"
    if wins >= 1800:
        division = "Master V"
    if wins >= 2000:
        division = "Legend"
    if wins >= 2600:
        division = "Legend II"
    if wins >= 3200:
        division = "Legend III"
    if wins >= 3800:
        division = "Legend IV"
    if wins >= 4400:
        division = "Legend V"
    if wins >= 5000:
        division = "Grandmaster"
    if wins >= 6000:
        division = "Grandmaster II"
    if wins >= 7000:
        division = "Grandmaster III"
    if wins >= 8000:
        division = "Grandmaster IV"
    if wins >= 9000:
        division = "Grandmaster V"
    if wins >= 10000:
        division = "Godlike"
    if wins >= 13000:
        division = "Godlike II"
    if wins >= 16000:
        division = "Godlike III"
    if wins >= 19000:
        division = "Godlike IV"
    if wins >= 22000:
        division = "Godlike V"
    if wins >= 25000:
        division = "Celestial"
    if wins >= 30000:
        division = "Celestial II"
    if wins >= 35000:
        division = "Celestial III"
    if wins >= 40000:
        division = "Celestial IV"
    if wins >= 45000:
        division = "Celestial V"
    if wins >= 50000:
        division = "Divine"
    if wins >= 60000:
        division = "Divine II"
    if wins >= 70000:
        division = "Divine III"
    if wins >= 80000:
        division = "Divine IV"
    if wins >= 90000:
        division = "Divine V"
    if wins >= 100000:
        division = "Ascended"
    return division


def game_to_number(game:str) -> int:
    if game == "BedWars":
        return 1
    elif game == "BridgeDuel":
        return 2
    elif game == "BridgeDoubles":
        return 3
    else:
        return 0


def current() -> list:
    refresh_log()
    searching = False
    log_size = len(log)
    for i in range(log_size-1, -1, -1):
        if "[Client thread/INFO]: [CHAT] The game starts in 1 second!" in log[i]:
            searching = True
            suche_fragezeichen = 0
            while searching:
                suche_fragezeichen += 1
                if "????????????????????????????????????????????????????????????????" in log[i + suche_fragezeichen]:
                    searching = False
            gamemode = str(log[i + suche_fragezeichen + 1])[39:].replace(" ", "")
            if "\\" in r"%r" % gamemode:
                lenght = len(gamemode) - 1
                gamemode = gamemode[:lenght]
            number = 0
            number = game_to_number(gamemode)
            index = i + suche_fragezeichen + 1
            result = [number, index]
            return result

            
def connector(result:list):
    game = int(result[0])
    row = int(result[1])
    if game == 0:
        notification("Error", "Something went wrong, please check the code", time=30)
    elif game == 1:
        bedwars(row)
    elif game == 2:
        bridge_duel(row)
    elif game == 3:
        bridge_doubles(row)
    else:
        notification("Error", "Something went wrong, please check the code", time=30)



def bridge_duel(row:int):
    print("bridge solo")
    opponent = str(log[row + 7])[39:].replace(" ", "").replace(":", "")[8:]
    if "\\" in r"%r" % opponent:
        lenght = len(opponent) - 1
        opponent = opponent[:lenght]
    if opponent.find("[") >= 0:
        in_klam = False
        z = ""
        for k in opponent:
            if k == "[":
                in_klam = True
            if k == "]":
                in_klam = False
            if not in_klam and k != "]":
                z = z + k
        opponent = z
    data = requests.get(
        url = "https://api.hypixel.net/player",
        params = {
            "key": hypixel_api_key,
            "name": opponent
        }
    ).json()
    try:
        wins = int(data["player"]["achievements"]["duels_bridge_wins"])
        notification(opponent, f"{wins}, {get_division(wins)}", 20)
    except:
        notification(opponent, f"NICKED", 20)


def bridge_doubles(row:int):
    print("bridge doubles")
    wins = []
    print(log[row+7])
    opponent_list = str(str(log[row + 7])[39:] + str(log[row + 8])[39:].replace(" ", "") if str(log[row + 8])[39:].replace(" ", "") != "" else "").replace(" ", "").replace(":", "")[9:].split(',')
    for i, opponent in enumerate(opponent_list):
        if "\\" in r"%r" % opponent:
            lenght = len(opponent) - 1
            opponent_list[i] = opponent[:lenght]
    print(opponent_list)
    for opponent in opponent_list:
        print(opponent)
        if opponent.find("[") >= 0:
            in_klam = False
            z = ""
            for k in opponent:
                if k == "[":
                    in_klam = True
                if k == "]":
                    in_klam = False
                if not in_klam and k != "]":
                    z = z + k
            opponent = z

        data = requests.get(
            url = "https://api.hypixel.net/player",
            params = {
                "key": hypixel_api_key,
                "name": opponent
            }
        ).json()
        try:
            wins.append(int(data["player"]["achievements"]["duels_bridge_wins"]))
        except:
            wins.append('NICKED')

    notification(f"{opponent_list[0]}, {opponent_list[1]}", f"{wins[0]}, {get_division(wins[0])}\n{wins[1]}, {get_division(wins[1])}", 20)
    

def bedwars(row:int):
    print("bedwars")
    opponents = []
    searching = False
    def find_start_search(row:int) -> int:
        searching = True
        suche_online = 0
        while searching:
            suche_online += 1
            if "[Client thread/INFO]: [CHAT] ONLINE:" in log[row - suche_online]:
                return row - suche_online
    online_row = find_start_search(row)
    opponents = str(log[online_row])[48:].replace(" ", "").split(',')
    for i in range(row - online_row):
        if "[Client thread/INFO]: [CHAT] " in log[online_row + i] and " has joined (" in log[online_row + i] and "/16)!" in log[online_row + i]:
            opponent_joined = str(log[online_row + i])[40:].split(' ')
            print(f"{opponent_joined} joined")
            opponents.append(opponent_joined[0])
        if "[Client thread/INFO]: [CHAT] " in log[online_row + i] and " has quit!" in log[online_row + i]:
            opponent_quit = str(log[online_row + i])[40:].split(' ')
            popper = 0
            print(f"{opponent_quit} quit")
            for i in opponents:
                if i == [opponent_quit[0]]:
                    opponents.pop(popper)
                popper += 1
    for i, opponent in enumerate(opponents):
        if "\\" in r"%r" % opponent:
            lenght = len(opponent) - 1
            opponents[i] = opponent[:lenght]
    print(opponents)
    wins = []
    for i in opponents:
        data = requests.get(
            url = "https://api.hypixel.net/player",
            params = {
                "key": hypixel_api_key,
                "name": i
            }
        ).json()
        try:
            wins.append(int(data["player"]["achievements"]["bedwars_level"]))
        except:
            wins.append(-1)
    def sort(wins_list, opponents_list):
        print('hier sollen die drei mit den höchsten stars rausgefiltert werden')
    body_list = []
    for i in range(len(opponents)):
        body_list.append(f"{opponents[i]}, {wins[i]}")
    body_string = '\n'.join([str(elem) for elem in body_list])
    notification('Bedwars levels', body_string, 30)




def start():
    connector(current())


keyboard.add_hotkey('ctrl+alt+v', start)
keyboard.wait()
