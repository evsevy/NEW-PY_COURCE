 # Импорт библиотек
import numpy as np
from sklearn import decomposition
from sklearn import datasets
# Загрузка данных
iris = datasets.load_iris()
X = iris.data



 # Преобразование данных датасета Iris, уменьшающее размерность до 3
pca = decomposition.PCA(n_components=3)
print(pca.fit(X))
