import json
import matplotlib.pyplot as plt

with open("Death_File.json", "r") as f:
    data = json.load(f)
    
# query = ""

# for year in data.keys():
#     for month in data[year].keys():
#         for day, death_in_day in data[year][month].items():
#             for person in death_in_day:
#                 if query in person["Name"]:
#                     print(person)
#                     print(year, month, day)



dic_tot_death_year = {}
dic_tot_death_month = {}

tot_deaths = 0
for year in data.keys():
    tot_death_year = 0
    for month in data[year].keys():
        tot_death_month = 0
        # for day in data[year][month].keys():
        #     for death_in_day in data[year][month][day]:
        for day, death_in_day in data[year][month].items():
            for person in death_in_day:
                tot_death_month += 1
                
        average = tot_death_month/len(data[year][month].values())
        #print(year, month, "average:", int(average))
        dic_tot_death_month[year+ " " +month] = tot_death_month
        
        tot_death_year += tot_death_month
    dic_tot_death_year[year] = tot_death_year
    
    tot_deaths += tot_death_year 


plt.plot(dic_tot_death_year.keys(), dic_tot_death_year.values())
plt.suptitle("Death in year")
# plt.plot(dic_tot_death_month.keys(), dic_tot_death_month.values())
# plt.suptitle("Death in month per year")
plt.xticks(rotation=45)
plt.show()

