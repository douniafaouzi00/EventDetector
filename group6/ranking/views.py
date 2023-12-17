from django.shortcuts import render

from django.http import HttpResponse
import json


from django.views.decorators.csrf import csrf_exempt

#Local imports
from ranking.utils import parse_file, parse_body

from ranking.main import create_subareas_ranking

NUMBER_OF_SUBAREAS = 3

event_aoi_rankings = []

#For testing purposes: the GET returns a page that can perform a POST request with a specifically-crafted body
file_data = parse_file()
get_body_object = [
    dict(list(file_data[0].items())[:NUMBER_OF_SUBAREAS]),
    file_data[1]
]
@csrf_exempt
def index(request):
    #TODO Ideally, if parameters are specified, we should return the ranking if available instead of a page - add check
    if request.method == "GET":
        return HttpResponse(
            "<body>" +
            "<script>var myFunction = function() {" +
                "fetch('http://127.0.0.1:8000/ranking/', " +
                "{method: 'POST', mode: 'no-cors', headers: {'Content-Type': 'application/json'}, " +
                "body: JSON.stringify(" +
                    str(get_body_object) + ")})" +
                ".then(response => response.json())" +
                ".then(data => console.log(data))" +
                ".catch(error => console.error(error))" +
                "}" +
            "</script>"
            "<button onclick=myFunction()>Click to POST</button></body>"
        )
    if request.method == "POST":
        subareas = parse_body(request.body)
        event_id = subareas[1]["features"][0]["properties"]["event_id"]
        aoi_id = subareas[1]["features"][0]["properties"]["AoiID"]

        #Input checks on query parameters
        check_outcome = check_input(aoi_id, event_id)

        reply = {}
        if check_outcome == None:

            output_ranking = []
            ranking_exists = False
            for ranking in event_aoi_rankings:
                if ranking["event_id"] == event_id and ranking["aoi_id"] == aoi_id:
                    ranking_exists = True
                    output_ranking = ranking
                    break


            if not ranking_exists:
                subareas_ranking = create_subareas_ranking(subareas)
                output_ranking = {
                    "ranking_ord": "desc",
                    'event_id': event_id,
                    'aoi_id': aoi_id,
                    'subareas': subareas_ranking
                }

                event_aoi_rankings.append(output_ranking)

            reply['ranking'] = output_ranking
        else:
            reply = check_outcome

        #TODO Return JSON, not HTTP
        return HttpResponse(json.dumps(reply))

def check_input(aoi_id, event_id):
    if int(aoi_id) < 1 or int(aoi_id) > 999:
        return "The provided ID tuple doesn't have the correct format: the aoi has not a correct id"

    event_id_sep = event_id.split(sep='-')
    if event_id_sep[0] != "gr1" and event_id_sep[0] != "gr2":
        return "The provided ID tuple doesn't have the correct format: the group is wrong"
    elif event_id_sep[1].isalpha() == False:
        return "The provided ID tuple doesn't have the correct format: the country is wrong"
    #elif validate_date(event_id_sep[2]) == False or validate_date(event_id_sep[3]) == False: TODO readd check after double-checking event_id
    #    return "The provided ID tuple doesn't have the correct format: the date-time is wrong"
    elif event_id_sep[4].isalpha() == False:
        return "The provided ID tuple doesn't have the correct format: the event type is wrong"

    return None

