import requests


S1 = "https://rinkeby-api.opensea.io/api/v1/asset/0x437e1c50b229c229b3e601767fed65242bec8490/"
S2 = "/?force_update=true"

for i in range(0,5):
    requests.get(S1 + str(i) + S2)
    