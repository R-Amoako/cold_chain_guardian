from datetime import datetime
from data_generator.producers.temperature_producer import build_temperature_event

def test_build_temperature_event_returns_expected_fields():
    fridge = {
        "fridge_id": "FRIDGE-001",
        "location": "Clinic A - Vaccine Room",
    }

    temperature_c = 5.4

    event = build_temperature_event(fridge, temperature_c)
    
    assert event['fridge_id'] == "FRIDGE-001"
    assert event['location'] == "Clinic A - Vaccine Room"
    assert event['temperature_c'] == 5.4
    assert "event_time" in event



def test_build_temperature_event_event_time_is_valid_iso_format():
    fridge = {
        "fridge_id": "FRIDGE-001",
        "location": "Clinic A - Vaccine Room",
    }

    event = build_temperature_event(fridge, 6.2)

    parsed = datetime.fromisoformat(event["event_time"])
    assert parsed is not None



