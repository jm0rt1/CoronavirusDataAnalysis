from csv_handler import csv_handler
from matplotlib import pyplot

class Plotter():
    def __init__(self,data_path):
        self.handler = csv_handler(data_path)
    

    def plot_country_data(self, country):
        pos, data, dates = self.handler.get_country_data(country)
        pyplot.figure(id(country))
        pyplot.plot(pos, data)
        pyplot.xticks(ticks = pos, labels=dates , rotation = 'vertical', fontsize= 5)
        pyplot.title("Coronavirus Cases in {} vs Date".format(country))

    def show_plots(self):
        pyplot.show()
        

