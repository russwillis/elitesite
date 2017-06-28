from app import db


class Modules(db.Model):
    __tablename__ = 'modules'

    id = db.Column(db.Integer, primary_key=True)
    mod_class = db.Column(db.String())
    rating = db.Column(db.String())
    price = db.Column(db.Integer)
    ship = db.Column(db.String())
    group_name = db.Column(db.String())
    group_category = db.Column(db.String())

    def __init__(self, id, mod_class, rating, price,
    ship, group_name, group_category):
        self.id = id
        self.mod_class = mod_class
        self.rating = rating
        self.price = price
        self.ship = ship
        self.group_name = group_name
        self.group_category = group_category

    def __repr__(self):
        return '<id {}>'.format(self.id)
