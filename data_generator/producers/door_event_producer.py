# data-generator/src/producers/door_event_producer.py

from datetime import datetime, timezone
import random


def build_door_event(fridge: dict) -> dict:
    return {
        "fridge_id": fridge["fridge_id"],
        "location": fridge["location"],
        "event_type": random.choice(["OPEN", "CLOSE"]),
        "event_time": datetime.now(timezone.utc).isoformat(),
    }