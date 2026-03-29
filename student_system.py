# 定义Student数据类，封装学生核心属性
class Student:
    # 初始化方法：接收姓名、性别、班级、学号、学院五个核心属性
    def __init__(self, name, gender, cls, student_id, college):
        self.name = name  # 姓名
        self.gender = gender  # 性别
        self.cls = cls  # 班级（名单中为数字1/2/3，直接用整型）
        self.student_id = student_id  # 学号
        self.college = college  # 学院

    # 重写__str__魔术方法，实现学生信息的友好打印
    def __str__(self):
        # 格式化输出，保证打印对象时能清晰看到所有信息
        return f"学号：{self.student_id}，姓名：{self.name}，性别：{self.gender}，班级：{self.cls}，学院：{self.college}"


# 【检测代码】直接运行该文件即可验证Student类是否实现成功
# 模拟从文件中读取的单条学生数据，创建Student对象
if __name__ == "__main__":
    # 以名单中第一条数据（张三）为例创建实例
    stu1 = Student("张三", "男", 1, "2001101", "电气")
    # 打印对象，验证__str__方法是否生效
    print(stu1)

    # 额外验证：直接访问对象的单个属性，确认初始化正常
    print("单独获取姓名：", stu1.name)
    print("单独获取学号：", stu1.student_id)

    # 再创建一个实例（李四），验证多对象创建无问题
    stu2 = Student("李四", "女", 2, "2001102", "能动")
    print("\n第二个学生信息：")
    print(stu2)