
from flask import Flask, abort, jsonify,send_file, safe_join
import json
import requests

url = "https://test-nft-react.herokuapp.com/"
file = open('nfts.json', 'r')
data = json.load(file)
app = Flask(__name__)

@app.route('/app.py')
def test2():
    return "app.py"

@app.route('/api/test')
def test():
    return "/api/test"

@app.route('/app.py/test')
def test3():
    return "/app.py/test"
@app.route('/test')
def test4():
    return "/test"

@app.route('/app.py/api/<token_id>')
def creature(token_id):

    supply = requests.get(url).text

    if int(token_id) > (int(supply)-1):
        abort(404)

    

    eyes = data[int(token_id)]["eyes"]
    background = data[int(token_id)]["background"]
    skin = data[int(token_id)]["skin"]
    imgUrl = data[int(token_id)]["imgUrl"]
    name = ("Crypto Whalez #%s" %token_id)

    attributes = []
    _add_attribute(attributes, 'eyes', eyes)
    _add_attribute(attributes, 'background', background)
    _add_attribute(attributes, 'skin', skin)


    return jsonify({
        'name': name,
        'description': 'Whales from the ocean',
        'image': imgUrl,
        'external_url': 'https://openseacreatures.io/%s' % token_id,
        'attributes': attributes
    })


@app.route('/app.py/image/<filename>')

def get_image(filename):

    token_id = filename.split(".")[0]

    supply = requests.get(url).text

    if int(token_id) > (int(supply)-1):
        abort(404)

    safe_path = safe_join("./images/", filename)
    return send_file(safe_path, mimetype='image/gif')

def _add_attribute(existing, attribute_name, value):
    trait = {
        'trait_type': attribute_name,
        'value': value
    }

    existing.append(trait)
