import numpy as np
import random

class QLearning:
    def __init__(self, shape, learning_rate, discount_factor, epsilon):
        assert 0 < learning_rate < 1, "Learning rate must be between 0 and 1."
        assert 0 < discount_factor < 1, "Discount factor must be between 0 and 1."
        assert 0 <= epsilon <= 1, "Epsilon must be between 0 and 1."

        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.q_table = np.zeros(shape=shape)

    def update(self, s_t, a_t, reward, s_next):
        self.q_table[s_t[0], s_t[1], a_t] += self.learning_rate * (
            reward + self.discount_factor * np.max(self.q_table[s_next[0], s_next[1]])
            - self.q_table[s_t[0], s_t[1], a_t]
        )

    def get_best_action(self, s_t):
        return np.argmax(self.q_table[s_t[0], s_t[1]])

    def get_action(self, s_t):
        if random.uniform(0, 1) < self.epsilon:
            return random.choice([0, 1, 2, 3])  # Up, Down, Left, Right
        else:
            return self.get_best_action(s_t)

