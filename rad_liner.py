# python main.py athlete_events.csv -medals UKR 2004
# python main.py athlete_events.csv -total 1992
# python main.py athlete_events.csv -overall UKR USA Germany NIG
import csv
import sys
def year_exist_check(year):
    years = 0
    for i in range(len(rows)):
        if rows[i][9] == year:
            years += 1
    if years == 0:
        return 1
def country_exist_check(country):
    countrys = 0
    for i in range(len(rows)):
        if rows[i][7] == country or rows[i][6] == country:
                countrys += 1
    if countrys == 0:
        return 1
def print_medals(listgiven, gold, silver, bronze):
    if len(listgiven) > 10:
        for i in range(10):
            print(listgiven[i][0],":",listgiven[i][1],",",listgiven[i][2])
        print("Gold:", gold)
        print("Silver:", silver)
        print("Bronze:", bronze)
    else:
        for i in range(len(listgiven)):
            print(listgiven[i][0],":",listgiven[i][1],",",listgiven[i][2])
        print("Gold:", gold)
        print("Silver:", silver)
        print("Bronze:", bronze)
def get_medals(country, year):
    medalsanswer = []
    goldmedalists = []
    silvermedalists = []
    bronzemedalists = []
    namedalsxd = []
    for i in range(len(rows)):
        row = rows[i]
        if row[7] == country or row[6] == country:
            if row[9] == year:
                if row[-1] == 'Gold':
                    goldmedalists.append([row[1], row[-2], row[-1]])
                if row[-1] == 'Silver':
                    silvermedalists.append([row[1], row[-2], row[-1]])
                if row[-1] == 'Bronze':
                    bronzemedalists.append([row[1], row[-2], row[-1]])
                if row[-1] == 'NA':
                    namedalsxd.append([row[1], row[-2], row[-1]])
    if len(bronzemedalists) == 0 and len(silvermedalists) == 0 and len(goldmedalists) == 0:
        return (namedalsxd,0,0,0)
    else:
        for medalist in goldmedalists:
            medalsanswer.append(medalist)
        for medalist in silvermedalists:
            medalsanswer.append(medalist)
        for medalist in bronzemedalists:
            medalsanswer.append(medalist)
        return [medalsanswer,len(goldmedalists),len(silvermedalists),len(bronzemedalists)]
def create_dict_for_year(year):
    dict = {}
    for i in range(len(rows)):
        row = rows[i]
        country_in_line = row[6]
        if row[9] == year:
            if row[-1] == "Gold":
                if country_in_line not in dict:
                    dict[country_in_line] = [0,0,0]
                if country_in_line in dict:
                    dict[country_in_line][0] += 1
            if row[-1] == "Silver":
                if country_in_line not in dict:
                    dict[country_in_line] = [0, 0, 0]
                if country_in_line in dict:
                    dict[country_in_line][1] += 1
            if row[-1] == "Bronze":
                if country_in_line not in dict:
                    dict[country_in_line] = [0, 0, 0]
                if country_in_line in dict:
                    dict[country_in_line][2] += 1
    return dict
def print_for_total_from_dict(dict):
    countrylist = [] #для сортировки
    for country in dict:
        countrylist.append([country,[dict[country][0],dict[country][1],dict[country][2]]])
    countrylist.sort()
    for i in range(len(countrylist)):
        country = countrylist[i][0]
        medal = countrylist[i][1]
        goldmedal = medal[0]
        silvermedal = medal[1]
        bronzemedal = medal[2]
        print(1 + i, country, ":", goldmedal, "- Gold;", silvermedal, "- Silver;", bronzemedal, "- Bronze;")
    return
def convert_years_data(country_list_input):
    N_of_countrys = len(country_list_input)
    medals_list = []

    for country in range(N_of_countrys):
        if country_list_input[country] not in medals_list:
            x = [country_list_input[country]]
            medals_list.append(x)
            medals_list[country].append({})
    for i in range(len(rows)):
        row = rows[i]
        year_in_row = row[9]
        for country in range(N_of_countrys):
            if country_list_input[country] == row[6] or country_list_input[country] == row[7]:
                dict_for_country = medals_list[country][1]
                if year_in_row not in dict_for_country:
                    dict_for_country[year_in_row] = 0
                medal_qual = row[-1]
                if medal_qual == "Gold" or medal_qual == "Silver" or medal_qual == "Bronze":
                    dict_for_country[year_in_row] += 1
    return(medals_list,N_of_countrys)
def look_for_best_year(amazing_list,N_of_countrys):
    best_year_list = []
    years_list = []
    for country in range(N_of_countrys):
        best_year_list.append([0])
        years_list.append(0)
        dict_for_country = amazing_list[country][1]
        for year in dict_for_country:
            if dict_for_country[year] > best_year_list[country][0]:
                best_year_list[country][-1] = dict_for_country[year]
                years_list[country] = year
    return (best_year_list,years_list)
def print_for_overall(country_list,best_years_list,N_of_countrys,years_list):
   # best_years_list.reverse()
    for country in range(N_of_countrys):
        print(country_list[country],":",best_years_list[country][0],",",years_list[country])


# -HEAD
importeddata = sys.argv[1]
rows = []
with open(importeddata, 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
arg = sys.argv
print(arg)
if len(arg) < 4:
    print("wrong input")
    exit()
command = arg[2]
# -medals call
if command == '-medals' and len(arg) == 5:
    country = arg[3]
    year = arg[4]
    if year_exist_check(year) != 1 and country_exist_check(country) != 1:
        medals = get_medals(country, year)
        print_medals(medals[0], medals[1], medals[2], medals[3])
# -total call
elif command == '-total' and len(arg) == 4:
    year = arg[3]
    if year_exist_check(year) != 1:
        dict = create_dict_for_year(year)
        print_for_total_from_dict(dict)
# -overall call
elif command == '-overall' and len(arg) >= 4:
    country_list_for_overall = []
    for i in range(len(arg) - 3):
        country_list_for_overall.append(arg[-1 - i])
    amazing_list = convert_years_data(country_list_for_overall)
    best_years_list = look_for_best_year(amazing_list[0],amazing_list[1])
    print_for_overall(country_list_for_overall,best_years_list[0],amazing_list[1],best_years_list[1])
else:
    print("wrong input")




