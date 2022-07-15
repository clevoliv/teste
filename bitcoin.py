import requests
import sys

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    obj = response.json()

    #print(json.dumps(response.json(), indent=2 ))

    if float(sys.argv[1]):
        print(f'${float(sys.argv[1])*obj["bpi"]["USD"]["rate_float"]:,.4f}')


except requests.RequestException:
    sys.exit("Missing arguments")
except ValueError:
    sys.exit("Command-line argument is not a number")
except IndexError:
    sys.exit("Missing Command-line arguments")