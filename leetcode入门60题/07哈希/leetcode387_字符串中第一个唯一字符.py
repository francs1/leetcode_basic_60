import collections

class Solution:
    def firstUniqChar(self, s: str) -> int:        
        dic = collections.OrderedDict()#有序字典
        for i in range(len(s)):#遍历字符串
            c = s[i]#当前字符
            if c not in dic:#第一次出现，key是字符，value是一个二元组[字符频率,字符索引]
                dic[c] = [1,i]
            else:
                dic[c][0] += 1#出现多次，key是字符，value二元组修改，字符频率+1
                dic[c][1] = -1#字符索设定为-1，表示此字符不符合题目要求
        for _,v in dic.items():#dic有序
            if v[0] == 1:#字符出现了一次
                return v[1]#返回对应的索引
        return -1
        