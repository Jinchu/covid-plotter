from flask import render_template, url_for
from app import app
from app.forms import CountryForm
from config import STATIC_CONT

import fetchPatientData
import visualizeData


@app.route('/covid', methods=['GET', 'POST'])
def covid():

    countryForm = CountryForm()
    return render_template('index.html', title='Home', form=countryForm)


@app.route('/covid/results', methods=['GET', 'POST'])
def results():
    countryForm = CountryForm()

    if countryForm.validate_on_submit():
        country = countryForm.country.data
    else:
        country = 'Germany'
    folder = '/home/tracker/static/plots/'

    return getCountryStats(country, countryForm)


@app.route('/covid/finland', methods=['GET', 'POST'])
def finland():
    return getCountryStats("Finland")

@app.route('/covid/sweden', methods=['GET', 'POST'])
def sweden():
    return getCountryStats("Sweden")

@app.route('/covid/denmark', methods=['GET', 'POST'])
def denmark():
    return getCountryStats("Denmark")

@app.route('/covid/norway', methods=['GET', 'POST'])
def norway():
    return getCountryStats("Norway")

@app.route('/covid/germany', methods=['GET', 'POST'])
def germany():
    return getCountryStats("Germany")

@app.route('/covid/south-korea', methods=['GET', 'POST'])
def south_korea():
    return getCountryStats("South-Korea")

@app.route('/covid/us', methods=['GET', 'POST'])
def us():
    return getCountryStats("US")


def getCountryStats(country, form=None):
    if form is None:
        form = CountryForm()

    folder = '/home/tracker/static/plots/'

    raw = fetchPatientData.WorldOMeterCoronaPage(
        "https://www.worldometers.info/coronavirus/country/" + country)
    raw.fetch()

    # Sometimes the logged number of daily new cases may be lower than length of the total cases
    if len(raw.total_cases) > len(raw.daily_new_cases):
        # Let's make the length of the entries match
        warning = "WARNING!: the length of data array for "
        warning += "daily new cases is lower than for total cases."
        print(warning)
        cPlot = visualizeData.CovidPlot(raw.total_cases[:len(raw.daily_new_cases)],
                                        raw.daily_new_cases)
    else:
        cPlot = visualizeData.CovidPlot(raw.total_cases, raw.daily_new_cases)
    cPlot.plotRollingAverageNewCasesToTotal(country, folder)
    # This url needs to point to a place that provides the delivery of static assets.
    plot_url = STATIC_CONT + country + '-new-to-total.png'

    return render_template('results.html', title='Results', country=country, file_path=plot_url,
                           form=form)
