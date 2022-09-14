#3rd Question

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

#Hello000 Sir!!, I'm looking for Azman, age: 30, from Rantau Panjang & his phone no. :+6012-3456789({**__mobile__**})
# i) End of character in text '[!@#\\$%\\^\\&*\\)\\(+=._-]$'
# ii) All digits pattern '\d'
# iii) All word pattern '[a-zA-Z]+'
# iv) All alphabetic characters '[a-zA-Z]'
# v) All alphanumeric characters '.'
# vi) All punctuation characters '\W'
# vii) Match all except space  '\S'
# viii) Match all except digits '\D'
# ix) Customized pattern, age 'age..\d{2}'
# x) Customized pattern, match phone number '.\d{4}.\d{7}'


pattern = re.compile(r'age..\d{2}')

matches = pattern.findall(text)

for match in matches:
    print(match)
