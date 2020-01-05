import pandas as pd
import os

class ReadData(object):
    '''
    class to read data from data folder

    '''
    def __init__(self):
        self.path = os.path.join('.', 'data')
        self.columns = ['city', 'lat', 'lng', 'iso2']

    def read_process_data(self):

        files = [x for x in os.listdir(self.path) if x.endswith('.csv')]
        data = []
        for file in files:
            file_path = os.path.join(self.path, file)
            temp = pd.read_csv(file_path)
            if 'us' in file:
                temp['iso2'] = 'US'
            temp = temp[self.columns].rename({'lng':'lon'}, axis=1)
            data.append(temp)

        df = pd.concat(data, axis=0, sort=False)
        return df

    def query_by_country(self, country):

        df = self.read_process_data()
        df = df[df.iso2 == country].reset_index(drop=True)

        return df[['lat', 'lon']]
