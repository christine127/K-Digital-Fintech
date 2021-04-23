#Module name : lec_eda_tool.py

import sweetviz as sv
import pandas_profiling as pp
from sklearn.model_selection import train_test_split

import pandas as pd
df = pd.read_csv("iris.csv")
train_X, test_X = train_test_split(df, test_size=0.2, random_state=1212, shuffle=True)
print(df.info())
#-------------------------------------------
# sv_report = sv.compare([train_X, 'Train'], [test_X, 'Test'], 'target')
# sv_report.show_html('eda/sv_report.html')
#-------------------------------------------
# df.profile_report()
pr_report=df.profile_report()
pr_report.to_file('eda/pp_report.html')
#-------------------------------------------
pd.read_csv("sample.txt", sep=",")
import  warnings
warnings.filterwarnings(action="ignore")
import seaborn as sns
sns.heatmap(df.corr(), fmt=".4f")

from sklearn.datasets import load_iris
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score, recall_score, f1_score, roc_auc_score, roc_curve
import warnings

def myscore(y_test,pred,proba, pr_curve=0, auc_curve=0):
    accuracy = accuracy_score(pred ,  y_test)
    precision = precision_score(pred ,  y_test, average='macro')
    recall = recall_score(pred ,  y_test, average='macro')
    f1 = f1_score(pred ,  y_test, average='macro')
    auc = roc_auc_score(y_test, proba[:,-1],  average="macro")
    print("Accuracy:{:.6f}  precision:{:.6f}, recall:{:.6f}, f1:{:.6f}, auc:{:.6f}".format(accuracy, precision, recall, f1, auc))
    mtx = confusion_matrix(y_test, pred)
    print(mtx)


