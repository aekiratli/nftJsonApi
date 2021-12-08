
from flask import Flask, abort, jsonify, send_file, safe_join
import json
import requests
from io import BytesIO

from werkzeug.exceptions import ExpectationFailed

url = "https://supply-fetch.vercel.app/"

file = open('nfts.json', 'r')
data = json.load(file)
application = Flask(__name__)


@application.route('/api/<token_id>')
def creatur2e(token_id):

    supply = requests.get(url).text
    supply = int(supply)
    
    if int(token_id) > (int(supply)-1):
        abort(404)
    try:
        accs1 = data[int(token_id)]["accessoire1"]
        accs2 = data[int(token_id)]["accessoire2"]
        mouth = data[int(token_id)]["mouth"]
        eyes = data[int(token_id)]["eye"]
        background = data[int(token_id)]["background"]
        body = data[int(token_id)]["body"]
        imgUrl = data[int(token_id)]["imgUrl"]
        name = ("Crypto Whale #%s" % token_id)

        attributes = []
        addToJson(attributes, 'eyes', eyes)
        addToJson(attributes, 'accessoire 1', accs1)
        addToJson(attributes, 'accessoire 2', accs2)
        addToJson(attributes, 'mouth', mouth)
        addToJson(attributes, 'background', background)
        addToJson(attributes, 'body', body)
        return jsonify({
            'name': name,
            'description': 'Whales from the ocean',
            'image': imgUrl,
            'external_url': 'https://openseacreatures.io/%s' % token_id,
            'attributes': attributes
        })
    except KeyError:
        imgUrl = data[int(token_id)]["imgUrl"]
        name = ("Crypto Whale #%s" % token_id)
        attributes = []
        return jsonify({
        'name': name,
        'description': 'Whales from the ocean',
        'image': imgUrl,
        'external_url': 'https://openseacreatures.io/%s' % token_id,
        'attributes': attributes
        })


def addToJson(existing, attribute_name, value):
    trait = {
        'trait_type': attribute_name,
        'value': value
    }

    existing.append(trait)
