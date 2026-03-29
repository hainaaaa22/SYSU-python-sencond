# ====================== 【任务1】Student 数据类 ======================
class Student:
    # 初始化方法：接收姓名、性别、班级、学号、学院五个核心属性
    def __init__(self, name, gender, cls, student_id, college):
        self.name = name        # 姓名
        self.gender = gender    # 性别
        self.cls = cls          # 班级（名单中为数字1/2/3，直接用整型）
        self.student_id = student_id  # 学号
        self.college = college  # 学院

    # 重写__str__魔术方法，实现学生信息的友好打印
    def __str__(self):
        # 格式化输出，保证打印对象时能清晰看到所有信息
        return f"学号：{self.student_id}，姓名：{self.name}，性别：{self.gender}，班级：{self.cls}，学院：{self.college}"


# ====================== 【任务2】ExamSystem 逻辑控制类 ======================
class ExamSystem:
    # 初始化系统：传入学生名单文件路径
    def __init__(self, file_path="人工智能编程语言学生名单.txt"):
        self.file_path = file_path  # 学生文件路径
        self.student_list = []      # 存储所有学生对象的列表
        self.read_student_file()    # 一创建系统就自动读取文件

    # 修正后的读取学生名单方法
    def read_student_file(self):
        try:
            # 打开文件（UTF-8 编码防止乱码）
            with open(self.file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()

            # 遍历每一行，转为 Student 对象
            for index, line in enumerate(lines):
                line = line.strip()  # 去掉换行/空格
                if not line:
                    continue  # 跳过空行
                # 跳过第一行的表头（序号	姓名	性别	班级	学号	学院）
                if index == 0:
                    continue
                # 按制表符\t切割（原始文件是制表符分隔）
                parts = line.split("\t")
                # 按原始文件字段顺序取值
                name = parts[1]
                gender = parts[2]
                cls = int(parts[3])
                student_id = parts[4]
                college = parts[5]

                # 创建学生对象并加入列表
                student = Student(name, gender, cls, student_id, college)
                self.student_list.append(student)

            print(f"✅ 成功读取学生文件！共加载 {len(self.student_list)} 名学生信息")

        # 异常处理：文件找不到
        except FileNotFoundError:
            print(f"❌ 错误：未找到文件 {self.file_path}，请把文件放在同一目录！")
            self.student_list = []
        # 单独捕获整型转换错误，提示更友好
        except ValueError as e:
            print(f"❌ 数据格式转换错误：{e}，请检查学生名单文件的字段格式！")
            self.student_list = []
        # 其他异常
        except Exception as e:
            print(f"❌ 读取文件失败：{e}")
            self.student_list = []


# ====================== 检测代码 ======================
if __name__ == "__main__":
    # 1. 创建系统（自动读取学生名单）
    system = ExamSystem()

    # 2. 打印所有学生，验证是否读取成功
    print("\n===== 所有学生信息 =====")
    for stu in system.student_list:
        print(stu)

    # 3. 打印总人数
    print(f"\n📊 学生总数：{len(system.student_list)}")