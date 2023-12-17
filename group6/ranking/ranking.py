from ranking.localdata import weights, master_satellites

from ranking.utils import HOURS_PER_DAY
from ranking.utils import MINUTES_PER_HOUR
from ranking.utils import SECONDS_PER_MINUTE

#### PERFORMANCE: For better performance, max/min of different fields should be calculated just once in a single loop. Negligible improvement with our dataset -> we won't care.

#ENSURES
#travelTime returned in seconds

def get_travel_time(satellite):
    return float(satellite["travelTime"])


def get_suitability_to_event_rating(satellite, event_type):
    suitability_to_event_rating = 0
    if event_type in [e.name for e in satellite["eventTypes"]]:
        suitability_to_event_rating = 10
    return suitability_to_event_rating

def get_suitability_to_weather_rating(satellite):
    visibility_threshold = satellite["visibility_threshold"] #TODO Follow camelCase convention -.-"
    visibility = satellite["weatherConditions"]["visibility"]
    delta = visibility - visibility_threshold
    if delta > 0:
        return 10
    return 10 * (delta + 1)**2  #Delta is negative and [0, 1] in modulus

def get_suitability_to_time_of_day_rating(satellite):
    time_of_day_rating = 5
    if satellite["weatherConditions"]['isDay'] == True and satellite["worksDuringDay"]==True:
        time_of_day_rating = 10
    elif satellite["weatherConditions"]['isDay'] == False and satellite["worksDuringNight"]==True:
        time_of_day_rating = 10
    else:
        time_of_day_rating = 0
    return time_of_day_rating


BEST_RES = min(master_satellites, key=lambda satellite: satellite["spatialResolution"])["spatialResolution"]
WORST_RES = max(master_satellites, key=lambda satellite: satellite["spatialResolution"])["spatialResolution"]
def get_spatial_resolution_rating(satellite):
    #TODO the rating here should be event-based perhaps - read webpage

    spatial_resolution_rating = 10 * (1 - (satellite['spatialResolution'] - BEST_RES) / (WORST_RES - BEST_RES)) if WORST_RES != BEST_RES else 10
    return spatial_resolution_rating

        
MAX_FOU = max(master_satellites, key=lambda satellite: satellite["temporalResolution"])["temporalResolution"]
def get_frequency_of_update_rating(satellite):
    frequency_of_update_rating = (1 - satellite["temporalResolution"]/MAX_FOU) * 10
    return frequency_of_update_rating
        
MAX_PRICE = max(master_satellites, key=lambda satellite: satellite["price"])["price"]
def get_price_rating(satellite):
    price_rating = (1 - satellite["price"]/MAX_PRICE) * 10
    return price_rating    

def get_data_quality_rating(satellite):
    #It's hardcoded for now - we could come up with something elaborate
    data_quality_rating = satellite["dataQualityRating"]
    return data_quality_rating   


def rank_satellites(subarea, event_type, satellites):
    filtered_satellites = []
    for satellite in satellites:
        satellite_travel_time = float(satellite["travelTime"])
        timeliness_rating = 10 * (1 - satellite_travel_time/(float(satellite["temporalResolution"]) * HOURS_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE))

        '''
        if timeliness_rating < 0:
            timeliness_rating = (timeliness_rating * -1) % 10
        '''

        suitability_to_event_rating = get_suitability_to_event_rating(satellite, event_type)

        suitability_to_weather_rating= get_suitability_to_weather_rating(satellite)

        suitability_to_time_of_day_rating= get_suitability_to_time_of_day_rating(satellite)

        spatial_resolution_rating= get_spatial_resolution_rating(satellite)

        frequency_of_update_rating= get_frequency_of_update_rating(satellite)

        price_rating = get_price_rating(satellite)

        data_quality_rating = get_data_quality_rating(satellite)

        overall_rating = (weights["timeliness"] * timeliness_rating + \
                         weights["suitability_to_weather_type"] * suitability_to_weather_rating + \
                         weights["suitability_to_time_of_the_day"] * suitability_to_time_of_day_rating + \
                         weights["suitability_to_event_type"] * suitability_to_event_rating + \
                         weights["spatial_resolution"] * spatial_resolution_rating + \
                         weights["frequency_of_update"] * frequency_of_update_rating + \
                         weights["price"] * price_rating + \
                         weights["data_quality"] * data_quality_rating) / \
                         sum(weights.values())



        satellite_object_with_all_ratings = {
            "family": satellite["family"],
            "name": satellite["name"],
            "rating": overall_rating,
            "details": {
                "timeliness": timeliness_rating,
                "suitability_to_weather_type": suitability_to_weather_rating,
                "suitability_to_time_of_the_day": suitability_to_time_of_day_rating,
                "suitability_to_event_type": suitability_to_event_rating,
                "geographical_definition": spatial_resolution_rating,
                "frequency_of_update": frequency_of_update_rating,
                "apiURL": satellite["apiName"],
                "price": price_rating,
                "data_quality": data_quality_rating
            }
        }

        filtered_satellites.append(satellite_object_with_all_ratings)

    sorted_satellite_objects = sorted(filtered_satellites, key=lambda x: x['rating'], reverse=True)

    return sorted_satellite_objects
