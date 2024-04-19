LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8422 Johnson Pike"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 Emory Drive"
    }
]

def get_all_locations():
    return LOCATIONS

def create_location(location):
    # Get the id value of the last animal in the list
    max_id = LOCATIONS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    location["id"] = new_id

    # Add the animal dictionary to the list
    LOCATIONS.append(location)

    # Return the dictionary with `id` property added
    return location

def get_single_location(id):
    requested_location = None
    
    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location
            
    return requested_location

def delete_location(id):

    location_index = -1

    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            
            location_index = index

    if location_index >= 0:
        LOCATIONS.pop(location_index)
        
def update_location(id, new_location):

    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:

            LOCATIONS[index] = new_location
            break
