def read_file(file):
    """
    @参数 file:文件名，字符串类型
    读文件中的学校名到列表中，返回排名前10学校集合，集合类型。
    """
    ls = []
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            ls.append(line.split()[1])
            if len(ls) == 10:
                break
    set_ls = set(ls)
    return set_ls


def either_in_top(alumni, soft):
    """
    @参数 alumni：alumni大学排行榜中排名前10的学校的集合，集合类型
    @参数 soft：soft大学排行榜中排名前10的学校的集合，集合类型
    接收两个排行榜前10高校名字集合，返回在这两个排行榜中均名列前10的学校名。
    """
    g = alumni & soft
    return g


def all_in_top(alumni, soft):
    """
    @参数 alumni：alumni大学排行榜中排名前10的学校的集合，集合类型
    @参数 soft：soft大学排行榜中排名前10的学校的集合，集合类型
    接收两个排行榜前10高校名字集合，
    返回在两个榜单中名列前10的所有学校名。
    """
    b = alumni | soft
    return b


def only_alumni(alumni, soft):
    """
    @参数 alumni：alumni大学排行榜中排名前10的学校的集合，集合类型
    @参数 soft：soft大学排行榜中排名前10的学校的集合，集合类型
    接收两个排行榜前10高校名字集合，返回在alumni榜单中名列前10但soft榜单中未进前10的学校名。
    """
    s = alumni | soft - soft
    return s


def only_one(alumni, soft):
    """
    @参数 alumni：alumni大学排行榜中排名前10的学校的集合，集合类型
    @参数 soft：soft大学排行榜中排名前10的学校的集合，集合类型
    接收两个排行榜前10高校名字集合，返回在alumni和soft榜单中名列前10，
    但不同时出现在两个榜单的学校名。
    """
    s = alumni ^ soft
    return s


if __name__ == '__main__':
    alumni_set = read_file('alumni.txt')
    soft_set = read_file('soft.txt')
    print(f'两榜单中均名列前10的学校: {either_in_top(alumni_set, soft_set)}')
    print(f'两榜单名列前10的所有学校: {all_in_top(alumni_set, soft_set)}')
    print(f'alumni中名列前10，soft中未进前10的学校: {only_alumni(alumni_set, soft_set)}')
    print(f'不同时出现在两个榜单前10的学校: {only_one(alumni_set, soft_set)}')
