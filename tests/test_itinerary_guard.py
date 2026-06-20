from itinerary_guard import ItineraryGuard, Itinerary

def test_ingest_data():
    guard = ItineraryGuard()
    data = [
        {'id': 1, 'airline': 'Airline1', 'hotel': 'Hotel1', 'transportation': 'Transportation1'},
        {'id': 2, 'airline': 'Airline2', 'hotel': 'Hotel2', 'transportation': 'Transportation2'}
    ]
    guard.ingest_data(data)
    assert len(guard.itineraries) == 2

def test_verify_itinerary():
    guard = ItineraryGuard()
    data = [
        {'id': 1, 'airline': 'Airline1', 'hotel': 'Hotel1', 'transportation': 'Transportation1'}
    ]
    guard.ingest_data(data)
    itinerary = guard.verify_itinerary(1)
    assert itinerary.id == 1
    assert itinerary.airline == 'Airline1'

def test_cross_verify():
    guard = ItineraryGuard()
    data = [
        {'id': 1, 'airline': 'Airline1', 'hotel': 'Hotel1', 'transportation': 'Transportation1'}
    ]
    guard.ingest_data(data)
    assert guard.cross_verify(1) == True
    assert guard.cross_verify(2) == False
