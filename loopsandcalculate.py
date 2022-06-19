def compute_accuracy(a, b):
    correct_predictions = 0
    for true, predicted in zip(a, b):
        if true == predicted:
            correct_predictions += 1
            accuracy = correct_predictions / len(a)
    return accuracy
    return correct_predictions


a = (1, 0, 1, 0, 1)
b = (1, 1, 1, 1, 1)
x = zip(a, b)
Y = compute_accuracy(a, b)
print(x)
print(Y)
