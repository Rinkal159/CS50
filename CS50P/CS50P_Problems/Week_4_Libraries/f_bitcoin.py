import requests
import sys

try:
    number = float(sys.argv[1])
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=c2f63d6c8f526c3dbd436ea6a963ee531abf208c19be2c4b2a130170b9a23e11")
    price = float(response.json()["data"]["priceUsd"])
    print(f"${(number * price):,.4f}")
except requests.RequestException:
    sys.exit()
except ValueError:
    sys.exit("Command-line argument is not a number")
except IndexError:
    sys.exit("Missing command-line argument")