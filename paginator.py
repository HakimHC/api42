# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    paginator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hakahmed <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/10 00:50:08 by hakahmed          #+#    #+#              #
#    Updated: 2023/03/10 04:41:03 by hakahmed         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import requests
import time
import pandas as pd
import json
from pymongo import MongoClient
import ssl


client = MongoClient("mongodb+srv://hakimdb:FN9MDwiJi0WUZ7gl@cluster0.w3nu1yq.mongodb.net", ssl_cert_reqs=ssl.CERT_NONE)

db = client.kaki
collection = db.kaka
headers = {

    "Authorization": "Bearer eb58b4f1726af3e371a9c08a83acabea55f77dc4fab601c4a67d45f4bb834a5a"
}

i = 0 
while True:
    print(i)
    params = {
        "page": i
    }
    url =  "https://api.intra.42.fr/v2/campus/madrid/users"
    response = requests.get(url, headers=headers, params=params)
    if response.text == "[]":
        break
    js = json.loads(response.text)
    print(response)
    print(js)
    collection.insert_many(js)
    i += 1
    time.sleep(.5)
