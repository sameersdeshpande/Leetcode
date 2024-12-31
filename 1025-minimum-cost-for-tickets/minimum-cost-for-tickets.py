class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0]*366
        travel_days = set(days)

        for day in range (1,366):
            if day not in travel_days:
                dp[day]= dp[day-1]
            else:
                option1= dp[day-1]+costs[0]
                option2 = dp[max(0, day - 7)] + costs[1]
                option3= dp[max(0,day-30)]+costs[2]

                dp[day] = min(option1,option2,option3)
        return dp[day]