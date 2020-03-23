from csv_handler import csv_handler
from datetime import datetime
from matplotlib import pyplot
from Plotter import Plotter
def main():
    handler = csv_handler("/Users/James/James's Files/Programming/Python/Coronavirus_Data/Data/full_data.csv")
    US_cases = handler.get_total_cases(["United States"])
    first_case = handler.get_date_of_first_case("United States")
    countries_list = handler.list_countries()
    world_total = handler.get_world_total("2019-12-31")
    china_US_total = handler.get_country_total("2020-01-21", ["China","United States"])
    p = Plotter("/Users/James/James's Files/Programming/Python/Coronavirus_Data/Data/full_data.csv")
    p.plot_country_data("China")
    p.plot_country_data("United States")
    p.plot_country_data("Italy")
    p.show_plots()

if __name__ == "__main__":
    main()