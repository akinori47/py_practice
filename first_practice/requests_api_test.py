# testing free api from db-ip.com
# works good
import requests

response = requests.get('http://api.db-ip.com/v2/free/81.30.196.90/countryName').text
print(response)