import csv
import statistics
import sys


with open(r'scores.csv',"r",encoding="utf-8") as f:
    reader = csv.DictReader(f)
    total_rows=0
    score_list=[]
    subject_groups={}

    #计算行数#
    for row in reader:
        total_rows+=1

        #排除空值#
        subj = row["subject"]
        if  subj.strip() == "":
            subj = "未标记"
        # 这里如果读取不到科目，则输出为nothing#

        if subj not in subject_groups:
                subject_groups[subj]={'count':0, 'score':[]}
        subject_groups[subj]['count']+=1

        #记录分数，如果为空值，则不计入总计算，避免记为0#
        score_str=row["score"].strip()
        if score_str !="":
            score_val=float(score_str)
            score_list.append(score_val)
            subject_groups[subj]['score'].append(score_val)


    if score_list :
        mean=statistics.mean(score_list)
        Max=max(score_list)
        Min=min(score_list)


    print(f"一共有{total_rows}行数据\n")
    if score_list:
        print(f'最高分数:{Max}，最低分数:{Min}，平均分数:{mean:.2f}')
    else:
        print('分数缺少数据')
    for subj_name, item in subject_groups.items():
        score=item['score']
        count=item['count']
        if  score:
            subject_mean = statistics.mean(score)
            print(f'科目：{subj_name},记录数：{count},平均分：{subject_mean:.2f}')
        else:
            print(f'科目：{subj_name},记录数：{count},平均分：缺少数据')

