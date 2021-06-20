# 合并排列数组
'''
两个有序数组，合并成一个新数组，要保证新数组也是有序的
比如：list_a = [1,2,5],list_b = [3,4,8],合并成的新数组  list_c =[1,2,3,4,5,8]
'''


class Solution:
    def mergeSortedArray(self, a, b):  # 传入2个参数，这两个参数为list型
        """
        :param a: 有序列表
        :param b: 有序列表
        :return: c:合成后的有序列表
        """
        i, j = 0, 0
        c = []
        while i < len(a) and j < len(b):  # len方法，返回列表长度
            if a[i] < b[j]:
                c.append(a[i])
                i += 1
            else:
                c.append(b[j])
                j += 1
        while i < len(a):
            c.append(a[i])
            i += 1
        while j < len(b):
            c.append(b[j])
            j += 1
        return c


if __name__ == '__main__':
    a = [1, 5, 7]
    b = [1, 2, 3, 4, 8]
    d = [1, 2, 3, 4, 6]
    e = [2, 4, 6, 8]
    solution = Solution()
    print('输入：', a, ' ', b)
    print('输出：', solution.mergeSortedArray(a, b))
    print('输入：', d, ' ', e)
    print('输出：', solution.mergeSortedArray(d, e))

'''
想一下，我们怎么让输出的列表去重呢？就当作课后习题了，也欢迎大家留言评论～～
'''
