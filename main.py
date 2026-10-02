import csv
import sys


# 判断分数类型#
def safe_float(s):
    if s is None:
        return None
    s = s.strip()
    if s == "":
        return None
    try:
        return float(s)
    except ValueError:
        return None


def cal_nums(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            print("文件为空或没有表头")
            return None
        for k in range(len(reader.fieldnames)):
            reader.fieldnames[k]=reader.fieldnames[k].strip()
        if 'subject' not in reader.fieldnames or 'score' not in reader.fieldnames:
            print('检测到表格数据问题：请检查您表格格式和数据')
            return None
        total_rows = 0
        score_all = {
            "max": None,
            "min": None,
            "sum_score": 0,
            "valid_score": 0
        }

        subject_groups = {}

        # 计算行数#
        for row in reader:
            total_rows += 1

            # 排除科目空值#
            subj = row.get("subject", "")
            if subj.strip() == "":
                subj = "未标记"
            # 这里如果读取不到科目，则输出为未标记#

            # 定义分组#
            if subj not in subject_groups:
                subject_groups[subj] = {'count': 0, 'sum_score': 0, 'valid_score': 0}
            subject_groups[subj]['count'] += 1

            # 记录分数，如果为空值，则不计入总计算，避免记为0#
            score_val = safe_float(row.get("score", ""))
            if score_val is not None:
                subject_groups[subj]['sum_score'] += score_val
                subject_groups[subj]['valid_score'] += 1
                # 排大小#
                if score_all['max'] is None:
                    score_all['max'] = score_val
                    score_all['min'] = score_val
                else:
                    score_all['max'] = max(score_all['max'], score_val)
                    score_all['min'] = min(score_all['min'], score_val)

                # 求总值的最大，最小，平均#
                score_all['sum_score'] += score_val
                score_all['valid_score'] += 1

        print(f"一共有{total_rows}行数据\n")
        if score_all['valid_score'] != 0:
            mean = score_all['sum_score'] / score_all['valid_score']
            print(f"最高分数:{score_all['max']}，最低分数:{score_all['min']}，平均分数:{mean:.2f}")
        else:
            print('分数缺少数据')
        for subj_name, item in subject_groups.items():
            score = item['sum_score']
            count = item['count']
            if item['valid_score'] != 0:
                subject_mean = score / item['valid_score']
                print(f'科目：{subj_name},记录数：{count},平均分：{subject_mean:.2f}')
            else:
                print(f'科目：{subj_name},记录数：{count},平均分：缺少数据')


def main():
    if len(sys.argv) < 2:
        print("用法：python csvstat.py 文件1.csv 文件2.csv...")
        sys.exit(1)
    file_paths = sys.argv[1:]
    for file_path in file_paths:
        print(f"正在处理你的文件：{file_path}")
        try:
            ret=cal_nums(file_path)
        except FileNotFoundError:
            print(f"该文件{file_path}不存在")
            continue
        except UnicodeDecodeError:
            print(f"错误：文件{file_path}编码不是utf-8，无法读取")
            continue
        else :
            if ret is  None:
                continue


if __name__ == "__main__":
    main()