# csv_stat
> 纯Python标准库实现的CSV文件统计命令行工具。

## 项目介绍
读取CSV文件，输出数据统计摘要：
1. 统计总行数据行数
2. score列：最大值、最小值、平均值（处理空值以及使用def safe_float处理脏数据）
3. subject分组：每组记录数量、分组平均分
4. 空值处理：空subject标记为`未标记`，跳过空score
5.分模块读取要处理的多个文件地址，并处理不存在文件和错误编码报错
6.空间复杂度降至O(k)


本项目仅使用Python内置标准库：`csv`、`sys`。

## 环境要求
- Python >=3.8
- 仅使用Python自带标准库，无需pip安装包

## csv格式要求
-必须要有表头：`subject,score`，不然DictReader读取会出错。

## 使用方法
1. 将测试数据 `scores.csv` 放在项目根目录
2. 运行脚本
```bash
python csvstat.py test1.csv test2.csv

