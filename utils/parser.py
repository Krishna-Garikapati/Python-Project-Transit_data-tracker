import csv


#To parse data from API that is choice 1
def parse_data(data):
    parsed = []
    #checking if 'data' is dcitionary and if it contains
    if isinstance(data, dict):
        #for app i need id,routeID, latitude and longitude all these are under entity key in data dictionary
        data_values = data["entity"]
    else:
        return []

    for each_item in data_values:
        try:
                bus = {
                    "id": each_item["id"],
                    "route": int(each_item["vehicle"]["trip"]["routeId"]),
                    "latitude": float(each_item["vehicle"]["position"]["latitude"]),
                    "longitude": float(each_item["vehicle"]["position"]["longitude"])
                }

                parsed.append(bus)

        except (ValueError, TypeError, KeyError):
            continue

    return parsed

#CSV fall back
# To parse data from CSV file that is choice 2
def parse_csv_data(data):
    parsed = []

    for item in data:
        try:
            bus = {
                "id": item["id"],
                "route": int(item["route"]),
                "latitude": float(item["latitude"]),
                "longitude": float(item["longitude"])
            }
            parsed.append(bus)
        except (KeyError, ValueError, TypeError):
            continue

    return parsed

def filter_routes(data, min_route=1, max_route=10):
    return [
        bus for bus in data
        if min_route <= bus["route"] <= max_route
    ]

def load_csv(file_path):
    data = []

    try:
        with open(file_path, newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print("CSV file not found.")

    return data

#“The parser module is responsible for transforming raw API data into a clean and structured format. It handles missing values, converts data types, and filters relevant records while safely skipping invalid entries.”