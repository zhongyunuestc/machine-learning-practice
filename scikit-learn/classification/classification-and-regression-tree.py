from sklearn import datasets
from sklearn.model_selection import cross_val_score, KFold
from sklearn.tree.tree import DecisionTreeClassifier

iris = datasets.load_iris()

score = cross_val_score(estimator=DecisionTreeClassifier(), X=iris.data, y=iris.target, cv=KFold(n_splits=10))

print(score.mean())
print(score.std())
