
#自动生成用户名，字母开头，五位组成
import random
import string


def generate_random_string(length=5):
    """
    生成一个指定长度的随机字符串，该字符串必须以字母开头，默认长度为5。

    参数:
    length (int): 要生成的随机字符串的长度，必须大于等于1。

    返回:
    str: 生成的随机字符串。
    """
    if length < 1:
        raise ValueError("Length must be at least 1")

        # 定义可用的字符集：小写字母和大写字母
    letters = string.ascii_letters  # 包含所有小写和大写字母
    digits_and_letters = string.ascii_letters + string.digits  # 包含所有小写和大写字母以及数字
    # print(digits_and_letters)
    # 随机选择一个字母作为字符串的第一个字符
    first_char = random.choice(letters)
    # print(first_char)
    # 随机选择剩余的 length-1 个字符（可以是字母或数字）
    remaining_chars = ''.join(random.choices(digits_and_letters, k=length - 1))
    # print(remaining_chars)

    # 组合成完整的字符串
    random_string = first_char + remaining_chars
    # print(random_string)
    return random_string


# 示例使用
random_str = generate_random_string()
# print(random_str)


