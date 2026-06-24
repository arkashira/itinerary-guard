from itinerary_guard import ItineraryGuard, Advisory

def test_parse_feed():
    feed = {"USA": "Level 3 – Do Not Travel", "Canada": "Level 1 – Exercise Normal Precautions"}
    guard = ItineraryGuard([feed])
    advisories = guard.aggregated_advisories
    assert len(advisories) == 2
    assert advisories[0].destination == "USA"
    assert advisories[0].severity == "Level 3 – Do Not Travel"
    assert advisories[1].destination == "Canada"
    assert advisories[1].severity == "Level 1 – Exercise Normal Precautions"

def test_get_advisory():
    feed = {"USA": "Level 3 – Do Not Travel", "Canada": "Level 1 – Exercise Normal Precautions"}
    guard = ItineraryGuard([feed])
    advisory = guard.get_advisory("USA")
    assert advisory.destination == "USA"
    assert advisory.severity == "Level 3 – Do Not Travel"

def test_check_itinerary():
    feed1 = {"USA": "Level 3 – Do Not Travel", "Canada": "Level 1 – Exercise Normal Precautions"}
    feed2 = {"Mexico": "Level 2 – Exercise Increased Caution", "UK": "Level 1 – Exercise Normal Precautions"}
    guard = ItineraryGuard([feed1, feed2])
    itinerary = ["USA", "Canada", "Mexico"]
    advisories = guard.check_itinerary(itinerary)
    assert len(advisories) == 3
    assert advisories[0].destination == "USA"
    assert advisories[0].severity == "Level 3 – Do Not Travel"
    assert advisories[1].destination == "Canada"
    assert advisories[1].severity == "Level 1 – Exercise Normal Precautions"
    assert advisories[2].destination == "Mexico"
    assert advisories[2].severity == "Level 2 – Exercise Increased Caution"

def test_update_feeds():
    feed1 = {"USA": "Level 3 – Do Not Travel", "Canada": "Level 1 – Exercise Normal Precautions"}
    feed2 = {"Mexico": "Level 2 – Exercise Increased Caution", "UK": "Level 1 – Exercise Normal Precautions"}
    guard = ItineraryGuard([feed1])
    guard.update_feeds([feed1, feed2])
    advisories = guard.aggregated_advisories
    assert len(advisories) == 4
    assert advisories[0].destination == "USA"
    assert advisories[0].severity == "Level 3 – Do Not Travel"
    assert advisories[1].destination == "Canada"
    assert advisories[1].severity == "Level 1 – Exercise Normal Precautions"
    assert advisories[2].destination == "Mexico"
    assert advisories[2].severity == "Level 2 – Exercise Increased Caution"
    assert advisories[3].destination == "UK"
    assert advisories[3].severity == "Level 1 – Exercise Normal Precautions"
