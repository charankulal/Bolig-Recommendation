import json
import math


tenancies_data = [
    {
        "name": "Dusager 38 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 38, 8200 Aarhus N, Denmark",
        "latitude": 56.19409301,
        "longitude": 10.1851524,
        "rooms": 2,
        "rent": 5446.0,
        "size_sqm": 63.0
    }, 
    {
        "name": "Skejbytoften 198-221 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Skejbytoften 198-221, 8200 Aarhus N, Denmark",
        "latitude": 56.199739537675924,
        "longitude": 10.185624465759005,
        "rooms": 4,
        "rent": 11670.0,
        "size_sqm": 100.0
    },
    {
        "name": "Kantorvænget 48 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Kantorvænget 48, 8200 Aarhus N, Denmark",
        "latitude": 56.198210662443984,
        "longitude": 10.204757253477787,
        "rooms": 5,
        "rent": 11670.0,
        "size_sqm": 115.0
    },
    {
        "name": "Dusager 39 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 39, 8200 Aarhus N, Denmark",
        "latitude": 56.19265465,
        "longitude": 10.18428729,
        "rooms": 4,
        "rent": 6106.0,
        "size_sqm": 94.0
    },
    {
        "name": "Dusager 40 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 40, 8200 Aarhus N, Denmark",
        "latitude": 56.19320939,
        "longitude": 10.185939,
        "rooms": 5,
        "rent": 5508.0,
        "size_sqm": 105.0
    },
    {
        "name": "Dusager 41 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 41, 8200 Aarhus N, Denmark",
        "latitude": 56.19320939,
        "longitude": 10.185939,
        "rooms": 3,
        "rent": 5388.0,
        "size_sqm": 81.1
    },
    {
        "name": "Dusager 42 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 42, 8200 Aarhus N, Denmark",
        "latitude": 56.19265465,
        "longitude": 10.18428729,
        "rooms": 4,
        "rent": 6160.0,
        "size_sqm": 96.0
    },
    {
        "name": "Dusager 42 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 42, 8200 Aarhus N, Denmark",
        "latitude": 56.19265465,
        "longitude": 10.18428729,
        "rooms": 4,
        "rent": 6160.0,
        "size_sqm": 96.0
    },
    {
        "name": "Tousvej 31 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Tousvej 31, 8230 Aarhus N, Denmark",
        "latitude": 56.15140306737696,
        "longitude": 10.1490826927513,
        "rooms": 4,
        "rent": 8160.0,
        "size_sqm": 116.0
    },
    {
        "name": "Dusager 43 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 43, 8200 Aarhus N, Denmark",
        "latitude": 56.19320939,
        "longitude": 10.185939,
        "rooms": 3,
        "rent": 6524.0,
        "size_sqm": 82.0
    },
    {
        "name": "Dusager 44 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 44, 8200 Aarhus N, Denmark",
        "latitude": 56.19320939,
        "longitude": 10.185939,
        "rooms": 4,
        "rent": 6470.0,
        "size_sqm": 98.0
    },
    {
        "name": "Dusager 45 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 45, 8200 Aarhus N, Denmark",
        "latitude": 56.19320939,
        "longitude": 10.185939,
        "rooms": 2,
        "rent": 3228.0,
        "size_sqm": 48.0
    },
    {
        "name": "Dusager 45 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 45, 8200 Aarhus N, Denmark",
        "latitude": 56.19320939,
        "longitude": 10.185939,
        "rooms": 3,
        "rent": 5700.0,
        "size_sqm": 68.0
    },
    {
        "name": "Dusager 45 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 45, 8200 Aarhus N, Denmark",
        "latitude": 56.19320939,
        "longitude": 10.185939,
        "rooms": 5,
        "rent": 11700.0,
        "size_sqm": 120.0
    },
    {
        "name": "Dusager 46 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 46, 8200 Aarhus N, Ved Kysten, Borrehusvej, Denmark",
        "latitude": 56.19320939,
        "longitude": 10.185939,
        "rooms": 4,
        "rent": 7028.0,
        "size_sqm": 97.0
    },
    {
        "name": "Dusager 49 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 49, 8200 Aarhus N, Denmark",
        "latitude": 56.19320939,
        "longitude": 10.185939,
        "rooms": 2,
        "rent": 4765.0,
        "size_sqm": 73.0
    },
    {
        "name": "Dusager 12 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 12, 8200 Aarhus N, Denmark",
        "latitude": 56.19385194,
        "longitude": 10.18358478,
        "rooms": 4,
        "rent": 9092.0,
        "size_sqm": 135.0
    },
    {
        "name": "Dusager 13 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 13, 8200 Aarhus N, Denmark",
        "latitude": 56.19391206,
        "longitude": 10.18434408,
        "rooms": 1,
        "rent": 3105.0,
        "size_sqm": 39.0
    },
    {
        "name": "Dusager 14 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 14, 8200 Aarhus N, Denmark",
        "latitude": 56.19440499,
        "longitude": 10.18494445,
        "rooms": 4,
        "rent": 6115.0,
        "size_sqm": 105.0
    },
    {
        "name": "Dusager 15 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 15, 8200 Aarhus N, Denmark",
        "latitude": 56.19391206,
        "longitude": 10.18434408,
        "rooms": 5,
        "rent": 7429.0,
        "size_sqm": 128.0
    },
    {
        "name": "Dusager 16 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 16, 8200 Aarhus N, Kirkevænget, Kløvervej, Kokobbelvej, Denmark",
        "latitude": 56.19478066,
        "longitude": 10.18479254,
        "rooms": 4,
        "rent": 9800.0,
        "size_sqm": 140.0
    },
    {
        "name": "Dusager 19 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 19, 8200 Aarhus N, Denmark",
        "latitude": 56.19391206,
        "longitude": 10.18434408,
        "rooms": 4,
        "rent": 8171.0,
        "size_sqm": 121.0
    },
    {
        "name": "Dusager 20 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 20, 8200 Aarhus N, Denmark",
        "latitude": 56.19475738,
        "longitude": 10.1833419,
        "rooms": 4,
        "rent": 5592.0,
        "size_sqm": 112.3
    },
    {
        "name": "Dusager 21 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 21, 8200 Aarhus N, Denmark",
        "latitude": 56.19265465,
        "longitude": 10.18428729,
        "rooms": 5,
        "rent": 6046.0,
        "size_sqm": 110.0
    },
    {
        "name": "Dusager 22 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 22, 8200 Aarhus N, Denmark",
        "latitude": 56.19599217,
        "longitude": 10.18340587,
        "rooms": 4,
        "rent": 8569.0,
        "size_sqm": 121.0
    },
    {
        "name": "Dusager 23 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 23, 8200 Aarhus N, Denmark",
        "latitude": 56.19265465,
        "longitude": 10.18428729,
        "rooms": 4,
        "rent": 6278.0,
        "size_sqm": 104.0
    },
    {
        "name": "Dusager 24 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 24, 8200 Aarhus N, Denmark",
        "latitude": 56.19265465,
        "longitude": 10.18428729,
        "rooms": 4,
        "rent": 5694.0,
        "size_sqm": 108.3
    },
    {
        "name": "Dusager 26 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 26, 8200 Aarhus N, Denmark",
        "latitude": 56.19265465,
        "longitude": 10.18428729,
        "rooms": 1,
        "rent": 2633.0,
        "size_sqm": 42.5
    },
    {
        "name": "Dusager 28 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 28, 8200 Aarhus N, Denmark",
        "latitude": 56.19265465,
        "longitude": 10.18428729,
        "rooms": 2,
        "rent": 3888.0,
        "size_sqm": 54.0
    },
    {
        "name": "Dusager 30 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 30, 8200 Aarhus N, Denmark",
        "latitude": 56.19391206,
        "longitude": 10.18434408,
        "rooms": 5,
        "rent": 8581.0,
        "size_sqm": 121.0
    },
    {
        "name": "Dusager 31 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 31, 8200 Aarhus N, Seggelundvej, Denmark",
        "latitude": 56.19391206,
        "longitude": 10.18434408,
        "rooms": 3,
        "rent": 8430.0,
        "size_sqm": 115.0
    },
    {
        "name": "Dusager 32 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 32, 8200 Aarhus N, Denmark",
        "latitude": 56.19265465,
        "longitude": 10.18428729,
        "rooms": 2,
        "rent": 2856.0,
        "size_sqm": 52.0
    },
    {
        "name": "Dusager 33 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 33, 8200 Aarhus N, Denmark",
        "latitude": 56.19265465,
        "longitude": 10.18428729,
        "rooms": 4,
        "rent": 5359.0,
        "size_sqm": 96.0
    },
    {
        "name": "Dusager 35 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 35, 8200 Aarhus N, Denmark",
        "latitude": 56.19571931,
        "longitude": 10.18108133,
        "rooms": 5,
        "rent": 6253.0,
        "size_sqm": 103.3
    },
    {
        "name": "Dusager 36 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 36, 8200 Aarhus N, Denmark",
        "latitude": 56.19385348,
        "longitude": 10.18530005,
        "rooms": 5,
        "rent": 6467.0,
        "size_sqm": 103.3
    },
    {
        "name": "Dusager 37 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 37, 8200 Aarhus N, Denmark",
        "latitude": 56.19265465,
        "longitude": 10.18428729,
        "rooms": 5,
        "rent": 6682.0,
        "size_sqm": 107.0
    },
    {
        "name": "Dusager 50 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 50, 8200 Aarhus N, Denmark",
        "latitude": 56.19391206,
        "longitude": 10.18434408,
        "rooms": 5,
        "rent": 9765.0,
        "size_sqm": 129.0
    },
    {
        "name": "Dusager 51 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 51, 8200 Aarhus N, Denmark",
        "latitude": 56.19391206,
        "longitude": 10.18434408,
        "rooms": 5,
        "rent": 9465.0,
        "size_sqm": 130.0
    },
    {
        "name": "Dusager 52 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 52, 8200 Aarhus N, Denmark",
        "latitude": 56.19265465,
        "longitude": 10.18428729,
        "rooms": 5,
        "rent": 8849.0,
        "size_sqm": 114.0
    },
    {
        "name": "Dusager 53 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 53, 8200 Aarhus N, Denmark",
        "latitude": 56.19571931,
        "longitude": 10.18108133,
        "rooms": 4,
        "rent": 7652.0,
        "size_sqm": 114.7
    },
    {
        "name": "Dusager 54 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 54, 8200 Aarhus N, Denmark",
        "latitude": 56.19320939,
        "longitude": 10.185939,
        "rooms": 2,
        "rent": 5702.0,
        "size_sqm": 61.0
    },
    {
        "name": "Dusager 56 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 56, 8200 Aarhus N, Denmark",
        "latitude": 56.19385348,
        "longitude": 10.18530005,
        "rooms": 3,
        "rent": 6177.0,
        "size_sqm": 83.0
    },
    {
        "name": "Dusager 57 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 57, 8200 Aarhus N, Denmark",
        "latitude": 56.19571931,
        "longitude": 10.18108133,
        "rooms": 1,
        "rent": 7003.0,
        "size_sqm": 70.2
    },
    {
        "name": "Dusager 59 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 59, 8200 Aarhus N, Denmark",
        "latitude": 56.19571931,
        "longitude": 10.18108133,
        "rooms": 1,
        "rent": 6882.0,
        "size_sqm": 70.2
    },
    {
        "name": "Dusager 60 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 60, 8200 Aarhus N, Denmark",
        "latitude": 56.19385348,
        "longitude": 10.18530005,
        "rooms": 4,
        "rent": 8207.0,
        "size_sqm": 105.0
    },
    {
        "name": "Dusager 61 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 61, 8200 Aarhus N, Denmark",
        "latitude": 56.19385348,
        "longitude": 10.18530005,
        "rooms": 4,
        "rent": 9826.0,
        "size_sqm": 114.59
    },
    {
        "name": "Dusager 62 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 62, 8200 Aarhus N, Denmark",
        "latitude": 56.19265465,
        "longitude": 10.18428729,
        "rooms": 2,
        "rent": 3676.0,
        "size_sqm": 50.0
    },
    {
        "name": "Dusager 63 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 63, 8200 Aarhus N, Denmark",
        "latitude": 56.19385348,
        "longitude": 10.18530005,
        "rooms": 2,
        "rent": 3678.0,
        "size_sqm": 50.0
    },
    {
        "name": "Dusager 64 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 64, 8200 Aarhus N, Denmark",
        "latitude": 56.19320939,
        "longitude": 10.185939,
        "rooms": 3,
        "rent": 8098.0,
        "size_sqm": 100.0
    },
    {
        "name": "Dusager 65 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 65, 8200 Aarhus N, Denmark",
        "latitude": 56.19385348,
        "longitude": 10.18530005,
        "rooms": 1,
        "rent": 3669.0,
        "size_sqm": 50.0
    },
    {
        "name": "Dusager 66 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 66, 8200 Aarhus N, Denmark",
        "latitude": 56.19385348,
        "longitude": 10.18530005,
        "rooms": 1,
        "rent": 3791.0,
        "size_sqm": 50.0
    },
    {
        "name": "Dusager 70 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 70, 8200 Aarhus N, Denmark",
        "latitude": 56.19391206,
        "longitude": 10.18434408,
        "rooms": 4,
        "rent": 8570.0,
        "size_sqm": 109.0
    },
    {
        "name": "Dusager 71 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 71, 8200 Aarhus N, Denmark",
        "latitude": 56.19391206,
        "longitude": 10.18434408,
        "rooms": 2,
        "rent": 4725.0,
        "size_sqm": 71.0
    },
    {
        "name": "Dusager 74 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 74, 8200 Aarhus N, Denmark",
        "latitude": 56.19320939,
        "longitude": 10.185939,
        "rooms": 1,
        "rent": 3719.0,
        "size_sqm": 50.0
    },
    {
        "name": "Dusager 76 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 76, 8200 Aarhus N, Denmark",
        "latitude": 56.19385348,
        "longitude": 10.18530005,
        "rooms": 2,
        "rent": 4865.0,
        "size_sqm": 50.0
    },
    {
        "name": "Dusager 78 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 78, 8200 Aarhus N, Denmark",
        "latitude": 56.19409301,
        "longitude": 10.1851524,
        "rooms": 4,
        "rent": 8300.0,
        "size_sqm": 111.0
    },
    {
        "name": "Dusager 79 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 79, 8200 Aarhus N, Denmark",
        "latitude": 56.19265465,
        "longitude": 10.18428729,
        "rooms": 2,
        "rent": 6139.0,
        "size_sqm": 68.0
    },
    {
        "name": "Dusager 84 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 84, 8200 Aarhus N, Denmark",
        "latitude": 56.19320939,
        "longitude": 10.185939,
        "rooms": 3,
        "rent": 9517.0,
        "size_sqm": 115.0
    },
    {
        "name": "Dusager 89 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 89, 8200 Aarhus N, Denmark",
        "latitude": 56.19409301,
        "longitude": 10.1851524,
        "rooms": 3,
        "rent": 8380.0,
        "size_sqm": 103.0
    },
    {
        "name": "Dusager 92 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 92, 8200 Aarhus N, Denmark",
        "latitude": 56.19265465,
        "longitude": 10.18428729,
        "rooms": 3,
        "rent": 4662.0,
        "size_sqm": 77.0
    },
    {
        "name": "Dusager 93 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 93, 8200 Aarhus N, Denmark",
        "latitude": 56.19265465,
        "longitude": 10.18428729,
        "rooms": 5,
        "rent": 4616.0,
        "size_sqm": 118.0
    },
    {
        "name": "Dusager 94 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 94, 8200 Aarhus N, Denmark",
        "latitude": 56.19320939,
        "longitude": 10.185939,
        "rooms": 4,
        "rent": 5482.0,
        "size_sqm": 126.0
    },
    {
        "name": "Dusager 95 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Dusager 95, 8200 Aarhus N, Denmark",
        "latitude": 56.19571931,
        "longitude": 10.18108133,
        "rooms": 4,
        "rent": 6547.0,
        "size_sqm": 99.0
    },
    {
        "name": "Tousvej 5 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Tousvej 5, 8230 Aarhus, Denmark",
        "latitude": 56.15313180979905, 
        "longitude": 10.145723764429121,
        "rooms": 2,
        "rent": 3580.0,
        "size_sqm": 35.0
    },
    {
        "name": "Tousvej 5 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Tousvej 5, 8230 Aarhus, Denmark",
        "latitude": 56.15313180979905, 
        "longitude": 10.145723764429121,
        "rooms": 3,
        "rent": 4590.0,
        "size_sqm": 55.0
    },
    {
        "name": "Tousvej 5 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Tousvej 5, 8230 Aarhus, Denmark",
        "latitude": 56.15313180979905, 
        "longitude": 10.145723764429121,
        "rooms": 4,
        "rent": 7600.0,
        "size_sqm": 85.0
    },
    {
        "name": "Tousvej 5 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Tousvej 5, 8230 Aarhus, Denmark",
        "latitude": 56.15313180979905, 
        "longitude": 10.145723764429121,
        "rooms": 5,
        "rent": 8900.0,
        "size_sqm": 115.0
    },
    {
        "name": "Tousvej 5 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Tousvej 5, 8230 Aarhus, Denmark",
        "latitude": 56.15313180979905, 
        "longitude": 10.145723764429121,
        "rooms": 6,
        "rent": 11900.0,
        "size_sqm": 135.0
    },
    {
        "name": "Neptunvej 35 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Neptunvej 35, 8270 Aarhus, Denmark",
        "latitude": 56.12271294662526, 
        "longitude": 10.177227047004136, 
        "rooms": 4,
        "rent": 7900.0,
        "size_sqm": 95.0
    },
    {
        "name": "Neptunvej 35 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus N, Denmark, suitable for individuals or families.",
        "address": "Neptunvej 35, 8270 Aarhus, Denmark",
        "latitude": 56.12271294662526, 
        "longitude": 10.177227047004136, 
        "rooms": 5,
        "rent": 9900.0,
        "size_sqm": 105.0
    },
    {
        "name": "Albert Naurs Vej 35 Tenancy",
        "description": "A comfortable housing tenancy located in Højbjerg, Denmark, suitable for individuals or families.",
        "address": "Albert Naurs Vej 35, 8270 Højbjerg, Denmark",
        "latitude": 56.11601980832635, 
        "longitude": 10.19933458508383,
        "rooms": 3,
        "rent": 6900.0,
        "size_sqm": 75.0
    },
    {
        "name": "Albert Naurs Vej 35 Tenancy",
        "description": "A comfortable housing tenancy located in Højbjerg, Denmark, suitable for individuals or families.",
        "address": "Albert Naurs Vej 35, 8270 Højbjerg, Denmark",
        "latitude": 56.11601980832635, 
        "longitude": 10.19933458508383,
        "rooms": 4,
        "rent": 8900.0,
        "size_sqm": 95.0
    },
    {
        "name": "Albert Naurs Vej 35 Tenancy",
        "description": "A comfortable housing tenancy located in Højbjerg, Denmark, suitable for individuals or families.",
        "address": "Albert Naurs Vej 35, 8270 Højbjerg, Denmark",
        "latitude": 56.11713646103755, 
        "longitude": 10.19961449902135, 
        "rooms": 4,
        "rent": 8900.0,
        "size_sqm": 95.0
    },
    {
        "name": "Magnoliavej 33 Tenancy",
        "description": "A comfortable housing tenancy located in Viby, Denmark, suitable for individuals or families.",
        "address": "Magnoliavej 33, 8260 Viby, Denmark",
        "latitude": 56.134042470672085, 
        "longitude": 10.185763808964156, 
        "rooms": 2,
        "rent": 3900.0,
        "size_sqm": 35.0
    },
    {
        "name": "Magnoliavej 33 Tenancy",
        "description": "A comfortable housing tenancy located in Viby, Denmark, suitable for individuals or families.",
        "address": "Magnoliavej 33, 8260 Viby, Denmark",
        "latitude": 56.134042470672085, 
        "longitude": 10.185763808964156, 
        "rooms": 3,
        "rent": 4900.0,
        "size_sqm": 55.0
    },
    {
        "name": "Magnoliavej 33 Tenancy",
        "description": "A comfortable housing tenancy located in Viby, Denmark, suitable for individuals or families.",
        "address": "Magnoliavej 33, 8260 Viby, Denmark",
        "latitude": 56.134042470672085, 
        "longitude": 10.185763808964156, 
        "rooms": 4,
        "rent": 6900.0,
        "size_sqm": 75.0
    },
    {
        "name": "Magnoliavej 33 Tenancy",
        "description": "A comfortable housing tenancy located in Viby, Denmark, suitable for individuals or families.",
        "address": "Magnoliavej 33, 8260 Viby, Denmark",
        "latitude": 56.134042470672085, 
        "longitude": 10.185763808964156, 
        "rooms": 5,
        "rent": 8900.0,
        "size_sqm": 95.0
    },
    {
        "name": "Magnoliavej 33 Tenancy",
        "description": "A comfortable housing tenancy located in Viby, Denmark, suitable for individuals or families.",
        "address": "Magnoliavej 33, 8260 Viby, Denmark",
        "latitude": 56.134042470672085, 
        "longitude": 10.185763808964156, 
        "rooms": 6,
        "rent": 10900.0,
        "size_sqm": 115.0
    },
    {
        "name": "Decembervej 5 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus, Denmark, suitable for individuals or families.",
        "address": "Decembervej 5, 8210 Aarhus, Denmark",
        "latitude": 56.17373876563512, 
        "longitude": 10.153118426053256,  
        "rooms": 2,
        "rent": 4300.0,
        "size_sqm": 38.0
    },
    {
        "name": "Decembervej 5 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus, Denmark, suitable for individuals or families.",
        "address": "Decembervej 5, 8210 Aarhus, Denmark",
        "latitude": 56.17373876563512, 
        "longitude": 10.153118426053256,  
        "rooms": 3,
        "rent": 5300.0,
        "size_sqm": 58.0
    },
    {
        "name": "Decembervej 5 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus, Denmark, suitable for individuals or families.",
        "address": "Decembervej 5, 8210 Aarhus, Denmark",
        "latitude": 56.17373876563512, 
        "longitude": 10.153118426053256,  
        "rooms": 4,
        "rent": 7300.0,
        "size_sqm": 78.0
    },
    {
        "name": "Decembervej 5 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus, Denmark, suitable for individuals or families.",
        "address": "Decembervej 5, 8210 Aarhus, Denmark",
        "latitude": 56.17373876563512, 
        "longitude": 10.153118426053256,  
        "rooms": 5,
        "rent": 9300.0,
        "size_sqm": 98.0
    },
    {
        "name": "Decembervej 5 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus, Denmark, suitable for individuals or families.",
        "address": "Decembervej 5, 8210 Aarhus, Denmark",
        "latitude": 56.17373876563512, 
        "longitude": 10.153118426053256,  
        "rooms": 6,
        "rent": 11300.0,
        "size_sqm": 118.0
    },
    {
        "name": "Majvej 2 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus, Denmark, suitable for individuals or families.",
        "address": "Majvej 2, 8210 Aarhus, Denmark",
        "latitude": 56.17413153046026, 
        "longitude": 10.161510253313919, 
        "rooms": 2,
        "rent": 2900.0,
        "size_sqm": 28.0
    },
    {
        "name": "Majvej 2 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus, Denmark, suitable for individuals or families.",
        "address": "Majvej 2, 8210 Aarhus, Denmark",
        "latitude": 56.17413153046026, 
        "longitude": 10.161510253313919, 
        "rooms": 3,
        "rent": 3900.0,
        "size_sqm": 48.0
    },
    {
        "name": "Majvej 2 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus, Denmark, suitable for individuals or families.",
        "address": "Majvej 2, 8210 Aarhus, Denmark",
        "latitude": 56.17413153046026, 
        "longitude": 10.161510253313919, 
        "rooms": 4,
        "rent": 5900.0,
        "size_sqm": 68.0
    },
    {
        "name": "Majvej 2 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus, Denmark, suitable for individuals or families.",
        "address": "Majvej 2, 8210 Aarhus, Denmark",
        "latitude": 56.17413153046026, 
        "longitude": 10.161510253313919, 
        "rooms": 5,
        "rent": 7900.0,
        "size_sqm": 88.0
    },
    {
        "name": "Majvej 2 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus, Denmark, suitable for individuals or families.",
        "address": "Majvej 2, 8210 Aarhus, Denmark",
        "latitude": 56.17413153046026, 
        "longitude": 10.161510253313919, 
        "rooms": 6,
        "rent": 9900.0,
        "size_sqm": 108.0
    },
    {
        "name": "Aprilvej 28 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus, Denmark, suitable for individuals or families.",
        "address": "Aprilvej 28, 8210 Aarhus, Denmark",
        "latitude": 56.17668351307264, 
        "longitude": 10.163299640143805,  
        "rooms": 2,
        "rent": 3450.0,
        "size_sqm": 32.0
    },
    {
        "name": "Aprilvej 28 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus, Denmark, suitable for individuals or families.",
        "address": "Aprilvej 28, 8210 Aarhus, Denmark",
        "latitude": 56.17668351307264, 
        "longitude": 10.163299640143805,  
        "rooms": 3,
        "rent": 4450.0,
        "size_sqm": 52.0
    },
    {
        "name": "Aprilvej 28 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus, Denmark, suitable for individuals or families.",
        "address": "Aprilvej 28, 8210 Aarhus, Denmark",
        "latitude": 56.17668351307264, 
        "longitude": 10.163299640143805,  
        "rooms": 4,
        "rent": 6450.0,
        "size_sqm": 72.0
    },
    {
        "name": "Aprilvej 28 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus, Denmark, suitable for individuals or families.",
        "address": "Aprilvej 28, 8210 Aarhus, Denmark",
        "latitude": 56.17668351307264, 
        "longitude": 10.163299640143805,  
        "rooms": 5,
        "rent": 10450.0,
        "size_sqm": 118.0
    },
    {
        "name": "Trillegårdsvej 73 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus, Denmark, suitable for individuals or families.",
        "address": "Trillegårdsvej 73, 8210 Aarhus, Denmark",
        "latitude": 56.17891730085501,  
        "longitude": 10.169807406726113,  
        "rooms": 2,
        "rent": 4100.0,
        "size_sqm": 35.0
    },
    {
        "name": "Trillegårdsvej 73 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus, Denmark, suitable for individuals or families.",
        "address": "Trillegårdsvej 73, 8210 Aarhus, Denmark",
        "latitude": 56.17891730085501,  
        "longitude": 10.169807406726113,  
        "rooms": 3,
        "rent": 5100.0,
        "size_sqm": 55.0
    },
    {
        "name": "Trillegårdsvej 73 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus, Denmark, suitable for individuals or families.",
        "address": "Trillegårdsvej 73, 8210 Aarhus, Denmark",
        "latitude": 56.17891730085501,  
        "longitude": 10.169807406726113,  
        "rooms": 4,
        "rent": 7100.0,
        "size_sqm": 75.0
    },
    {
        "name": "Trillegårdsvej 73 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus, Denmark, suitable for individuals or families.",
        "address": "Trillegårdsvej 73, 8210 Aarhus, Denmark",
        "latitude": 56.17891730085501,  
        "longitude": 10.169807406726113,  
        "rooms": 5,
        "rent": 9100.0,
        "size_sqm": 95.0
    },
    {
        "name": "Trillegårdsvej 73 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus, Denmark, suitable for individuals or families.",
        "address": "Trillegårdsvej 73, 8210 Aarhus, Denmark",
        "latitude": 56.17891730085501,  
        "longitude": 10.169807406726113,  
        "rooms": 6,
        "rent": 11100.0,
        "size_sqm": 115.0
    },
    {
        "name": "Hedeager 40 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus, Denmark, suitable for individuals or families.",
        "address": "Hedeager 40, 8200 Aarhus, Denmark",
        "latitude": 56.195189311755676, 
        "longitude": 10.178108952265369,  
        "rooms": 2,
        "rent": 5500.0,
        "size_sqm": 40.0
    },
    {
        "name": "Hedeager 40 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus, Denmark, suitable for individuals or families.",
        "address": "Hedeager 40, 8200 Aarhus, Denmark",
        "latitude": 56.195189311755676, 
        "longitude": 10.178108952265369,  
        "rooms": 3,
        "rent": 6500.0,
        "size_sqm": 60.0
    },
    {
        "name": "Hedeager 40 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus, Denmark, suitable for individuals or families.",
        "address": "Hedeager 40, 8200 Aarhus, Denmark",
        "latitude": 56.195189311755676, 
        "longitude": 10.178108952265369,  
        "rooms": 4,
        "rent": 8500.0,
        "size_sqm": 80.0
    },
    {
        "name": "Hedeager 40 Tenancy",
        "description": "A comfortable housing tenancy located in Aarhus, Denmark, suitable for individuals or families.",
        "address": "Hedeager 40, 8200 Aarhus, Denmark",
        "latitude": 56.195189311755676, 
        "longitude": 10.178108952265369,  
        "rooms": 5,
        "rent": 10500.0,
        "size_sqm": 100.0
    },
    {
        "name": "Langelandsgade 133",
        "description": "A comfortable housing tenancy located in Aarhus, Denmark, suitable for individuals or families.",
        "address": "Langelandsgade 133, 8000 Aarhus, Denmark",
        "latitude": 56.16622753703583, 
        "longitude":  10.197198413264392, 
        "rooms": 1,
        "rent": 3100.0,
        "size_sqm": 30.0
    },
    {
        "name": "Langelandsgade 133",
        "description": "A comfortable housing tenancy located in Aarhus, Denmark, suitable for individuals or families.",
        "address": "Langelandsgade 133, 8000 Aarhus, Denmark",
        "latitude": 56.16622753703583, 
        "longitude":  10.197198413264392, 
        "rooms": 2,
        "rent": 5100.0,
        "size_sqm": 50.0
    },
    {
        "name": "Langelandsgade 133",
        "description": "A comfortable housing tenancy located in Aarhus, Denmark, suitable for individuals or families.",
        "address": "Langelandsgade 133, 8000 Aarhus, Denmark",
        "latitude": 56.16622753703583, 
        "longitude":  10.197198413264392, 
        "rooms": 3,
        "rent": 7500.0,
        "size_sqm": 80.0
    }     
]


facilities = {
    "hospital": [
        {"lat": 56.191998, "lng": 10.172236},
        {"lat": 56.170417, "lng": 10.206278},
        {"lat": 56.1412, "lng": 10.18806},
        {"lat": 56.19167, "lng": 10.17222},
        {"lat": 56.158472, "lng": 10.1865}
    ],
    "school": [
        {"lat": 56.154826, "lng": 10.212434},
        {"lat": 56.15281, "lng": 10.136},
        {"lat": 56.1465, "lng": 10.1874},
        {"lat": 56.2, "lng": 10.1167},
        {"lat": 56.193, "lng": 10.14}
    ],
    "gym": [
        {"lat": 56.162, "lng": 10.203},
        {"lat": 56.178, "lng": 10.182},
        {"lat": 56.184, "lng": 10.113},
        {"lat": 56.14887, "lng": 10.207873},
        {"lat": 56.148, "lng": 10.207}
    ],
    "supermarket": [
        {"lat": 56.18231, "lng": 10.14},
        {"lat": 56.146047, "lng": 10.202726},
        {"lat": 56.17325, "lng": 10.202726},
        {"lat": 56.20161, "lng": 10.2449},
        {"lat": 56.17325, "lng": 10.202726}
    ]
}

# Haversine formula to calculate distance between two points (in kilometers)
def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0
    
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    
    return distance


for tenancy in tenancies_data:
    lat = tenancy["latitude"]
    lon = tenancy["longitude"]
    
    
    for category in facilities:
        min_dist = min(haversine(lat, lon, f["lat"], f["lng"]) for f in facilities[category])
        tenancy[f"distance_to_{category}"] = round(min_dist, 2)


output_file = "tenancies_with_distances.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(tenancies_data, f, ensure_ascii=False, indent=4)

print(f"Updated data with distances has been saved to {output_file}")