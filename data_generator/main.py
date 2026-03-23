# data-generator/src/main.py

from pprint import pprint

from config import FRIDGES, MEDICINES
from producers.temperature_producer import build_temperature_event
from producers.door_event_producer import build_door_event
from producers.inventory_producer import build_inventory_event


def main() -> None:
    print("=== INVENTORY EVENTS ===")
    for i, fridge in enumerate(FRIDGES, start=1):
        event = build_inventory_event(fridge, MEDICINES[0], i)
        pprint(event)

    print("\n=== NORMAL TEMPERATURE EVENTS ===")
    for fridge in FRIDGES:
        event = build_temperature_event(fridge, 2)
        pprint(event)

    print("\n=== DOOR EVENTS ===")
    for fridge in FRIDGES:
        event = build_door_event(fridge)
        pprint(event)

    print("\n=== EXCURSION TEMPERATURE EVENTS ===")
    for fridge in FRIDGES:
        event = build_temperature_event(fridge, 9)
        pprint(event)


if __name__ == "__main__":
    main()