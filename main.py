# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hakahmed <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/09 23:03:23 by hakahmed          #+#    #+#              #
#    Updated: 2023/03/10 02:38:13 by hakahmed         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import requests
import json
import pandas as pd

headers = {

    "Authorization": "Bearer dcd81527930ed2fd82dd7c55e7e3b62ffddeff16a15f7fff8a24f6a956aa2a45"
}

inp = input("Login: ")
url = f"https://api.intra.42.fr/v2/users?filter[login]={inp}"

response = requests.get(url, headers=headers)

js = json.loads(response.text)

df = pd.DataFrame(js)
print(df)
userid = js[0]["id"]

with open("bro.jpg", "wb") as f:
    r = requests.get(js[0]["image"]["link"])
    f.write(r.content)


url = f"https://api.intra.42.fr/v2/users/{userid}/projects_users"

response = requests.get(url, headers=headers)
#print(response.text)
