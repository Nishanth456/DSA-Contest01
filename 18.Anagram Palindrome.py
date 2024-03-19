class Solution:

    def isPossible(self, S):
        dict={}
        for i in S:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        odd_count = 0
        for count in dict.values():
            if count % 2 != 0:
                odd_count += 1
        if odd_count <=1 :
            return 1
        else:
            return 0