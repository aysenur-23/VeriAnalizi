
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

# dosya içeri alma
veriler = pd.read_csv("C://Users//aslan//Desktop//eksikveriler.csv")

print(veriler)

# eksik veriler

imputer = SimpleImputer(missing_values=np.nan, strategy = 'mean') 
#mean=ortalama nan'değerler yerine ortalam yazılacak

Yas = veriler.iloc[:,1:4].values 
print(Yas)

imputer = imputer.fit(Yas[:,1:4])
# fit fonksiyonu eğitmek için kullanılır
# yaşın 1'den 4'e kadar olan kolonlarını öğrenmesini söylüyoruz stratejimiz mean olduğu için kolonların ortalama değerini öğrenir

Yas[:,1:4] = imputer.transform(Yas[:,1:4])
# transform ile öğrendiğini uygulamasını istiyoruz 
# yani nan değerlerini mean'le değiştiriyor

print(Yas)
