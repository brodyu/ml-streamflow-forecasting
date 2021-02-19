from wwo_hist import retrieve_hist_data

# Credit to Ekapope Viriyakovithya's Medium article for the wwo_hist library
class WorldWeatherOnline:

    def __init__(self, frequency, start_date, end_date, api_key, location_list):
        self.frequency = frequency
        self.start_date = start_date
        self.end_date = end_date
        self.api_key = api_key
        self.location_list = location_list

    def call_api (self):
        hist_weather_data = retrieve_hist_data(api_key = self.api_key, location_list = self.location_list, start_date = self.start_date, end_date = self.end_date, frequency = self.frequency, location_label = False, export_csv = True, store_df = True)

if __name__ == "__main__":
    # Data pull frequency by hour
    frequency = 24
    # Time horizon for data pull, remember limited to 500 API calls a day
    start_date = '11-JAN-2020'
    end_date = '11-JAN-2021'
    # Input API key here:
    api_key = 'xxxxxxxxxxxxxxxxxxxxx'
    # Location list: input can be city name, zip code, state, country, etc
    location_list = ['96789','96822']

    model = WorldWeatherOnline(frequency, start_date, end_date, api_key, location_list)
    model.call_api()