import pandas as pd
import numpy as np
import warnings
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.decomposition import PCA

warnings.filterwarnings('ignore')

df = pd.read_csv('apple_quality.csv')
df = df.dropna()
df['Acidity'] = [float(i) for i in df['Acidity']] # converting string to float
df['Quality'] = [1 if i=='good' else 0 for i in df['Quality']]

def clip_outliers(part):
    q3 = np.percentile(part, 75)
    q1 = np.percentile(part, 25)
    return np.clip(part, q1-1.5*(q3-q1), q3+1.5*(q3-q1) )

x = df.iloc[:, 1:-1]
y = df.iloc[:, -1]
for i in x.columns: x[i] = clip_outliers(x[i])

pca = PCA(n_components=7)
x_pca = pca.fit_transform(x)

scaler = StandardScaler()
X = scaler.fit_transform(x_pca)

import random
v = random.randint(0, 100)

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=2)
svm = SVC(C = 90, random_state=42, probability=True)
svm.fit(x_train, y_train)
# accuracy_score(y_test, svm.predict(x_test))

d1 = pd.read_csv('table1.csv')
d2 = pd.read_csv('table2.csv')
d3 = pd.read_csv('table3.csv')
def table1(): return d1.to_dict(orient='records')
def table2(): return d2.to_dict(orient='records')
def table3(): return d3.to_dict(orient='records')

def getPred():
    rand = random.randint(0, x_test.shape[0]-1) 
    probs = svm.predict_proba([x_test[rand]])[0]
    a, b = float(probs[0]), float(probs[1])
    og = pca.inverse_transform(scaler.inverse_transform([x_test[rand]]))[0]
    cols = list(x.columns.values)
    
    actual_value = int(y_test.values[rand])
    predicted_value = int(svm.predict([x_test[rand]])[0])
    
    og_list = [float(val) for val in og.round(2)]
    
    ret_dict = {
        'Columns': [cols],
        'Data': [og_list], 
        'Actual': [actual_value], 
        'Predicted': [predicted_value], 
        'Prob 0': [round(float(a/(a+b)), 4)], 
        'Prob 1': [round(float(b/(a+b)), 4)] 
    }
    
    ret = pd.DataFrame(ret_dict)
    return ret.to_dict(orient='records')

def input(li):
    li_x = pca.transform([li])
    li = scaler.transform(li_x)
    return int(svm.predict(li)[0])

if __name__ == '__main__':
    print(table1())
    print(table2())
    print(table3())
    print(getPred())