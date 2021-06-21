"""
生成一个升序排列的整数数组nums，再给一个要查找的目标整数target，查找target第1次出现的下标（从0开始）
"""
import random


class Solution:
    def binary_search(self, nums, target):
        return self.search(nums, 0, len(nums) - 1, target)

    def search(self, nums, start, end, target):
        """
        :param nums: 传入的列表参数
        :param start: 开始值
        :param end: 结束值
        :param target: 寻找的目标
        :return: 返回的目标index
        """
        if start > end:
            return -1
        mid = (start + end) // 2
        if nums[mid] > target:
            return self.search(nums, start, mid, target)
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            return self.search(nums, mid, end, target)


if __name__ == '__main__':
    n = 25
    my_solution = Solution()
    nums = sorted([x + random.randint(1, 80) for x in range(1, n)])
    target = nums[random.randint(0, len(nums) - 2)]
    target_index = my_solution.binary_search(nums, target)
    print("输入：nums = ", nums, " ", "target = ", target)
    print("输出：", target_index)
