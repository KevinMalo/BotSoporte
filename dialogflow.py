import os.path
import sys
import json

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

CLIENT_ACCESS_TOKEN = 'af8f01865f994a5186d4ae0b0b250d11'


def main():
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    request.lang = 'es'  # optional, default value equal 'en'

    request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"

    request.query = "Hola"

    response = request.getresponse()

    json_parse = json.loads( response.read() ) 

    print (json_parse['result']['fulfillment']['speech'])


if __name__ == '__main__':
    main()