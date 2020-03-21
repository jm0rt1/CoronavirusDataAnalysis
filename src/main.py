from csv_handler import csv_handler
from datetime import datetime
from matplotlib import pyplot
def main():
    handler = csv_handler("/Users/James/James's Files/Programming/Python/Coronavirus_Data/Data/full_data.csv")
    US_cases = handler.get_total_cases(["United States"])
    first_case = handler.get_date_of_first_case("United States")
    countries_list = handler.list_countries()
    world_total = handler.get_world_total("2019-12-31")
    china_US_total = handler.get_country_total("2020-01-21", ["China","United States"])
    pos, china_data, dates = handler.get_country_data("China")

    pyplot.plot(pos, china_data)
    pyplot.xticks(ticks = pos, labels=dates , rotation = 'vertical', fontsize= 5)
    pyplot.show()
    pass

if __name__ == "__main__":
    main()