"""
旋转字符串实例
描述：给一个字符串，再给一个偏移量，按照偏移量来从左到右旋转字符

问题示例：
输入 str="abcdefg"，偏移量 offset=n。当n=1时，打印旋转后的字符串为"gabcdef"，当n=3时，
打印旋转后的字符串为"efgabcd"，以此类推
"""


class Solution:
    def rotate_string(self, s, offset: int):
        """
        :param s: string 一串字符串
        :param offset:int 一个整数
        :return:string
        """
        if len(s) > 0:  # 这里说明下，假如列表长度5，偏移12，这时候就要用到取模，实际偏移12%5=2个
            offset = offset % len(s)  # 重新定义offset，让其小于len(s)

        # 下面考虑下，长度10，偏移3，实际就是10-3:20-3，也就是7～17这几个字符
        new_s = (s + s)[len(s) - offset:2 * len(s) - offset]
        return new_s


if __name__ == '__main__':
    s = ["a", "b", "e", "g", "h", "f", "f", "y", "c", "l"]
    offset = 8
    solution = Solution()
    new_s = solution.rotate_string(s, offset)
    print("输入：", s, " ", "offset = ", offset)
    print("输出：", new_s)
