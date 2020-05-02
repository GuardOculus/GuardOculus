from app.models import Location, Camera, MapObject
from app import db


def test_get_mapobjects_by_camera(app):
    """Ensure that objects can be got by camera id"""
    location = Location(name="hall", x=10, y=10, width=10, height=10)
    db.session.add(location)
    camera = Camera(location_id=location.id, x=10, y=10, angle=10)
    db.session.add(camera)
    mapobject = MapObject(camera_id=camera.id, x=10, y=10)
    db.session.add(mapobject)

    mapobject_from_db = MapObject.query.filter_by(camera_id=camera.id).first()

    assert mapobject_from_db == mapobject
