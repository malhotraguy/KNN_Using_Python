import pandas as pd
import io
import time
import sys
import requests
from fake_useragent import UserAgent
ua = UserAgent()
hdr = {'User-Agent':str(ua.chrome)}

with requests.Session() as s:
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    page = s.get(url, headers=hdr)
cont=page.content
print(cont)
print(type(cont))

df = pd.read_csv(io.StringIO(cont.decode('utf-8')), sep=',',header=0, names=['sepal length(cm)','sepal width(cm)','petal length(cm)','petal width(cm)',"class",])
print(df)
writer = pd.ExcelWriter('IrisData.xlsx')
df.to_excel(writer, sheet_name='Sheet',index=False)
writer.save()