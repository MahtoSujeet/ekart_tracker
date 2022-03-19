import requests


class Ekart:
    """API for ekart

    :param api_key: str
    """

    def __init__(self, api_key) -> None:
        self._endpoint = "https://api.trackingmore.com"
        self._headers = {
            "Content-Type": "application/json",
            "Trackingmore-Api-Key": api_key,
        }

    def get_status(self, order_id, carrier_code: str = "ekart") -> str:
        """Gets static of order.

        :param order_id
        :carrier_code (optional)
        """
        return requests.get(
            f"{self._endpoint}/v2/trackings/{carrier_code}/{order_id}",
            headers=self._headers,
        ).text
