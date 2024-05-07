import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

x = np.array([[1],[2],[3],[4],[5]])
y = np.array([2,3.9,4,5,6])
model = LinearRegression()
model.fit(x,y)
y_pred = model.predict(x)

plt.scatter(x,y,color = 'blue')
plt.plot(x,y_pred,color = 'red')
plt.title('Linear Regression')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
print("Intercept:", model.intercept_)
print("Coefficient:", model.coef_)