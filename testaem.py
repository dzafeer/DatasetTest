from http.client import FOUND
import pyodbc
import urllib
import pandas as pd
import sqlalchemy as sa
import re

params = urllib.parse.quote_plus("DRIVER={SQL Server Native Client 11.0};"
                                 "SERVER=server.aemenersol.com;"
                                 "DATABASE=DatasetTest;"
                                 "UID=data_test;"
                                 "PWD=Test@123")
engine = sa.create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))
query = "SELECT WELL_BORE_CODE, \
COUNT(WELL_BORE_CODE) AS recordCount, \
WELL_TYPE + ' ' + FLOW_KIND AS wellType,\
MIN(AVG_DOWNHOLE_TEMPERATURE) AS [minDownholeTemp], \
MAX(AVG_ANNULUS_PRESS) AS [maxAnnulusPress], \
AVG(AVG_DP_TUBING) AS [avgDpTubing], \
SUM(BORE_OIL_VOL) AS [totalOilVolume], \
SUM(BORE_GAS_VOL) AS [totalGasVolume], \
SUM(BORE_WAT_VOL) AS [totalWaterVolume] \
FROM dbo.production_data_volve \
GROUP BY WELL_BORE_CODE, WELL_TYPE + ' ' + FLOW_KIND \
ORDER BY totalOilVolume desc, totalGasVolume desc, totalWaterVolume desc" 

#data = pd.read_sql(query, engine)
#print(data)
# task 3

query = "SELECT top 1 text_sample from dbo.text_sample" 

data = pd.read_sql(query, engine)
text = data.iloc[0]['text_sample']
print(text)
# regex expression  
# i)g$
# ii)  [0-9]
# iii) [A-Z]
# vii) [^\s-]
# viii)[^0-9]
#ix \d{2}[,.]
# x

# 
#Hello000 Sir!!, I'm looking for Azman, age: 30, from Rantau Panjang & his phone no. :+6012-3456789({**__mobile__**})
condition = '[a-z]'
try:
    find = re.search(condition,text).group()
    print('found')
    print(find)

except AttributeError:
    print('not found')
    pass

find2 = re.findall(condition,text)
print(find2)