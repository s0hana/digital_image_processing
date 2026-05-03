import numpy as np
import matplotlib.pyplot as plt

data = np.random.rand(5000, 2)
#print(data)

train_data = data[:3000]
test_data = data[3000:]

def assign_label(point):
    d0 = ((point[0] - 0)**2 + (point[1] - 0)**2) ** 0.5
    d1 = ((point[0] - 1)**2 + (point[1] - 1)**2) ** 0.5
    return 0 if d0 < d1 else 1

train_labels = []

for p in train_data:
    label = assign_label(p)
    train_labels.append(label)

train_labels = np.array(train_labels)

sum_0 = [0, 0]
sum_1 = [0, 0]

count_0 = 0
count_1 = 0

for i in range(len(train_data)):
    if train_labels[i] == 0:
        sum_0[0] += train_data[i][0]
        sum_0[1] += train_data[i][1]
        count_0 += 1
    else:
        sum_1[0] += train_data[i][0]
        sum_1[1] += train_data[i][1]
        count_1 += 1

mean_0 = [sum_0[0] / count_0, sum_0[1] / count_0]
mean_1 = [sum_1[0] / count_1, sum_1[1] / count_1]

#print("Mean of Group 0:", mean_0)
#print("Mean of Group 1:", mean_1)

def predict(point):
    d0 = ((point[0] - mean_0[0])**2 + (point[1] - mean_0[1])**2) ** 0.5
    d1 = ((point[0] - mean_1[0])**2 + (point[1] - mean_1[1])**2) ** 0.5
    
    if d0 < d1:
        return 0
    else:
        return 1
test_predictions = []

for p in test_data:
    label = predict(p)
    test_predictions.append(label)

test_predictions = np.array(test_predictions)

true_labels = []

for p in test_data:
    label = assign_label(p)
    true_labels.append(label)

true_labels = np.array(true_labels)

correct = 0

for i in range(len(test_data)):
    if test_predictions[i] == true_labels[i]:
        correct += 1
#for i in range(2000):
 #   print(f"Predict data: {test_predictions[i]}, True data: {true_labels[i]}")
accuracy = correct / len(test_data)

print("Accuracy:", accuracy*100, "%")
x1, y1 = mean_0
x2, y2 = mean_1

a = x2 - x1
b = y2 - y1
c = (x1**2 + y1**2 - x2**2 - y2**2) / 2

print("Bisector Line Equation:")
print(f"{a}x + {b}y + {c} = 0")

plt.figure()

# scatter plot
plt.scatter(test_data[:, 0], test_data[:, 1], c=true_labels, cmap='bwr', alpha=0.5)

# bisector line
x_vals = np.linspace(0, 1, 100)

if b != 0:
    y_vals = -(a * x_vals + c) / b
    plt.plot(x_vals, y_vals, color='black', linewidth=2, label="Bisector")

plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Bisector Decision Boundary")
plt.legend()
plt.show()