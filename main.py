from services.api_service import fetch_transit_data
from utils.parser import parse_data, filter_routes, load_csv, parse_csv_data

#functions
def display_data(data):
    print("\nTransit Data:\n")
    for bus in data:
        print(f"Bus {bus['id']} | Route {bus['route']} | "
              f"Location ({bus['latitude']}, {bus['longitude']})")


def main():
    #Enter user choice
    print("1. Load data from transit API")
    print("2. Load data from CSV")

    choice = input("Choose option (1 or 2): ")


    #basing on choice call related function
    if choice == "1":
        raw_data = fetch_transit_data()
         #Lets parse data as per requirement. Change data the way we want for app
        parsed_data = parse_data(raw_data)
    elif choice == "2":
        raw_data = load_csv("data/sample.csv")
        parsed_data = parse_csv_data(raw_data)
    else:
        print("Invalid choice.")
        return
    

    #If no raw data or parsed data returned from choice 1 or 2
    if not raw_data:
        print("No data available.")
        return
      
    if not parsed_data:
        print("No valid data after parsing.")
        return



    # user input to find buses data in given range
    try:
        print("Enter Routes 1-10")
        min_route = int(input("Enter minimum route number: "))
        max_route = int(input("Enter maximum route number: "))
    except ValueError:
        print("Invalid input. Using default range (1–10).")
        min_route, max_route = 1, 10

    filtered_data = filter_routes(parsed_data, min_route, max_route)

    if not filtered_data:
        print("No routes found in range.")
        return

    display_data(filtered_data)




#code

#__name__ is a built-in variable that stores the module’s name, however the below condition doesnt work if main is a imported module
#Run directly   → __name__ = "__main__" → condition True  → runs
# Imported file  → __name__ = "main"     → condition False → does not run

if __name__ == "__main__":
    main() 