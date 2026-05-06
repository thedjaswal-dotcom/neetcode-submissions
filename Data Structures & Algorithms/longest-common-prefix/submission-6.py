class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        sm_s=strs[0]
        l_s_st=len(sm_s)
        if len(strs)==1:
            return strs[0]
        else:
          while l_s_st>0:
              count=1
              for i in range(1,len(strs)):
               if strs[i].startswith(sm_s[:l_s_st]):
                   count+=1
                   if count==len(strs):
                       return sm_s[:l_s_st]   
              l_s_st+=-1
          
          return ""
        


