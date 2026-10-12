import main
import pytest



#测试文件打开
def test_safe_open(tmp_path):
    csv_file1 = tmp_path / "open1.csv"
    csv_count1 = ("""subject,score
    数学,79
    """)
    csv_file1.write_text(csv_count1, encoding="gbk")

    csv_file2 = tmp_path / "open2.csv"
    csv_count2 = (""",score
    数学,79
    """)
    csv_file2.write_text(csv_count2, encoding="utf-8")

    csv_file3 = tmp_path / "open3.csv"

    file_path1_str = str(csv_file1)
    file_path2_str = str(csv_file2)

    with pytest.raises(FileNotFoundError):
        main.cal_nums(csv_file3)

    with pytest.raises(UnicodeDecodeError):
        main.cal_nums(file_path1_str)

    assert main.cal_nums(file_path2_str) is  None 

#测试成绩
def test_score_safefloat(tmp_path):
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
    result=main.cal_nums(file_path_str)
    
    assert result is True
    assert main.safe_float("88") == 88.0
    assert main.safe_float(" 45 ") == 45.0
    assert main.safe_float("") is None
    assert main.safe_float("abc") is None
    assert main.safe_float("shuxue") is None
    assert main.safe_float("数学") is None
    print('通过')

#测试科目
def test_subj(tmp_path):
    csv_file = tmp_path / "subj.csv"
    csv_content="""subject,score
    数学,79
    ,80
    """
    csv_file.write_text(csv_content,encoding="utf-8")
    file_path_str=str(csv_file)
    result=main.cal_nums(file_path_str)
    assert result is True




if __name__=='__main__':
    test_score_safefloat()
    test_safe_open()
