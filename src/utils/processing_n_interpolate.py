# Class to process dataframe with time (yyyy-mm-dd) 
# and a set of point corresponding at these dates and interpolate these points

import pandas as pd

class ProcessInterpolate :

    # Only input a dataframe of two column dates and points to interpolate

    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.dates = dataframe["Position date YYYY-MM-DD"]
        self.points = dataframe.drop("Position date YYYY-MM-DD", axis = 1)

    def time_into_n_days(self) :
        self.dates['Position date YYYY-MM-DD'] = pd.to_datetime(self.dates['Position date YYYY-MM-DD'])
        oldest_date = self.self.dates['Position date YYYY-MM-DD'].min()
        self.dates['Days from oldest date YYYY-MM-DD'] = (self.dates['Position date YYYY-MM-DD'] - oldest_date).dt.days
        self.dates_in_days = self.dates.drop("Position date YYYY-MM-DD", axis = 1)
        self.dates = self.dates.drop("Days from oldest date YYYY-MM-DD", axis = 1)

    def get_dates_in_days(self) :
        return self.dates