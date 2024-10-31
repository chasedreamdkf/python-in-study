import sqlite3


if __name__ == "__main__":
    conn = sqlite3.connect('./temp.db')      # 创建链接数据库对象
    # 操作数据库
    cursor = conn.cursor()

    # # 建表
    # sql = '''
    # create table student(
    # id integer primary key autoincrement not null,
    # name text,
    # age integer
    # )
    # '''
    # cursor.execute(sql)

    # # 插入数据
    # data = (1, 'Amy', 18)
    # sql = "insert into student values (?, ?, ?)"
    # cursor.execute(sql, data)               # 插入单个数据
    # data = [
    #     (2, 'Tom', 19),
    #     (3, 'Jim', 20)
    # ]
    # cursor.executemany(sql, data)           # 插入多个数据

    # # 查询数据
    # sql = 'select * from student'
    # cursor.execute(sql)
    # for item in cursor:
    #     print(item)

    # # 条件查询
    # sql = 'select * from student where age=18'
    # cursor.execute(sql)
    # for item in cursor:
    #     print(item)

    # # 数据修改
    # sql = "update student set age = 20 where name = 'Tom'"
    # cursor.execute(sql)

    # # 条件删除表记录
    # sql = "delete from student where name='Mike'"
    # cursor.execute(sql)

    # # 清楚表中所有记录
    # sql = 'delete from student'
    # cursor.execute(sql)

    # # 删除表
    # sql = 'drop table student'
    # cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()                        # 关闭数据库文件
