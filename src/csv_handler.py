import csv
from datetime import datetime
class csv_handler():
    def __init__(self, path):
        def populate_data():
            for line_number,line in enumerate(self.csv_reader):
                if line_number == 0:
                    self.headers = line
                else:
                    self.data.append(line)

        self.file = open(path)
        self.csv_reader = csv.reader(self.file,delimiter=',')
        self.headers = []
        self.data = []

        populate_data()

    def get_total_cases(self, countries:list):
        last_line = [None]*5
        for line in self.data:
            if last_line[1] != line[1] and last_line[1] in countries and last_line[0] != None:
                return int(last_line[4].strip())
            last_line = line

    def get_date_of_first_case(self, for_country:str):
        for line in self.data:
            if line[1] == for_country and int(line[4]) > 0:
                    return datetime.strptime(line[0], '%Y-%m-%d')
                    

    def list_countries(self):
        countries = []
        for line in self.data:
            if line[1] not in countries:
                countries.append(line[1])

        return sorted(countries)

    def get_country_total(self, on_date:str, countries:list):
        total = 0
        for line in self.data:
            if line[1] in countries and line[0] == on_date:
                total += int(line[4])

        return total

    def get_world_total(self, on_date:str):
        total = 0
        for line in self.data:
            if line[0] == on_date and line[1] == "World":
                total += int(line[4])

        return total

    def get_country_data(self, country):
        def build_totals_list():
            totals_list = []
            count = 0
            position = []
            dates = []
            for line in country_data:
                totals_list.append(int(line[4]))
                position.append(count)
                count+=1
                dates.append(line[0])
            return position, totals_list, dates

        country_data = []
        for line in self.data:
            if line[1] == country:
                country_data.append(line)
        return build_totals_list()