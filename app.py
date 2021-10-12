
from flask import Flask, abort, jsonify,send_file, safe_join
import json
from os import name

file = open('nfts.json', 'r')
data = json.load(file)
app = Flask(__name__)

@app.route('/api/<token_id>')
def creature(token_id):

    race = data[int(token_id)]["race"]
    bodyType = data[int(token_id)]["body build"]
    weapon = data[int(token_id)]["weapon"]
    imgUrl = data[int(token_id)]["tokenUri"]
    name = ("My Collection #%s" %token_id)

    attributes = []
    _add_attribute(attributes, 'Race', race)
    _add_attribute(attributes, 'Body Type', bodyType)
    _add_attribute(attributes, 'Weapon', weapon)


    return jsonify({
        'name': name,
        'description': 'Friendly OpenSea Creature that enjoys long swims in the ocean.',
        'image': imgUrl,
        'external_url': 'https://openseacreatures.io/%s' % token_id,
        'attributes': attributes
    })


@app.route('/image/<filename>')
def get_image(filename):

    safe_path = safe_join("./images/", filename)
    return send_file(safe_path, mimetype='image/gif')

def _add_attribute(existing, attribute_name, value):
    trait = {
        'trait_type': attribute_name,
        'value': value
    }

    existing.append(trait)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    app.run(host='0.0.0.0')