import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn import preprocessing

veriler = pd.read_csv("C://Users//aslan//Desktop//eksikveriler.csv")
imputer = SimpleImputer(missing_values=np.nan, strategy = 'mean') 
Yas = veriler.iloc[:,1:4].values 
imputer = imputer.fit(Yas[:,1:4])
Yas[:,1:4] = imputer.transform(Yas[:,1:4])

ulke = veriler.iloc[:,0:1].values

le = preprocessing.LabelEncoder()
# etiketleri kodlamak için kullanılır

ulke[:,0] = le.fit_transform(veriler.iloc[:,0])
#veriler ilk kolonu alarak 1,2,3 gibi sayısal değerlere dönüştürür

ohe = preprocessing.OneHotEncoder()
# kategorik özellikleri sayısal dizi olarak kodlar

ulke = ohe.fit_transform(ulke).toarray()
# öğrenme ve dönüştürme ve diziye çevirme işlemi yapılır
print(ulke)
