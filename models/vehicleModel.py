from database import db
from vehicleType import VehicleType

class Vehicle(db.Model):
    __tablename__ = 'vehicle'

    id = db.Column(db.Integer, primary_key=True)
    vehicle_type = db.Column(db.Enum(VehicleType), nullable=False)
    reg_no = db.Column(db.String(15), nullable = False, unique = True)
    colour = db.Column(db.String(30))

    def __init__(self, vehicle_type, reg_no, colour):
        self.vehicle_type = vehicle_type
        self.reg_no = reg_no
        self.colour = colour

    def save(self):
        db.session.add(self)
        db.session.commit()
