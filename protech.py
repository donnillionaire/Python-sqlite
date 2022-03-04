import sqlite3
from numpy import append
import pandas as pd
import sqlalchemy


engine = sqlalchemy.create_engine('sqlite:///main_database2.db')
#create a new table masterfile
#create a new table protech_report

#master=pd.read_sql('main_table', engine)
report=pd.read_sql('reports_table', engine)

#print(report)



# df_masterfile = pd.read_csv("masterfile.csv")
# df_report = pd.read_csv("protech_report.csv")
df2_report = pd.read_csv("protech_report.csv")

#print(df2_report)

# df_masterfile.to_sql('protech_master_file_table', engine, if_exists=append)
# df_masterfile.to_sql('protech_report_file_table', engine)
#df2_report.to_sql('report2', engine)

report_data = pd.read_sql('report2', engine)
print(report_data)

#masterfile=pd.read_sql('protech_master_file_table', engine)
#report2 = pd.read_sql('reports2_table', engine)
masterfile=pd.read_sql('protech_master_file_table', engine)
#print(report2)
print("MASTER FILE STARTS HERE>>>")
print(masterfile)

print("now reports table")
print(" ")
report=pd.read_sql('protech_report_file_table', engine)
#print(report)

#engine.execute("CREATE INDEX state ON report2(STATE)") 
dr = "ALTER TABLE protech_master_file_table RENAME COLUMN 'LP' TO lp_1"
get_missing="select * from protech_master_file_table where lp_1 not in ( select lp_1 from report2 ) group by lp_1 having count(*) > 1;"
q = "SELECT * FROM report2 WHERE state = STATE"
insert_random = "INSERT INTO report2 (lp_1) VALUES ('aaaa')"
# m = "SELECT LP FROM report2,protech_master_file_table WHERE report2.lp_1 != protech_master_file_table.LP" 

#q = "SELECT LP, 'LICENSE PLATE' FROM protech_report_file_table INNER JOIN report2 on report2.LICENSE = protech_report_file_table.LP, "
print (pd.read_sql_query(get_missing, engine))
#print(q)


# select * from table1, table 
# where 
# table1.col1 = table2.col2 and table1.col1 > someValue;