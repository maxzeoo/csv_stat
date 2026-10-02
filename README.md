\# csvstat

> 纯Python标准库实现的CSV文件统计命令行工具，\*\*不使用pandas\*\*。



\## 项目介绍

读取CSV文件，输出数据统计摘要：

1\. 统计总行数据行数

2\. score列：最大值、最小值、平均值

3\. subject分组：每组记录数量、分组平均分

4\. 空值处理：空subject标记为`nothing`，跳过空score



本项目仅使用Python内置标准库：`csv`、`statistics`。



\## 环境要求

\- Python >=3.8

\- 仅使用Python自带标准库，无需pip安装包



\## 使用方法

1\. 将测试数据 `scores.csv` 放在项目根目录

2\. 运行脚本

```bash

python main.py



