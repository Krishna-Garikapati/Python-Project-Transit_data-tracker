import unittest
import requests
from unittest.mock import patch
from services.api_service import fetch_transit_data


class TestAPIService(unittest.TestCase):

    @patch("services.api_service.requests.get")
    def test_fetch_transit_data_success(self, mock_get):
    # Mock response object
        mock_response = unittest.mock.Mock()
        mock_response.json.return_value = {"entity": [{"id": "1"}]}
        mock_response.raise_for_status.return_value = None

        mock_get.return_value = mock_response

        result = fetch_transit_data()

        self.assertEqual(result, {"entity": [{"id": "1"}]})


if __name__ == "__main__":
    unittest.main()