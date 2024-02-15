import json

# TODO: add other python code here (@aabha text message csv, @martina counting algo, @miley emoji_to_image map)

def convert_to_data_array(data_structure):
    data_array = []
    total_occurrences = sum(data_structure.values())
    
    for key, value in data_structure.items():
        datapoint = {
            "name": key,
            "value": (value / total_occurrences) * 100,  # calculate percentage
            "marker": {
                "symbol": 'url(https://upload.wikimedia.org/wikipedia/en/thumb/9/9a/Trollface_non-free.png/220px-Trollface_non-free.png)' # TODO: @miley replace url link with respective emoji image using map
            }
        }
        data_array.append(datapoint)
    
    return data_array

word_to_emoji = {'book': 2, 'stressed': 2, 'sad': 1, 'shrug': 1, 'home': 1, 'sleepy': 1, 'bye': 1} # TODO: replace this with the word_to_emoji variable from Martina's implementation
data_array = convert_to_data_array(word_to_emoji)
# writes the data to a separate JSON file to be used in highcharts and html
with open('data.json', 'w') as json_file:
    json.dump(data_array, json_file)

print("Data has been written to 'data.json' file.")
