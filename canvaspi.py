from canvasapi import Canvas
import json

def extract_key_value(json_file, key):
    # Read JSON data from file
    with open(json_file, "r") as infile:
        json_data = infile.read()
    
    # Parse JSON data
    data = json.loads(json_data)
    value = data.get(key)
    return value

def save(json_file, data):
    # Serializing json
    json_object = json.dumps(data, indent=4)
 
    # Writing to save.json
    with open(json_file, "w") as outfile:
        outfile.write(json_object)

try:
    token = extract_key_value('save.json', "token")
    web_url = extract_key_value('save.json', 'web_url')
except json.decoder.JSONDecodeError:
    token = input("""Please insert your canvas user access token. 
    This will be written so you don't have to do it later.""")
    web_url = input("""Put in your organization's URL. 
    This will be formatted like https://____.instructure.com""")
    freshdata = {
        "token": token,
        "web_url": web_url
    }
    save('save.json', freshdata)

