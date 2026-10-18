import main
import pytest
import sys,subprocess
from pathlib import Path


#测试main函数L95
def test_main_argvexit(monkeypatch):

    monkeypatch.setattr(sys, 'argv', ['main.py'])
    with pytest.raises(SystemExit) as e:
        main.main()
    assert e.value.code == 1

def test_main_argvprint(monkeypatch,capsys):

    monkeypatch.setattr(sys, 'argv', ['main.py'])
    with pytest.raises(SystemExit) as e:
        main.main()
    assert '用法：python main.py 文件1.csv 文件2.csv...' in capsys.readouterr().out

#测试main函数L103
def test_main_argvprint2(monkeypatch,capsys):
    monkeypatch.setattr(sys, 'argv', ['main.py','test.csv'])
    with pytest.raises(SystemExit) as e:
        main.main()
    assert '该文件test.csv不存在' in capsys.readouterr().out

#测试main函数L106
def test_main_argvprint3(monkeypatch,capsys,tmp_path):
    csv_file= tmp_path / 'test.csv'
    csv_content="""subject,score
    数学,79
    """
    csv_file.write_text(csv_content, encoding='gbk')
    monkeypatch.setattr(sys, 'argv', ['main.py', str(csv_file)])
    with pytest.raises(SystemExit) as e:
        main.main()
    assert f'错误：文件{str(csv_file)}编码不是utf-8，无法读取' in capsys.readouterr().out

#测试main函数L110
def test_main_argvprint4(monkeypatch,capsys,tmp_path):
    csv_file1 = tmp_path / "open1.csv"
    csv_count1 = (""",score
    数学,79
    """)
    csv_file1.write_text(csv_count1, encoding="utf-8")

    monkeypatch.setattr(sys,'argv',['main.py',str(csv_file1)])
    with pytest.raises(SystemExit) as e:
        main.main()
    captured = capsys.readouterr()
    assert f'检测到表格数据问题：请检查您表格格式和数据' in captured.out
    assert f'该文件{str(csv_file1)}内容不存在或存在错误' in captured.out

def test_main_argvprint5(monkeypatch,capsys,tmp_path):
    csv_file2 = tmp_path / "open2.csv"
    csv_count2 = (""",
    数学,79
    """)
    csv_file2.write_text(csv_count2, encoding="utf-8")

    monkeypatch.setattr(sys,'argv',['main.py',str(csv_file2)])
    with pytest.raises(SystemExit) as e:
        main.main()
    captured = capsys.readouterr()
    assert f'该文件{str(csv_file2)}内容不存在或存在错误' in captured.out



#测试成绩
def test_score_safe(capsys,tmp_path):
    csv_file = tmp_path / "score.csv"
    csv_content="""subject,score
数学,-1
数学,0
数学,99
数学,100
数学,101
"""
    csv_file.write_text(csv_content,encoding="utf-8")
    file_path_str=str(csv_file)
    main.cal_nums(file_path_str)
    captured = capsys.readouterr()
    assert '一共有5行数据' in captured.out
    assert '有2条成绩登记错误' in captured.out
    assert '最高分数:100.0，最低分数:0.0，平均分数:66.33' in captured.out
    assert '科目：数学,记录数：5,平均分：66.33' in captured.out

def test_score_safe1(capsys,tmp_path):
    csv_file = tmp_path / "score.csv"
    csv_content="""subject,score
数学,"""
    csv_file.write_text(csv_content,encoding="utf-8")
    file_path_str=str(csv_file)
    main.cal_nums(file_path_str)
    captured = capsys.readouterr()
    assert '分数缺少数据' in captured.out
  

def test_safe_float():
    assert main.safe_float("88") == 88.0
    assert main.safe_float(" 45 ") == 45.0
    assert main.safe_float("") is None
    assert main.safe_float("abc") is None
    assert main.safe_float("shuxue") is None
    assert main.safe_float("数学") is None

#测试科目
def test_subj(capsys,tmp_path):
    csv_file = tmp_path / "subj.csv"
    csv_content="""subject,score
数学,79
,80
语文,"""
    csv_file.write_text(csv_content,encoding="utf-8")
    file_path_str=str(csv_file)
    main.cal_nums(file_path_str)
    captured = capsys.readouterr()
    assert '最高分数:80.0，最低分数:79.0，平均分数:79.50' in captured.out
    assert '科目：未标记,记录数：1,平均分：80.00' in captured.out
    assert '科目：语文,记录数：1,平均分：缺少数据' in   captured.out

def test_nopecsv(tmp_path):
    MAIN=Path(__file__).parent/'main.py'
    r=subprocess.run([sys.executable, str(MAIN), tmp_path / "nope.csv"],capture_output=True)
    assert r.returncode == 1

def test_emptycsv(tmp_path):
    MAIN=Path(__file__).parent/'main.py'
    csv_file=tmp_path/'empty.csv'
    csv_file.write_text("""""",encoding="utf-8")
    r=subprocess.run([sys.executable, str(MAIN), str(csv_file)],capture_output=True)
    assert r.returncode == 1
sys
def test_nocolcsv(tmp_path):
    MAIN=Path(__file__).parent/'main.py'
    csv_file=tmp_path/'nocol.csv'
    csv_file.write_text("""name,score
a,1""",encoding="utf-8")
    r=subprocess.run([sys.executable, str(MAIN), str(csv_file)],capture_output=True)
    assert r.returncode == 1

if __name__=='__main__':
    test_score_safe()
    test_score_safe1()
    test_safe_float()
    test_subj()
    test_main_argvexit()
    test_main_argvprint()
    test_main_argvprint2()
    test_main_argvprint3()
    test_main_argvprint4()
    test_main_argvprint5()
    test_nopecsv()
    test_emptycsv()
    test_nocolcsv()

