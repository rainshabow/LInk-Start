import csv
from student import Student

def export_students_to_csv(students: list[Student]):
    path = "save.csv"

    """将学生列表写入 CSV（utf-8-sig，包含表头）"""
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["学生ID", "学生名", "年龄", "专业"])
        for s in students:
            writer.writerow([s.id, s.name, s.age, s.major])
    print(f"已导出 {len(students)} 条学生数据到 {path}")

def import_students_from_csv():
    path = "save.csv"

    """从 CSV 读取学生列表，返回 Student 对象列表。遇到错误的年龄字段设为 0。"""
    students = []
    try:
        with open(path, "r", newline="", encoding="utf-8-sig") as f:
            reader = csv.reader(f)
            # 跳过表头（如果存在）
            header = next(reader, None)
            for row in reader:
                if not row:
                    continue
                id = row[0] if len(row) > 0 else ""
                name = row[1] if len(row) > 1 else ""
                age_str = row[2] if len(row) > 2 else "0"
                major = row[3] if len(row) > 3 else ""
                try:
                    age = int(age_str)
                except ValueError:
                    age = 0
                students.append(Student(id, name, age, major))
    except FileNotFoundError:
        print(f"未找到文件: {path}")

    return students