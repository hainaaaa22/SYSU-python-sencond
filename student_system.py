# 引入作业允许的Python标准库
import random
import os
import time


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


# ====================== 【任务2-7】ExamSystem 逻辑控制类（完整功能） ======================
class ExamSystem:
    def __init__(self, file_path="人工智能编程语言学生名单.txt"):
        self.file_path = file_path  # 学生文件路径
        self.student_list = []  # 存储所有学生对象的列表
        self.read_student_file()  # 初始化自动读取文件
        self.shuffled_students = []  # 存储打乱后的学生列表，供考场表/准考证复用

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

    # 【任务4】随机点名方法
    def random_call(self):
        if not self.student_list:
            print("❌ 暂无学生数据，无法执行随机点名！")
            return

        total = len(self.student_list)
        print(f"\n===== 随机点名功能 =====")
        print(f"当前可点名人数范围：1 - {total}")
        try:
            num = int(input(f"请输入需要点名的学生数量："))
            if num < 1 or num > total:
                print(f"❌ 输入错误！数量必须在1-{total}之间，请重新输入！")
                return
            # 无放回抽样，保证不重复
            random_students = random.sample(self.student_list, num)
            print(f"\n✅ 本次随机点名{num}名学生，结果如下：")
            for i, stu in enumerate(random_students, 1):
                print(f"{i}. 姓名：{stu.name}，学号：{stu.student_id}，学院：{stu.college}")
        except ValueError:
            print(f"❌ 输入错误！请输入纯数字的有效数量！")

    # 【任务5】静态方法 - 路径拼接
    @staticmethod
    def join_path(*args):
        """
        静态方法：统一处理路径拼接，兼容Windows/Mac/Linux系统
        :param args: 路径片段，如("准考证", "01.txt")、(".", "考场安排表.txt")
        :return: 拼接后的完整路径
        """
        return os.path.join(*args)

    # 【任务6】生成考场安排表方法
    def generate_exam_table(self):
        # 前置校验：无学生数据直接返回
        if not self.student_list:
            print("❌ 暂无学生数据，无法生成考场安排表！")
            return False

        # 随机打乱学生顺序，结果存入实例属性供准考证复用
        self.shuffled_students = random.sample(self.student_list, len(self.student_list))
        # 获取格式化生成时间（严格按作业要求：2026-03-23 10:00:00）
        create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # 拼接考场安排表文件路径（根目录）
        table_path = self.join_path(".", "考场安排表.txt")

        try:
            # 写入考场安排表文件（UTF-8编码防止中文乱码）
            with open(table_path, "w", encoding="utf-8") as f:
                # 首行写入生成时间（作业硬性要求）
                f.write(f"生成时间：{create_time}\n")
                # 遍历打乱后的学生，按【座位号 姓名 学号】格式写入
                for seat_num, stu in enumerate(self.shuffled_students, 1):
                    f.write(f"{seat_num}\t{stu.name}\t{stu.student_id}\n")

            print(f"\n✅ 考场安排表生成成功！")
            print(f"📁 文件路径：{os.path.abspath(table_path)}")
            return True  # 返回成功标识，供准考证方法判断
        # 处理文件写入异常
        except PermissionError:
            print(f"❌ 生成失败：无文件写入权限，请检查目录权限！")
            return False
        except Exception as e:
            print(f"❌ 考场安排表生成失败：{e}")
            return False

    # 【任务7】新增：生成准考证文件夹+独立文件（最后一个功能）
    def generate_admission_ticket(self):
        # 前置校验1：无学生数据直接返回
        if not self.student_list:
            print("❌ 暂无学生数据，无法生成准考证！")
            return
        # 前置校验2：未生成考场安排表（无打乱数据），先提示生成
        if not self.shuffled_students:
            print("⚠️  未检测到考场安排数据，请先生成考场安排表！")
            # 自动尝试生成考场安排表
            if not self.generate_exam_table():
                return

        # 核心步骤1：拼接准考证文件夹路径（根目录）
        ticket_dir = self.join_path(".", "准考证")
        # 核心步骤2：创建文件夹，exist_ok=True兼容文件夹已存在的情况（不报错）
        os.makedirs(ticket_dir, exist_ok=True)

        try:
            # 遍历打乱后的学生，生成对应序号的准考证文件
            for seat_num, stu in enumerate(self.shuffled_students, 1):
                # 文件名补零为2位（01.txt、02.txt...10.txt），符合作业要求
                file_name = f"{seat_num:02d}.txt"
                # 拼接单个准考证文件的完整路径
                ticket_file = self.join_path(ticket_dir, file_name)
                # 写入准考证信息：考场座位号、姓名、学号
                with open(ticket_file, "w", encoding="utf-8") as f:
                    f.write(f"考场座位号：{seat_num}\n")
                    f.write(f"姓名：{stu.name}\n")
                    f.write(f"学号：{stu.student_id}\n")

            print(f"\n✅ 准考证全部生成成功！")
            print(f"📁 准考证文件夹路径：{os.path.abspath(ticket_dir)}")
            print(f"📄 共生成 {len(self.shuffled_students)} 份准考证文件")
        except PermissionError:
            print(f"❌ 生成失败：无文件写入权限，请检查目录权限！")
        except Exception as e:
            print(f"❌ 准考证生成失败：{e}")


# ====================== 【任务1-7】综合检测代码（完整功能测试） ======================
if __name__ == "__main__":
    # 1. 初始化系统（自动读取学生数据）
    system = ExamSystem()
    if not system.student_list:
        exit()  # 无学生数据则直接退出

    # 2. 测试学号查找功能
    print("\n===== 学生信息查找功能 =====")
    student_id = input("请输入要查询的学生学号：")
    system.search_student_by_id(student_id)

    # 3. 测试随机点名功能
    system.random_call()

    # 4. 测试静态方法-路径拼接
    print("\n===== 静态方法-路径拼接 测试 =====")
    exam_table_path = ExamSystem.join_path(".", "考场安排表.txt")
    print(f"考场安排表完整路径：{exam_table_path}")
    ticket_path = system.join_path("准考证", "01.txt")
    print(f"准考证01.txt完整路径：{ticket_path}")

    # 5. 测试生成考场安排表功能
    print("\n===== 生成考场安排表功能 =====")
    system.generate_exam_table()

    # 6. 【任务7】测试生成准考证功能
    print("\n===== 生成准考证功能 =====")
    system.generate_admission_ticket()