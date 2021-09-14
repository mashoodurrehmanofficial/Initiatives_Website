from  geopy.geocoders import Nominatim
import names




def get_geo_info(country,city):
    user_agent = names.get_first_name()
    print(user_agent)
    geolocator = Nominatim(user_agent=str(user_agent)) 
    loc = geolocator.geocode(city+','+ country)
    print("Locaion generated -->> ", loc)
    return loc

 