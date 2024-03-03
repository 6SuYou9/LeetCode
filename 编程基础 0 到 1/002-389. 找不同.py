# Author: Su

class Solution:
    def findTheDifference1(self, s: str, t: str) -> str:
        """
        我的写法
        :param s:
        :param t:   字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
        :return:
        """
        s = list(s)
        for i in t:
            if i not in s:
                return i
            s.remove(i)

    def findTheDifference2(self, s: str, t: str) -> str:
        """
        学习大佬解法  确实很启发思维
        核心思想：
            每一个字符都对应一个 ASCII 数字，那么那个不同的数字的 ASCII 码就等于 t 的所有字符码之和 - s 的
            ord 函数将单个字符转换为 ASCII 码， chr相反
        作者：⚗ Knife丶👆👆
        来源：力扣（LeetCode）
        小知识：
            在Python中，map()是一个内置函数，它接受一个函数和一个或多个可迭代对象（如列表、元组等），并返回一个新的迭代器，该迭代器将传入的函数应用到可迭代对象的每一个元素上。map()函数在处理集合数据并应用某个函数到集合的每个元素时非常有用。
        :param s:
        :param t:   字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
        :return:
        """
        return chr(sum(map(ord, t)) - sum(map(ord, s)))



S = Solution()
print(S.findTheDifference2("abcd","abcde"))