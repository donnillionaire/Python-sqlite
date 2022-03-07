import sqlite3
import numpy as np
from numpy import append
import pandas as pd
import sqlalchemy
import time


list = []

engine = sqlalchemy.create_engine('sqlite:///main_database2.db')
#create a new table masterfile
#create a new table protech_report

#master=pd.read_sql('main_table', engine)
#report=pd.read_sql('reports_table', engine)

#print(report)


df_masterfile = pd.read_csv("masterfile.csv")
# df_report = pd.read_csv("protech_report.csv")
df2_report = pd.read_csv("protech_report.csv")

# print (df_masterfile)
# print(df2_report)

for indx in range(0, 1000):
    LP_report = df2_report.iloc[indx]["LICENSE"]
    print(LP_report)
    #LP_report.append(list)
    list.append(LP_report)

#conversion to numpy array

#print(list)
report_LP_list_arr = np.array(list)

master_arr = df_masterfile.to_numpy()
report_arr = df2_report.to_numpy()

#print(report_LP_list_arr)



for x in report_LP_list_arr:
  #print(x)
    found = np.where(master_arr== x)

    # print(found)
    # print("type:")
    # print(type(found))

    if(found[0].size == 0):
        
        print("not found")
        print(" {0}, {1}".format(x,"not found"))
    elif(found[0].size > 0):
        print( "found")
        print(" {0}, {1}".format(x,"found"))


    time.sleep(0.5)


#print (df2_report)


#search
shape = master_arr.shape
LP_column = df2_report

#print(shape)

# for ind in range(0,50000):
        

#     found = np.where(master_arr== 'ZSP7021')

#     print(found)
#     print("type:")
#     print(type(found))

#     if(found[0].size == 0):
#         print("not found")
#     elif(found[0].size > 0):
#         print( "found")


