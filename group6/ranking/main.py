import pandas
import requests
import geohash
import copy


#Local imports
from ranking.localdata import master_satellites
from ranking.ranking import rank_satellites
from ranking.timeliness import calculate_travel_time_and_weather_details
from ranking.localdata import external_API_enabled
from ranking.utils import get_timestamp
from ranking.utils import extract_polygon_from_geohash

tle_data = {}
def create_subareas_ranking(subareas):
        rankings = []
        #TODO handle concatenated version
        subareas_keys = list(subareas[0].keys())

        if subareas != "error":
            for index, subarea_key in enumerate(subareas_keys): #if enumerate doesn't work on keys, go list(keys)

                subarea_parameters = pandas.DataFrame(subareas[0][subarea_key])

                lat, lon = geohash.decode(subarea_key)
                alt = 0
                polygon = extract_polygon_from_geohash(subarea_key)

                date_format = "%Y-%m-%d %H:%M:%S"
                event_timestamp = get_timestamp(subareas[1]["date"], date_format)

                event_type = subareas[1]["features"][0]["properties"]["type"].upper()

                '''
                # Call to NASA API to get satellite TLE data
                Removed, now using N2YO
                tle_url = "https://tle.ivanstanojevic.me/api/tle/"
                '''
                target_location = {
                    "lat": lat,
                    "lon": lon,
                    "alt": alt
                }
                satellites = []

                n2yo_url = "https://api.n2yo.com/rest/v1/satellite/tle/"
                api_key = "RFLDHD-2N265V-UFLW6Z-512K"
                for satellite in master_satellites:

                    #Currently not working if API is disabled AND a satellite is missing
                    #Also, there is a **ton** of redudancy here with structures and data, and the control flow could use some revamping. But we'll take it until (if ever) refactoring time comes.
                    if external_API_enabled:
                        #Cache results since they are pretty accurate if updated hourly
                        sat_id = satellite["id"]
                        n2yo_endpoint = n2yo_url + sat_id + "?" + "apiKey=" + api_key

                        if sat_id not in tle_data:
                            satellite_data_request = requests.get(n2yo_endpoint)
                            satellite_data = satellite_data_request.json()
                            satellite_tle = satellite_data["tle"]
                            if satellite_data_request.status_code == 200 and satellite_tle != "":
                                tle_data[sat_id] = satellite_tle
                            else:
                                tle_data[sat_id] = None

                        if tle_data[sat_id] is not None:
                            tle = tle_data[sat_id].split(sep="\r\n")
                            satellite["line1"] = tle[0]
                            satellite["line2"] = tle[1]

                            # Attach estimatedTravelTime to each satellite and obtain weather details in that specific location
                            satellite["travelTime"], satellite["weatherConditions"] = \
                                calculate_travel_time_and_weather_details(satellite, target_location, event_timestamp, subarea_parameters)

                            satellites.append(satellite)

                subarea_ranking = rank_satellites(subarea_parameters, event_type, satellites)

                rankings.append({
                    "centroid": {"lat": lat, "lon": lon, "alt": alt},
                    "ranking": copy.deepcopy(subarea_ranking),
                    "geometry": {"coordinates": copy.deepcopy(polygon), "type": "Polygon"}              
                })

            print(rankings)
            return copy.deepcopy(rankings)
        else:
            print("Empty reply: no events")








