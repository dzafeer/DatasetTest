#2nd AEMTest Question
#Import the same production_data_volve table in Q1 into Python

import urllib
import pandas as pd
import sqlalchemy as sa

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

data = pd.read_sql(query, engine)
print(data)
