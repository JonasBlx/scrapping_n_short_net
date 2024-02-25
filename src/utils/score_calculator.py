"""
compute the score of an investor given a dataframe with short net positions and the share price
"""

from scipy.interpolate import interp1d


# Try with "BLACKROCK INVESTMENT MANAGEMENT UK LIMITED", 'CASINO GUICHARD-PERRACHON',df_sorted,False
# emetteur =  'CASINO GUICHARD-PERRACHON'
# ticker = ticker_dic.get(emetteur, False)

# Use visualiser_investissment and visuel_action_invest_min_max/get_shares
# to have cgg_rows and data["Close"]
def score_calculator(short_net_positions, share_performance) :
    date_numeric = (share_performance.index - share_performance.index[0]).days
    interpolation_function = interp1d(date_numeric, share_performance["Share Performance"], kind='linear')
    print(share_performance.index[0])
    print(interpolation_function(10))
