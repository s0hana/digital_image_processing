import numpy as np
import matplotlib.pyplot as plt

data = np.random.rand(5000, 2)
#print(data)
labels = []
for i in range(len(data)):
    x1 = data[i][0]
    x2 = data[i][1]
    if x1 + x2 >= 1:
        labels.append(1)
    else:
        labels.append(0)
#labels = np.array(labels)
X_train = data[:3000]
y_train = labels[:3000]
X_test = data[3000:]
y_test = labels[3000:]
X_train_aug = []
for i in range(len(X_train)):
    row = X_train[i]
    new_row = [row[0], row[1], 1]   
    X_train_aug.append(new_row)
X_train_aug = np.array(X_train_aug)
X_test_aug = []
for i in range(len(X_test)):
    row = X_test[i]
    new_row = [row[0], row[1], 1]   
    X_test_aug.append(new_row)
X_test_aug = np.array(X_test_aug)
def perceptron_train(X, y, lr=0.001, epochs=50):
    w = np.random.randn(3)
    errors_per_epoch = []
    best_w = w.copy()
    min_error = float('inf')
    for epoch in range(epochs):
        error = 0 
        for i in range(len(X)):
            dot_product = 0
            for j in range(len(w)):
                dot_product += w[j] * X[i][j]
            pred = 1 if dot_product >= 0 else 0
            if pred != y[i]:
                error += 1
                if y[i] == 1:
                    w += lr * X[i]
                else:
                    w -= lr * X[i]
        errors_per_epoch.append(error)
        acc = (len(X) - error) / len(X)
        print(f"Epoch {epoch+1}: Error = {error}, Accuracy = {acc:.4f}")
        if error < min_error:
            min_error = error
            best_w = w.copy()
    return best_w, errors_per_epoch
w, errors = perceptron_train(X_train_aug, y_train)
print("\nBest Weight Vector:", w)
def predict(X, w):
    predictions = []
    for i in range(len(X)):
        score = 0
        for j in range(len(w)):
            score += X[i][j] * w[j]
        if score >= 0:
            predictions.append(1)
        else:
            predictions.append(0)
    predictions = np.array(predictions)
    return predictions
y_pred = predict(X_test_aug, w)
correct = 0
total = len(y_test)
for i in range(total):
    if y_pred[i] == y_test[i]:
        correct += 1
accuracy = correct / total
print("Test Accuracy:", accuracy)

plt.figure()
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap='bwr', alpha=0.5, s=10)

x_vals = np.linspace(0, 1, 100)
y_vals = -(w[0]*x_vals + w[2]) / w[1]

plt.plot(x_vals, y_vals)
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Perceptron Decision Boundary")
plt.show()