import json
from app.base.models import Tenancy

def show_data():
    for t in Tenancy.objects.all():
        print(
            f"ID={t.id}, Name={t.name}, Rooms={t.total_rooms}, "
            f"Rent={t.rent_amount}, Size={t.size}, HospitalDist={t.hospital_distance}"
        )

def insert_data():
    with open("tenancy_data_preparation/tenancy_with_distances.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    for item in data:
        tenancy = Tenancy.objects.create(
            name=item["name"],
            description=item.get("description", ""),
            rent_amount=item.get("rent"),
            size=item.get("size_sqm"),
            total_rooms=item.get("rooms"),
            address=item.get("address", ""),
            hospital_distance=item.get("distance_to_hospital"),
            gym_distance=item.get("distance_to_gym"),
            school_distance=item.get("distance_to_school"),
            supermarket_distance=item.get("distance_to_supermarket"),
            latitude=item.get("latitude"),
            longitude=item.get("longitude"),
        )
        print("Inserted:", tenancy.name)

if __name__ == "__main__":
    show_data()