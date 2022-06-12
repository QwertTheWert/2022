import requests

response = requests.get("http://data.fixer.io/api/latest?access_key=ecfc86372fe5de2ac47f391508d3d4e2")


print(response.text)