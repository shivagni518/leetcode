class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # max=0
        # for customer in accounts:
        #     wealth=0
        #     for money in customer:
        #         wealth=wealth+money
        #     if wealth>max:
        #         max=wealth
        # return max        

        return max(sum(customer) for customer in accounts)
        