from yahoofinancials import YahooFinancials as yf
import pandas as pd
import json
import time
import sys



if __name__ == "__main__":

    # Get list of companies to be compared
    tickerList = []
    n = int(input('Enter the number of stocks to be compared: '))
    for i in range(0,n):
        ele = input('Enter a ticker: ')
        tickerList.append(ele)

    # Show user the company list
    print(tickerList)

    print('\nFetching market data...\n')

    # Get stock data's key stats
    company = yf(tickerList)
    data = company.get_key_statistics_data()
    dataframe = pd.DataFrame(data)
    useful_data = dataframe.take([1,3,7,20,13,21,23,26,31,35,36,40,43,45], 0)
    # Print useful data
    print(useful_data)

    # Query user for creation of report
    reportQuery = input('\nWould you like to save this in a CSV file? (Y/N)\n')
    reportQuery = str(reportQuery.upper())

    if (reportQuery == 'Y'):
        print('Report will be created.')
        dataframe_report = useful_data.transpose()
        dataframe_report.to_csv('report.csv')
    else:
        print('Report not created.')

print("Program terminated.")
time.sleep(2)
sys.exit()