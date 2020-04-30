#!/usr/bin/env python
import requests 
import csv 
import tkinter 
import pandas as pd
import numpy
#import matplotlib 
#matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
import plotly.express as px


def gui_versioncheck() :
    gui_env = ['TKAgg','GTKAgg','Qt4Agg','WXAgg']
    for gui in gui_env:
        try:
            print ("testing", gui)
            matplotlib.use(gui,warn=False, force=True)
            from matplotlib import pyplot as plt
            break
        except:
            continue



def createdeathgraph(file_name) :
    df = pd.read_csv(file_name)
    times = df["TimeStamp"]
    Deaths = df["Deaths"]
    x = []
    y = []
    x = list(times)
    y = list(Deaths)
    plt.scatter(x,y)
    plt.xlabel('Time Stamp')
    plt.ylabel('Deaths')
    plt.title('Deaths due to covid over a timeperiod')
    plt.show()





def createconfirmedgraph(file_name) :
    df = pd.read_csv(file_name)
    times = df["TimeStamp"]
    Conformer = df["Confirmed Cases"]
    x = []
    y = []
    x = list(times)
    y = list(Conformer)
    plt.scatter(x,y)
    plt.xlabel('Time Stamp')
    plt.ylabel('Confirmed Cases')
    plt.title('Virus spreads due to covid over a timeperiod')
    plt.show()





def global_statistics(url) :
    request = requests.get(url)
    #print(request.text)
    Global_json = request.json()
    Global_key = Global_json['Global']
    print("The Global stats : ")
    print("New Confirmed : ",Global_key['NewConfirmed'])
    print("Total Confirmed : ",Global_key['TotalConfirmed'])
    print("New Deaths : ",Global_key['NewDeaths'])
    print("Total Deaths : ",Global_key['TotalDeaths'])
    print("New Recovered : ",Global_key['NewRecovered'])
    print("Total Recovered : ",Global_key['TotalRecovered'])




if __name__ == "__main__" : 

    url = "https://api.covid19api.com/summary"
    global_statistics(url)


    url = "https://api.covid19api.com/countries"
    request = requests.get(url)
    #print(request.text)


    country = input("Enter the country name you want to get status of : ").lower().replace(" ","-")
    print(country)
    file_name = country + ".csv"
    csv_file = open(file_name,'w')          #creating a csv file
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Country','ID','Latitude','Longitude','Confirmed Cases','Deaths','Recovered','Active','TimeStamp'])

    url = "https://api.covid19api.com/country/" + country
    request = requests.get(url)


    country_json = request.json()


    for i in range(len(country_json)) :
        country_key = country_json[i]
        print("Country : ",country_key['Country'])
        print("Contry Code : ",country_key['CountryCode'])
        print("Latitude : ",country_key['Lat'])
        print("Longitude : ",country_key['Lon'])
        print("Confirmed Cases : ",country_key['Confirmed'])
        print("Deaths : ",country_key['Deaths'])
        print("Recovered : ",country_key['Recovered'])
        print("Active : ",country_key['Active'])
        print("Time Stamp : ",country_key['Date'])
        csv_writer.writerow([country_key['Country'],country_key['CountryCode'],country_key['Lat'],country_key['Lon'],country_key['Confirmed'],country_key['Deaths'],country_key['Recovered'],country_key['Active'],country_key['Date']])
        print()
        print() 

    csv_file.close()

    createdeathgraph(file_name)
    createconfirmedgraph(file_name)
