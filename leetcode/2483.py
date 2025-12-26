class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        penalty = customers.count("Y")
        index = 0
        min_penalty = penalty

        for i in range(n):
            if customers[i] == "N":
                penalty += 1
            if customers[i] == "Y":
                penalty -= 1
            if penalty < min_penalty:
                index = i + 1
                min_penalty = penalty

        return index
