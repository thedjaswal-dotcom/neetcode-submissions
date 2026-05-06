class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        smallest_str=strs[0]
        len_sm_st=len(smallest_str)
        if len(strs)==1:
            return strs[0]
        else:
          while len_sm_st>0:
              count=1
              for i in range(1,len(strs)):
               if strs[i].startswith(smallest_str[:len_sm_st]):
                   count+=1
                   if count==len(strs):
                       return smallest_str[:len_sm_st]   
              len_sm_st+=-1
          
          return ""
        


