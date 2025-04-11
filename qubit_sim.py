import numpy as np

def recursive_hadamard(n):
    if n == 1:
        return (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]])
    else:
        Hn_1 = recursive_hadamard(n-1)
        return np.block([
            [Hn_1, Hn_1],
            [Hn_1, -Hn_1]
        ])

# No valid qubit vector or tensor application.
try:
    H3 = recursive_hadamard(3)
    print("Generated Hadamard matrix:\n", H3)
    state = np.array([1, 0])  # invalid shape for H3 * state
    result = np.dot(H3, state)
    print("Result:", result)
except Exception as e:
    print("Error during simulation:", str(e))