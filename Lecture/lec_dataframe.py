# Module Name : lec_dataframe.py

import pandas as pd
import numpy as np
import cx_Oracle
conn = cx_Oracle.connect("ft/0000@localhost:1521/xe")

df = pd.read_sql("select * from emp", conn)
print(df)

# select ename from emp
print(df["ENAME"])
print(df.ENAME)

# select ename, sal from emp
print(df[["ENAME","SAL"]])

# select comm + sal from emp
print(df["SAL"] + df["COMM"])

# select ename, sal from emp where deptno=10
조건 = df["DEPTNO"]==10
셀렉트 = ["ENAME","SAL"]
# print(df[셀렉트][조건])  #df[ ["ENAME","SAL"] ][  df["deptno"]==10  ]
print(df[조건][셀렉트])    #df[  df["deptno"]==10  ] [ ["ENAME","SAL"] ]


# select ename, sal from emp where deptno=10 order by sal desc
print(df[셀렉트][조건].sort_values(by="SAL", ascending=False))
print(df[df["DEPTNO"]==10][["ENAME","SAL"]].sort_values(by="SAL", ascending=False))

# select ename from emp where comm is null
# comm is null
# df.COMM.isna()
# df["COMM"].isna()
# df["ENAME"][df["COMM"].isna()==True]
print(df[df["COMM"].isna()]["ENAME"])

# Group 함수
# max() min() avg() sum() count()
# select max(sal) from emp
print(df  ["SAL"].max())
# select count(sal) from emp
print(df  ["SAL"].count())

# select max(sal), min(sal) from emp
print( [ df["SAL"].max(), df["SAL"].min()])
print( df["SAL"].agg([max,min] ) )

# select max(sal), count(deptno) from emp
dic = {"SAL":max, "DEPTNO":'count'}
print( df[["SAL","DEPTNO"]].agg([max,'count']) )
print(df.agg(dic))

# Group by
# select deptno, sum(sal) from emp group by deptno, job
print(df.groupby(["DEPTNO","JOB"])["SAL"].sum())
# df.groupby(df["DEPTNO"])["SAL"].sum()
# df['SAL'].groupby(df['DEPTNO']).sum()

# select deptno, sum(sal) from emp group by deptno order by deptno desc
print(df.groupby(df["DEPTNO"], as_index=False)["SAL"].sum().sort_values(by="SAL", ascending=False))
print(df.groupby(df["DEPTNO"])["SAL"].sum().sort_index(ascending= False))
print(df.groupby(df["DEPTNO"], as_index=False )["SAL"].sum())

# Join = merge()
# df.merge()
# select e.empno, d.dname from emp e, dept d where e.deptno = d.deptno
# select e.empno, d.dname from emp e join dept d on e.deptno = d.deptno
emp_df  = pd.read_sql("select * from emp", conn)
dept_df = pd.read_sql("select * from dept", conn)
print(emp_df.merge(dept_df, on="DEPTNO")[["EMPNO","DNAME"]])
print(pd.merge(dept_df, emp_df, how="outer", on= "DEPTNO")[["EMPNO","DEPTNO"]])
# {'left', 'right', 'outer', 'inner'},
# select e.empno, d.dname from emp e inner join dept d on e.deptno = d.deptno


#delete from emp where ename='SMITH'
# 'labels', 'index' or 'columns'"
emp_df = emp_df.drop(axis=0, index=df[df["ENAME"]=='SMITH'].index)
emp_df = emp_df.drop("AGE", axis="1") #, inplace=True)


# fill missing Fare with median fare for each Pclass
train["Fare"].fillna(5000)

# fill missing Fare with median fare for each Pclass
train["Fare"].fillna(train.groupby("Pclass")["Fare"].transform("median"), inplace=True)
