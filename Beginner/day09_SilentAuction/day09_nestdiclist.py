
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nest a list in Dict
travel_log = {
    "Greece": ["Athens", "Nexos"], #just one value to one key
    "UK": ["London", "Newcastle"],
}

#Nest a Dict in Dict
travel_log2 = {
    "Greece": {
        "Athens": 2,
        "Naxos": 3,
    },

    "UK": {
        "cities_visited": ["London", "Newcastle"],
        "total_visits": 12,
    },
    
}

#Nest a Dict in List
travel_log3 = [
    {
        "country": "Greece",
        "cities": ["Athens","Naxos"],
        "total_visits": 12,
    },
    {
        "country": "UK",
        "cities": ["London","Newcastle"],
        "total_visits": 2,
    }
]


#Do sth to Nested Structures
travel_plan = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(contry_visited, total_visits, cities_vosited):
    new_country = {}
    new_country["country"] = contry_visited
    new_country["visits"] = total_visits
    new_country["cities"] = cities_vosited
    travel_plan.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_plan)

