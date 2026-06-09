TRAVEL_DATA = {
    "Paris": [
        {"name": "Eiffel Tower Visit",        "cost": 30,  "duration": 3, "interest": ["sightseeing", "culture"]},
        {"name": "Louvre Museum",              "cost": 20,  "duration": 4, "interest": ["culture", "art"]},
        {"name": "Seine River Cruise",         "cost": 25,  "duration": 2, "interest": ["sightseeing", "relaxation"]},
        {"name": "Montmartre Walking Tour",    "cost": 0,   "duration": 2, "interest": ["culture", "art", "sightseeing"]},
        {"name": "Palace of Versailles",       "cost": 20,  "duration": 5, "interest": ["history", "culture"]},
        {"name": "French Cooking Class",       "cost": 80,  "duration": 4, "interest": ["food", "culture"]},
        {"name": "Musée d'Orsay",              "cost": 16,  "duration": 3, "interest": ["art", "culture"]},
        {"name": "Champs-Élysées Shopping",   "cost": 100, "duration": 3, "interest": ["shopping"]},
        {"name": "Notre-Dame Cathedral",       "cost": 0,   "duration": 2, "interest": ["history", "sightseeing"]},
        {"name": "Latin Quarter Food Tour",    "cost": 45,  "duration": 3, "interest": ["food", "culture"]},
    ],
    "Tokyo": [
        {"name": "Shibuya Crossing & Area",    "cost": 5,   "duration": 2, "interest": ["sightseeing", "culture"]},
        {"name": "Senso-ji Temple",            "cost": 0,   "duration": 2, "interest": ["history", "culture"]},
        {"name": "Tsukiji Fish Market",        "cost": 30,  "duration": 3, "interest": ["food", "culture"]},
        {"name": "TeamLab Borderless",         "cost": 32,  "duration": 3, "interest": ["art", "culture"]},
        {"name": "Mount Fuji Day Trip",        "cost": 60,  "duration": 8, "interest": ["adventure", "sightseeing"]},
        {"name": "Akihabara Tech Tour",        "cost": 50,  "duration": 3, "interest": ["shopping", "culture"]},
        {"name": "Ramen Cooking Class",        "cost": 70,  "duration": 3, "interest": ["food"]},
        {"name": "Shinjuku Gyoen Garden",      "cost": 5,   "duration": 2, "interest": ["relaxation", "sightseeing"]},
        {"name": "Harajuku Fashion Walk",      "cost": 20,  "duration": 2, "interest": ["shopping", "culture"]},
        {"name": "Odaiba Waterfront",          "cost": 10,  "duration": 3, "interest": ["sightseeing", "relaxation"]},
    ],
    "New York": [
        {"name": "Statue of Liberty & Ellis Island", "cost": 25, "duration": 4, "interest": ["history", "sightseeing"]},
        {"name": "Central Park Walk",          "cost": 0,   "duration": 3, "interest": ["relaxation", "sightseeing"]},
        {"name": "Metropolitan Museum of Art","cost": 30,  "duration": 4, "interest": ["art", "culture"]},
        {"name": "Broadway Show",              "cost": 120, "duration": 3, "interest": ["culture", "art"]},
        {"name": "Brooklyn Bridge Walk",       "cost": 0,   "duration": 2, "interest": ["sightseeing"]},
        {"name": "High Line Park",             "cost": 0,   "duration": 2, "interest": ["relaxation", "sightseeing"]},
        {"name": "Times Square & 5th Ave",     "cost": 50,  "duration": 3, "interest": ["shopping", "sightseeing"]},
        {"name": "Chelsea Food Market",        "cost": 40,  "duration": 2, "interest": ["food"]},
        {"name": "MOMA",                       "cost": 25,  "duration": 3, "interest": ["art"]},
        {"name": "Empire State Building",      "cost": 40,  "duration": 2, "interest": ["sightseeing"]},
    ],
    "Dubai": [
        {"name": "Burj Khalifa Observation",   "cost": 40,  "duration": 3, "interest": ["sightseeing"]},
        {"name": "Dubai Mall & Aquarium",      "cost": 35,  "duration": 4, "interest": ["shopping", "sightseeing"]},
        {"name": "Desert Safari",              "cost": 80,  "duration": 5, "interest": ["adventure", "culture"]},
        {"name": "Dubai Creek Heritage Walk",  "cost": 0,   "duration": 3, "interest": ["history", "culture"]},
        {"name": "Dhow Cruise Dinner",         "cost": 60,  "duration": 3, "interest": ["food", "relaxation"]},
        {"name": "Palm Jumeirah Tour",         "cost": 20,  "duration": 2, "interest": ["sightseeing"]},
        {"name": "Spice & Gold Souk",          "cost": 30,  "duration": 2, "interest": ["shopping", "culture"]},
        {"name": "Jumeirah Mosque Visit",      "cost": 5,   "duration": 2, "interest": ["history", "culture"]},
        {"name": "Wild Wadi Water Park",       "cost": 70,  "duration": 5, "interest": ["adventure", "relaxation"]},
        {"name": "Dubai Frame",                "cost": 15,  "duration": 2, "interest": ["sightseeing", "history"]},
    ],
    "Istanbul": [
        {"name": "Hagia Sophia",               "cost": 15,  "duration": 2, "interest": ["history", "culture"]},
        {"name": "Grand Bazaar",               "cost": 20,  "duration": 3, "interest": ["shopping", "culture"]},
        {"name": "Bosphorus Cruise",           "cost": 20,  "duration": 3, "interest": ["sightseeing", "relaxation"]},
        {"name": "Topkapi Palace",             "cost": 25,  "duration": 3, "interest": ["history", "culture"]},
        {"name": "Turkish Bath (Hammam)",      "cost": 50,  "duration": 2, "interest": ["relaxation", "culture"]},
        {"name": "Blue Mosque",                "cost": 0,   "duration": 2, "interest": ["history", "sightseeing"]},
        {"name": "Spice Bazaar & Food Tour",   "cost": 40,  "duration": 3, "interest": ["food", "culture"]},
        {"name": "Basilica Cistern",           "cost": 12,  "duration": 2, "interest": ["history"]},
        {"name": "Dolmabahce Palace",          "cost": 20,  "duration": 3, "interest": ["history", "art"]},
        {"name": "Balat Neighborhood Walk",    "cost": 0,   "duration": 2, "interest": ["culture", "art"]},
    ],
}

# Budget for daily accommodation (added as fixed cost per day)
ACCOMMODATION_COST_PER_DAY = {
    "Paris":    80,
    "Tokyo":    70,
    "New York": 100,
    "Dubai":    90,
    "Istanbul": 50,
}

def get_activities(destination):
    """Return list of available activities for a destination."""
    return TRAVEL_DATA.get(destination, [])

def get_accommodation_cost(destination):
    """Return daily accommodation cost."""
    return ACCOMMODATION_COST_PER_DAY.get(destination, 60)

def get_destinations():
    """Return all available destinations."""
    return list(TRAVEL_DATA.keys())