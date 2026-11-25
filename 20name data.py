import pandas as pd
data={
"Name":["Ram","Shyam","Sita","Geeta","Anita","Babita","Deepika","Ritika","Minika","Nikita"],
"Age":[21,22,19,17,25,31,28,15,24,23],
"Gender":["Male","Male","Female","Female","Female","Female","Female","Female","Female","Female"],
"City":["Panchkula","Panipat","Hisar","Rohtak","Kurukshetra","Sonipat","Gurugram","Panchkula","Rohtak","Faridabad"],
}
df=pd.DataFrame(data)
print(df.iloc[5] )