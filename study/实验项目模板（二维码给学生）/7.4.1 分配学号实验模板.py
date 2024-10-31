# ------------      -------    --------    -----------    -----------
# @File       : 7.4.1 分配学号实验模板.py    
# @Contact    : vasp@qq.com
# @Copyright  : 2018-2025, Wuhan University of Technology
# @Modify Time: 2021/4/27 16:17
# @Author     : 赵广辉
# @Version    : 1.0
# @License    : 仅限用于Python程序设计基础实践教程(赵广辉,高等教育出版社)配套实验
# ------------      -------    --------    -----------    -----------
def read_file(filename):
    """接收文件名为参数，根据逗号将每行切分为列表，返回二维列表。
    @参数 filename：文件名，字符串类型
    """
    with open(filename, 'r', encoding='utf-8') as file:  # 只读模式打开文件
        file_lst = [line.strip().split(',') for line in file]
        # 文件全部内容读取出来放入列表中，每个元素为一行字符串
    return file_lst                                  # 以列表形式返回文件中的数据


def student_id(ls_student, ls_school, ls_major):
    """接收学生列表、学院列表和专业列表为参数，生成学号并与学生信息合并为一个包含学生详细信息的列表，
    返回学生详细信息列表。
    @参数 ls_student：学生信息列表，列表类型
    @参数 ls_school：学院信息列表，列表类型
    @参数 ls_major：专业信息列表，列表类型
    """
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================


def student_info(stu_name, ls_student):
    """接收学生名和学生信息列表为参数，返回学生详细信息。
    @参数 stu_name：学生名，字符串类型
    @参数 ls_student：学生信息列表，列表类型
    """
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================


def classmate(stu_class, ls_student):
    """接收学生班级和学生列表为参数，返回同班同学的信息，列表类型。
    @参数 stu_class：学生班级，字符串类型
    @参数 ls_student：学生信息列表，列表类型
    """
    # =======================================================
    # 此处去掉注释符号“#”并补充你的代码

    # =======================================================


if __name__ == '__main__':
    stuName = input()                                                  # 输入学生姓名
    stuClass = input()                                                 # 输入班级
    student_list = read_file('studentList.csv')[1:]                    # 获得学生信息列表,去掉标题行
    school_code = read_file('schoolCode.csv')                          # 获得学院信息列表
    major_code = read_file('MajorCode.csv')                            # 获得专业信息列表
    studentDetail = student_id(student_list, school_code, major_code)  # 调用函数计算ID并插入到列表中
    print(*student_info(stuName, studentDetail))                       # 输出学生信息
    ls_classmate = classmate(stuClass, studentDetail)                  # 返回同班同学信息列表
    for classmate in ls_classmate:                                     # 逐个输出同学信息
        print(*classmate)
