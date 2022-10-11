from math import log, exp

# NOTE - can be refactored to make use of polymorphism. But this is simpler.

class SingleQueryModel():
    
    def within_budget(self, epsilon: float, expected_cost: float, budget: float) -> bool:
        return ((exp(epsilon) - 1) * expected_cost) <= budget
    
    def within_accuracy_constraint(self, epsilon: float, N: int, desired_error: float, accuracy_constraint: float) -> bool:
        first_term = 2 * exp(-1 * (N * ((desired_error**2)) / 12))
        second_term = exp(-1 * ((desired_error * N * epsilon) / 2))
        return (first_term + second_term) <= accuracy_constraint

    def parameters_feasible_for_accuracy(self, N: int, desired_error: float, accuracy_constraint: float) -> bool:
        return (3 * exp(-1 * (N * (desired_error**2)) / 12)) <= accuracy_constraint

    def parameters_feasible_for_budget(self, N: int, expected_cost: float, epsilon: float, budget: float) -> bool:
        return (((exp(epsilon) - 1) * expected_cost) * N) <= budget

    def lower_bound_for_N(self, desired_error: float, accuracy_constraint: float) -> float:
        return (12 / (desired_error**2)) * log(3 / accuracy_constraint)
        
    def lower_bound_for_epsilon(self, desired_error: float) -> float:
        return desired_error / 6

    def max_value_for_epsilon(self, budget: float, desired_error: float, expected_cost: float, accuracy_constraint: float) -> float:
        return log(1 + (budget * (desired_error**2)) / (12 * expected_cost * log(3 / accuracy_constraint)))