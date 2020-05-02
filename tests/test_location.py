from app.models import Location
from app import db


def test_get_all_locations(app):
    """Test that locations can be got from database"""
    location1 = Location(name="Hall", x=10, y=10, width=10, height=10)
    location2 = Location(name="Kitchen", x=30, y=10, width=100, height=100)
    db.session.add(location1)
    db.session.add(location2)

    all_locations = Location.query.all()

    assert all_locations[0] == location1
    assert all_locations[1] == location2
