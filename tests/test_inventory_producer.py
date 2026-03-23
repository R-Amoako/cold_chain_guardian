from data_generator.producers.inventory_producer import build_inventory_event


def test_build_inventory_event_returns_expected_fields():
    fridge = {
        "fridge_id": "FRIDGE-001",
        "location": "Clinic A - Vaccine Room",
    }

    medicine = {
        "medicine_name": "COVID-19 Vaccine",
        "safe_min_c": 2.0,
        "safe_max_c": 8.0,
    }

    event = build_inventory_event(fridge, medicine, 1)

    assert event["batch_id"] == "BATCH-001"
    assert event["fridge_id"] == "FRIDGE-001"
    assert event["medicine_name"] == "COVID-19 Vaccine"
    assert event["safe_min_c"] == 2.0
    assert event["safe_max_c"] == 8.0


def test_build_inventory_event_batch_number_is_zero_padded():
    fridge = {
        "fridge_id": "FRIDGE-002",
        "location": "Clinic B - Pharmacy",
    }

    medicine = {
        "medicine_name": "Insulin",
        "safe_min_c": 2.0,
        "safe_max_c": 8.0,
    }

    event = build_inventory_event(fridge, medicine, 7)

    assert event["batch_id"] == "BATCH-007"