class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         self_element=[]
         processed = set()  # Track which indices have been added
         for i in range(len(strs)):
          # Check if index i is already processed
          if i not in processed:
           self_element.append([strs[i]])
           processed.add(i)
          for j in range(len(strs)):
            if len(strs[i])!=len(strs[j]):
             pass
            elif len(strs[i])==len(strs[j]):
             # Check if all characters match in count
             flag=True
             for ch in strs[i]: 
              if strs[i].count(ch)!=strs[j].count(ch):
                flag=False
                break           
             if flag and i!=j and j not in processed:
                # Find the group containing strs[i] and add strs[j] to it
                for group in self_element:
                 if strs[i] in group:
                  group.append(strs[j])
                  processed.add(j)
                  break 
         return self_element
            


