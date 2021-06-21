"""
根据N名运动员得分，找出最高的前三名，分别获得金牌、银牌、铜牌，第四名和第五名，打印出分数，N是正整数，不能超过10000，
所有运动员的分数都要独一无二
"""
import random  # 引入random模块，随机数


def find_relative_ranks(nums):   # 定义find函数，传入nums方法
    sorted_score = sorted(nums, reverse=True)   # sorted()方法进行排序，按照降序排列
    top_five = sorted_score[0:5]  # 取前五名
    top_five[0] = "Gold medal:" + str(top_five[0])
    top_five[1] = "Silver medal:" + str(top_five[1])
    top_five[2] = "Bronze medal:" + str(top_five[2])
    return top_five


if __name__ == '__main__':
    num = random.sample(range(1, 10000), 888)  # random模块的sample()创建1～10000以内的888个数，range表示范围，888表示个数
    answer = find_relative_ranks(num) # 调用find方法
    print("输入：", num)
    print(answer)
