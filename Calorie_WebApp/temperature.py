import requests
from selectorlib import Extractor


class Temperature:
    """
    A scraper that uses a yml file to read the xpath of a value it needs to extract from
     the timeanddate.com/weather webpage.
    """
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) brave/1.42.88 Chrome/47.0.2526.110 Brave/1.42.88 Safari/537.36"}
    base_url = 'https://www.timeanddate.com/weather/'
    yml_path = 'temperature.yaml'

    def __init__(self, country, city):
        self.country = country.replace(" ", "-")
        self.city = city.replace(" ", "-")

    def _build_url(self):
        """Build the url string adding country and city"""
        url = self.base_url + self. country + "/" + self.city
        return url

    def _scrape(self):
        """Extracts a value as instructed by the yml file and returns dictionary"""
        url = self._build_url()
        extractor = Extractor.from_yaml_file(self.yml_path)
        r = requests.get(url, headers=self.headers)
        full_content = r.text
        raw_content = extractor.extract(full_content)
        return raw_content

    def get(self):
        """Cleans the output of _scrape"""
        scraped_content = self._scrape()
        return float(scraped_content['temp'].replace("°C", "").strip())


if __name__ == "__main__":
    temperature = Temperature(country="usa", city="san francisco")
    print((temperature.get()))
