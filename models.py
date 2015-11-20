from database import db

class House(db.Model):

    __tablename__ = 'houses'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    geojson = db.Column(db.String)

    def __init__(self, id, price, bedrooms, bathrooms, geojson):

        self.id = id
        self.price = price
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.geojson = geojson

    def __repr__(self):

        return 'House ID: %s' % str(self.id)