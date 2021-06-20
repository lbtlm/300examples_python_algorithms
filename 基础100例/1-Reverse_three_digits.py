# 反转一个三位数

# 问题描述，给一个三位数，例如123，输出为321，如果给出的是900，输出9
# 关于int()用法请参照  https://www.runoob.com/python/python-func-int.html

# 定义解决方案class
class Solution:
    # 定义reverseInterger方法
    def reverseInterger(self, number):  # 传入参数
        """
        :param number:int 传入一个三位数
        :return: int 返回新的三位数
        """
        h = int(number / 100)  # 获得百位数，896/100，取整得8，这点要注意下，后面的小数都被舍去，而不是四舍五入
        t = int(number % 100 / 10)  # 这里注意顺序  %是取模，就是余数的意思，896%100，模为96，再次96/10=9.6，最后得到9
        z = int(number % 10)  # 这个就不用说了  896%10 余6
        return 100 * z + 10 * t + h  # 返回新的三位数


if __name__ == '__main__':
    solution = Solution()  # 创建新对象 solution = Solution类
    num = 896
    ans = solution.reverseInterger(num)  # 调用solution的reverseInterger方法转换
    print('输入的数字是：', num)
    print('输出的数字是：', ans)
