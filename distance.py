places = [
    # jakpus
    #   "Thamrin City Mall",
    #     "Lotte Mall Jakarta",
    #     "West Mall Grand Indonesia.",
    #     "-6.19362014422445, 106.82227317239264",
    #     "Sarinah Jakarta",
    #     "Plaza Atrium",
    #     "Gajah Mada Plaza",
    #     "Mall Golden Trully",
    # jaksel
    # "Citywalk Sudirman",
    # "ITC Kuningan",
    # "Kuningan City",
    # "Mall Ambasaddor",
    # "The Bellagio Boutique Mall",
    # "Senayan Park",
    # "FX Sudirman",
    # "Blok M Plaza",
    # "Blok M Square",
    # "Ratu Plaza",
    # "Mall Senayan City",
    # "Plaza Senayan",
    # "Senayan Trade Center",
    # "Pacific Place Mall",
    # "Plaza Setiabudi/Setiabudi One",
    # "Kota Kasablanca",
    # "Ashta District 8",
    # "Epicentrum Walk/Epicentrum Mall",
    # "Plaza Festival",
    # "The Darmawangsa Square",
    # "Pejaten Village Mall",
    # "Kalibata City Square",
    # "Plaza Kalibata",
    # "Melawai Plaza",
    # "Mall Metro Cipulir",
    # "ITC Cipulir",
    # "The Bellezza Shopping Arcade",
    # "Grand ITC Permata Hijau",
    # "Gandaria City",
    # jaksel depok
    # "Lippo Mall Kemang",
    # "Cilandak Town Square",
    # "One Bellpark Cinere",
    # "Points Mall Lebak Bulus",
    # "Cinere Bellevue Mall",
    # "Mall Cinere",
    # "Living Park Ciputat",
    # "Plaza Bintaro Satoe",
    # "Bintaro Plaza",
    # "South Quarter Lebak Bulus",
    # "Transmart Cilandak",
    # jakbar
    "Plaza Slipi Jaya",
    "Hublife Taman Anggrek",
    "Mall Taman Anggrek",
    "Mall Central Park",
    "Mall Neo SOHO",
    "ITC Roxy Mas",
    "-6.168292270551479, 106.78655052113889",


    #jakbarsel
    # "Mall Metro"

    # jaktim
    #     "Green Pramuka Square",
    # "Mall Bassura City",
        "ITC Roxy Mas",
        "Glodok Plaza",
        "Pancoran ChinaTown Point",
        "TM Harco Glodok",
        "ITC Mangga Dua",
        "WTC Mangga Dua",
        'Mangga Dua Square',
        "Lokasari Square",
    #     "Ciplaz Klender",
    #     "Ciplaz Jatinegara",
    #     "Pondok Kelapa Town Square",
    #jaktim bawah
# "Aeon Tanjung Barat",
# "De Entrance Arkadia",
# "Mal Kalibata City Square",
# "Plaza Kalibata",
# "PGC Cililitan",
# "Mall Cipinang Indah",
# "Lippo Plaza Kramat Jadi",
# "Mall Graha Cijantung",
# "Mall Tamini",
    # jakut
    # "Bella Terra Lifestyle Center",
    #pluit
    "Emporium Pluit Mall",
    "Pluit Village",
    "Baywalk Mall",
    "AEON MALL Jakarta Garden City",
    "Mal Grand Cakung",
    "PIK Avenue",
    "Central Market PIK",
    "By The Sea PIK Mall",
    "Bandara City Mall",
    "Ozone Eatery Mall",

    #daan mogot
    "Mall Taman Palem",
    "Green Sedayu Mall",
    "Pluit Juction Mall",
    "Mall Matahari Daan Mogot",
    "Puri Indah Mall",


    "Lippo Mall Puri",

    #depok
    # "Margo City Depok",
    # "Depok Town Square",
    # "Pesona Square",
]
import requests


test = [

]

places2 = [
# {
#     "name": "Rumah Sakit Bhakti Mulia",
#     "embel": " - 3,5 - 734 review"
#     },
#     {
#     "name": "RS Murni Teguh Sudirman Jakarta (MTSJ)",
#     "embel": " - 4,0 - 210 review"
#     },
#     {
#     "name": "Rumah Sakit Pelni",
#     "embel": " - 3,9 - 2170 review"
#     },
#     {
#     "name": "MRCCC Siloam Hospitals Semanggi",
#     "embel": " - 3,9 - 2185 review"
#     },
#     {
#     "name": "Rumah Sakit Agung",
#     "embel": " - 3,0 - 422 review"
#     },
#     {
#     "name": "Rumah Sakit YPK Mandiri",
#     "embel": " - 4,0 - 263 review"
#     },
#     {
#     "name": "RSIA TAMBAK",
#     "embel": " - 4,3 - 316 review"
#     },
#     {
#     "name": "Rumah Sakit Ibu dan Anak Budhi Jaya",
#     "embel": " - 4,0 - 142 review"
#     },
#     {
#     "name": "Primaya Hospital PGI Cikini",
#     "embel": " - 4,1 - 569 review"
#     },
#     {
#     "name": "Rumah Sakit Medistra",
#     "embel": " - 4,1 - 836 review"
#     },
#     {
#     "name": "RSU Bunda Jakarta",
#     "embel": " - 3,7 - 327 review"
#     },
    {
    "name": "Kartini Hospital",
    "embel": " - 4,0 - 472 review"
    },
    {
    "name": "Rumah Sakit Jakarta Semanggi",
    "embel": " - 4,0 - 730 review"
    },
    {
    "name": "RS MMC",
    "embel": " - 4,0 - 411 review"
    },
    {
    "name": "BRAWIJAYA HOSPITAL SAHARJO",
    "embel": " - 4,6 - 1612 review"
    },
    # {
    # "name": "Rumah Sakit St. Carolus",
    # "embel": " - 3,9 - 1.123 review"
    # },
    # {
    # "name": "RSUD Mampang Prapatan",
    # "embel": " - 3,8 - 297 review"
    # },
    # {
    # "name": "Rumah Sakit Dr. Cipto Mangunkusomo (RSCM)",
    # "embel": " - 3,6 - 295 review"
    # },
    # {
    # "name": "Rumah Sakit Patria IKKT",
    # "embel": " - 3,2 - 325 review"
    # },
    {
    "name": "RS Medika Permata Hijau",
    "embel": " - 3,3 - 539 review"
    },
    {
    "name": "Mayapada Hospital Kuningan",
    "embel": " - 4,2 - 759 review"
    },
    # {
    # "name": "Rumah Sakit Hermina Jatinegara",
    # "embel": " - 4,2 - 3093 review"
    # },
    {
    "name": "Siloam Hospitals Mampang",
    "embel": " - 4,5 - 306 review"
    },
    # {
    #     "name": "Siloam Hospitals ASRI",
    #     "embel": " - 4,0 - 927 review"
    # },
    # {
    #     "name": "RS Premier Jatinegara",
    #     "embel": " - 3,5 - 542 review"
    # },
    # {
    #     "name": "RSIA Brawijaya Duren Tiga",
    #     "embel": " - 4,7 - 378 review"
    # },
#
{
    "name": "Rumah Sakit Budi Kemuliaan",
    "embel": " - 4,2 - 598 review"
    },
    {
    "name": "RSIA Metro Hospitals Kebon Jeruk",
    "embel": " - 3,7 - 228 review"
    },
    {
    "name": "Siloam Hospitals Kebon Jeruk",
    "embel": " - 4,1 - 1.759 review"
    },
    {
    "name": "Rumah Sakit Anggrek Mas",
    "embel": " - 4,2 - 452 review"
    },
    {
    "name": "RS Grha Kedoya",
    "embel": " - 3,9 - 1.109 review"
    },
    {
    "name": "Rumah Sakit Bhakti Mulia",
    "embel": " - 3,5 - 734 review"
    },
    {
    "name": "RSUD Tanah Abang",
    "embel": " - 4,3 - 235 review"
    },
    {
    "name": "RS Abdi Waluyo",
    "embel": " - 4,4 - 1.164 review"
    },
    {
    "name": "Rumah Sakit Pusat Angkatan Darat Gatot Soebroto",
    "embel": " - 4,0 - 1.292 review"
    },
    {
    "name": "Rumah Sakit Husada",
    "embel": " - 3,6 - 976 review"
    },
    {
    "name": "Rumah Sakit Umum Daerah - RSUD Sawah Besar",
    "embel": " - 3,7 - 201 review"
    },
    {
    "name": "RSU Hermina Kemayoran",
    "embel": " - 4,2 - 1.747 review"
    },
    {
    "name": "Rumah Sakit Pluit",
    "embel": " - 3,2 - 402 review"
    },
    {
    "name": "Rumah Sakit Atma Jaya",
    "embel": " - 3,6 - 489 review"
    },
    {
    "name": "RS Pondok Indah - Puri Indah",
    "embel": " - 4,8 - 2.253 review"
    },
    {
    "name": "RSUD Kembangan",
    "embel": " - 3,8 - 1.027 review"
    },
{
"name": "Rumah Sakit Royal Taruma",
"embel": " - 3,7 - 817 review"
},
{
"name": "Rumah Sakit Ukrida",
"embel": " - 4,5 - 480 review"
},
{
"name": "Rumah Sakit Sumber Waras",
"embel": " - 3,3 - 591 review"
},
{
"name": "RS Kanker Dharmais",
"embel": " - 3,5 - 1126 review"
},
{
"name": "RS Pelni",
"embel": " - 3,9 - 2170 review"
},
{
"name": "RSIA Kemang Medical Care",
"embel": " - 3,9 - 322 review"
},
{
"name": "Rumah Sakit Umum Pusat Fatmawati",
"embel": " - 3,2 - 1.937 review"
},
{
"name": "Rumah Sakit Helsa Ciputat",
"embel": " - 4,7 - 163 review"
},
{
"name": "RSUD Pesanggrahan",
"embel": " - 3,7 - 532 review"
},
{
"name": "RSUD Pondok Aren",
"embel": " - 4,8 - 52 review"
},
{
"name": "RSUD Kebayoran Baru",
"embel": " - 4,1 - 418 review"
},
{
"name": "RSUD Kebayoran Lama",
"embel": " - 4,7 - 686 review"
},
{
"name": "RSUD Pasar Minggu",
"embel": " - 4,0 - 1.448 review"
},
{
"name": "RSUD Jati Padang",
"embel": " - 4,1 - 274 review"
},
{
"name": "Rumah Sakit Siaga Raya",
"embel": " - 4,6 - 490 review"
},
{
"name": "RS Yadika Kebayoran Lama",
"embel": " - 4,1 - 312 review"
},
{
"name": "Rumah Sakit Gandaria",
"embel": " - 3,4 - 201 review"
},
{
"name": "Rumah Sakit Pusat Pertamina",
"embel": " - 4,1 - 912 review"
},
{
"name": "Kartini Hospital",
"embel": " - 4,0 - 472 review"
},
{
    "name": "Rumah Sakit Siaga Raya",
    "embel": " - 4,6 - 490 review"
},
{
    "name": "Rumah Sakit Bhayangkara TK.I R. Said Sukanto",
    "embel": " - 4,0 - 485 review"
},
{
    "name": "Rumah Sakit Pusat Otak Nasional Prof. Dr. dr. Mahar Mardjono Jakarta",
    "embel": " - 4,1 - 1.044 review"
},
{
    "name": "RUMAH SAKIT TEBET",
    "embel": " - 4,7 - 1.664 review"
},
{
    "name": "RSIA Brawijaya Duren Tiga",
    "embel": " - 4,7 - 379 review"
},
{
    "name": "Rumah Sakit Umum Daerah Matraman",
    "embel": " - 3,6 - 454 review"
},
{
"name": "RS Pengayoman Cipinang",
"embel": " - 3,9 - 52 review"
},
# {
# "name": "Rumah Sakit Umum Daerah Pasar Rebo",
# "embel": "4,0 - (1.666 review)"
# },
# {
# "name": "Rumah Sakit Jantung Binawaluya",
# "embel": "4,4 - (164 review)"
# },
# {
# "name": "Rumah Sakit Harapan Bunda Pasar Rebo",
# "embel": "4,1 - (1.818 review)"
# },
# {
# "name": "RSUD Jati Padang",
# "embel": "4,1 - (274 review)"
# },
# {
# "name": "Rumah Sakit Umum Pusat Fatmawati",
# "embel": "3,2 - (1.937 review)"
# },
# {
# "name": "Rumah Sakit Umum Daerah Jagakarsa",
# "embel": "3,2 - (338 review)"
# },
# {
# "name": "Rumah Sakit Harum Sisma Medika",
# "embel": " - 3,1 - 585 review"
# },
# {
# "name": "Rumah Sakit Yadika Pondok Bambu",
# "embel": " - 4,2 - 921 review"
# },
# {
# "name": "RSIA SamMarie Basra",
# "embel": " - 4,4 - 297 review"
# },
# {
# "name": "Rumah Sakit Umum Pusat (RSUP) Persahabatan",
# "embel": " - 3,1 - 1.240 review"
# },
# {
# "name": "Rumah Sakit Angkatan Udara Dr. Esnawan Antariksa",
# "embel": " - 4,5 - 838 review"
# },
{
    "name": "Rumah Sakit Mitra Keluarga Bintaro",
    "embel": " - 4,6 - 2339 review"
},
{
    "name": "RSIA Bina Medika Bintaro",
    "embel": " - 4,6 - 1033 review"
},
{
    "name": "Rumah Sakit Dr. Suyoto",
    "embel": " - 3,3 - 482 review"
},
{
"name": "RSU Hermina Podomoro",
"embel": " - 4,6 - 2.288 review"
},
{
"name": "RSUD Kemayoran",
"embel": " - 3,0 - 417 review"
},
{
"name": "RSU Hermina Kemayoran",
"embel": " - 4,2 - 1.747 review"
},
{
"name": "Rumah Sakit Royal Progress",
"embel": " - 3,7 - 814 review"
},
{
"name": "Rumah Sakit Satya Negara",
"embel": " - 3,7 - 438 review"
},
{
"name": "Rumah Sakit Mitra Keluarga Kemayoran",
"embel": " - 4,0 - 1.117 review"
},
{
"name": "RS EMC Pulomas",
"embel": " - 4,3 - 1.010 review"
},
{
"name": "RSKB Columbia Asia Pulomas",
"embel": " - 4,3 - 1.469 review"
},
{
"name": "Rumah Sakit Khusus Bedah Rawamangun",
"embel": " - 3,4 - 185 review"
},

    {
        "name": "Rumah Sakit Karang Tengah Medika",
        "embel": " - 3,8 -  292 review",

    },
    {
        "name": "Rumah Sakit Umum Bhakti Asih",
        "embel": " - 3,6 -  1.424 review",

    },
    {
        "name": "Rumah Sakit Mulya Tangerang",
        "embel": " - 4,2 -  1.012 review",

    },
    {
        "name": "Radjak Hospital Cengkareng",
        "embel": " - 4,8 -  61 review",

    },
    {
        "name": "Mitra Keluarga Kalideres",
        "embel": " - 4,3 -  2.546 review",

    },
    {
        "name": "Rumah Sakit Hermina Daan Mogot",
        "embel": " - 4,5 -  3.837 review",

    },
    {
        "name": "Rumah Sakit Umum Daerah (RSUD) Cengkareng",
        "embel": " - 4,1 -  1.827 review",

    },
    {
        "name": "Rumah Sakit Umum Daerah Kalideres",
        "embel": " - 3,5 -  299 review",

    },
    {
        "name": "Ciputra Hospital CitraGarden City",
        "embel": " - 4,3 -  1.390 review",

    },
    {
        "name": "Rumah Sakit Pantai Indah Kapuk",
        "embel": " - 4,2 -  1.173 review",

    },
    {
        "name": "Rumah Sakit Angkatan Udara Dr. Esnawan Antariksa",
        "embel": " - 4,5 -  838 review",

    },
{
"name": "RS SARI ASIH CIPONDOH",
"embel": " - 4,5 - 1.229 review"
},
{
"name": "Mandaya Royal Hospital Puri",
"embel": " - 4,7 - 2.314 review"
},


]

nplaces = [
    "Grand Mall Cimanggis",
    "Margo City",
    "Pesona Square",
    "Depok Town Square",
    "DMall Depok",
    "ITC Depok",
    "Ciplaz Depok",
    "Plaza Jagakarsa",
    "Mall Graha Cijantung",
    "Mal Tamini",
    "Green Terrace Taman Mini",
]
API_KEY = ""
mode = 1
origin = "Apartemen Cibubur Village"
dataall = []
if mode == 1:
    for place in nplaces:
        # filtered_place_location = f"{filtered_place['geometry']['location']['lat']},{filtered_place['geometry']['location']['lng']}"
        url = "" \
              f"https://maps.googleapis.com/maps/api/directions/json?destination={place}&origin={origin}&key={API_KEY}" \
              ""

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        data = response.json()['routes']

        val = data[0]['legs'][0]['distance']['value']

        url = "" \
              f"https://maps.googleapis.com/maps/api/directions/json?destination={origin}&origin={place}&key={API_KEY}" \
              ""

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        data = response.json()['routes']

        val += data[0]['legs'][0]['distance']['value']

        # val += val + ()

        if data[0]['legs'][0]['distance']['value'] < 1000:
            routes_distance = f"{round(val / 2)} m"
        else:
            routes_distance = f"{round((val / 1000) / 2)} km"

        # if data[0]['legs'][0]['distance']['value'] < 1000:
        #     routes_distance = f"{val} m"
        # else:
        #     routes_distance = f"{round(val/1000)} km"


        if place == "-6.19362014422445, 106.82227317239264":
            name = "Plaza Indonesia"
        elif place == "-6.168292270551479, 106.78655052113889":
            name = "Mall Ciputra Jakarta"
        else:
            name = place

        dataall.append({
            "name": name,
            "routes_distance": routes_distance,
            "rval": round(val / 2)
        })
        print("searching", place)


    for datas in sorted(dataall, key=lambda d: d['rval']):
        print(f"{datas['name']} ({datas['routes_distance']})")
else:
    for place in places2:
        # filtered_place_location = f"{filtered_place['geometry']['location']['lat']},{filtered_place['geometry']['location']['lng']}"
        url = "" \
              f"https://maps.googleapis.com/maps/api/directions/json?destination={place['name']}&origin={origin}&key={API_KEY}" \
              ""

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        data = response.json()['routes']

        val = data[0]['legs'][0]['distance']['value']

        url = "" \
              f"https://maps.googleapis.com/maps/api/directions/json?destination={origin}&origin={place['name']}&key={API_KEY}" \
              ""

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        data = response.json()['routes']

        val += data[0]['legs'][0]['distance']['value']

        if data[0]['legs'][0]['distance']['value'] < 1000:
            routes_distance = f"{round(val / 2)} m"
        else:
            routes_distance = f"{round((val / 1000) / 2)} km"

        if place == "-6.19362014422445, 106.82227317239264":
            name = "Plaza Indonesia"
        elif place == "-6.168292270551479, 106.78655052113889":
            name = "Mall Ciputra Jakarta"
        else:
            name = place

        dataall.append({
            "name": place['name'],
            "routes_distance": routes_distance,
            "embel": place['embel'],
            "rval": round(val / 2)
        })
        print("searching", place)

    for datas in sorted(dataall, key=lambda d: d['rval']):
        print(f"{datas['name']}{datas['embel']} ({datas['routes_distance']})")