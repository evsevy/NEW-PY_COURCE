import numpy as np
x = np.array([[0.1, 1.0, 22.8],
               [0.5, 5.0, 41.2],
               [1.2, 12.0, 2.8],
               [0.8, 8.0, 14.0]])
print(x)


from sklearn.preprocessing import StandardScaler
from sklearn import cluster, datasets 
 # Загрузка данных
iris = datasets.load_iris() 
# создание трех кластеров 
k=3 
k_means = cluster.KMeans(k) 
# обучение модели 
k_means.fit(iris.data)

# новые данные для которых мы хотим получить предсказание
test = np.array([[5, 1], [0, 3], [2, 1], [11, 1], [9, 3], [9, 1]]) 
# получение предсказания для метода k-средних и нового набора данных                
y = k_means.predict(test) 
print('Предсказание: ', y)
