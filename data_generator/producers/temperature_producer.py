from datetime import datetime, timezone
import random


def build_temperature_event(fridge: dict, temprature_c: float) -> dict:
    return {
        "fridge_id": fridge["fridge_id"],
        "location": fridge["location"],
        "temperature_c": temprature_c,
        "event_time": datetime.now(timezone.utc).isoformat(),
    }