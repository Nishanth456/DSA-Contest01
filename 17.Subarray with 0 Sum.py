class Solution:
    def subArrayExists(self,arr,n):
        dict = {}
        summ = 0
        
        for i in range(n):
            summ += arr[i]
            if summ == 0 or summ in dict:
                return True
            dict[summ] = i
        return False