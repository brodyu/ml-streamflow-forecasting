from wwo_hist import retrieve_hist_data

frequency = 24
start_date = '11-JAN-2010'
end_date = '11-JAN-2021'
api_key = 'c1146f76cc0c48e090552459211902'
location_list = ['96816','96822']
hist_weather_data = retrieve_hist_data(api_key, location_list, start_date, end_date, frequency, location_label = False, export_csv = True, store_df = True)