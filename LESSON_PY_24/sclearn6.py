from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.tree import DecisionTreeClassifier
# import some data within sklearn for iris classification
iris = datasets.load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)

from sklearn.pipeline import Pipeline
pipe = Pipeline([('pca', PCA(n_components = 2)), ('std', StandardScaler()), ('Decision_tree', DecisionTreeClassifier())], verbose = True)

pipe.fit(X_train, y_train)

# to see all the hyper parameters
pipe.get_params()
