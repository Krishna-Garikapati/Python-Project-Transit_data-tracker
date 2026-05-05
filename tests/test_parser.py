import unittest
from utils.parser import parse_data, filter_routes,parse_csv_data


class TestParser(unittest.TestCase):

    # ✅ Test API parsing
    def test_parse_data(self):
        mock_api_data = {
            "entity": [
                {
                    "id": "1",
                    "vehicle": {
                        "trip": {"routeId": "5"},
                        "position": {"latitude": 44.65, "longitude": -63.57}
                    }
                }
            ]
        }

        result = parse_data(mock_api_data)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["route"], 5)
        self.assertEqual(result[0]["latitude"], 44.65)

    # ✅ Test CSV parsing
    def test_parse_csv_data(self):
        mock_csv_data = [
            {"id": "1001", "route": "3", "latitude": "44.66", "longitude": "-63.58"}
        ]

        result = parse_csv_data(mock_csv_data)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["route"], 3)

    # ✅ Test invalid data (should skip)
    def test_parse_invalid_data(self):
        bad_data = [
            {"id": "1", "route": "abc"}  # invalid route
        ]

        result = parse_data(bad_data)

        self.assertEqual(len(result), 0)

    # ✅ Test filtering
    def test_filter_routes(self):
        data = [
            {"id": "1", "route": 2, "latitude": 0, "longitude": 0},
            {"id": "2", "route": 15, "latitude": 0, "longitude": 0}
        ]

        result = filter_routes(data, 1, 10)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["route"], 2)


if __name__ == "__main__":
    unittest.main()