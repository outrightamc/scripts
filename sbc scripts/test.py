import pandas as pd

L = ['Thanks You', 'Its fine no problem', 'Are you sure']
N = ['fisrta', 'wela', 'hols']

dic = {'Palabras':L, 'weas':N}

#create new df 
df = pd.DataFrame(dic)
print (df)
