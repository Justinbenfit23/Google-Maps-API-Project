import googlemaps
import pprint
import time
import urllib.request
from test3 import get_my_key




API_KEY = 'AIzaSyDe-Cmt9A6tMFsqJUPtsaY73kYfYt_tzjg'


#define our Client
gmaps = googlemaps.Client(key = API_KEY)
#Define our Search
places_result = gmaps.places_nearby(location= "40.35003,-111.95206", radius= 40000,open_now= False,type= 'car_repair')
pprint.pprint(places_result)
pause script for 3 
time.sleep(3)

#get next 20 results
places_result = gmaps.places_nearby(page_token = places_result['next_page_token'])

pprint.pprint(places_result)


#loop through each place in the results 

for place in places_result['results']:
	my_place_id = place['place_id']

	#define my fields
	my_fields = ['name','formatted_phone_number','type']

	#make a request for the details
	place_details = gmaps.place(place_id = my_place_id, fields = my_fields)

	#print the results
	pprint.pprint(place_details)

	#NEXT FIGURE OUT HOW TO SPECIFY BODY SHOPS IN FIELDS AND EXPORT DATA TO CSV









