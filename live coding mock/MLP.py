"""
Multi-Layer Perceptron (MLP) - Forward Pass

Implement the forward pass of a simple 2-layer MLP for binary classification.

Dataflow:
    Input (input_dim) -> Hidden (hidden_dim) -> Output (output_dim)

Task:
    Complete the __init___() and forward() methods below.
"""

import numpy as np


class MLP:
    def __init__(self, input_dim, hidden_dim, output_dim):
        # TODO: initialize weights and biases 
        self.W1 = np.random.randn(input_dim, hidden_dim) # pitfall, using np to initialize.
        self.b1 = np.random.randn(hidden_dim)
        self.W2 = np.random.randn(hidden_dim, output_dim)
        self.b2 = np.random.randn(output_dim)


    def sigmoid(self, x):
        return 1/(1+np.exp(-x)) # pitfall: 1/(1+e^(-x))

    def forward(self, X):
        """
        Args:
            X: input matrix of shape (m, input_dim), where m is the number of samples
        Returns:
            output of shape (m, output_dim)
        """
        # TODO: implement forward pass
        W1 = self.W1
        W2 = self.W2
        b1 = self.b1
        b2 = self.b2
        hidden_output = np.dot(X, W1) + b1
        hidden_activitions = self.sigmoid(hidden_output) # pitfall: this is important to introduce non-linearity, this the difference between linear and Neural Network.
        output = np.dot(hidden_activitions, W2) + b2
        output = self.sigmoid(output) # output_name

        return output


# --- Test ---
if __name__ == "__main__":
    n_samples = 10          # number of samples
    input_dim = 20
    hidden_dim = 4
    output_dim = 1

    np.random.seed(0)
    X = np.random.randn(n_samples, input_dim)

    model = MLP(input_dim=input_dim, hidden_dim=hidden_dim, output_dim=output_dim)
    output = model.forward(X)

    print("Input shape:", X.shape)
    assert X.shape == (n_samples, input_dim), f"Input shape mismatch: {X.shape}"

    print("Output shape:", output.shape)
    assert output.shape == (n_samples, output_dim), f"Output shape mismatch: {output.shape}"
    assert (output >= 0).all() and (output <= 1).all(), "Output should be between 0 and 1"

    threshold = 0.7
    label = (output >= threshold).astype(int)
    assert label.shape == output.shape, f"Label shape mismatch: {label.shape}"

    print("Output:\n", output)
    print("Label:\n", label)




# question1: what's K-components in RAG
# question2: What's A/B test and the function of it? How to test the improvement of A/B test(ATE)
# question3: If you want to analysis the feedback from the user, but we don't have gold data, what technique should we take? LLM-as-judge
# question4: Attention mechanism: The meaning of sequential encoding and the pros and cons between differet sequential encoding (fixed-size, learnable).
# question5: Why PySpark not pandas or polars.