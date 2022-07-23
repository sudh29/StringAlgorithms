class Solution:

#     def firstRepChar(self, s):
#         # for character
#         res={}
#         for i in s:
#             if i in res:
#                 res[i]+=1
#                 if res[i]>1:
#                     return i
#             else:
#                 res[i]=1
#         return -1
  
    # word
    res={}
    for i in s.split():
        if i in res:
            word_count[i] += 1
        else:
            word_count[i] = 1
        if word_count[i] > 1:
            return i
    return -1
