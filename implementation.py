import json

# TODO: add other python code here (@aabha text message csv, @martina counting algo)

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

def convert_to_data_array(data_structure):
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

# TODO: replace this with the word_to_emoji variable from Martina's implementation
word_to_emoji = {'so funny': 2, 'crazy': 2, 'poop': 1, 'okay': 2, 'cool': 4, 'love': 2, 'happy': 3, 'delicious': 1, 'book': 2, 'stressed': 2, 'sad': 1, 'shrug': 1, 'home': 1, 'sleepy': 1, 'bye': 1}

data_array = convert_to_data_array(word_to_emoji)
# writes the data to a separate JSON file to be used in highcharts and html
with open('data.json', 'w') as json_file:
    json.dump(data_array, json_file)

print("Data has been written to 'data.json' file.")
