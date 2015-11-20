from models import House
import json
import os

from flask import request, jsonify

from database import app, db
from models import House


@app.route('/listings', methods=['GET'])
def listings():

    params = request.args.items()

    raw = House.query

    for p in params:
    	kw = p[0]
    	arg = p[1]
        if kw == 'min_price':
            raw = raw.filter(House.price >= int(arg))
        elif kw == 'max_price':
            raw = raw.filter(House.price <= int(arg))
        elif kw == 'min_bed':
            raw = raw.filter(House.bedrooms >= int(arg))
        elif kw == 'max_bed':
            raw = raw.filter(House.bedrooms <= int(arg))
        elif kw == 'min_bath':
            raw = raw.filter(House.bathrooms >= int(arg))
        elif kw == 'max_bath':
            raw = raw.filter(House.bathrooms <= int(arg))

    return jsonify({
            "type": "FeatureCollection",
            "features": [h.geojson for h in raw.all()]
            })


if __name__ == '__main__':

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port = port, debug=True)




