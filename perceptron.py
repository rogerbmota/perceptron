def main():
    print("The result of the perceptron input is: ", perceptron_input([1, 2, 3], [0.1, 0.2, 0.3], 0.4))

def perceptron_input(inputs, weights, bias):
    weighted_sum = sum(i * w for i, w in zip(inputs, weights))
    return weighted_sum + bias

def perceptron_output(inputs, weights, bias):
    
    return 1 if perceptron_input(inputs, weights, bias) >= 0 else 0

def perceptron_output(inputs, weights):
    
    return 1 if perceptron_input(inputs, weights) >= 0 else 0

if __name__ == "__main__":
    main()