class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_1, hashmap_2 = {}, {}
        s1, s2 = list(s), list(t)

        for s in s1:
            value = hashmap_1.get(s)
            if value != None:
                hashmap_1[s] = hashmap_1[s] + 1
            else:
                hashmap_1[s] = 1
        for t in s2:
            value = hashmap_2.get(t)
           
            if value != None:
                hashmap_2[t] = hashmap_2[t] + 1
            else: 
                hashmap_2[t] = 1
        
        return hashmap_2 == hashmap_1
            


        