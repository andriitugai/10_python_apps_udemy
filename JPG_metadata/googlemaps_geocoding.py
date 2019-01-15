import googlemaps
from datetime import datetime
from pprint import pprint

gmaps = googlemaps.Client(key = "AIzaSyBHwzjDTwec95YZ6a1p1ts0Ygr5LVw5wCk")

reverse_geocode_result = gmaps.reverse_geocode((50.43138888888889,30.4875))

address =  reverse_geocode_result[0]

#pprint(address)

pprint(address['formatted_address'])
pprint(address['place_id'])
