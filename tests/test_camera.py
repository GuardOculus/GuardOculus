from app.models import Location, Camera
from app import db


def test_get_cameras_by_location(app):
    location = Location(name="Hall", x=10, y=10, width=10, height=10)
    db.session.add(location)
    camera = Camera(location_id=location.id, token=None, x=10, y=10, angle=10)
    db.session.add(camera)

    camera_from_db = Camera.query.filter_by(location_id=location.id).first()

    assert camera == camera_from_db
