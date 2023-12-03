from database import db

class ParkingLot:
    __tablename__ = 'parking_lot'

    id = db.Column(db.String(10), primary_key=True, default='PR1234')
    floor = db.Column(db.Integer, nullable=False, default=1, autoincrement=True)

    
