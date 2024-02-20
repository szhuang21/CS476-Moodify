import json
import pandas as pd
import string
import re

# call create_data_json() to create data.json 

emoji_to_image = {
    "delicious": "url(https://cdn.shopify.com/s/files/1/1061/1924/products/Hungry_Emoji_Icon_c20f1808-f3e2-4051-8941-3d157764e8cb.png?v=1485573460)",
    "happy": "url(https://cdn.shopify.com/s/files/1/1061/1924/files/Smliing_Emoji_Icon.png?13752525173949329807)",
    "love": "url(https://cdn.smallseotools.com/emojis/Apple/Red-Heart-on-Apple-iOS-13.3/Red-Heart-on-Apple-iOS-13.3.png)",
    "cool": "url(https://cdn.shopify.com/s/files/1/1061/1924/products/Emoji_Icon_-_Sunglasses_cool_emoji.png?v=1485573433)",
    "sad": "url(https://cdn.shopify.com/s/files/1/1061/1924/products/Emoji_Icon_-_Sad_Emoji_70x70.png?v=1485573425)",
    "okay": "url(https://cdn.shopify.com/s/files/1/1061/1924/products/OK_Hand_Sign_Emoji_Icon_ios10_70x70.png?v=1511943170)",
    "poop": "url(https://cdn.shopify.com/s/files/1/1061/1924/products/Poop_Emoji_2.png?v=1485573482)",
    "crazy": "url(https://cdn.shopify.com/s/files/1/1061/1924/files/Tongue_Out_Emoji_1_70x70.png?13752525173949329807)",
    "sleepy": "url(https://cdn.shopify.com/s/files/1/1061/1924/products/Sleeping_Emoji_2.png?v=1485573494)",
    "book": "url(https://em-content.zobj.net/source/apple/354/open-book_1f4d6.png)",
    "so funny": "url(https://cdn.shopify.com/s/files/1/1061/1924/products/Tears_Emoji_Icon_2_70x70.png?v=1485573515)",
    "stressed": "url(https://cdn.shopify.com/s/files/1/1061/1924/products/Weary_Face_Emoji_Icon_ios10.png?v=1511762076)",
    "shrug": "url(https://em-content.zobj.net/source/apple/354/woman-shrugging_1f937-200d-2640-fe0f.png)",
    "home": "url(https://em-content.zobj.net/source/apple/354/house_1f3e0.png)",
    "bye": "url(https://cdn.shopify.com/s/files/1/1061/1924/products/Waving_Hand_Sign_Emoji_Icon_ios10_70x70.png?v=1511943171)"
}

final = [ ("delicious", ["delicious", "yummy", "nom nom", "nomnom", "tasty","yum", "goofy", "hungry", "licking lips", "icking my lips", "tongue smiley"]),
("happy", ["happy", "smile", "smiley", "smiley face", "so happy","that’s great", "so great", "yay", "hooray", "hurrah", "cheerful", "delighted", "joyful", "pleased"]),
("love",  ["love", "heart"]),
("cool", ["sunglasses", "cool", "sunglasses on", "smiling face with sunglasses","sunglasses emoji", "sunglasses smiley", "stunner shades", "sunny","cool kid", "ballin", "chillin", "cool guy", "cool dude", "cool chick","cool girl", "baller", "awesome", "relaxing", "relaxed", "no stress"]),
("sad", ["sad", "hurt", "sad emoji", "sad face", "sullen", "oh well", "sigh","disappointed", "lonely", "feel bad", "downcast", "long face", "somber","solemn", "melancholy", "dejected", "glum", "gloomy", "heartbroken","dreary", "unhappy", "sorrowful", "bummed out", "long-faced"]),
("okay", ["ok", "perfect", "okay", "sounds good", "dece", "a-ok"]),
("poop",  ["poop", "poo", "doo doo", "dookie", "crap", "caca", "turd", "poops", "turds"]),
("crazy", ["crazy", "silly", "hehe", "hee hee", "teehee", "cray", "wild", "excited", "loco", "sticking my tongue out", "tongue out emoji", "tongue out face", "tongue out smiley"]),
("sleepy", ["sleepy", "sleeping", "tired", "napping", "sleepy face", "sleeping face", "nap", "sleep", "snoring", "nap time", "asleep", "exhausted", "zzz", "Zs"]),
("book", ["book", "study", "reading", "books"]),
("so funny", [ "so funny", "too funny", "hilarious", "lol", "cracking up", "cracked up","crack me up", "dying laughing", "tears of joy", "tears of happiness","funny", "funniest", "laugh", "haha", "hehe", "crying smiley", "smiley face","laughing", "lmao", "lolz", "lols", "lulz", "rotfl", "rotflmao"]),
("stressed", ["stressed", "worried", "distraught", "flustered", "whiny", "distressed","anxious", "tormented", "apprehensive"]),
("shrug", ["shrug", "shrugging", "man shrugging", "confused man", "confused","undecided", "indecisive", "I don’t know", "i dunno", "dunno", "shrugged","shruggie", "don’t care", "i don’t care"]),
("home", ["home", "house", "townhouse", "townhome", "town home", "homes", "houses","townhouses", "townhomes", "town homes"]),
("bye", ["bye", "hi", "hello", "see ya", "bye bye", "hey", "slap", "wave", "waving","goodbye", "wave goodbye", "waving goodbye", "see you later", "ttfn"])],
final = final[0]

def create_data_json():
    print("create_data_json() called")
    word_to_emoji = read_messages_csv()
    data_array = convert_to_data_array(word_to_emoji)
    print("data_array: ", data_array)

    # writes the data to a separate JSON file to be used in highcharts and html
    with open('static/data.json', 'w') as json_file:
        json.dump(data_array, json_file)

    print("Data has been written to 'data.json' file.")

def read_messages_csv(): # Will upload CSV and find the column with "Text"
    print("read_messages_csv() called")
    data = pd.read_csv("staticFiles/uploads/messages.csv", encoding='latin1')
    data.head()
    text_data = data['Text'].tolist()

    # Removing punctuation and converting to lowercase
    cleaned_data = [''.join(c for c in s if isinstance(s, str) and (c.isalpha() or c.isspace())) for s in text_data if s is not None and isinstance(s, str)]
    cleaned_data = [s.replace('Â\xa0', '') for s in cleaned_data]
    cleaned_data = [s.lower() for s in cleaned_data]
    print("\ncleaned data: ", cleaned_data)

    word_to_emoji = {}
    for sentence in cleaned_data:  #get sentence from the text file
        for map_word, list_of_words in final: #go through all the emoji word lists above
            for curr_word in list_of_words:
                if re.search(r'\b' + curr_word + r'\b', sentence):  #make sure the entire word is in one of the words in the list. E.g. Fixes "ok" in {book} to be false.
                    if map_word in word_to_emoji.keys():
                        word_to_emoji[map_word] += 1
                    else:
                        word_to_emoji[map_word] = 1

    word_to_emoji = dict(sorted(word_to_emoji.items(), key=lambda item: item[1], reverse=True))
    print(word_to_emoji)
    return word_to_emoji

def convert_to_data_array(data_structure):
    print("covert_to_data_array() called")
    data_array = []
    total_occurrences = sum(data_structure.values())
    for key, value in data_structure.items():
        datapoint = {
            "name": key,
            "value": (value / total_occurrences) * 100,  # calculate percentage
            "marker": {
                "symbol": emoji_to_image[key]
            }
        }
        data_array.append(datapoint)
    return data_array