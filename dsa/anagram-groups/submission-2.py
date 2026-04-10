class Solution:
    def is_anagrams(self, str1, str2):
        len_1 = len(str1)
        len_2 = len(str2)

        if len_1 != len_2:
            return False
        
        dict_1 = {}
        dict_2 = {}

        for _ in range(len_1):
            if str1[_] in dict_1.keys():
                dict_1[str1[_]] += 1
            else:
                dict_1[str1[_]] = 1
            if str2[_] in dict_2.keys():
                dict_2[str2[_]] += 1
            else:
                dict_2[str2[_]] = 1
        
        if dict_1.keys() != dict_2.keys():
            return False
        for key in dict_1.keys():
            if dict_1[key] != dict_2[key]:
                return False
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_list = []

        while strs:

            sub_list = []

            if len(strs) == 1:
                sub_list.append(strs[0])
                result_list.append(sub_list)
                return result_list

            sub_list.append(strs[0])

            for _ in range(1, len(strs)):
                if self.is_anagrams(strs[0], strs[_]):
                    sub_list.append(strs[_])

            result_list.append(sub_list)

            for string in sub_list:
                strs.remove(string)

        return result_list