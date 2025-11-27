import requests
import json

def get_current_standings():
    url = "http://api.jolpi.ca/ergast/f1/2025/driverstandings/"
    data = requests.get(url).json()

    standings = (
        data["MRData"]
            ["StandingsTable"]
            ["StandingsLists"][0]
            ["DriverStandings"]
    )

    drivers = []
    points = {}
    wins = {}

    for entry in standings:
        fname = entry["Driver"]["familyName"]     # e.g. "Norris"
        pts = float(entry["points"])
        w = int(entry["wins"])

        drivers.append(fname)
        points[fname] = pts
        wins[fname] = w

    return drivers, points, wins
