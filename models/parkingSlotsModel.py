from database import db
from vehicleType import VehicleType

class ParkingSlots:
    __tablename__ = 'parking_slots'

    parking_lot_id = db.Column(db.Integer, db.ForeignKey('parking_lot.id'),nullable = False)
    floor = db.Column(db.Integer,db.ForeignKey('parking_lot.floor'),nullable=False)
    slots = db.Column(db.Integer, nullable=False, default=1, autoincrement=True)
    vehicle_type = db.Column(db.Enum(VehicleType), nullable=False)
    is_available = db.Column(db.Boolean, nullable = False, default = True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), default = None)
    
