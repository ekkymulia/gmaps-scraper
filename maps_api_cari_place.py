# search restaurant
import requests

mall_list = [
    "-6.212360951558682, 106.78417224679752"
]
API_KEY = ""
types = "hospital"
radius = "6000"
cleaned_restaurant_data = []
print("log2")
for mall in mall_list:
    url = "" \
          f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={mall}&radius={radius}&language=id&type={types}&key={API_KEY}" \
          ""

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()['results']
    filtered_data = []
    for data_place in data:
        try:
            if data_place['user_ratings_total'] > 0:
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
        "location": mall,
        "restaurants":  []
    }

    i=0
    for t in sorted(filtered_data, key=lambda d: d['user_ratings_total'], reverse=True):
       # i+=1
       # if i < 6:
       restaurant_data['restaurants'].append(t)
       # else:
       #     break

    cleaned_restaurant_data.append(restaurant_data)

for p in cleaned_restaurant_data:
    print(p['location'])
    for r in p['restaurants']:
        print(r['printed'])