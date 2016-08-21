from DataModels import *
from flask import url_for
shuttle_list = [
    ShuttleRoute("Campus Shuttle circling Ring Road", "7am-10:35pm",
                 "runs every hour",
                 ["Students Union", "Irvine Hall Gate",
                  "Mary Seacole", "Phillip Sherlock Centre",
                  "Social Sciences",
                  "Medical Sciences", "Medical Library",
                  "Dept of Medicine", "ABC Hall",
                  "Sickle Cell Clinic", "Golding Circle",
                  "St Michaels Seminary", "Irvine Hall",
                  "Accident and Emergecny Unit UWHI",
                  "Itensive Care Unit UWHI", "Medical Sciences",
                  "Aqueduct", "Taylor Hall",
                  "Irvine Hall", "Health Care Centre",
                  "Postgraduate Flats",
                  "Students Union"]),

    ShuttleRoute("Campus to Neighbouring Communities", "9pm -2am",
                 "runs every hour,Monday-Friday",
                 ["Karachi Pines", "Wellington", "Karachi", "Tavern Drive",
                  "Mona Heights", "Elleston Flats",
                  "Gordon Town Road", "Hermitage", "Hope Pastures"]),

    ShuttleRoute("Campus to Papine", "7am-10:35pm", "runs every hour",
                 ["Students Union", "Irvine Hall", "Mary Seacole Hall",
                  "Faculty of Science And Technology",
                  "Mona School of Business",
                  "Taylor Hall", "Irvine Hall",
                  "St Michaels Theological Seminary",
                  "UWHI Entrance", "UWHI Sickle Cell Clinic",
                  "UWHI Golding Avenue",
                  "Papine", "Papine Square",
                  "University Cresent", "Papine Market",
                  "UWHI Gate", "St Michaels Theological Seminary",
                  "Irvine Hall", "Students Union"]),

    ShuttleRoute("Liguanea to Campus via Mona Road", "7am-10:35pm",
                 "runs every hour",
                 ["Liguanea Post Office",
                  "Hope Road & Richings Avenue",
                  "Hope Road & Sandy Park Lane", "Scotia Bank",
                  "Blue Castle Drive & Mona Road",
                  "Mona Heights - Aralie Drive",
                  "Mona Heights - Daisy Avenue",
                  "Mona Heights - Garden Boulevard",
                  "Garden Boulevard & Hermitage Road",
                  "Inter - Faculty Lecture Theatre",
                  "Faculty of Social Sciences",
                  "Taylor Hall", "Irvine Hall", "Students Union",
                  "Irvine Hall", "Mary Seacole Hall", "IFLT",
                  "Social Sciences", "Taylor Hall",
                  "Irvine Hall",
                  "Uwi Hospital Gate", "Papine"]),

    ShuttleRoute("Liguanea Campus via Hope Road", "7am-10:35pm", "runs every hour",
                 ["Liguanea Post Office", "Hope Road & Richings Avenue",
                  "Hope Road & Sandy Park Lane", "Scotia Bank",
                  "Jamaica College", "Hope Gardens", "Papine Market",
                  "UWHI Gate", "Golding Circle",
                  "St Michaels Theological Seminary",
                  "Irvine Hall", "Mary Seacole",
                  "IFLT", "Social Sciences",
                  "Taylor Hall", "Irvine Hall",
                  "Students Union", "Irvine Hall",
                  "Mary Seacole", "IFLT", "Social Sciences",
                  "Taylor Hall", "Irvine Hall", "Papine"])
]

taxi_list = [
    TaxiService(
            ["876-968-4780", "876-929-1742", "876-929-4060",
             "876-968-4772", "876-926-3866"],
        "On Time Taxi Service", " ontimetaxi1@yahoo.com"),
    TaxiService(
        ["876-969-9993", "876-618-2005"], "Apollo Taxi Service",
        "apollotaxija@gmail.com"
    ),
    TaxiService(["876-923-7253", "876-923-7728",
                 "876-923-7286", "876-923-7730", "876-901-4650"],
                "Express Taxi Serv", "expresstaxi2008@yahoo.com"),

    TaxiService(["876-925-5227",
                 " 876-925-1394",
                 " 876-969-5062",
                 " 876-924-4833", ],
                "Mortec Taxi Service", ""
                ),
    TaxiService(["876-930-2012",
                 "876-930-1589"], "Cool Cabs", "collcabs1@hotmail.com"),

    TaxiService(["876-929-8294"], "Blue Diamond Taxi-Cab Ltd",
                "bluediamondtaxicabjm@gmail.com"),
    TaxiService(
        [" 876-969-2016", "876-969-6729", "876-969-2016",
            "876-924-2266", "876-969-3989"], "El Shaddai Taxi Service",
        "elshaddaitaxi@yahoo.com"),
    TaxiService(
        ["876-758-2604"], "City Guide Taxi Service Ltd",
        "cityguidetaxi@yahoo.com"),
]

JUTCList = [
    JRoute("73", "Half Way Tree", "Uwi Irvine Gate",
           ["Hope Road", "Papine", "Liguanea"]),
    JRoute("77", "Down Town", "August Town", [
           "Papine", "Liguanea", "Old Hope Road", "Mountain View", "Vineyard Town"]),
    JRoute("78", "Down Town", "August Town", [
           "Papine", "Liguanea", "Old Hope Road", "Cross Roads"]),
    JRoute("75EX", "Six Miles", "Uwi Irvine Gate", [
           "Washington Boulevard", "Molynes Road", "Half Way Tree", "Hope Road", "Liguanea"]),
    JRoute("24EX", "Spanish Town", "Uwi Irvine Gate", [
           "Mandella Highway", "Washington Boulevard", "Half Way Tree", "Liguanea", "Papine"]),
    JRoute("66", "Hermitage", "Down Town", [
           "Old Hope Road", "Tom Redcam Drive", "Mona Road ", "Marescaux Road", "East Street"]),
    JRoute("72", "August Town", "Half Way Tree", ["Mona Road", " Hope Road"]),
    JRoute("95EX", "Bull Bay", "Uwi Irvine Gate", [
           "Mountain View", "Windward Road", "Old Hope Road", "Papine", "Liguanea"])
]


eateries_list = [

    Restaurant("Opens 9am-12am", "Ring Rd, Chancellor Hall",
               "Kentucky Fried Chicken", False, 18.006170, -76.744724, "http://rox116.pythonanywhere.com/static/images/Restaurants/kfc.png"),

    Restaurant("Opens 6am-7pm", "Faculty of Science and Technology",
               "Juici Patties", False, 18.005052, -76.748482, "http://rox116.pythonanywhere.com/static/images/Restaurants/juici.png"),

    Restaurant("Opens 9am-10pm", "Students Union",
               "Yao Chinese Restaurant", False, 18.000850, -76.743325, "http://rox116.pythonanywhere.com/static/images/Restaurants/yao.png"),

        Restaurant("Opens 7am-6pm", "Ring Rd, Humanities and Education",
               "BeeHive", False, 18.004532, -76.746367, "http://rox116.pythonanywhere.com/static/images/Restaurants/beehive.png"),

                   Restaurant("Opens 6am-3am", "Humanities and Education",
                              "Nardo's Snack Shop", False, 18.004991, -76.745777, "http://rox116.pythonanywhere.com/static/images/Restaurants/nardo.png"),

                   Restaurant("Opens 11am-8pm", "Students Union",
                              "The Spot Sports Bar and Grill", False, 18.000850, -76.743325, "http://rox116.pythonanywhere.com/static/images/Restaurants/spot.png"),

                   Restaurant("Opens 7am-6pm", "Ring Rd, Chancellor Hall",
                              "Pages Cafe", False, 0, 0, "http://rox116.pythonanywhere.com/static/images/Restaurants/pages.png"),

                   Restaurant("Opens 7am-6pm", "Social Welfare Training Centre",
                              "Social Welfare Cafeteria", False, 0, 0, "http://rox116.pythonanywhere.com/static/images/Restaurants/preston.png"),

                   Restaurant("Opens 7am-6pm", "Mary Seacole Hall",
                              "Mae's Cafeteria", False, 0, 0, "http://rox116.pythonanywhere.com/static/images/Restaurants/maes.png"),

                   Restaurant("Opens 7am-6pm", "ABC Hall",
                              "ABC Cafeteria", False, 0, 0, "http://rox116.pythonanywhere.com/static/images/Restaurants/abc.png"),

                   Restaurant("Opens 8am-7pm", "Faculty of Social Sciences",
                              "Board Walk Cafe", False, 0, 0, "http://rox116.pythonanywhere.com/static/images/Restaurants/boardwalk.png"),

                   Restaurant("Opens 7am-6pm", "A.Z Preston Hall",
                              "A.Z Preston Hall Cafeteria", False, 0, 0, "http://rox116.pythonanywhere.com/static/images/Restaurants/preston.png"),

                   Restaurant("Opens 7am-6pm", "Talyor Hall",
                              "Taylor Hall Cafeteria", False, 0, 0, "http://rox116.pythonanywhere.com/static/images/Restaurants/taylor.png"),

                   Restaurant("Opens 7am-6pm", "Rex Nettleford Hall",
                              "Rex Nettleford Hall Cafeteria", False, 0, 0, "http://rox116.pythonanywhere.com/static/images/Restaurants/rex.png")
               ]

guild_list = [
        GuildRoute("Harbour View", ["Harbour Drive","Harbour View Mini-Stadium", "Fort Nugent", "Mars Drive","Rockfort","Winward Road", "Mountain View Avenue",
        "Old Hope Road", "Wellington Drive", "Mona Road", "UWI"], "$150", "6:30 AM 9:30 PM"),
        GuildRoute("Duhaney Park", ["Pete's Bakery", "Glendale Scheme", "Hughenden", "Queensborough", "Price Right", "Perkins Boulevard",
        "Meadowbrook Estate", "Duhaney Drive", "Duhaney Park Plaze","Washington Boulevard", "Patrick Dirve", "Pembrook Hall Drive","Half-Way-Tree", "Hope Road", "Mona Road", "UWI"],"$150", "6:00 AM, 6:30 AM, 9:30 PM"),
        GuildRoute("Spanish Town", ["L.O.J. Shopping Centre", "TwickenHam Park", "Greendale", "Central Village", "Mandela Drive", "6 Miles",
        "3 Miles", "Spanish Town Road", "Maxfield Avenue", "Russell Road", "Beechwood Avenue", "Half-Way-Tree Road", "Oxford Road", "Old Hope Road"], "$160", "6:00 AM, 6:30 AM, 4:30 PM, 7:30 PM, 9:30 PM"),
        GuildRoute("20 Route", ["UWI", "Mona Road", "Wellington Road", "Old Hope Road", "Oxford Road", "Half-Way-Tree Road",
        "Beechwood Avenue", "Russell Road", "Maxfield Avenue", "Spanish Town Road", "3 Miles", "Marcus Garvey Drive", "Causeway Bridge & Toll Road",
        "Portmore Mall", "Silverstone", "Scotia Bank", "Esso Gas Station", "Caribbean Estate", "One North", "Monza", "Daytona", "3 North", "Epsom"], "$180", "9:30 PM"),
        GuildRoute("Greater Portmore", ["2 East", "3 East", "3 West", "4 West", "5 west", "6 East", "Farmcare", "Braeton",
        "Petcom Gas Station", "85(KFC, Burger King)", "Texaco Gas Station", "Marine Park","Naggo Head",
        "Bayside","Edgewater", "Bridgeport", "West Meade", "Garvey Meade", "Bridgeview", "Passage Fort", "PortmoreMall,",
        "Causeway Bridge", "Marcus Garvey Drive", "3 Miles", "Spanish Town Road", "Maxfield Avenue",
        "Russell Road", "Beechwood Avenue", "Halfway Tree Road", "Oxford Road", "Old Hope Road", "Wellington Drive",
        "Mona Road", "UWI"], "$100", "5:00 AM, 6:00 AM, 4:30 PM, 7:30 PM, 9:30 PM"),
        GuildRoute("Monza", ["Greater Portmore Round-a-bout", "Epsom 6 West", "7 West", "8 West", "3 North",
        "Daytona", "Monza", "One North", "Caribbean Estate", "Esso Gas Station", "Scotia Bank", "Silverstone",
        "Portmore Pines", "Newland Road", "Cumberland Round-a-Bout", "Cumberland Morant Avenue",
        "Agusta Drive", "Portmore Drive", "Heart Academy", "Portmore Mall", "Toll Road", "Maxfield Avenue",
        "Russell Road", "Beechwood Avenue", "Half-way Tree Road", "Oxford Road", "Old Hope Road", "Wellington Drive",
        "Mona Road", "UWI"], "$160", "6:00 AM, 9:30 PM"),
        GuildRoute("Gregory Park", ["Christian Gardens", "Christian Pen", "Gregory Park Police Station", "Independence City",
        "Shell Gas Station", "Caymanas Park Entrance", "Top Waterford", "Waterford Park-way", "Waterford Terminus", "Portsmouth",
        "Passage Fort", "Heart Academy", "Portmore Mall", "Toll Road & Causeway Bridge", "Marcus Garvey Drive",
        "3 Miles Avenue", "Half-Way Tree Road", "Oxford Road", "Old Hope Road", "Wellington Drive", "UWI"],
        "$160", "6:00 AM, 9:30 PM")
    ]