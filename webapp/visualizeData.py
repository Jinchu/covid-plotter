import sys
import matplotlib.pyplot as plt

class CovidPlot(object):
    """ Useful for plotting Covid related data. """
    def __init__(self, x_val, y_val):
        self.x = x_val
        self.y = y_val

    def rollingAverage(self, input_data):
        """ Returns array as long as input_data, but rolling averages as values. """
        smoothered = []
        i = 0
        for raw in input_data:
            if i == 0:
                smoothered.append(raw/3)
            elif i == 1:
                smoothered.append((raw + input_data[0]) / 3)
            else:
                smoothered.append((input_data[i] + input_data[i - 1] + input_data[i - 2])/3)
            i += 1

        return smoothered

    def plotRollingAverageNewCasesToTotal(self, country_id, folder):
        """ Plot using rolling average. Returns the name of the file where plot is stored. """
        smooth_x = self.rollingAverage(self.x)
        smooth_y = self.rollingAverage(self.y)

        file_path = folder + '/' + country_id + '-new-to-total.png'

        fig1 = plt.figure(figsize=(9,6), facecolor='y', edgecolor='k')
        plot1 = plt.subplot(111, facecolor='silver')
        plot1.set_yscale('log')
        plot1.grid(color='white', linestyle='-', linewidth=1)
        plot1.set_xscale('log')
        plot1.set_ylabel('daily new cases')
        plot1.set_xlabel('total cases')
        plot1.plot(smooth_x, smooth_y)
        #plt.figure(figsize = (10,14), dpi=100)
        plt.title('Ratio of New Cases to All Cases in '+ country_id)
        fig1.savefig(file_path, dpi=140)
        print("image saved: " + file_path)

        return file_path


def read_test_data_file(file_name):
    """ Helper for unit testing. """
    test_data = []

    with open(file_name, 'r') as file_in:
        content = file_in.read()
        for i in content.split(','):
            test_data.append(int(i))

    return test_data


def main():
    """ Main function for testing """
    test_total_cases = []
    test_daily_new = []

    test_total_cases = read_test_data_file('covid-19/test-plot-total-cases.txt')
    test_daily_new = read_test_data_file('covid-19/test-plot-daily-new.txt')

    testerPlot = CovidPlot(test_total_cases, test_daily_new)
    figure_file = testerPlot.plotRollingAverageNewCasesToTotal('Test-Country', './covid-19')

    if figure_file != './covid-19/Test-Country-new-to-total.png':
        print ("Error in storage file name")
        return 4

    return 0


if __name__ == "__main__":
    sys.exit(main())
