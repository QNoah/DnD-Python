import json

class Monsters:
    def __init__(self):
        try:
            with open('json/monsters.json') as f:
                data = json.load(f)
        
                for monster in data['monsters']:
                    print(f"{monster['name']}, Hit points: {monster['Hit Points']}")
        except FileNotFoundError:
            print("File could not be found")
        except KeyError:
            print("De verwachte sleutel 'Name' is niet gevonden")
        f.close()
    
    def showAll(self):
        pass

Monsters()