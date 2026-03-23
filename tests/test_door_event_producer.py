from datetime import datetime

from data_generator.producers.door_event_producer import build_door_event


def test_build_door_event_returns_expected_fields():
    fridge = {
        "fridge_id": "FRIDGE-001",
        "location": "Clinic A - Vaccine Room",
    }

    event = build_door_event(fridge)

    assert event["fridge_id"] == "FRIDGE-001"
    assert event["location"] == "Clinic A - Vaccine Room"
    assert event["event_type"] in ["OPEN", "CLOSE"]
    assert "event_time" in event


def test_build_door_event_event_time_is_valid_iso_format():
    fridge = {
        "fridge_id": "FRIDGE-002",
        "location": "Clinic B - Pharmacy",
    }

    event = build_door_event(fridge)

    parsed = datetime.fromisoformat(event["event_time"])
    assert parsed is not None