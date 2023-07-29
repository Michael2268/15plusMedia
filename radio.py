# 15+ Media Group - Radio Station Checker
# Coding by Michael Hatsov (https://vk.com/mihacker7x)
# All radio streams belongs to 15+ Media Group and their official founders.

import time, vlc, colorama, getpass
colorama.init(autoreset=True)

def streamplay(url):
    Instance = vlc.Instance()
    player = Instance.media_player_new()
    Media = Instance.media_new(url)
    Media.get_mrl()
    player.set_media(Media)
    player.play()
    time.sleep(1)
    value = player.is_playing()
    wait = 0
    while value == 0:
        wait = wait + 1
        print("Buffering...")
        value = player.is_playing()
        time.sleep(1)
        if wait == 10:
            value == 2
            break
    if value == 1:
        print("\n" + colorama.Back.BLUE + "Station:", Media.get_meta(0))
        print(colorama.Back.BLUE + "Now playing:", Media.get_meta(12))
        time.sleep(10)
        print(colorama.Back.GREEN + "Pass")
        player.stop()
    else:
        print(colorama.Back.RED + "Stream open error! Skipping...")
        player.stop()
        pass
    global res
    res = res + value
res = 0

links = {
    1: {"name": "RadioHeart / Radio Afrodita",
        "link": "http://s0.radioheart.ru:8000/RadioAfrodita"},
    2: {"name": "RadioHeart / Radio Afrodita (+2)",
        "link": "http://s0.radioheart.ru:8000/RadioAfrodita_h2"},
    3: {"name": "RadioHeart / Radio Afrodita (+4)",
        "link": "http://s0.radioheart.ru:8000/RadioAfrodita_h4"},
    4: {"name": "Radio 61 region",
        "link": "http://stream.zeno.fm/mavesrntf48uv"},
    5: {"name": "L2MR / Radio Afrodita Ural (Ekaterinburg)",
        "link": "http://freeuk27.listen2myradio.com:3408/stream"},
    6: {"name": "MR24 / Radio Afrodita Sibir (Krasnoyarsk)",
        "link": "http://listen5.myradio24.com:9000/36860"},
    7: {"name": "nMR24 / Seawave",
        "link": "https://listen7.myradio24.com/39338"},
    8: {"name": "MR24 / Seawave (Kemerovo)",
        "link": "https://listen7.myradio24.com/25527"},
    9: {"name": "Zeno Radio / Seawave (Barnaul)",
        "link": "https://stream.zeno.fm/3qe9vvf78ehvv"},
    10:{"name": "MR24 / Seawave (Barnaul)",
        "link": "http://listen3.myradio24.com:9000/73076"}, 
    11:{"name": "RadioHeart / 15+ Music Radio",
        "link": "http://s0.radioheart.ru:8000/15plusMR"},
    12:{"name": "RadioHeart / Cringe FM",
        "link": "http://s0.radioheart.ru:8000/CringeFM"},
    13:{"name": "RadioHeart / FLEX FM",
        "link": "http://s0.radioheart.ru:8000/flexfm"},
    14:{"name": "RadioHeart / Radio FLEX FM (Moscow)",
       "link": "http://s0.radioheart.ru:8000/FLEXFM_MSK"},
    15:{"name": "MR24 / Radio M (Krasnoyarsk)",
        "link": "http://listen7.myradio24.com:9000/56149"},
    16:{"name": "Zeno Radio / Radio FLEX FM Meme",
        "link": "http://stream.zeno.fm/xwsnvbq7t18uv"},
    17:{"name": "Zeno Radio / Radio FLEX FM Meme 64kbps",
        "link": "http://stream.zeno.fm/yfepheq7t18uv"},
    18:{"name": "Zeno Radio / Radio FLEX FM Gachi",
        "link": "https://stream-149.zeno.fm/zumem6ap2uhvv"},
    19:{"name": "Zeno Radio / Radio FLEX FM Gachi 64kbps",
        "link": "https://stream-150.zeno.fm/6x0n08ap2uhvv"}
}

for i in range (1,20):
    print("\n" + colorama.Back.WHITE + colorama.Fore.BLACK + links[i]["name"])
    streamplay(links[i]["link"])


if res == 19:
    print(colorama.Fore.GREEN + "\nAll servers and stations working correctly.\nPress Enter to exit.")
    getpass.getpass("")
else:
    print(colorama.Fore.RED + "\nSome radio streams aren't working. Perhaps this is due to:\n\n1. Your Internet connection is unstable.\n2. Some radio services are not working or experiencing technical difficulties.\n3. Station(s) has been turned off.\n\nPress Enter to exit.")
    getpass.getpass("")