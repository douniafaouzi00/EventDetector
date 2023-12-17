from pyorbital.orbital import Orbital
from ranking.localdata import external_API_enabled
from ranking.utils import get_timestamp, interpolate

from ranking.utils import HOURS_PER_DAY
from ranking.utils import MINUTES_PER_HOUR
from ranking.utils import SECONDS_PER_MINUTE
SLACK = 1

#TODO Review REQUIRES

# REQUIRES
# satelliteData
## key1: name
## key2: line1
## key3: line2
## key4: minimumSnapshotArea
## key5: orbitDuration

# targetLocation - API request to group 5 to obtain the event location
## key1: lat
## key2: lon
## key3: alt

# ENSURES
## The arrival time (UTC) if the satellite is going to cross the target location
## The weather conditions in the target location at the time of arrival
def calculate_travel_time_and_weather_details(satellite_data, target_location, timestamp, subarea_parameters):
    # Specify the TLE data for the satellite
    line1 = satellite_data["line1"] if external_API_enabled == True else None
    line2 = satellite_data["line2"] if external_API_enabled == True else None

    tle = Orbital(
        satellite_data["name"],
        None,
        line1,
        line2
    )

    # Specify the desired location
    lat = float(target_location["lat"]) # New York City latitude
    lon = float(target_location["lon"]) # New York City longitude
    alt = float(target_location["alt"]) # Altitude in km

    # Calculate the time required for the satellite to reach the specified location
    #dt = 300  # Time interval in seconds - TODO What is the LSB we want to use? - USED FOR A DIFFERENT ALGO, read below
    time = timestamp
    temporal_resolution = float(satellite_data["temporalResolution"])

    next_pass_list = tle.get_next_passes(time, int(temporal_resolution * HOURS_PER_DAY + SLACK), lon, lat, alt, 1)

    #First element of the array as it's the closest in time; third of the tuple as it's the maximum-distance position
    arrival_timestamp = next_pass_list[0][2]
    delta_arrival_event = arrival_timestamp - time

    first_available_forecast_time = get_timestamp(subarea_parameters["time"][0])

    delta_arrival_forecast = arrival_timestamp - first_available_forecast_time

    #Instead of doing a table lookup, we exploit the regularity of the table structure.
    #ASSUMPTION: that regularity is maintained.
    last_available_forecast_time = get_timestamp(subarea_parameters["time"][-1])
    if arrival_timestamp <= last_available_forecast_time:
        left_offset = int(delta_arrival_forecast.total_seconds() / MINUTES_PER_HOUR / SECONDS_PER_MINUTE)
    else:
        left_offset = subarea_parameters["time"].count() - 2 #It's a stopgap solution for low-availability-of-data environments
    right_offset = left_offset + 1


    delta_arrival_closest = arrival_timestamp - get_timestamp(subarea_parameters["time"][left_offset])
    weight = delta_arrival_closest.total_seconds() / MINUTES_PER_HOUR / SECONDS_PER_MINUTE
    visibility, is_day = populate_weather_params(subarea_parameters, left_offset, right_offset, weight)

    return delta_arrival_event.total_seconds(), {"visibility": visibility, "isDay": is_day}


def populate_weather_params(subarea_parameters, left_offset, right_offset, weight):
    cloudiness_weight = 0.8
    rain_weight = 0.2
    cloudcover = interpolate(float(subarea_parameters["cloudcover"][left_offset]),
                             float(subarea_parameters["cloudcover"][right_offset]), weight) / 100 * cloudiness_weight
    rain = interpolate(float(subarea_parameters["cloudcover"][left_offset]),
                       float(subarea_parameters["cloudcover"][right_offset]), weight) / 100 * rain_weight
    visibility = 1 - (cloudcover + rain)
    is_day = True if subarea_parameters["is_day"][left_offset] == 1 else False

    return visibility, is_day


    '''
    now = time

    #Currently using built-in get_next_passes library function 
    orbit_duration = float(satellite_data["orbitDuration"])
    dt_per_orbit = orbit_duration / dt
    minimum_snapshot_area = float(satellite_data["minimumSnapshotArea"])

    while dt_per_orbit > 0:
        
        pos, _ = tle.get_position(time)
        dist = pos.distance_from(lat, lon, alt) #TODO check format. Is it comparable with snapshot_area?
        # Here, we should consider the area size too. If it's too large, there could be some pieces missing
        if dist < sqrt(minimum_snapshot_area):  # If satellite is within 5 km of the location, break out of the loop - TODO the threshold is selected by picking the square root of the minimum snapshot area
            return time - now
        time += timedelta(seconds=dt)
        dt_per_orbit -= 1

    # Done like this because of the formula in the rating algorithm: 10(1 - delta/orbitDuration) -> 0 if no match is found
    return orbit_duration
    '''



