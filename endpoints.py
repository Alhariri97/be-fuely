def endPoints():
    return {
    "endpoints": {
        "/api/stations": {
            "expected request": {
                "user": "string",
                "lng": "number (between -180 and 180)",
                "lat": "number (between -90 and 90)",
                "allStations": [
                    "string"
                ]
            },
            "expected response": {
                "user": "string",
                "lng": "30.222",
                "lat": "39.333",
                "allStations": [
                    {
                        "name": "string",
                        "station_id": "ChIJJSrpXvQyyRQRyZLxeBQdsJE",
                        "address": "string",
                        "coordinates": {
                            "lat": "number",
                            "lng": "number"
                        },
                        "price": [
                            {
                                "price": "number between 180 and 250",
                                "time_submitted": "06/07/2022 16:09:00",
                                "user": "string"
                            }
                        ],
                        "votes": "number"
                    }
                ]
            },
            "queries": "none"
        }
    },
    "/api/price": {
        "expected request": {
            "station_id": "ChIJd4YjVxjwfkgRQQY7j_0SJUw",
            "user": "string",
            "price": "number between 180 to 250"
        },
        "expected response": {
            "updated_station": {
                "name": "string",
                "station_id": "ChIJJSrpXvQyyRQRyZLxeBQdsJE",
                "address": "string",
                "coordinates": {
                    "lat": 39.235237,
                    "lng": 30.116817
                },
                "price": [
                    {
                        "price": 194.9,
                        "time_submitted": "06/07/2022 16:09:00",
                        "user": "default"
                    },
                    {
                        "price": 190,
                        "time_submitted": "06/07/2022 16:10:02",
                        "user": "string"
                    }
                ],
                "votes": 0
            }
        }
    },
    "queries": "none"
}