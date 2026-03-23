def build_inventory_event(fridge: dict, medicine: dict, batch_no: int) -> dict:
    return {
        "batch_id": f"BATCH-{batch_no:03d}",
        "fridge_id": fridge["fridge_id"],
        "medicine_name": medicine["medicine_name"],
        "safe_min_c": medicine["safe_min_c"],
        "safe_max_c": medicine["safe_max_c"],
    }