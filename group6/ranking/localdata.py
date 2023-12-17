from enum import Enum

external_API_enabled = True

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
        "id": "27424",
        "apiName": "https://planetarycomputer.microsoft.com/api/stac/v1",
        "travelTime": "",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.VOLCANIC_ERUPTION, eventTypes.STORM],
        "visibility_threshold": 0.7,    
        "spatialResolution": 250,
        "temporalResolution": 2, #in days
        "swathWidth": 2.330, #in km
        "orbitDuration": "76000", #should be in seconds - It could be found using tle.period
        "worksDuringNight": True, 
        "worksDuringDay": True, 
        "price": 6,
        "dataQualityRating": 10
    },
    {   
        "family": "Modis",
        "name": "Terra",
        "id": "25994",
        "apiName": "https://planetarycomputer.microsoft.com/api/stac/v1",
        "travelTime": "",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.VOLCANIC_ERUPTION, eventTypes.STORM],
        "visibility_threshold": 0.85,    
        "spatialResolution": 250,
        "temporalResolution": 2, #in days
        "swathWidth": 2330, #in km
        "orbitDuration": "", #should be in seconds - It could be found using tle.period
        "worksDuringNight": False,
        "worksDuringDay": True, 
        "price": 6, 
        "dataQualityRating": 10
    },
    {   
        "family": "Sentinel",
        "name": "Sentinel-1A",
        "id": "39634",
        "apiName": "https://planetarycomputer.microsoft.com/api/stac/v1",
        "travelTime": "",
        "eventTypes": [eventTypes.FLOOD, eventTypes.EARTHQUAKE, eventTypes.OIL_SPILL],
        "visibility_threshold": 1,
        "spatialResolution": 5,
        "temporalResolution": 12, #in days
        "swathWidth": 250, #km
        "orbitDuration": "", #with the function
        "worksDuringNight": True, 
        "worksDuringDay": True, 
        "price": 0, 
        "dataQualityRating": 10
    },
    {   
        "family": "Sentinel",
        "name": "Sentinel-5P",
        "id": "40697",
        "apiName": "https://planetarycomputer.microsoft.com/api/stac/v1",
        "travelTime": "",
        "eventTypes": [eventTypes.FIRE, eventTypes.FLOOD, eventTypes.VOLCANIC_ERUPTION, eventTypes.OIL_SPILL],
        "visibility_threshold": 0.9,
        "spatialResolution": 10,
        "temporalResolution": 5, #in days
        "swathWidth": 290,
        "orbitDuration": "", #with the function
        "worksDuringNight": False, 
        "worksDuringDay": True, 
        "price": 0,
        "dataQualityRating": 10
    },
    {
        "family": "Sentinel",
        "name": "Sentinel-3A",
        "id": "41335",
        "apiName": "https://planetarycomputer.microsoft.com/api/stac/v1",
        "travelTime": "",
        "eventTypes": [eventTypes.STORM, eventTypes.TSUNAMI],
        "visibility_threshold": 0.9,
        "spatialResolution": 300,
        "temporalResolution": 2, #in days
        "swathWidth": 1270,
        "orbitDuration": "", #with the function
        "worksDuringNight": True,
        "worksDuringDay": True, 
        "price": 0,
        "dataQualityRating": 10
    },
    {
        "family": "Landsat",
        "name": "Landsat-8",
        "id": "39084",
        "apiName": "https://planetarycomputer.microsoft.com/api/stac/v1",
        "travelTime": "",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.VOLCANIC_ERUPTION],
        "visibility_threshold": 0.7,
        "spatialResolution": 15,
        "temporalResolution": 16, #in days
        "swathWidth": 185,
        "orbitDuration": "", #with the function
        "worksDuringNight": False,
        "worksDuringDay": True, 
        "price": 0,
        "dataQualityRating": 10
    },
    {
        "family": "Eros",
        "name": "EOS-Aura", #Eros-B
        "id": "29079",
        "apiName": "https://apollomapping.com/buy-imagery",
        "travelTime": "",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.OIL_SPILL],
        "visibility_threshold": 0.7,
        "spatialResolution": 0.7,
        "temporalResolution": 3, #in days
        "swathWidth": 12,
        "orbitDuration": "", #with the function
        "worksDuringNight": False,
        "worksDuringDay": True, 
        "price": 6,
        "dataQualityRating": 10
    },
    {
        "family": "Planet",
        "name": "Skysat-17",
        "id": "39418",
        "apiName": "https://www.planet.com/contact-sales/",
        "travelTime": "",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.EARTHQUAKE],
        "visibility_threshold": 0.9,
        "spatialResolution": 0.75,
        "temporalResolution": 1, #in days 
        "swathWidth": 16,
        "orbitDuration": "", #with the function
        "worksDuringNight": False, 
        "worksDuringDay": True, 
        "price": 14,
        "dataQualityRating": 10
    },
    {   
        "family": "Maxar",
        "name": "NOAA-16", #WORLDVIEW-1 (WV-1)"
        "id": "32060",
        "apiName": "https://securewatch.maxar.com/mapservice",
        "travelTime": "",
        "eventTypes": [eventTypes.EARTHQUAKE, eventTypes.FLOOD, eventTypes.FIRE, eventTypes.OIL_SPILL, eventTypes.TSUNAMI],
        "visibility_threshold": 0.3,
        "spatialResolution": 0.5,
        "temporalResolution": 1.7, #TODO .7?
        "swathWidth": 17.6,
        "orbitDuration": "", #with the function
        "worksDuringNight": False, 
        "worksDuringDay": True, 
        "price": 20,
        "dataQualityRating": 10
    },
    {
        "family": "Airbus",
        "name": "ONEWEB-0066",
        "id": "45424",
        "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive",
        "travelTime": "",
        "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
        "visibility_threshold": 0.3,
        "spatialResolution": 0.5,
        "temporalResolution": 1, #in days
        "swathWidth": 60,
        "orbitDuration": "", #with the function
        "worksDuringNight": True, 
        "worksDuringDay": True, 
        "price": 12.5,
        "dataQualityRating": 10
    },


    {
        "family": "Planet",
        "name": "SKYSAT-18",
        "id": "40072",
        "apiName": "https://www.planet.com/contact-sales/",
        "travelTime": "",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.EARTHQUAKE],
        "visibility_threshold": 0.9,
        "spatialResolution": 0.75,
        "temporalResolution": 1, #in days
        "swathWidth": 16, 
        "orbitDuration": "", #with the function
        "worksDuringNight": False,
        "worksDuringDay": True,
        "price": 14,
        "dataQualityRating": 10
    },
    {   
        "family": "Planet",
        "name": "SKYSAT-1",
        "id": "41601",
        "apiName": "https://www.planet.com/contact-sales/",
        "travelTime": "",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.EARTHQUAKE],
        "visibility_threshold": 0.85,
        "spatialResolution": 1,
        "temporalResolution": 1, #in days
        "swathWidth": 10, 
        "orbitDuration": "", #with the function
        "worksDuringNight": False, 
        "worksDuringDay": True,
        "price": 14,
        "dataQualityRating": 10
    },
    {
        "family": "Planet",
        "name": "SKYSAT-2",
        "id": "41771",
        "apiName": "https://www.planet.com/contact-sales/",
        "travelTime": "",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.EARTHQUAKE],
        "visibility_threshold": 0.85,
        "spatialResolution": 1,
        "temporalResolution": 1, #in days
        "swathWidth": 10, 
        "orbitDuration": "", #with the function
        "worksDuringNight": False,
        "worksDuringDay": True,
        "price": 14,
        "dataQualityRating": 10
    },
    {
        "family": "Planet",
        "name": "SKYSAT-13",
        "id": "43802",
        "apiName": "https://www.planet.com/contact-sales/",
        "travelTime": "",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.EARTHQUAKE],
        "visibility_threshold": 0.85,
        "spatialResolution": 1,
        "temporalResolution": 1, #in days
        "swathWidth": 16, 
        "orbitDuration": "", #with the function
        "worksDuringNight": False,
        "worksDuringDay": True,
        "price": 14,
        "dataQualityRating": 10
    },
    {
        "family": "Planet",
        "name": "SKYSAT-14",
        "id": "45788",
        "apiName": "https://www.planet.com/contact-sales/",
        "travelTime": "",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.EARTHQUAKE],
        "visibility_threshold": 0.85,
        "spatialResolution": 1,
        "temporalResolution": 1, #in days
        "swathWidth": 16, 
        "orbitDuration": "", #with the function
        "worksDuringNight": False,
        "worksDuringDay": True,
        "price": 14,
        "dataQualityRating": 10
    },
    {
        "family": "Planet",
        "name": "SKYSAT-16",
        "id": "45789",
        "apiName": "https://www.planet.com/contact-sales/",
        "travelTime": "",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.EARTHQUAKE],
        "visibility_threshold": 0.85,
        "spatialResolution": 1,
        "temporalResolution": 1, #in days
        "swathWidth": 16, 
        "orbitDuration": "", #with the function
        "worksDuringNight": False,
        "worksDuringDay": True,
        "price": 14,
        "dataQualityRating": 10
    },
    {
        "family": "Planet",
        "name": "SKYSAT-15",
        "id": "45790",
        "apiName": "https://www.planet.com/contact-sales/",
        "travelTime": "",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.EARTHQUAKE],
        "visibility_threshold": 0.85,
        "spatialResolution": 1,
        "temporalResolution": 1, #in days
        "swathWidth": 16, 
        "orbitDuration": "", #with the function
        "worksDuringNight": False,
        "worksDuringDay": True,
        "price": 14,
        "dataQualityRating": 10
    },
    {
        "family": "Planet",
        "name": "SKYSAT-5",
        "id": "41772",
        "apiName": "https://www.planet.com/contact-sales/",
        "travelTime": "",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.EARTHQUAKE],
        "visibility_threshold": 0.85,
        "spatialResolution": 1,
        "temporalResolution": 1, #in days
        "swathWidth": 16, 
        "orbitDuration": "", #with the function
        "worksDuringNight": False,
        "worksDuringDay": True,
        "price": 14,
        "dataQualityRating": 10
    },
    {
        "family": "Planet",
        "name": "SKYSAT-3",
        "id": "41774",
        "apiName": "https://www.planet.com/contact-sales/",
        "travelTime": "",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.EARTHQUAKE],
        "visibility_threshold": 0.85,
        "spatialResolution": 1,
        "temporalResolution": 1, #in days
        "swathWidth": 16, 
        "orbitDuration": "", #with the function
        "worksDuringNight": True,
        "worksDuringDay": True,
        "price": 14,
        "dataQualityRating": 10
    },
    {
        "family": "Planet",
        "name": "SKYSAT-11",
        "id": "42987",
        "apiName": "https://www.planet.com/contact-sales/",
        "travelTime": "",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.EARTHQUAKE],
        "visibility_threshold": 0.85,
        "spatialResolution": 1,
        "temporalResolution": 1, #in days
        "swathWidth": 16, 
        "orbitDuration": "", #with the function
        "worksDuringNight": False,
        "worksDuringDay": True,
        "price": 14,
        "dataQualityRating": 10
    },
    {
        "family": "Planet",
        "name": "SKYSAT-10",
        "id": "42988",
        "apiName": "https://www.planet.com/contact-sales/",
        "travelTime": "",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.EARTHQUAKE],
        "visibility_threshold": 0.85,
        "spatialResolution": 1,
        "temporalResolution": 1, #in days
        "swathWidth": 16, 
        "orbitDuration": "", #with the function
        "worksDuringNight": False, #and also during day
        "worksDuringDay": True,
        "price": 14,
        "dataQualityRating": 10
    },
    {
        "family": "Planet",
        "name": "SKYSAT-9",
        "id": "42989",
        "apiName": "https://www.planet.com/contact-sales/",
        "travelTime": "",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.EARTHQUAKE],
        "visibility_threshold": 0.85,
        "spatialResolution": 1,
        "temporalResolution": 1, #in days
        "swathWidth": 16, 
        "orbitDuration": "", #with the function
        "worksDuringNight": False,
        "worksDuringDay": True,
        "price": 14,
        "dataQualityRating": 10
    },
    {
        "family": "Planet",
        "name": "SKYSAT-8",
        "id": "42990",
        "apiName": "https://www.planet.com/contact-sales/",
        "travelTime": "",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.EARTHQUAKE],
        "visibility_threshold": 0.85,
        "spatialResolution": 1,
        "temporalResolution": 1, #in days
        "swathWidth": 16, 
        "orbitDuration": "", #with the function
        "worksDuringNight": False,
        "worksDuringDay": True,
        "price": 14,
        "dataQualityRating": 10
    },
    {
        "family": "Planet",
        "name": "SKYSAT-7",
        "id": "42991",
        "apiName": "https://www.planet.com/contact-sales/",
        "travelTime": "",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.EARTHQUAKE],
        "visibility_threshold": 0.85,
        "spatialResolution": 1,
        "temporalResolution": 1, #in days
        "swathWidth": 16, 
        "orbitDuration": "", #with the function
        "worksDuringNight": False,
        "worksDuringDay": True,
        "price": 14,
        "dataQualityRating": 10
    },
    {
        "family": "Planet",
        "name": "SKYSAT-6",
        "id": "42992",
        "apiName": "https://www.planet.com/contact-sales/",
        "travelTime": "",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.EARTHQUAKE],
        "visibility_threshold": 0.85,
        "spatialResolution": 1,
        "temporalResolution": 1, #in days
        "swathWidth": 16, 
        "orbitDuration": "", #with the function
        "worksDuringNight": False, 
        "worksDuringDay": True,
        "price": 14,
        "dataQualityRating": 10
    },
    {
        "family": "Planet",
        "name": "SKYSAT-C12",
        "id": "43797",
        "apiName": "https://www.planet.com/contact-sales/",
        "travelTime": "",
        "eventTypes": [eventTypes.FLOOD, eventTypes.FIRE, eventTypes.EARTHQUAKE],
        "visibility_threshold": 0.85,
        "spatialResolution": 1,
        "temporalResolution": 1, #in days
        "swathWidth": 16, 
        "orbitDuration": "", #with the function
        "worksDuringNight": False, 
        "worksDuringDay": True,
        "price": 14,
        "dataQualityRating": 10
    },
    {
        "family": "Airbus",
        "name": "ONEWEB-0305",
        "id": "70305",
        "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive   ",
        "travelTime": "",
        "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
        "visibility_threshold": 0.2,
        "spatialResolution": 0.5,
        "temporalResolution": 1, #in days
        "swathWidth": 16,
        "orbitDuration": "", #with the function
        "worksDuringNight": True,
        "worksDuringDay": True,
        "price": 12.5,
        "dataQualityRating": 10
    },
    {
        "family": "Airbus",
        "name": "ONEWEB-0432",
        "id": "50502",
        "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive",
        "travelTime": "",
        "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
        "visibility_threshold": 0.3,
        "spatialResolution": 0.5,
        "temporalResolution": 1, #in days
        "swathWidth": 16,
        "orbitDuration": "", #with the function
        "worksDuringNight": True,
        "worksDuringDay": True,
        "price": 12.5,
        "dataQualityRating": 10
    },
    {
        "family": "Airbus",
        "name": "ONEWEB-0058",
        "id": "45161",
        "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive",
        "travelTime": "",
        "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
        "visibility_threshold": 0.4,
        "spatialResolution": 0.5,
        "temporalResolution": 1, #in days
        "swathWidth": 16,
        "orbitDuration": "", #with the function
        "worksDuringNight": True,
        "worksDuringDay": True,
        "price": 12.5,
        "dataQualityRating": 10
    },
    {
        "family": "Airbus",
        "name": "ONEWEB-0303",
        "id": "70303",
        "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive",
        "travelTime": "",
        "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
        "visibility_threshold": 0.5,
        "spatialResolution": 0.5,
        "temporalResolution": 1, #in days
        "swathWidth": 16,
        "orbitDuration": "", #with the function
        "worksDuringNight": True,
        "worksDuringDay": True,
        "price": 12.5,
        "dataQualityRating": 10
    },
    {
        "family": "Airbus",
        "name": "ONEWEB-0107",
        "id": "48048",
        "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive",
        "travelTime": "",
        "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
        "visibility_threshold": 0.6,
        "spatialResolution": 0.5,
        "temporalResolution": 1, #in days
        "swathWidth": 16,
        "orbitDuration": "", #with the function
        "worksDuringNight": True,
        "worksDuringDay": True,
        "price": 12.5,
        "dataQualityRating": 10
    },
    {
        "family": "Airbus",
        "name": "ONEWEB-0053",
        "id": "45157",
        "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive",
        "travelTime": "",
        "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
        "visibility_threshold": 0.7,
        "spatialResolution": 0.5,
        "temporalResolution": 1, #in days
        "swathWidth": 16,
        "orbitDuration": "", #with the function
        "worksDuringNight": True,
        "worksDuringDay": True,
        "price": 12.5,
        "dataQualityRating": 10
    },
    {
        "family": "Airbus",
        "name": "ONEWEB-0032",
        "id": "45141",
        "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive",
        "travelTime": "",
        "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
        "visibility_threshold": 0.8,
        "spatialResolution": 0.5,
        "temporalResolution": 1, #in days
        "swathWidth": 16,
        "orbitDuration": "", #with the function
        "worksDuringNight": True,
        "worksDuringDay": True,
        "price": 12.5,
        "dataQualityRating": 10
    },
    {
        "family": "Airbus",
        "name": "ONEWEB-0012",
        "id": "44057",
        "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive",
        "travelTime": "",
        "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
        "visibility_threshold": 0.9,
        "spatialResolution": 0.5,
        "temporalResolution": 1, #in days
        "swathWidth": 16,
        "orbitDuration": "", #with the function
        "worksDuringNight": True,
        "worksDuringDay": True,
        "price": 12.5,
        "dataQualityRating": 10
    },
    {
        "family": "Airbus",
        "name": "ONEWEB-0063",
        "id": "45448",
        "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive",
        "travelTime": "",
        "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
        "visibility_threshold": 0.10,
        "spatialResolution": 0.5,
        "temporalResolution": 1, #in days
        "swathWidth": 16,
        "orbitDuration": "", #with the function
        "worksDuringNight": True,
        "worksDuringDay": True,
        "price": 12.5,
        "dataQualityRating": 10
    },
    {
        "family": "Airbus",
        "name": "ONEWEB-0064",
        "id": "45433",
        "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive",
        "travelTime": "",
        "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
        "visibility_threshold": 0.11,
        "spatialResolution": 0.5,
        "temporalResolution":  1,#in days
        "swathWidth": 16,
        "orbitDuration": "", #with the function
        "worksDuringNight": True,
        "worksDuringDay": True,
        "price": 12.5,
        "dataQualityRating": 10
    },
    {
        "family": "Airbus",
        "name": "ONEWEB-0054",
        "id": "45158",
        "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive",
        "travelTime": "",
        "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
        "visibility_threshold": 0.12,
        "spatialResolution": 0.5,
        "temporalResolution": 1, #in days
        "swathWidth": 16,
        "orbitDuration": "", #with the function
        "worksDuringNight": True,
        "worksDuringDay": True,
        "price": 12.5,
        "dataQualityRating": 10
    },
    {
        "family": "Airbus",
        "name": "ONEWEB-0033",
        "id": "45142",
        "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive",
        "travelTime": "",
        "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
        "visibility_threshold": 0.13,
        "spatialResolution": 0.5,
        "temporalResolution": 1, #in days
        "swathWidth": 16,
        "orbitDuration": "", #with the function
        "worksDuringNight": True,
        "worksDuringDay": True,
        "price": 12.5,
        "dataQualityRating": 10
    },
    {
        "family": "Airbus",
        "name": "ONEWEB-0010",
        "id": "44058",
        "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive",
        "travelTime": "",
        "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
        "visibility_threshold": 0.14,
        "spatialResolution": 0.5,
        "temporalResolution": 1, #in days
        "swathWidth": 16,
        "orbitDuration": "", #with the function
        "worksDuringNight": True,
        "worksDuringDay": True,
        "price": 12.5,
        "dataQualityRating": 10
    },
    {
        "family": "Airbus",
        "name": "ONEWEB-0019",
        "id": "45449",
        "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive",
        "travelTime": "",
        "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
        "visibility_threshold": 0.15,
        "spatialResolution": 0.5,
        "temporalResolution": 1, #in days
        "swathWidth": 16,
        "orbitDuration": "", #with the function
        "worksDuringNight": True,
        "worksDuringDay": True,
        "price": 12.5,
        "dataQualityRating": 10
    },
    {
        "family": "Airbus",
        "name": "ONEWEB-0018",
        "id": "45434",
        "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive",
        "travelTime": "",
        "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
        "visibility_threshold": 0.16,
        "spatialResolution": 0.5,
        "temporalResolution": 1, #in days
        "swathWidth": 16,
        "orbitDuration": "", #with the function
        "worksDuringNight": True,
        "worksDuringDay": True,
        "price": 12.5,
        "dataQualityRating": 10
    },
    {
        "family": "Airbus",
        "name": "ONEWEB-0056",
        "id": "45159",
        "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive",
        "travelTime": "",
        "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
        "visibility_threshold": 0.17,
        "spatialResolution": 0.5,
        "temporalResolution": 1, #in days
        "swathWidth": 16,
        "orbitDuration": "", #with the function
        "worksDuringNight": True,
        "worksDuringDay": True,
        "price": 12.5,
        "dataQualityRating": 10
    },
    {
        "family": "Airbus",
        "name": "ONEWEB-0035",
        "id": "45143",
        "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive",
        "travelTime": "",
        "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
        "visibility_threshold": 0.18,
        "spatialResolution": 0.5,
        "temporalResolution": 1, #in days
        "swathWidth": 16,
        "orbitDuration": "", #with the function
        "worksDuringNight": True,
        "worksDuringDay": True,
        "price": 12.5,
        "dataQualityRating": 10
    },
    {
        "family": "Airbus",
        "name": "ONEWEB-0008",
        "id": "44059",
        "apiName": "https://www.intelligence-airbusds.com/imagery/oneatlas/order-form/?oneatlas_subscription_type_of_inquiry=Pleiades_Neo_tasking_archive",
        "travelTime": "",
        "eventTypes": [eventTypes.VOLCANIC_ERUPTION, eventTypes.FLOOD, eventTypes.FIRE],
        "visibility_threshold": 0.19,
        "spatialResolution": 0.5,
        "temporalResolution": 1, #in days
        "swathWidth": 16,
        "orbitDuration": "", #with the function
        "worksDuringNight": True,
        "worksDuringDay": True,
        "price": 12.5,
        "dataQualityRating": 10
    },
    {
        "family": "Maxar",
        "name": "WORLDVIEW-2 (WV-2)",
        "id": "35946",
        "apiName": "https://securewatch.maxar.com/mapservice",
        "travelTime": "",
        "eventTypes": [eventTypes.EARTHQUAKE, eventTypes.FLOOD, eventTypes.FIRE, eventTypes.OIL_SPILL, eventTypes.TSUNAMI],
        "visibility_threshold": 0.3,
        "spatialResolution": 0.46,
        "temporalResolution": 1.7, #in days
        "swathWidth": 16.4,
        "orbitDuration": "", #with the function
        "worksDuringNight": False,
        "worksDuringDay": True,
        "price": 20,
        "dataQualityRating": 10
    },
    {
        "family": "Maxar",
        "name": "WORLDVIEW-3 (WV-3)",
        "id": "40115",
        "apiName": "https://securewatch.maxar.com/mapservice",
        "travelTime": "",
        "eventTypes": [eventTypes.EARTHQUAKE, eventTypes.FLOOD, eventTypes.FIRE, eventTypes.OIL_SPILL, eventTypes.TSUNAMI],
        "visibility_threshold": 0.4,
        "spatialResolution": 0.31,
        "temporalResolution": 1.7, #in days
        "swathWidth": 13.1,
        "orbitDuration": "", #with the function
        "worksDuringNight": False,
        "worksDuringDay": True,
        "price": 20,
        "dataQualityRating": 10
    },
    {
        "family": "Maxar",
        "name": "WORLDVIEW-4",
        "id": "41848",
        "apiName": "https://securewatch.maxar.com/mapservice",
        "travelTime": "",
        "eventTypes": [eventTypes.EARTHQUAKE, eventTypes.FLOOD, eventTypes.FIRE, eventTypes.OIL_SPILL, eventTypes.TSUNAMI],
        "visibility_threshold": 0.4,
        "spatialResolution": 0.31,
        "temporalResolution": 1.7, #in days
        "swathWidth": 13.1,
        "orbitDuration": "", #with the function
        "worksDuringNight": False,
        "worksDuringDay": True,
        "price": 20,
        "dataQualityRating": 10
    }
]
