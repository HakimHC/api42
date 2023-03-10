# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    paginator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hakahmed <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/10 00:50:08 by hakahmed          #+#    #+#              #
#    Updated: 2023/03/10 02:17:59 by hakahmed         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import requests
import time
import pandas as pd
import json
from sqlalchemy import *
import sqlalchemy

headers = {

    "Authorization": "Bearer dcd81527930ed2fd82dd7c55e7e3b62ffddeff16a15f7fff8a24f6a956aa2a45"
}

conn_str = "postgresql://doadmin:AVNS_3ySmhXsce8tYzPfT5af@db-postgresql-fra1-53122-do-user-13725825-0.b.db.ondigitalocean.com:25060/defaultdb?sslmode=require"

engine = create_engine(conn_str)

with engine.connect() as conn:
    result = conn.execute('SELECT version()')
    print(result.fetchone())


i = 144 
df = pd.DataFrame()
while True:

    params = {
        "page": i
    }
    url =  "https://api.intra.42.fr/v2/campus/madrid/users"
    response = requests.get(url, headers=headers, params=params)
    if response.text == "[]":
        break
    js = json.loads(response.text)
    df = df.append(js, ignore_index=True)
    i += 1
    print(df)
    time.sleep(.5)

df = df[~df['email'].str.startswith('3b3')]
print(df)
