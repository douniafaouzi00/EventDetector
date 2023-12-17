from enum import Enum

NASA = True
class eventTypes(Enum):

    FLOOD = 1
    FIRE = 2
    VOLCANIC_ERUPTION = 3
    EARTHQUAKE = 4
    OIL_SPILL = 5
    STORM = 6
    TSUNAMI = 7
    

weights = {
    'timeliness': 10,
    'suitability_to_weather_type': 8,
    'suitability_to_time_of_the_day': 8,
    'suitability_to_event_type': 8,
    'spatial_resolution': 6,
    'frequency_of_update': 1,
    'price': 7,
    'data_quality': 3
}

master_satellites = [
    {
        "family": "Modis",
        "name": "Aqua",
        "id": "25994", #"27424",
        "apiName": "https://planetarycomputer.microsoft.com/api/stac/v1",
        "travelTime": "",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.VOLCANIC_ERUPTION],
        "visibility_threshold": 0.7,
        "spatialResolution": 250,
        "frequencyOfUpdate": 0.5,
        "minimumSnapshotArea": 100, #in km
        "orbitDuration": "",# found using tle.period, don't fill
        "worksDuringNight": True,
        "price": 10,
        "dataQualityRating": 1
    }
]
'''
    {
        "family": "Sentinel",
        "name": "Sentinel 1",
        "id": "",
        "apiName": "https://planetarycomputer.microsoft.com/api/stac/v1",
        "eventTypes": [eventTypes.FLOOD, eventTypes.EARTHQUAKE, eventTypes.OIL_SPILL],
        "visibility_threshold": 0,
        "spatialResolution": 5,
        "frequencyOfUpdate": 6,
        "minimumSnapshotArea": "",
        "orbitDuration": "",
        "worksDuringNight": True, #TODO add for others as well @Olmar
        "price": 0,
        "dataQualityRating": 1 #TODO 
    },
    {
        "family": "Sentinel",
        "name": "Sentinel 2",
        "id": "",
        "apiName": "https://planetarycomputer.microsoft.com/api/stac/v1",
        "eventTypes": [eventTypes.FIRE, eventTypes.FLOOD, eventTypes.VOLCANIC_ERUPTION, eventTypes.OIL_SPILL],
        "visibility_threshold": 0.9,
        "spatialResolution": 10,
        "frequencyOfUpdate": 5,
        "minimumSnapshotArea": "",
        "orbitDuration": "",
        "worksDuringNight": True, #TODO add for others as well @Olmar
        "price": 0,
        "dataQualityRating": 1 #TODO 
    },
    {
        "family": "Sentinel",
        "name": "Sentinel 3",
        "id": "",
        "apiName": "https://planetarycomputer.microsoft.com/api/stac/v1",
        "eventTypes": [eventTypes.STORM, eventTypes.TSUNAMI],
        "visibility_threshold": 0.9,
        "spatialResolution": 300,
        "frequencyOfUpdate": 1,
        "minimumSnapshotArea": "",
        "orbitDuration": "",
        "worksDuringNight": True, #TODO add for others as well @Olmar
        "price": 0,
        "dataQualityRating": 1 #TODO 
    },
    {
        "family": "Landsat",
        "name": "Landsat 8",
        "id": "",
        "apiName": "https://planetarycomputer.microsoft.com/api/stac/v1",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.VOLCANIC_ERUPTION],
        "visibility_threshold": 0.7,
        "spatialResolution": 15,
        "frequencyOfUpdate": 16,
        "minimumSnapshotArea": "",
        "orbitDuration": "",
        "worksDuringNight": True, #TODO add for others as well @Olmar
        "price": 0,
        "dataQualityRating": 1 #TODO 
    },
    {
        "family": "Planet",
        "name": "Planet",
        "id": "",
        "apiName": "https://www.planet.com/contact-sales/",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.STORM],
        "visibility_threshold": 0.2,
        "spatialResolution": 3.7,
        "frequencyOfUpdate": 1,
        "minimumSnapshotArea": "",
        "orbitDuration": "",
        "worksDuringNight": True, #TODO add for others as well @Olmar
        "price": 14,
        "dataQualityRating": 1 #TODO 
    },
    {
        "family": "Airbus",
        "name": "Airbus",
        "id": "",
        "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.VOLCANIC_ERUPTION],
        "visibility_threshold": 0.7,
        "spatialResolution": 0.5,
        "frequencyOfUpdate": 1,
        "minimumSnapshotArea": "",
        "orbitDuration": "",
        "worksDuringNight": True, #TODO add for others as well @Olmar
        "price": 12.5,
        "dataQualityRating": 1 #TODO 
    },
    {
        "family": "Eros-B",
        "name": "Eros-B",
        "id": "",
        "apiName": "https://apollomapping.com/buy-imagery",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.OIL_SPILL],
        "visibility_threshold": 0.7,
        "spatialResolution": 0.7,
        "frequencyOfUpdate": 4,
        "minimumSnapshotArea": "",
        "orbitDuration": "",
        "worksDuringNight": True, #TODO add for others as well @Olmar
        "price": 6,
        "dataQualityRating": 1 #TODO 
    },
    {
        "family": "Maxar",
        "name": "Maxar",
        "id": "",
        "apiName": "https://securewatch.maxar.com/mapservice",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.STORM],
        "visibility_threshold": 0.7,
        "spatialResolution": 0.3,
        "frequencyOfUpdate": 1,
        "minimumSnapshotArea": "",
        "orbitDuration": "",
        "worksDuringNight": True, #TODO add for others as well @Olmar
        "price": 20,
        "dataQualityRating": 1 #TODO 
    }

]
#TODO Remove comments when the list is ready
'''
