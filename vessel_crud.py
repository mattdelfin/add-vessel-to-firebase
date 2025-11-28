from google.cloud import firestore
from datetime import datetime, timezone

db = firestore.Client.from_service_account_json("replace with json location")

# ------------------------------
# CREATE
# ------------------------------
def add_vessel(
    vessel_id: str,
    name: str,
    imo: str,
    vessel_type: str,
    status: str,
    draft_m: float,
    loa_m: float,
    ops_minutes: int,
    capacity: float,
    eta_utc: datetime
):
    doc = db.collection("Vessels").document(vessel_id)
    data = {
        "draft_m": draft_m,
        "eta": eta_utc.replace(tzinfo=timezone.utc),
        "imo": imo,
        "loa_m": loa_m,
        "name": name,
        "ops_minutes": ops_minutes,
        "status": status,
        "vessel_type": vessel_type,
        "capacity": capacity,
        "vessel_id": vessel_id,
    }
    doc.set(data)
    print(f"Added vessel {vessel_id}")

# ------------------------------
# READ
# ------------------------------
def read_vessel(vessel_id: str):
    doc = db.collection("Vessels").document(vessel_id).get()
    if doc.exists:
        print(doc.to_dict())
    else:
        print("Vessel not found.")

# ------------------------------
# UPDATE
# ------------------------------
def update_vessel(vessel_id: str, field: str, value):
    db.collection("Vessels").document(vessel_id).update({field: value})
    print(f"Updated {vessel_id}: {field} = {value}")

# ------------------------------
# DELETE
# ------------------------------
def delete_vessel(vessel_id: str):
    db.collection("Vessels").document(vessel_id).delete()
    print(f"Deleted vessel {vessel_id}")


# EXAMPLE USAGE
if __name__ == "__main__":
    add_vessel(
        vessel_id="5",
        name="MV New Voyager",
        imo="10000",
        vessel_type="Container",
        status="waiting",
        draft_m=7.5,
        loa_m=120.0,
        ops_minutes=3,
        capacity=30000,
        eta_utc=datetime(2025, 1, 20, 10, 30, tzinfo=timezone.utc)
    )

    read_vessel("6")

    # update_vessel("MV001", "status", "berthed")

    # delete_vessel("MV001")
