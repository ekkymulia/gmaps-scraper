import json

import requests

list_apartemen = [
# "Bintaro Park View",
# "Casa Grande Residences",
# "Cibubur Village",
# "Green Lake Sunter Tower 2",
# "Kemang Village",
#     "Westmark"
# "Mediterania Garden Residences 1",
# "Mediterania Garden Residences 2",
# "Royale Springhill Residence",
# "Seasons City",
# "Sentraland Cengkareng",
# "Sunter Icon",
# "The H Residence",
# "The Kuningan Place",
# "The Mansion at Dukuh Golf Kemayoran",
# "The Pakubuwono House",
# "Bintaro park view",
# "Aspen Residences di Fatmawati",
# "Gandaria Heights",
# "1Park Avenue",
# "1Park Residences",
# "Branz BSD",
# "Sky House BSD",
# "Casa de Parco BSD",
# "Permata Hijau Suites",
# "Taman Rasuna",
# "Daan Mogot City",
# "South Hills",
# "The Mansion Bougenville Kemayoran",
# "Denpasar Residences",
# "Bellagio Residence",
# "Newton Ciputra World 2",
# "Archies Sudirman",
"Cosmo Terrace",
# "Sahid sudirman residence",
# "Pavilion",
# "Pavilion",
# "Signature Park Grande",
# "Capitol Park Residence",
# "Essence Darmawangsa",
# "Pejagen Park Residence",
# "Nine Residence",
# "Royal Olive Residence",
# "Gardenia Boulevard",
# "Izzara",
# "Cervino Village",
#     "Wang Residence"
]

detail_list_apartemen = []
API_KEY = ""

for apartemen in list_apartemen:
    apartemen_formatted = apartemen.replace(" ", "%20")

    url = "" \
          f"https://maps.googleapis.com/maps/api/geocode/json?address=Apartemen%20{apartemen_formatted}&key={API_KEY}" \
          ""

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()

    cari_kelurahan = ""
    cari_kecamatan = ""
    for i in data['results'][0]['address_components']:
        if i['types'][0] == "administrative_area_level_3":
            cari_kecamatan = i['long_name']

        if i['types'][0] == "administrative_area_level_4":
            cari_kelurahan = i['long_name']

    detail_apartemen = {
        "nama": apartemen,
        "alamat": f"{data['results'][0]['formatted_address']}",
        "kecamatan": cari_kecamatan,
        "kelurahan": cari_kelurahan,
        "location": f"{data['results'][0]['geometry']['location']['lat']},{data['results'][0]['geometry']['location']['lng']}"
    }

    place_to_search_1 = [
        "hospital",
        "shopping_mall",
        "supermarket",
        "university",
        "school",
    ]

    excluded_place = [
        "Alfamart",
        "Indomaret"
    ]

    mall_list = []

    # search place and distance
    cleaned_place_data = []
    print("log1")
    for place in place_to_search_1:
        url = "" \
              f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={detail_apartemen['location']}&radius=7000&language=id&type={place}&key={API_KEY}" \
              ""

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        data = response.json()['results']
        filtered_data = []
        for data_place in data:
            try:
                if data_place['user_ratings_total'] > 100:
                    if not any(excluded in data_place['name'] for excluded in excluded_place):
                        filtered_data.append(data_place)
            except:
                continue

        # getting place distance
        cleaned_place_with_distance = []
        for filtered_place in filtered_data:
            filtered_place_location = f"{filtered_place['geometry']['location']['lat']},{filtered_place['geometry']['location']['lng']}"
            url = "" \
                  f"https://maps.googleapis.com/maps/api/directions/json?destination={filtered_place_location}&origin={detail_apartemen['location']}&key={API_KEY}" \
                  ""

            payload = {}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)
            data = response.json()['routes']

            if data[0]['legs'][0]['distance']['value'] < 1000:
                routes_distance = f"{data[0]['legs'][0]['distance']['value']} m"
            else:
                routes_distance = data[0]['legs'][0]['distance']['text']


            # try:
            #     fp_rating = filtered_place['rating']
            # except:
            #     fp_rating = 0

            cleaned_place = {
                "nama": filtered_place['name'],
                "rating": filtered_place['rating'],
                "location": f"{filtered_place['geometry']['location']['lat']},{filtered_place['geometry']['location']['lng']}",
                "user_ratings_total": filtered_place['user_ratings_total'],
                "routes_distance": routes_distance,
                "printed": f"{filtered_place['name']} - {filtered_place['rating']} - {filtered_place['user_ratings_total']} review ({routes_distance})"
            }
            if place == "shopping_mall":
                mall_list.append(cleaned_place)
            cleaned_place_with_distance.append(cleaned_place)
        print("log2")

        #append to cleaned_place_data
        cleaned_place_data.append({
            "type": place,
            "data": cleaned_place_with_distance
        })

    # search restaurant
    cleaned_restaurant_data = []
    print("log2")
    for mall in mall_list:
        url = "" \
              f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={mall['location']}&rankBy=distance&radius=500&language=id&type=restaurant&key={API_KEY}" \
              ""

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        data = response.json()['results']
        filtered_data = []
        for data_place in data:
            try:
                if data_place['user_ratings_total'] > 100:
                    filtered_data.append(
                        {
                            "nama": data_place['name'],
                            "rating": data_place['rating'],
                            "location": f"{data_place['geometry']['location']['lat']},{data_place['geometry']['location']['lng']}",
                            "user_ratings_total": data_place['user_ratings_total'],
                            "printed": f"{data_place['name']} - {data_place['rating']} - {data_place['user_ratings_total']} review"
                        }
                    )
            except:
                continue

        restaurant_data = {
            "shopping_mall": mall['nama'],
            "restaurants":  []
        }

        i=0
        for t in sorted(filtered_data, key=lambda d: d['user_ratings_total'], reverse=True):
           i+=1
           if i < 10:
               restaurant_data['restaurants'].append(t)
           else:
               break

        cleaned_restaurant_data.append(restaurant_data)

    keyword_list = [
        "Starbucks",
        "Ace Hardware",
        "Guardian",
        "Century",
        "Mc Donald's",
        "Electronic City",
        "Co Working Space",
        "Halte Transjakarta",
        "Kantor Kelurahan",
        "Kantor Kecamatan"
    ]

    special_keyword = [
        "Halte Transjakarta",
        "Kantor Kelurahan",
        "Kantor Kecamatan",
        "Co Working Space",
    ]

    # search by keywords
    print("log3")
    cleaned_keyword_data = []
    for keyword in keyword_list:
        if keyword == "Kantor Kelurahan":
            radius = "7000"
        else:
            radius = "1000"

        url = "" \
              f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword={keyword}&location={detail_apartemen['location']}&rankBy=distance&radius={radius}&language=id&key={API_KEY}" \
              ""

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        data = response.json()['results']
        filtered_data = []
        for data_place in data:
            try:
                if keyword in special_keyword:
                    filtered_place_location = f"{data_place['geometry']['location']['lat']},{data_place['geometry']['location']['lng']}"
                    url = "" \
                          f"https://maps.googleapis.com/maps/api/directions/json?destination={filtered_place_location}&origin={detail_apartemen['location']}&key={API_KEY}" \
                          ""
                    payload = {}
                    headers = {}
                    response = requests.request("GET", url, headers=headers, data=payload)
                    data = response.json()['routes']

                    if data[0]['legs'][0]['distance']['value'] < 1000:
                        routes_distance = f"{data[0]['legs'][0]['distance']['value']} m"
                    else:
                        routes_distance = data[0]['legs'][0]['distance']['text']

                    filtered_data.append(
                        {
                            "nama": data_place['name'],
                            "rating": data_place['rating'],
                            "location": f"{data_place['geometry']['location']['lat']},{data_place['geometry']['location']['lng']}",
                            "routes_distance": routes_distance,
                            "user_ratings_total": data_place['user_ratings_total'],
                            "printed": f"{data_place['name']} - {data_place['rating']} - {data_place['user_ratings_total']} review"
                        }
                    )
                else:
                    if data_place['user_ratings_total'] > 100:
                        filtered_data.append(
                            {
                                "nama": data_place['name'],
                                "rating": data_place['rating'],
                                "location": f"{data_place['geometry']['location']['lat']},{data_place['geometry']['location']['lng']}",
                                "user_ratings_total": data_place['user_ratings_total'],
                                "printed": f"{data_place['name']} - {data_place['rating']} - {data_place['user_ratings_total']} review"
                            }
                        )
            except:
                continue

        keyword_data = {
            "keyword": keyword,
            "data": []
        }
        print("log3a")
        i = 0
        if keyword in special_keyword:
            for t in sorted(filtered_data, key=lambda d: d['routes_distance']):
                i += 1
                if i < 16:
                    keyword_data['data'].append(t)
                else:
                    break
        else:
            for t in sorted(filtered_data, key=lambda d: d['user_ratings_total'], reverse=True):
                i += 1
                if i < 10:
                    keyword_data['data'].append(t)
                else:
                    break

        cleaned_keyword_data.append(keyword_data)

    # getting static transport distance
    keyword_st_list_distance = [
        "Bandara Soekarno Hatta",
        "Bandara Halim Perdana Kusuma",
        "Stasiun Gambir"
    ]
    cleaned_keyword_st_with_distance = []
    print("log4")
    for kld in keyword_st_list_distance:
        url = "" \
              f"https://maps.googleapis.com/maps/api/directions/json?destination={kld}&origin={detail_apartemen['location']}&key={API_KEY}" \
              ""

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        data = response.json()['routes']

        if data[0]['legs'][0]['distance']['value'] < 1000:
            routes_distance = f"{data[0]['legs'][0]['distance']['value']} m"
        else:
            routes_distance = data[0]['legs'][0]['distance']['text']

        cleaned_keyword_st_with_distance.append({
            "destination": kld,
            "routes_distance": routes_distance,
        })


    # get dynamic transport place and distance
    place_st_list_distance = [
        "train_station",
        "subway_station",
        "bus_station"
    ]
    cleaned_place_dy_with_distance = []
    print("log5")
    for place in place_st_list_distance:
        url = "" \
              f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={detail_apartemen['location']}&rankBy=distance&radius=6000&language=id&type={place}&key={API_KEY}" \
              ""

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        data = response.json()['results']
        filtered_data = []
        for data_place in data:
            try:
                if len(filtered_data) <= 3:
                    if data_place['user_ratings_total'] > 100:
                        filtered_data.append(data_place)
                else:
                    break
            except:
                continue

        # getting place distance
        cleaned_place_with_distance = []
        for filtered_place in filtered_data:
            filtered_place_location = f"{filtered_place['geometry']['location']['lat']},{filtered_place['geometry']['location']['lng']}"
            url = "" \
                  f"https://maps.googleapis.com/maps/api/directions/json?destination={filtered_place_location}&origin={detail_apartemen['location']}&key={API_KEY}" \
                  ""

            payload = {}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)
            data = response.json()['routes']

            if data[0]['legs'][0]['distance']['value'] < 1000:
                routes_distance = f"{data[0]['legs'][0]['distance']['value']} m"
            else:
                routes_distance = data[0]['legs'][0]['distance']['text']


            # try:
            #     fp_rating = filtered_place['rating']
            # except:
            #     fp_rating = 0

            cleaned_place = {
                "nama": filtered_place['name'],
                "rating": filtered_place['rating'],
                "location": f"{filtered_place['geometry']['location']['lat']},{filtered_place['geometry']['location']['lng']}",
                "user_ratings_total": filtered_place['user_ratings_total'],
                "routes_distance": routes_distance,
                "printed": f"{filtered_place['name']} - {filtered_place['rating']} - {filtered_place['user_ratings_total']} review ({routes_distance})"
            }
            if place == "shopping_mall":
                mall_list.append(cleaned_place)
            cleaned_place_with_distance.append(cleaned_place)
        print("log2")

        #append to cleaned_place_dy_with_distance
        cleaned_place_dy_with_distance.append({
            "type": place,
            "data": cleaned_place_with_distance
        })


    #
    # for search_place_2 in place_to_search_2:
    #
    #     for place_data in cleaned_place_data:
    #         temp_data = []
    #         if place_data['type'] == search_place_2['in']:
    #             for data in place_data['data']:
    #                 url = "" \
    #                       f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={data['location']}&rankBy=distance&radius=400&language=id&type={search_place_2['what_to_search']}&key={API_KEY}" \
    #                       ""
    #                 print(data)
    #
    #                 payload = {}
    #                 headers = {}
    #
    #                 response = requests.request("GET", url, headers=headers, data=payload)
    #                 data = response.json()['results']
    #                 filtered_data = []
    #                 for data_place in data:
    #                     try:
    #                         if data_place['user_ratings_total'] > 100:
    #                             filtered_data.append(data_place)
    #                     except:
    #                         continue
    #
    #                 cleaned_place = {
    #                     "where": data,
    #                     'data': filtered_data
    #                 }
    #
    #                 temp_data.append(cleaned_place)
    #
    #         # append to cleaned_place_data
    #         cleaned_place_data.append({
    #             "type": search_place_2['what_to_search'],
    #             "typein": search_place_2['in'],
    #             "data": temp_data
    #         })



    #append to detail_apartemen
    print("log6")
    detail_apartemen['permalink'] = str.lower(detail_apartemen['nama']).replace(" ", "_")
    detail_apartemen['nearby_place'] = cleaned_place_data
    detail_apartemen['restaurants_at_mall'] = cleaned_restaurant_data
    detail_apartemen['keyword_data'] = cleaned_keyword_data
    detail_apartemen['dynamic_transport'] = cleaned_place_dy_with_distance
    detail_apartemen['static_transport'] = cleaned_keyword_st_with_distance
    print("log7 - ", detail_apartemen['nama'])

    # detail_list_apartemen.append(detail_apartemen)

# =================
    try:
        # Serializing json
        json_object = json.dumps(detail_apartemen, indent=4)

        # Writing to sample.json
        with open(f"hasil_json/{detail_apartemen['nama']}", "w") as outfile:
            outfile.write(json_object)
    except:
        print("error json write")
        print("=============")
        print(detail_apartemen)

    with open(f"hasil/{detail_apartemen['nama']}.txt", "w", encoding="utf-8") as file:
        file.write(f"{detail_apartemen['nama']}")
        file.write(f"\n\n")
        file.write(f"{detail_apartemen['permalink']}")
        file.write(f"\n\n")
        file.write(f"Kordinat: {detail_apartemen['location']}")
        file.write(f"\n\n")
        file.write(f"{detail_apartemen['alamat']}")
        file.write(f"\n\n")

        file.write(f"===================")
        file.write(f"\n\n")

        for t in detail_apartemen['nearby_place']:
            file.write(f"{t['type']}:")
            file.write(f"\n\n")

            for i in t['data']:
                file.write(f"{i['printed']}")
                file.write(f"lokasi: {i['location']}")
                file.write(f"\n")

            file.write(f"\n\n")

        file.write(f"===================")
        file.write(f"\n\n")

        for t in detail_apartemen['restaurants_at_mall']:
            file.write(f"Rasto di Mall {t['shopping_mall']}:")
            file.write(f"\n\n")

            for i in t['restaurants']:
                file.write(f"{i['printed']}")
                file.write(f"lokasi: {i['location']}")
                file.write(f"\n")

            file.write(f"\n\n")

        file.write(f"===================")
        file.write(f"\n\n")

        for t in detail_apartemen['keyword_data']:
            file.write(f"Keyword Data {t['keyword']}:")
            file.write(f"\n\n")

            if t['keyword'] in special_keyword:
                for i in t['data']:
                    file.write(f"{i['nama']}, ")
            file.write(f"\n\n")

            for i in t['data']:
                try:
                    file.write(f"{i['printed']} - {i['routes_distance']}")
                except:
                    file.write(f"{i['printed']}")
                file.write(f"lokasi: {i['location']}")
                file.write(f"\n")

            file.write(f"\n\n")

            file.write(f"===================")
            file.write(f"\n\n")

        for t in detail_apartemen['dynamic_transport']:
            file.write(f"Dynamic Transport:")
            file.write(f"\n\n")
            try:
                for i in t['data']:
                    file.write(f"{t['type']}")
                    file.write(f"{i['printed']}")
                    file.write(f"lokasi: {i['location']}")
                    file.write(f"\n")
            except:
                file.write(f"error atau data kosong")
                file.write(f"\n")
            file.write(f"\n\n")

        file.write(f"===================")
        file.write(f"\n\n")

        file.write(f"Static Transport:")
        file.write(f"\n\n")
        for t in detail_apartemen['static_transport']:
            try:
                file.write(f"{t['destination']}")
                file.write(f"route distance: {t['routes_distance']}")
                file.write(f"\n")
            except:
                file.write(f"error atau data kosong")
                file.write(f"\n")
            file.write(f"\n\n")
    # except:
    #     print("write error")

