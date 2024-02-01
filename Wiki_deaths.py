import wikipediaapi
import requests
import json

def main():
    wiki = wikipediaapi.Wikipedia(language='en')

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    years = [x for x in range(1992, 2023)]
    
    check_pages(wiki, years, month)
    
    tot_data = {}
    for year in years:
        tot_data[year] = {}
        for month in months:
            print("processing", year, month)
            page = wiki.page(f'Deaths_in_{month}_{str(year)}')
            parsed_page = parse_page(page.text, month, years)
            tot_data[year][month] = parsed_page
            print("Added",sum(len(v) for v in parsed_page.values()),"deaths")

    with open("Death_File.json", "w") as file_json:
        json.dump(tot_data, file_json, indent=3)



# check existence
def check_pages(wiki, years, months):
    page_names = []
    for year in years:
        for month in months:
            page_names.append(f'Deaths_in_{month}_{str(year)}')

    existence = []
    for check in page_names:
        page_py = wiki.page(check)
        existence.append(page_py.exists())
        print(page_py.title)



def parse_page(text , months, years):
    text_divided = text.split("\n")
    day_to_death = {}
    day = 1
    flag_in_day = False
    for line in text_divided:
        if line == str(day):
            day_to_death[day] = []
            day += 1
            flag_in_day = True
        elif line != "" and not line.startswith("=") and flag_in_day == True:
            parsed_line = parse_line(line)
            if parsed_line is not None:
                day_to_death[day-1].append(parsed_line)
                
    return day_to_death



def parse_line(line):
    info_dic = {}
    line_list = line.strip(".").split(", ")
    
    if len(line_list) > 1:
        info_dic["Name"] = line_list[0]
        
        try:
            info_dic["Age"] = int(line_list[1])
        except ValueError as e:
            return None
        
        info_dic["Other_info"] = line_list[2:]
        
        return info_dic
    else:
        return None



def pprint (obj):
    print(json.dumps(obj, indent=3))


if __name__ == "__main__":
    main()
