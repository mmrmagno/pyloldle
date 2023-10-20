from flask import Flask, render_template, request, jsonify, session
import random
import os

app = Flask(__name__, static_url_path='/static', static_folder='src')
app.secret_key = 'your_secret_key_here'

champions = {
    "aatrox": {
        "ico": "src/img/aatrox.png",
        "Gender": "Male",
        "Positions": ["Top"],
        "Species": ["Darkin"],
        "Resource": "Manaless",
        "Range type": ["Melee"],
        "Region(s)": ["Shurima", "Runeterra"],
        "Release year": 2013
    },
    "ahri": {
        "ico": "src/img/ahri.png",
        "Gender": "Female",
        "Positions": ["Middle"],
        "Species": ["Vastaya"],
        "Resource": "Mana",
        "Range type": "Ranged",
        "Region(s)": ["Ionia"],
        "Release year": 2011
    },
    "akali": {
        "ico": "src/img/akali.png",
        "Gender": "Female",
        "Positions": ["Middle", "Top"],
        "Species": ["Human"],
        "Resource": "Energy",
        "Range type": ["Melee"],
        "Region(s)": ["Ionia"],
        "Release year": 2010
    },
    "akshan": {
        "ico": "src/img/akshan.png",
        "Gender": "Male",
        "Positions": ["Bottom"],
        "Species": ["Human"],
        "Resource": "Mana",
        "Range type": ["Ranged"],
        "Region(s)": ["Shurima"],
        "Release year": 2021
    },
    "alistar": {
        "ico": "src/img/alistar.png",
        "Gender": "Male",
        "Positions": ["Support"],
        "Species": ["Minotaur"],
        "Resource": "Mana",
        "Range type": ["Melee"],
        "Region(s)": ["Demacia"],
        "Release year": 2009
    },
    "amumu": {
        "ico": "src/img/amumu.png",
        "Gender": "Male",
        "Positions": ["Jungle"],
        "Species": ["Yordle"],
        "Resource": "Mana",
        "Range type": ["Melee"],
        "Region(s)": ["Shurima"],
        "Release year": 2009
    },
    "anivia": {
        "ico": "src/img/anivia.png",
        "Gender": "Female",
        "Positions": ["Middle"],
        "Species": ["Cryophoenix"],
        "Resource": "Mana",
        "Range type": ["Ranged"],
        "Region(s)": ["Freljord"],
        "Release year": 2009
    },
    "annie": {
        "ico": "src/img/annie.png",
        "Gender": "Female",
        "Positions": ["Middle"],
        "Species": ["Human"],
        "Resource": "Mana",
        "Range type": ["Ranged"],
        "Region(s)": ["Noxus", "Runeterra"],
        "Release year": 2009
    },
    "aphelios": {
        "ico": "src/img/aphelios.png",
        "Gender": "Male",
        "Positions": ["Bottom"],
        "Species": ["Human", "Spiritualist"],
        "Resource": "Mana",
        "Range type": ["Ranged"],
        "Region(s)": ["Targon"],
        "Release year": 2019
    },
    "ashe": {
        "ico": "src/img/ashe.png",
        "Gender": "Female",
        "Positions": ["Bottom"],
        "Species": ["Human"],
        "Resource": "Mana",
        "Range type": ["Ranged"],
        "Region(s)": ["Freljord"],
        "Release year": 2009
    },
    "aurelion sol": {
        "ico": "src/img/aurelionsol.png",
        "Gender": "Male",
        "Positions": ["Middle"],
        "Species": ["Celestial", "Dragon"],
        "Resource": "Mana",
        "Range type": ["Ranged"],
        "Region(s)": ["Runeterra",  "Targon"],
        "Release year": 2016
    },
    "azir": {
        "ico": "src/img/azir.png",
        "Gender": "Male",
        "Positions": ["Middle"],
        "Species": ["God Warrior"],
        "Resource": "Mana",
        "Range type": ["Ranged"],
        "Region(s)": ["Shurima"],
        "Release year": 2014
    },
    "bard": {
        "ico": "src/img/bard.png",
        "Gender": "Male",
        "Positions": ["Support"],
        "Species": ["Celestial"],
        "Resource": "Mana",
        "Range type": ["Ranged"],
        "Region(s)": ["Ionia"],
        "Release year": 2015
    },
    "bel veth": {
        "ico": "src/img/belveth.png",
        "Gender": "Female",
        "Positions": ["Jungle"],
        "Species": ["Void Being"],
        "Resource": "Manaless",
        "Range type": ["Melee"],
        "Region(s)": ["The Void"],
        "Release year": 2022
    },
    "blitzcrank": {
        "ico": "src/img/blitzcrank.png",
        "Gender": "N/A",
        "Positions": ["Support"],
        "Species": "Golem",
        "Resource": "Mana",
        "Range type": ["Melee"],
        "Region(s)": ["Zaun"],
        "Release year": 2009
    },
    "brand": {
        "ico": "src/img/brand.png",
        "Gender": "Male",
        "Positions": ["Mid", "Support"],
        "Species": ["Demon"],
        "Resource": "Mana",
        "Range type": ["Ranged"],
        "Region(s)": ["The Abyss"],
        "Release year": 2011
    },
    "braum": {
        "ico": "src/img/braum.png",
        "Gender": "Male",
        "Positions": ["Support"],
        "Species": ["Human"],
        "Resource": "Mana",
        "Range type": ["Melee"],
        "Region(s)": ["Freljord"],
        "Release year": 2013
    },
    "camille": {
        "ico": "src/img/camille.png",
        "Gender": "Female",
        "Positions": ["Top"],
        "Species": ["Human"],
        "Resource": "Mana",
        "Range type": ["Melee"],
        "Region(s)": ["Piltover"],
        "Release year": 2016
    },
    "cassiopeia": {
        "ico": "src/img/cassiopeia.png",
        "Gender": "Female",
        "Positions": ["Middle"],
        "Species": ["Human", "Half-Serpent"],
        "Resource": "Mana",
        "Range type": ["Ranged"],
        "Region(s)": ["Noxus"],
        "Release year": 2010
    },
    "cho gath": {
        "ico": "src/img/chogath.png",
        "Gender": "Male",
        "Positions": ["Top"],
        "Species": ["Void Being"],
        "Resource": "Mana",
        "Range type": ["Melee"],
        "Region(s)": ["The Void"],
        "Release year": 2009
    },
    "corki": {
        "ico": "src/img/corki.png",
        "Gender": "Male",
        "Positions": ["Middle"],
        "Species": ["Yordle"],
        "Resource": "Mana",
        "Range type": ["Ranged"],
        "Region(s)": ["Bandle City"],
        "Release year": 2009
    },
    "darius": {
        "ico": "src/img/darius.png",
        "Gender": "Male",
        "Positions": ["Top"],
        "Species": ["Human"],
        "Resource": "Mana",
        "Range type": ["Melee"],
        "Region(s)": ["Noxus"],
        "Release year": 2011
    },
    "diana": {
        "ico": "src/img/diana.png",
        "Gender": "Female",
        "Positions": ["Jungle", "Middle"],
        "Species": ["Human"],
        "Resource": "Mana",
        "Range type": ["Melee"],
        "Region(s)": ["Targon"],
        "Release year": 2012
    },
    "dr.mundo": {
        "ico": "src/img/drmundo.png",
        "Gender": "Male",
        "Positions": ["Top"],
        "Species": ["Mutant"],
        "Resource": "Rage",
        "Range type": ["Melee"],
        "Region(s)": ["Zaun"],
        "Release year": 2009
    },
    "draven": {
        "ico": "src/img/draven.png",
        "Gender": "Male",
        "Positions": ["Bottom"],
        "Species": ["Human"],
        "Resource": "Mana",
        "Range type": ["Ranged"],
        "Region(s)": ["Noxus"],
        "Release year": 2011
    },
    "ekko": {
        "ico": "src/img/ekko.png",
        "Gender": "Male",
        "Positions": ["Middle", "Jungle"],
        "Species": ["Human"],
        "Resource": "Energy",
        "Range type": ["Melee"],
        "Region(s)": ["Zaun", "Piltover"],
        "Release year": 2015
    }

}

@app.route('/')
def index():
    session['secret_champion'] = random.choice(list(champions.values()))
    session['previous_guesses'] = []
    return render_template('index.html', background_image_url='src/bc/summonersrift.jpg')

@app.route('/guess', methods=['POST'])
def guess():
    current_guess = request.json.get('guess')
    
    feedback = {}
    if current_guess in champions:
        guessed_champion = champions[current_guess]
        for property, value in guessed_champion.items():
            feedback["guessed_" + property] = value
            if type(value) is list:
                if set(value) & set(session['secret_champion'][property]):
                    feedback[property] = "yellow" if set(value) != set(session['secret_champion'][property]) else "green"
                else:
                    feedback[property] = "red"
            else:
                if value == session['secret_champion'][property]:
                    feedback[property] = "green"
                else:
                    feedback[property] = "red"
        
        if guessed_champion["Release year"] > session['secret_champion']["Release year"]:
            feedback["Release year direction"] = "down"
        elif guessed_champion["Release year"] < session['secret_champion']["Release year"]:
            feedback["Release year direction"] = "up"
        else:
            feedback["Release year direction"] = "equal"
        
        session['previous_guesses'].append(feedback)
    
    return jsonify(feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)
