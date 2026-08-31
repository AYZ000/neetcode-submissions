class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)

        for s in strs:
            # Sort the characters to create a canonical key for all anagrams
            sorted_key = "".join(sorted(s))
            groups[sorted_key].append(s)

        return list(groups.values())