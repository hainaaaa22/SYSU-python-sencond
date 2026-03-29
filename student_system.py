# ====================== 【任务1】Student 数据类 ======================
class Student:
    def __init__(self, name, gender, cls, student_id, college):
        self.name = name  # 姓名
        self.gender = gender  # 性别
        self.cls = cls  # 班级（整型）
        self.student_id = student_id  # 学号（字符串）
        self.college = college  # 学院

    def __str__(self):
        return f"学号：{self.student_id}，姓名：{self.name}，性别：{self.gender}，班级：{self.cls}，学院：{self.college}"


# ====================== 【任务2-4】ExamSystem 逻辑控制类 ======================
import random  # 引入Python标准库，符合作业要求


class ExamSystem:
    def __init__(self, file_path="人工智能编程语言学生名单.txt"):
        self.file_path = file_path  # 学生文件路径
        self.student_list = []  # 存储所有学生对象的列表
        self.read_student_file()  # 初始化自动读取文件

    # 读取学生名单文件方法（修正版）
    def read_student_file(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()

            for index, line in enumerate(lines):
                line = line.strip()
                if not line or index == 0:  # 跳过空行+表头行
                    continue
                parts = line.split("\t")
                name = parts[1]
                gender = parts[2]
                cls = int(parts[3])
                student_id = parts[4]
                college = parts[5]
                # 创建学生对象并加入列表
                student = Student(name, gender, cls, student_id, college)
                self.student_list.append(student)

            print(f"✅ 成功读取学生文件！共加载 {len(self.student_list)} 名学生信息")

        except FileNotFoundError:
            print(f"❌ 错误：未找到文件 {self.file_path}，请把文件放在同一目录！")
            self.student_list = []
        except ValueError as e:
            print(f"❌ 数据格式转换错误：{e}，请检查学生名单文件的字段格式！")
            self.student_list = []
        except Exception as e:
            print(f"❌ 读取文件失败：{e}")
            self.student_list = []

    # 【任务3】按学号查找学生方法
    def search_student_by_id(self, input_id):
        for student in self.student_list:
            if student.student_id == input_id:
                print("\n✅ 查询到学生信息：")
                print(student)
                return
        print(f"\n❌ 未查询到学号为【{input_id}】的学生，请检查学号是否输入正确！")

    # 【任务4】随机点名方法（核心新功能）
    def random_call(self):
        # 先判断是否有学生数据，避免无数据时报错
        if not self.student_list:
            print("❌ 暂无学生数据，无法执行随机点名！")
            return

        total = len(self.student_list)
        print(f"\n===== 随机点名功能 =====")
        print(f"当前可点名人数范围：1 - {total}")
        try:
            # 获取用户输入并转换为整型
            num = int(input(f"请输入需要点名的学生数量："))
            # 校验输入数量是否在合法范围
            if num < 1 or num > total:
                print(f"❌ 输入错误！数量必须在1-{total}之间，请重新输入！")
                return
            # 随机抽取不重复的学生（sample：无放回抽样，完美实现不重复）
            random_students = random.sample(self.student_list, num)
            # 打印点名结果
            print(f"\n✅ 本次随机点名{num}名学生，结果如下：")
            for i, stu in enumerate(random_students, 1):
                print(f"{i}. 姓名：{stu.name}，学号：{stu.student_id}，学院：{stu.college}")
        # 处理用户输入非数字的异常（ValueError）
        except ValueError:
            print(f"❌ 输入错误！请输入纯数字的有效数量！")


# ====================== 【任务1-4】综合检测代码 ======================
if __name__ == "__main__":
    # 1. 初始化系统（自动读取学生数据）
    system = ExamSystem()
    if not system.student_list:
        exit()  # 无学生数据则直接退出，避免后续功能报错

    # 2. 测试学号查找功能
    print("\n===== 学生信息查找功能 =====")
    student_id = input("请输入要查询的学生学号：")
    system.search_student_by_id(student_id)

    # 3. 测试随机点名功能（核心测试）
    system.random_call()