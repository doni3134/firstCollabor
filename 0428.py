# Python3 샘플 코드 #


import requests

url = 'http://openapi.yeongdo.go.kr:8081/openapi-data/service/rest/tour/list'
params ={'serviceKey' : 'HWzXFwEzSKsXyCBuU%2BBLk3uJv55BoaGCH5zryyjxIdHAM9ripB7FjLzudGR2A7LMCQWoj1BEkPbsVWwrdfu4mA%3D%3D', 'numOfRows' : '', 'pageNo' : '', 'addr' : '', 'title' : '' }

response = requests.get(url, params=params)
print(response.content)