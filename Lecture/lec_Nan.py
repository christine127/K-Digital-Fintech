# Module Name : lec_Nan
import pandas as pd
import numpy as np
dic = { "name" : ["kim","lee","NaN", "nan", np.nan],
        "kor" : [np.nan,90,80,70,60],   #np.nan -- float64
        "eng" : [50,40,30,20,10],
        "tot" : [0,0,0,0,0]
       }
df = pd.DataFrame(dic)
df["tot"] = df["kor"] + df["eng"]

print(df.head())
print(df.info())
# NaN : nan : Not a Number(float32)
#print("NaN %",df.isna().sum(),  df.isna().sum()/df.isna().count() *100)
print("NaN %",df.isna().sum(),  df.isna().sum()/df.shape[0] *100)

print(np.nan == np.nan)   #False


s = df["kor"].values
if s[0] != np.nan:
    print(s,"nan")


n = df["name"].values
if n[3] == 'nan':
    print(n,"NaN글자")
else:
    print("---")


# [1 2 3]   ndarry
# [1, 2, 3] list


# 0     True
# 1    False
# 2    False
# 3    False
# 4    False
#------------------------------------------
series = df["kor"].isna()
varr   = df["kor"].values           # [nan  90.0  80.0  70.  60.]
list   = df["kor"].values.tolist()  # [nan, 90., 80., 70., 60.]
# listToArray = np.array([1,2,3])
# arrayToList = listToArray.tolist()
#------------------------------------------
# select count(comm) from emp   #4
print(df["kor"].count())        #4  **** 주의
print("series", series.count()) #5  df["kor"].isna().count()
print("arr",  len(varr))        #5
print("list", len(list))        #5
#------------------------------------------
# casting:scaler단일값
# converting:객체타입변환
num = 4.7
f = int(num)
print(f)

arr = [np.nan, 1, 2]
print(type(arr))                #<class 'list'>
print(type(np.array([1,2,3])))  #<class 'numpy.ndarray'>


