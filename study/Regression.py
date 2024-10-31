from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

# 加载鸢尾花数据集
iris = load_iris()
X = iris.data
y = iris.target

# 将数据集分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 创建决策树分类器对象
clf = DecisionTreeClassifier(random_state=42)

# 使用训练集对决策树模型进行训练
clf.fit(X_train, y_train)

# 使用测试集对模型进行预测
y_pred = clf.predict(X_test)

# 输出模型的准确率
print(f"Accuracy: {clf.score(X_test, y_test)}")

# 可视化决策树（仅适用于少量特征的数据集）
fig = plt.figure(figsize=(15, 10))
_ = tree.plot_tree(clf,
                   feature_names=iris.feature_names,
                   class_names=iris.target_names,
                   filled=True)
plt.show()
