import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib.pyplot import pie ,axis,show


def plotit():
    my_sheet='Sheet1'
    file='/frontendworkflow/static/upload/Income and Expenditure.xlsx'
    df = pd.read_excel(file, sheet_name = my_sheet)
    sums = df.groupby(df["Month"])["Expenses"].sum()
    axis('equal')
    pie(sums, labels=sums.index)
    plt.savefig('/frontendworkflow/static/upload/pie.png')
    
