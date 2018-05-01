# -*- coding: utf-8 -*-

"""

	Multi-Player Online Battle Games
	Matches and Players Analysis Application Server

	http://linserv2.cims.nyu.edu:40555/

"""


import os
import numpy as np

######################## IMAGE PLOT ###########################

from io import BytesIO
import base64
#from matplotlib.figure import Figure
#from matplotlib.dates import DateFormatter
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#figPath = os.path.join('static', 'skillradar')

######################## LOAD MODEL ###########################
# import pre-trained models
import pyspark
from pyspark import SparkContext, SparkConf
from pyspark.mllib.tree import RandomForest, RandomForestModel

conf = SparkConf().setAppName('GameAnalysis').setMaster('local')
sc = SparkContext()
# player skill analyzing model
model_player = RandomForestModel.load(sc, 'model/RandomForestModel/myRandomForestRegressionModel')
# match result predicting model
model_match = RandomForestModel.load(sc, "model/Dota2RandomForestModel")


######################## WEB SERVER ###########################
from flask import Flask, render_template, request, redirect, flash, url_for, make_response
from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectMultipleField, Form, widgets
from wtforms.validators import DataRequired, InputRequired

from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'secret-for-dev'
PORT = os.getenv('PORT', '40555')
#app.config['UPLOAD_FOLDER'] = figPath
factor = 0.75
heroes_count = 112
items_count = 189
HEROES = [(0, u'Anti-Mage'), (1, u'Axe'), (2, u'Bane'), (3, u'Bloodseeker'), (4, u'Crystal Maiden'), (5, u'Drow Ranger'), (6, u'Earthshaker'), (7, u'Juggernaut'), (8, u'Mirana'), (9, u'Morphling'), (10, u'Shadow Fiend'), (11, u'Phantom Lancer'), (12, u'Puck'), (13, u'Pudge'), (14, u'Razor'), (15, u'Sand King'), (16, u'Storm Spirit'), (17, u'Sven'), (18, u'Tiny'), (19, u'Vengeful Spirit'), (20, u'Windranger'), (21, u'Zeus'), (22, u'Kunkka'), (23, u'Lina'), (24, u'Lion'), (25, u'Shadow Shaman'), (26, u'Slardar'), (27, u'Tidehunter'), (28, u'Witch Doctor'), (29, u'Lich'), (30, u'Riki'), (31, u'Enigma'), (32, u'Tinker'), (33, u'Sniper'), (34, u'Necrophos'), (35, u'Warlock'), (36, u'Beastmaster'), (37, u'Queen of Pain'), (38, u'Venomancer'), (39, u'Faceless Void'), (40, u'Wraith King'), (41, u'Death Prophet'), (42, u'Phantom Assassin'), (43, u'Pugna'), (44, u'Templar Assassin'), (45, u'Viper'), (46, u'Luna'), (47, u'Dragon Knight'), (48, u'Dazzle'), (49, u'Clockwerk'), (50, u'Leshrac'), (51, u"Nature's Prophet"), (52, u'Lifestealer'), (53, u'Dark Seer'), (54, u'Clinkz'), (55, u'Omniknight'), (56, u'Enchantress'), (57, u'Huskar'), (58, u'Night Stalker'), (59, u'Broodmother'), (60, u'Bounty Hunter'), (61, u'Weaver'), (62, u'Jakiro'), (63, u'Batrider'), (64, u'Chen'), (65, u'Spectre'), (66, u'Ancient Apparition'), (67, u'Doom'), (68, u'Ursa'), (69, u'Spirit Breaker'), (70, u'Gyrocopter'), (71, u'Alchemist'), (72, u'Invoker'), (73, u'Silencer'), (74, u'Outworld Devourer'), (75, u'Lycan'), (76, u'Brewmaster'), (77, u'Shadow Demon'), (78, u'Lone Druid'), (79, u'Chaos Knight'), (80, u'Meepo'), (81, u'Treant Protector'), (82, u'Ogre Magi'), (83, u'Undying'), (84, u'Rubick'), (85, u'Disruptor'), (86, u'Nyx Assassin'), (87, u'Naga Siren'), (88, u'Keeper of the Light'), (89, u'Io'), (90, u'Visage'), (91, u'Slark'), (92, u'Medusa'), (93, u'Troll Warlord'), (94, u'Centaur Warrunner'), (95, u'Magnus'), (96, u'Timbersaw'), (97, u'Bristleback'), (98, u'Tusk'), (99, u'Skywrath Mage'), (100, u'Abaddon'), (101, u'Elder Titan'), (102, u'Legion Commander'), (103, u'Techies'), (104, u'Ember Spirit'), (105, u'Earth Spirit'), (106, u'Underlord'), (107, u'Terrorblade'), (108, u'Phoenix'), (109, u'Oracle'), (110, u'Winter Wyvern'), (111, u'Arc Warden')]
ITEMS = [(0, u'blink'), (1, u'blades_of_attack'), (2, u'broadsword'), (3, u'chainmail'), (4, u'claymore'), (5, u'helm_of_iron_will'), (6, u'javelin'), (7, u'mithril_hammer'), (8, u'platemail'), (9, u'quarterstaff'), (10, u'quelling_blade'), (11, u'ring_of_protection'), (12, u'gauntlets'), (13, u'slippers'), (14, u'mantle'), (15, u'branches'), (16, u'belt_of_strength'), (17, u'boots_of_elves'), (18, u'robe'), (19, u'circlet'), (20, u'ogre_axe'), (21, u'blade_of_alacrity'), (22, u'staff_of_wizardry'), (23, u'ultimate_orb'), (24, u'gloves'), (25, u'lifesteal'), (26, u'ring_of_regen'), (27, u'sobi_mask'), (28, u'boots'), (29, u'gem'), (30, u'cloak'), (31, u'talisman_of_evasion'), (32, u'cheese'), (33, u'magic_stick'), (34, u'magic_wand'), (35, u'ghost'), (36, u'clarity'), (37, u'flask'), (38, u'dust'), (39, u'bottle'), (40, u'ward_observer'), (41, u'ward_sentry'), (42, u'tango'), (43, u'courier'), (44, u'tpscroll'), (45, u'travel_boots'), (46, u'phase_boots'), (47, u'demon_edge'), (48, u'eagle'), (49, u'reaver'), (50, u'relic'), (51, u'hyperstone'), (52, u'ring_of_health'), (53, u'void_stone'), (54, u'mystic_staff'), (55, u'energy_booster'), (56, u'point_booster'), (57, u'vitality_booster'), (58, u'power_treads'), (59, u'hand_of_midas'), (60, u'oblivion_staff'), (61, u'pers'), (62, u'poor_mans_shield'), (63, u'bracer'), (64, u'wraith_band'), (65, u'null_talisman'), (66, u'mekansm'), (67, u'vladmir'), (68, u'flying_courier'), (69, u'buckler'), (70, u'ring_of_basilius'), (71, u'pipe'), (72, u'urn_of_shadows'), (73, u'headdress'), (74, u'sheepstick'), (75, u'orchid'), (76, u'cyclone'), (77, u'force_staff'), (78, u'dagon'), (79, u'necronomicon'), (80, u'ultimate_scepter'), (81, u'refresher'), (82, u'assault'), (83, u'heart'), (84, u'black_king_bar'), (85, u'aegis'), (86, u'shivas_guard'), (87, u'bloodstone'), (88, u'sphere'), (89, u'vanguard'), (90, u'blade_mail'), (91, u'soul_booster'), (92, u'hood_of_defiance'), (93, u'rapier'), (94, u'monkey_king_bar'), (95, u'radiance'), (96, u'butterfly'), (97, u'greater_crit'), (98, u'basher'), (99, u'bfury'), (100, u'manta'), (101, u'lesser_crit'), (102, u'armlet'), (103, u'invis_sword'), (104, u'sange_and_yasha'), (105, u'satanic'), (106, u'mjollnir'), (107, u'skadi'), (108, u'sange'), (109, u'helm_of_the_dominator'), (110, u'maelstrom'), (111, u'desolator'), (112, u'yasha'), (113, u'mask_of_madness'), (114, u'diffusal_blade'), (115, u'ethereal_blade'), (116, u'soul_ring'), (117, u'arcane_boots'), (118, u'orb_of_venom'), (119, u'stout_shield'), (120, u'ancient_janggo'), (121, u'medallion_of_courage'), (122, u'smoke_of_deceit'), (123, u'veil_of_discord'), (124, u'necronomicon_2'), (125, u'necronomicon_3'), (126, u'diffusal_blade_2'), (127, u'dagon_2'), (128, u'dagon_3'), (129, u'dagon_4'), (130, u'dagon_5'), (131, u'rod_of_atos'), (132, u'abyssal_blade'), (133, u'heavens_halberd'), (134, u'ring_of_aquila'), (135, u'tranquil_boots'), (136, u'shadow_amulet'), (137, u'enchanted_mango'), (138, u'ward_dispenser'), (139, u'travel_boots_2'), (140, u'lotus_orb'), (141, u'solar_crest'), (142, u'guardian_greaves'), (143, u'aether_lens'), (144, u'octarine_core'), (145, u'dragon_lance'), (146, u'faerie_fire'), (147, u'iron_talon'), (148, u'blight_stone'), (149, u'tango_single'), (150, u'crimson_guard'), (151, u'wind_lace'), (152, u'moon_shard'), (153, u'silver_edge'), (154, u'bloodthorn'), (155, u'echo_sabre'), (156, u'glimmer_cape'), (157, u'tome_of_knowledge'), (158, u'hurricane_pike'), (159, u'banana'), (160, u'infused_raindrop'), (161, u'halloween_candy_corn'), (162, u'mystery_hook'), (163, u'mystery_arrow'), (164, u'mystery_missile'), (165, u'mystery_toss'), (166, u'mystery_vacuum'), (167, u'halloween_rapier'), (168, u'greevil_whistle'), (169, u'greevil_whistle_toggle'), (170, u'present'), (171, u'winter_stocking'), (172, u'winter_skates'), (173, u'winter_cake'), (174, u'winter_cookie'), (175, u'winter_coco'), (176, u'winter_ham'), (177, u'winter_kringle'), (178, u'winter_mushroom'), (179, u'winter_greevil_treat'), (180, u'winter_greevil_garbage'), (181, u'winter_greevil_chewy'), (182, u'river_painter'), (183, u'river_painter2'), (184, u'river_painter3'), (185, u'river_painter4'), (186, u'river_painter5'), (187, u'river_painter6'), (188, u'river_painter7')]


######################## BUILD FORM ###########################
class PlayerStatsForm(FlaskForm):
    player_id = StringField('Player ID', [validators.DataRequired("Enter ID of Player")])
    player_assists = StringField('Player Assists', [validators.DataRequired("Enter number of assists of player"), validators.NumberRange(min=0, message="Invalid input")])
    player_dbno = StringField('Player DBNO', [validators.DataRequired("Enter number of dbno of player"), validators.NumberRange(min=0, message="Invalid input")])
    player_dist_ride = StringField('Player Ride Distance', [validators.DataRequired("Enter ride distance of player"), validators.NumberRange(min=0, message="Invalid input")])
    player_dist_walk = StringField('Player Walk Distance', [validators.DataRequired("Enter walk distance of player"), validators.NumberRange(min=0, message="Invalid input")])
    player_dmg = StringField('Player DMG', [validators.DataRequired("Enter damages of player"), validators.NumberRange(min=0, message="Invalid input")])
    player_kills = StringField('Player Kills', [validators.DataRequired("Enter number of kills of player"), validators.NumberRange(min=0, message="Invalid input")])
    player_survive_time = StringField('Player Survive Time', [validators.DataRequired("Enter survive time of player"), validators.NumberRange(min=0, message="Invalid input")])


class MultiCheckboxField(SelectMultipleField):
    #widget = widgets.TableWidget()
    option_widget = widgets.CheckboxInput()


class MatchStatsForm(FlaskForm):
    rediant_heroes = MultiCheckboxField('', choices=[h for h in HEROES])
    rediant_items = MultiCheckboxField('', choices=[i for i in ITEMS])
    dire_heroes = MultiCheckboxField('', choices=[h for h in HEROES])
    dire_items = MultiCheckboxField('', choices=[i for i in ITEMS])
 

######################## WEB APP SERVER ###########################
# Home Page
@app.route('/')
def home():    
    return render_template('index.html')

# PUBG Death Heapmap Page
@app.route('/death')
def death():
    return render_template('death.html')

# PUBG Player Analysis Input Form Page
@app.route('/player', methods = ['GET','POST'])
def player():
    playerform = PlayerStatsForm()
    
    if request.method == 'POST' and playerform.validate():
        
        player_id = request.form['player_id']
        player_assists = request.form['player_assists']
        player_dbno = request.form['player_dbno']
        player_dist_ride = request.form['player_dist_ride']
        player_dist_walk = request.form['player_dist_walk']
        player_dmg = request.form['player_dmg']
        player_kills = request.form['player_kills']
        player_survive_time = request.form['player_survive_time']

        try:
            # use pre-trained model to predict the team placement with input stats of a player
            # format of input data of model: np.array([0, 0, 0, 999.492249, 109, 0, 871.3560000000001])
            result = model_player.predict((np.array([player_assists, player_dbno, player_dist_ride, player_dist_walk, player_dmg, player_kills, player_survive_time])))    

            # Render skill Radar Plot
            dataLenth = 6
            labels = np.array(['assists','dbno','ride dist','walk dist','dmg','kills'])

            player_assists_full_score = 13 * factor
            player_dbno_full_score = 148 * factor
            player_dist_ride_full_score = 506175.4 * factor * (1-factor)
            player_dist_walk_full_score = 1273645.38 * factor * (1-factor)
            player_dmg_full_score = 9408.0 * factor
            player_kills_full_score = 10

            player_assists_score = 100.00 if player_assists >= player_assists_full_score else round(player_assists * 100.00 / player_assists_full_score, 2)
            player_dbno_score = 100.00 if player_dbno >= player_dbno_full_score else round(player_dbno * 100.00 / player_dbno_full_score, 2)
            player_dist_ride_score = 100.00 if player_dist_ride >= player_dist_ride_full_score else round(player_dist_ride * 100.00 / player_dist_ride_full_score, 2)
            player_dist_walk_score = 100.00 if player_dist_walk >= player_dist_walk_full_score else round(player_dist_walk * 100.00 / player_dist_walk_full_score, 2)
            player_dmg_score = 100.00 if player_dmg >= player_dmg_full_score else round(player_dmg * 100.00 / player_dmg_full_score, 2)
            player_kills_score = 100.00 if player_kills >= player_kills_full_score else round(player_kills * 100.00 / player_kills_full_score, 2)


            data = np.array([player_assists_score, player_dbno_score, player_dist_ride_score, player_dist_walk_score, player_dmg_score, player_kills_score])
            angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False)
            data = np.concatenate((data, [data[0]])) 
            angles = np.concatenate((angles, [angles[0]])) 
            
            fig = plt.figure()
            ax = fig.add_subplot(111, polar=True)
            ax.plot(angles, data, 'ro-', linewidth=2)
            ax.set_thetagrids(angles * 180/np.pi, labels)
            ax.set_title("Skill Scores", va='bottom')
            ax.grid(True)
            
            #plt.savefig('static/skillradar/skillradar.png') 

            figfile = BytesIO()
            plt.savefig(figfile, format='png')
            figfile.seek(0)
            img = base64.b64encode(figfile.getvalue())
        except:
            # send flash message and return to form if input data is not as required
            flash("Invalid Input! Please check your input stats")
            return (redirect(url_for('player')))
        return render_template("playerresult.html", result=str(round(result*100, 2))+"%", image=img)
    return render_template('player.html', form=playerform)


# DOTA2 Match Predict Request and Response Page
@app.route('/match', methods = ['GET','POST'])
def match():
    matchform = MatchStatsForm()
    if request.method == 'POST':
        r_heroes = matchform.rediant_heroes.data
        r_items = matchform.rediant_items.data
        d_heroes = matchform.dire_heroes.data
        d_items = matchform.dire_items.data
        try:
            rediant_heroes = [0] * heroes_count
            dire_heroes = [0] * heroes_count
            rediant_items = [0] * items_count
            dire_items = [0] * items_count

            for rh in r_heroes:
                rediant_heroes[int(rh)] = 1
            for ri in r_items:
                rediant_items[int(ri)] = 1
            for dh in d_heroes:
                dire_heroes[int(dh)] = 1
            for di in d_items:
                dire_items[int(di)] = 1

            # use pre-trained model to predict the result of match with selected heroes and itemes
            # format of input data of model: np.array([0, 0, ..., 1, ...])
            vec = rediant_heroes + rediant_items + dire_heroes + dire_items
            result = model_match.predict((np.array(vec)))
            winner = 'REDIANT' 
            if result != 1.0:
                winner = 'DIRE'
        except:
            # send flash message and return to form if input data is not as required
            flash("Invalid Select! Please check your selections")
            return (redirect(url_for('match')))
        return render_template("matchresult.html", winner=winner)
        #return redirect(url_for('match_result', r_heroes=r_heroes, r_items=r_items, d_heroes=d_heroes, d_items=d_items))
    return render_template('match.html', form=matchform)


######################################################################
#   M A I N
######################################################################
if __name__ == "__main__":
    print "***************************************"
    print " W E B   S E R V I C E   R U N N I N G"
    print "***************************************"
    app.run(host='0.0.0.0', port=int(PORT), debug=True)
