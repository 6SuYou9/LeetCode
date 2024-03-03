# Author: Su

from itertools import zip_longest

class Solution(object):
    def mergeAlternately1(self, word1:str, word2:str):
        """
        我的写法
        结果：
            执行用时分布：40ms左右
            消耗内存分布：16.3MB左右
        """
        word3 = []
        for i in range(max(len(word1), len(word2))):
            if i > len(word1)-1:
                word3.append("")
            else:
                word3.append(word1[i])
            if i > len(word2)-1:
                word3.append("")
            else:
                word3.append(word2[i])
        return "".join(word3)

    def mergeAlternately2(self, word1,word2):
        """
        简洁写法 学习到的
        知识点：
            zip_longest是Python标准库中itertools模块里的一个函数，用于将两个或多个列表按照最长的列表长度进行合并，并返回一个迭代器。如果其中一个列表比另一个列表长，zip_longest函数会用指定的填充值来填充短的列表。这个函数在处理不对齐的数据时尤为方便。
            具体来说，zip_longest函数的作用类似于zip函数，但是zip函数只能处理长度相同的可迭代对象，而zip_longest函数则可以处理长度不同的可迭代对象。在zip_longest函数中，可以通过fillvalue参数来指定填充值，以便在短的列表被填充时使用。
        :param word1:
        :param word2:
        :return:
        """
        res = []
        for ch1, ch2 in zip_longest(word1, word2, fillvalue=''):
            res += [ch1, ch2]
        return ''.join(res)

S = Solution()
print(S.mergeAlternately2("abc","desdfaf"))