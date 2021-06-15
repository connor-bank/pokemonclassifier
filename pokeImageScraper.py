# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 16:20:54 2020

@author: conno
"""

import re
import pandas as pd
import selenium
from selenium import webdriver
import time
import os
import requests
import io
import hashlib
import PIL

pokemon = 'Bulbasaur, Ivysaur, Venusaur, Charmander, Charmeleon, Charizard, Squirtle, Wartortle, Blastoise, Caterpie, Metapod, Butterfree, Weedle, Kakuna, Beedrill, Pidgey, Pidgeotto, Pidgeot, Rattata, Raticate, Spearow, Fearow, Ekans, Arbok, Pikachu, Raichu, Sandshrew, Sandslash, Nidoran, Nidorina, Nidoqueen, Nidorino, Nidoking, Clefairy, Clefable, Vulpix, Ninetales, Jigglypuff, Wigglytuff, Zubat, Golbat, Oddish, Gloom, Vileplume, Paras, Parasect, Venonat, Venomoth, Diglett, Dugtrio, Meowth, Persian, Psyduck, Golduck, Mankey, Primeape, Growlithe, Arcanine, Poliwag, Poliwhirl, Poliwrath, Abra, Kadabra, Alakazam, Machop, Machoke, Machamp, Bellsprout, Weepinbell, Victreebel, Tentacool, Tentacruel, Geodude, Graveler, Golem, Ponyta, Rapidash, Slowpoke, Slowbro, Magnemite, Magneton, Farfetch’d, Doduo, Dodrio, Seel, Dewgong, Grimer, Muk, Shellder, Cloyster, Gastly, Haunter, Gengar, Onix, Drowzee, Hypno, Krabby, Kingler, Voltorb, Electrode, Exeggcute, Exeggutor, Cubone, Marowak, Hitmonlee, Hitmonchan, Lickitung, Koffing, Weezing, Rhyhorn, Rhydon, Chansey, Tangela, Kangaskhan, Horsea, Seadra, Goldeen, Seaking, Staryu, Starmie, Mr. Mime, Scyther, Jynx, Electabuzz, Magmar, Pinsir, Tauros, Magikarp, Gyarados, Lapras, Ditto, Eevee, Vaporeon, Jolteon, Flareon, Porygon, Omanyte, Omastar, Kabuto, Kabutops, Aerodactyl, Snorlax, Articuno, Zapdos, Moltres, Dratini, Dragonair, Dragonite, Mewtwo, Mew'
#, Chikorita, Bayleef, Meganium, Cyndaquil, Quilava, Typhlosion, Totodile, Croconaw, Feraligatr, Sentret, Furret, Hoothoot, Noctowl, Ledyba, Ledian, Spinarak, Ariados, Crobat, Chinchou, Lanturn, Pichu, Cleffa, Igglybuff, Togepi, Togetic, Natu, Xatu, Mareep, Flaaffy, Ampharos, Bellossom, Marill, Azumarill, Sudowoodo, Politoed, Hoppip, Skiploom, Jumpluff, Aipom, Sunkern, Sunflora, Yanma, Wooper, Quagsire, Espeon, Umbreon, Murkrow, Slowking, Misdreavus, Unown, Wobbuffet, Girafarig, Pineco, Forretress, Dunsparce, Gligar, Steelix, Snubbull, Granbull, Qwilfish, Scizor, Shuckle, Heracross, Sneasel, Teddiursa, Ursaring, Slugma, Magcargo, Swinub, Piloswine, Corsola, Remoraid, Octillery, Delibird, Mantine, Skarmory, Houndour, Houndoom, Kingdra, Phanpy, Donphan, Porygon2, Stantler, Smeargle, Tyrogue, Hitmontop, Smoochum, Elekid, Magby, Miltank, Blissey, Raikou, Entei, Suicune, Larvitar, Pupitar, Tyranitar, Lugia, Ho-Oh, Celebi, Treecko, Grovyle, Sceptile, Torchic, Combusken, Blaziken, Mudkip, Marshtomp, Swampert, Poochyena, Mightyena, Zigzagoon, Linoone, Wurmple, Silcoon, Beautifly, Cascoon, Dustox, Lotad, Lombre, Ludicolo, Seedot, Nuzleaf, Shiftry, Taillow, Swellow, Wingull, Pelipper, Ralts, Kirlia, Gardevoir, Surskit, Masquerain, Shroomish, Breloom, Slakoth, Vigoroth, Slaking, Nincada, Ninjask, Shedinja, Whismur, Loudred, Exploud, Makuhita, Hariyama, Azurill, Nosepass, Skitty, Delcatty, Sableye, Mawile, Aron, Lairon, Aggron, Meditite, Medicham, Electrike, Manectric, Plusle, Minun, Volbeat, Illumise, Roselia, Gulpin, Swalot, Carvanha, Sharpedo, Wailmer, Wailord, Numel, Camerupt, Torkoal, Spoink, Grumpig, Spinda, Trapinch, Vibrava, Flygon, Cacnea, Cacturne, Swablu, Altaria, Zangoose, Seviper, Lunatone, Solrock, Barboach, Whiscash, Corphish, Crawdaunt, Baltoy, Claydol, Lileep, Cradily, Anorith, Armaldo, Feebas, Milotic, Castform, Kecleon, Shuppet, Banette, Duskull, Dusclops, Tropius, Chimecho, Absol, Wynaut, Snorunt, Glalie, Spheal, Sealeo, Walrein, Clamperl, Huntail, Gorebyss, Relicanth, Luvdisc, Bagon, Shelgon, Salamence, Beldum, Metang, Metagross, Regirock, Regice, Registeel, Latias, Latios, Kyogre, Groudon, Rayquaza, Jirachi, Deoxys, Turtwig, Grotle, Torterra, Chimchar, Monferno, Infernape, Piplup, Prinplup, Empoleon, Starly, Staravia, Staraptor, Bidoof, Bibarel, Kricketot, Kricketune, Shinx, Luxio, Luxray, Budew, Roserade, Cranidos, Rampardos, Shieldon, Bastiodon, Burmy, Wormadam, Mothim, Combee, Vespiquen, Pachirisu, Buizel, Floatzel, Cherubi, Cherrim, Shellos, Gastrodon, Ambipom, Drifloon, Drifblim, Buneary, Lopunny, Mismagius, Honchkrow, Glameow, Purugly, Chingling, Stunky, Skuntank, Bronzor, Bronzong, Bonsly, Mime Jr., Happiny, Chatot, Spiritomb, Gible, Gabite, Garchomp, Munchlax, Riolu, Lucario, Hippopotas, Hippowdon, Skorupi, Drapion, Croagunk, Toxicroak, Carnivine, Finneon, Lumineon, Mantyke, Snover, Abomasnow, Weavile, Magnezone, Lickilicky, Rhyperior, Tangrowth, Electivire, Magmortar, Togekiss, Yanmega, Leafeon, Glaceon, Gliscor, Mamoswine, Porygon-Z, Gallade, Probopass, Dusknoir, Froslass, Rotom, Uxie, Mesprit, Azelf, Dialga, Palkia, Heatran, Regigigas, Giratina, Cresselia, Phione, Manaphy, Darkrai, Shaymin, Arceus, Victini, Snivy, Servine, Serperior, Tepig, Pignite, Emboar, Oshawott, Dewott, Samurott, Patrat, Watchog, Lillipup, Herdier, Stoutland, Purrloin, Liepard, Pansage, Simisage, Pansear, Simisear, Panpour, Simipour, Munna, Musharna, Pidove, Tranquill, Unfezant, Blitzle, Zebstrika, Roggenrola, Boldore, Gigalith, Woobat, Swoobat, Drilbur, Excadrill, Audino, Timburr, Gurdurr, Conkeldurr, Tympole, Palpitoad, Seismitoad, Throh, Sawk, Sewaddle, Swadloon, Leavanny, Venipede, Whirlipede, Scolipede, Cottonee, Whimsicott, Petilil, Lilligant, Basculin, Sandile, Krokorok, Krookodile, Darumaka, Darmanitan, Maractus, Dwebble, Crustle, Scraggy, Scrafty, Sigilyph, Yamask, Cofagrigus, Tirtouga, Carracosta, Archen, Archeops, Trubbish, Garbodor, Zorua, Zoroark, Minccino, Cinccino, Gothita, Gothorita, Gothitelle, Solosis, Duosion, Reuniclus, Ducklett, Swanna, Vanillite, Vanillish, Vanilluxe, Deerling, Sawsbuck, Emolga, Karrablast, Escavalier, Foongus, Amoonguss, Frillish, Jellicent, Alomomola, Joltik, Galvantula, Ferroseed, Ferrothorn, Klink, Klang, Klinklang, Tynamo, Eelektrik, Eelektross, Elgyem, Beheeyem, Litwick, Lampent, Chandelure, Axew, Fraxure, Haxorus, Cubchoo, Beartic, Cryogonal, Shelmet, Accelgor, Stunfisk, Mienfoo, Mienshao, Druddigon, Golett, Golurk, Pawniard, Bisharp, Bouffalant, Rufflet, Braviary, Vullaby, Mandibuzz, Heatmor, Durant, Deino, Zweilous, Hydreigon, Larvesta, Volcarona, Cobalion, Terrakion, Virizion, Tornadus, Thundurus, Reshiram, Zekrom, Landorus, Kyurem, Keldeo, Meloetta, Genesect, Chespin, Quilladin, Chesnaught, Fennekin, Braixen, Delphox, Froakie, Frogadier, Greninja, Bunnelby, Diggersby, Fletchling, Fletchinder, Talonflame, Scatterbug, Spewpa, Vivillon, Litleo, Pyroar, Flabebe, Floette, Florges, Skiddo, Gogoat, Pancham, Pangoro, Furfrou, Espurr, Meowstic, Honedge, Doublade, Aegislash, Spritzee, Aromatisse, Swirlix, Slurpuff, Inkay, Malamar, Binacle, Barbaracle, Skrelp, Dragalge, Clauncher, Clawitzer, Helioptile, Heliolisk, Tyrunt, Tyrantrum, Amaura, Aurorus, Sylveon, Hawlucha, Dedenne, Carbink, Goomy, Sliggoo, Goodra, Klefki, Phantump, Trevenant, Pumpkaboo, Gourgeist, Bergmite, Avalugg, Noibat, Noivern, Xerneas, Yveltal, Zygarde, Diancie, Hoopa, Volcanion, Rowlet, Dartrix, Decidueye, Litten, Torracat, Incineroar, Popplio, Brionne, Primarina, Pikipek, Trumbeak, Toucannon, Yungoos, Gumshoos, Grubbin, Charjabug, Vikavolt, Crabrawler, Crabominable, Oricorio, Cutiefly, Ribombee, Rockruff, Lycanroc, Wishiwashi, Mareanie, Toxapex, Mudbray, Mudsdale, Dewpider, Araquanid, Fomantis, Lurantis, Morelull, Shiinotic, Salandit, Salazzle, Stufful, Bewear, Bounsweet, Steenee, Tsareena, Comfey, Oranguru, Passimian, Wimpod, Golisopod, Sandygast, Palossand, Pyukumuku, Type Null, Silvally, Minior, Komala, Turtonator, Togedemaru, Mimikyu, Bruxish, Drampa, Dhelmise, Jangmo-o, Hakamo-o, Kommo-o, Alolan Rattata, Alolan Raticate, Alolan Raichu, Alolan Sandshrew, Alolan Sandslash, Alolan Vulpix, Alolan Ninetales, Alolan Diglett, Alolan Dugtrio, Alolan Meowth, Alolan Persian, Alolan Geodude, Alolan Graveler, Alolan Golem, Alolan Grimer, Alolan Muk, Alolan Exeggutor, Alolan Marowak, Tapu Koko, Tapu Lele, Tapu Bulu, Tapu Fini, Cosmog, Cosmoem, Solgaleo, Lunala, Nihilego, Buzzwole, Pheromosa, Xurkitree, Celesteela, Kartana, Guzzlord, Necrozma, Magearna, Marshadow, Poipole, Naganadel, Stakataka, Blacephalon, Zeraora, Meltan, Melmetal, Grookey, Thwackey, Rillaboom, Scorbunny, Raboot, Cinderace, Sobble, Drizzile, Inteleon, Skwovet, Greedent, Rookidee, Corvisquire, Corviknight, Blipbug, Dottler, Orbeetle, Nickit, Thievul, Gossifleur, Eldegoss, Wooloo, Dubwool, Chewtle, Drednaw, yamper, Boltund, Rolycoly, Carkol, Coalossal, Applin, Flapple, Appletun, Silicobra, Sandaconda, Cramorant, Arrokuda, Barraskewda, Toxel, Toxtricity, Sizzlipede, Centiskorch, Clobbopus, Grapploct, Sinistea, Polteageist, Hatenna, Hattrem, Hatterene, Impidimp, Morgrem, Grimmsnarl, Galarian Zigzagoon, Galarian Linoone, Obstagoon, Galarian Meowth, Perrserker, Galarian Ponyta, Galarian Rapidash, Galarian Slowpoke, Galarian Slowbro, Galarian Slowking, Galarian Corsola, Cursola, Galarian Farfetch’d, Sirfetchd, Galarian Weezing, Galarian Mr. Mime, Mr. Rime, Galarian Darumaka, Galarian Darmanitan, Galarian Yamask, Runerigus, Galarian Stunfisk, Milcery, Alcremie, Falinks, Pincurchin, Snom, Frosmoth, Stonjourner, Eiscue, Indeedee, Morpeko, Cufant, Copperajah, Dracozolt, Arctozolt, Dracovish, Arctovish, Duraludon, Dreepy, Drakloak, Dragapult, Zacian, Zamazenta, Eternatus, Kubfu, Urshifu, Zarude, Regieleki, Regidrago, Glastrier, Spectrier, Calyrex, Galarian Articuno, Galarian Zapdos, Galarian Moltres'
pokelist = re.split('\,+', pokemon)

DRIVER_PATH = 'C:/Users/conno/Desktop/Scraping/chromedriver'

wd = webdriver.Chrome(executable_path=DRIVER_PATH)



def fetch_image_urls(query:str, max_links_to_fetch:int, wd:webdriver, sleep_between_interactions:int=1):
    def scroll_to_end(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(sleep_between_interactions)    
    
    # build the google query
    search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"

    # load the page
    wd.get(search_url.format(q=query))

    image_urls = set()
    image_count = 0
    results_start = 0
    while image_count < max_links_to_fetch:
        scroll_to_end(wd)

        # get all image thumbnail results
        thumbnail_results = wd.find_elements_by_css_selector("img.Q4LuWd")
        number_results = len(thumbnail_results)
        
        print(f"Found: {number_results} search results. Extracting links from {results_start}:{number_results}")
        
        for img in thumbnail_results[results_start:number_results]:
            # try to click every thumbnail such that we can get the real image behind it
            try:
                img.click()
                time.sleep(sleep_between_interactions)
            except Exception:
                continue

            # extract image urls    
            actual_images = wd.find_elements_by_css_selector('img.n3VNCb')
            for actual_image in actual_images:
                if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                    image_urls.add(actual_image.get_attribute('src'))

            image_count = len(image_urls)

            if len(image_urls) >= max_links_to_fetch:
                print(f"Found: {len(image_urls)} image links, done!")
                break
        else:
            print("Found:", len(image_urls), "image links, looking for more ...")
            time.sleep(30)
            return
            load_more_button = wd.find_element_by_css_selector(".mye4qd")
            if load_more_button:
                wd.execute_script("document.querySelector('.mye4qd').click();")

        # move the result startpoint further down
        results_start = len(thumbnail_results)

    return image_urls

def persist_image(folder_path:str,url:str):
    try:
        image_content = requests.get(url).content

    except Exception as e:
        print(f"ERROR - Could not download {url} - {e}")

    try:
        image_file = io.BytesIO(image_content)
        image = PIL.Image.open(image_file).convert('RGB')
        file_path = os.path.join(folder_path,hashlib.sha1(image_content).hexdigest()[:10] + '.jpg')
        with open(file_path, 'wb') as f:
            image.save(f, "JPEG", quality=85)
        print(f"SUCCESS - saved {url} - as {file_path}")
    except Exception as e:
        print(f"ERROR - Could not save {url} - {e}")
        
    
def search_and_download(search_term:str,driver_path:str,target_path='./images',number_images=100):
    target_folder = os.path.join(target_path,''.join(search_term.lower().split(' ')))

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    with webdriver.Chrome(executable_path=DRIVER_PATH) as wd:
        res = fetch_image_urls(search_term, number_images, wd=wd, sleep_between_interactions=0.5)
        
    for elem in res:
        persist_image(target_folder,elem)

for i in pokelist:
    search_and_download((i + ' pokemon'), DRIVER_PATH, target_path='C:/Users/conno/Documents/pokemonClassifier/pokemonimages')