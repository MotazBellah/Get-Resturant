import httplib2 # To use HTTP verbs
import json # convert python objects to a serialized JSON

def getGeocodeLocation(inputString):
    ''' Take an input string, that is a name of place we want to get the coordinates for. '''

    google_api_key = 'AIzaSyCAhZM8b4VE27t3Kl_4RAWMKCk7Z-xtTng' # Google API
    locationString = inputString.replace(" ", "+") # replace spaces with `+` sor the server can read it correctly
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'%(locationString, google_api_key))
    h = httplib2.Http() # create Http class
    response, content = h.request(url, 'GET')
    result = json.loads(contnet) # Formate the content to json format
    return result
