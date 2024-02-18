# # Write the commands to download the txt file in the given link.
# URL= https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt
import requests
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
path=os.path.join(os.getcwd(),'example1.txt')
r=requests.get(url)
with open(path,'wb') as f:
    f.write(r.content)

# Get data from APIs and store in text file and analysis tha data in pandas. 
import pandas as pd
import random
import json

#url=https://official-joke-api.appspot.com/jokes/ten

data2=requests.get('https://official-joke-api.appspot.com/jokes/ten')
#convert json file to text file.
res=json.loads(data2.text)
# convert text file to CSV file
df3 = pd.DataFrame(res)
df3.drop(columns=["type","id"],inplace=True)
print(df3)
# now we can perform operations on this data.