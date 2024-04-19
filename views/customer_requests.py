CUSTOMERS = [
    {
        "id": 1,
        "name": "Ryan Tanay"
    }
]

def get_all_customers():
    return CUSTOMERS

def create_customer(customer):
    max_id = CUSTOMERS[-1]["id"]

    new_id = max_id + 1

    customer["id"] = new_id

    CUSTOMERS.append(customer)
    
    return customer

def get_single_customer(id):
    requested_customer = None
    
    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer
            
    return requested_customer

def delete_customer(id):

    location_index = -1

    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            
            customer_index = index

    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)
