#3rd AEMTest Question

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

query = "SELECT top 1 text_sample from dbo.text_sample" 

data = pd.read_sql(query, engine)
text = data.iloc[0]['text_sample']
print(text)

patterns = ['.$','\d','[a-zA-Z]+','[a-zA-Z]','[^\W]','[^\w\s]','\S','\D','age..\d{2}','.\d{4}.\d{7}']
questions = ["# i) End of the character in text",
"ii) All digits pattern",
"iii) All word pattern",
"iv) All alphabetic characters",
"v) All alphanumeric characters",
"vi) All punctuation characters",
"vii) Match all except space",
"viii) Match all except digits",
"ix) Customized pattern, age",
"x) Customized pattern, match phone number"]
for x, pattern in enumerate(patterns):
    
    pattern = re.compile(pattern)

    matches = pattern.findall(text)
    print(' ')
    print('Question {}'.format(questions[x]))
    print('Answer')
    print(matches)
