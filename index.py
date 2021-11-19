
from flask import Flask, abort, jsonify, send_file, safe_join
import json
import requests
from io import BytesIO

url = "https://supply-fetch.vercel.app/"
img_ipfs = "https://gateway.pinata.cloud/ipfs/QmcJV2Kvta4ffP54Y3zW58zKYFMzwivEkkyp1rF2vp2pqX/"
json_ipfs = "https://gateway.pinata.cloud/ipfs/Qmf7Wp6RRso5eTtsYyqv8BRYS7JdMG86v6ChNQAmC3VQWy/"

file = open('nfts.json', 'r')
data = json.load(file)
application = Flask(__name__)


# @application.route('/api/<token_id>')
# def creature(token_id):

#     supply = requests.get(url).text
#     supply = int(supply)
    
#     if int(token_id) > (int(supply)-1):
#         abort(404)

#     accs1 = data[int(token_id)]["accessoire1"]
#     accs2 = data[int(token_id)]["accessoire2"]
#     mouth = data[int(token_id)]["mouth"]
#     eyes = data[int(token_id)]["eye"]
#     background = data[int(token_id)]["background"]
#     body = data[int(token_id)]["body"]
#     imgUrl = data[int(token_id)]["imgUrl"]
#     name = ("Crypto Whale #%s" % token_id)

#     attributes = []
#     addToJson(attributes, 'eyes', eyes)
#     addToJson(attributes, 'accessoire 1', accs1)
#     addToJson(attributes, 'accessoire 2', accs2)
#     addToJson(attributes, 'mouth', mouth)
#     addToJson(attributes, 'background', background)
#     addToJson(attributes, 'body', body)

#     return jsonify({
#         'name': name,
#         'description': 'Whales from the ocean',
#         'image': imgUrl,
#         'external_url': 'https://openseacreatures.io/%s' % token_id,
#         'attributes': attributes
#     })

@application.route('/ipfs/QmcJV2Kvta4ffP54Y3zW58zKYFMzwivEkkyp1rF2vp2pqX/<token_id>')
def creature(token_id):

    supply = requests.get(url).text
    supply = int(supply)
    
    if int(token_id) > (int(supply)-1):
        abort(404)

    jsonResp = requests.get(str(json_ipfs+str(token_id)+".json")).text

    print(jsonResp)
    return jsonResp

@application.route('/image/<filename>')
def get_image(filename):

    token_id = filename.split(".")[0]

    supply = requests.get(url).text

    if int(token_id) > (int(supply)-1):
        abort(404)

    image = requests.get(str(img_ipfs+str(token_id)+".png"))
    img = BytesIO(image.content)
    return send_file(img, mimetype='image/gif')


def addToJson(existing, attribute_name, value):
    trait = {
        'trait_type': attribute_name,
        'value': value
    }

    existing.append(trait)
