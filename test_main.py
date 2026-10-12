import main
import pytest

def test_safe_float():
    assert main.safe_float("88") == 88.0
    assert main.safe_float(" 45 ") == 45.0
    assert main.safe_float("") is None
    assert main.safe_float("abc") is None
    assert main.safe_float("shuxue") is None
    assert main.safe_float("数学") is None
    assert main.safe_float("<UNK>") is None
    print('通过')

def test_cal_nums(tmp_path):
    csv_file = tmp_path / "test.csv"
    csv_content="""name, subject ,            score               
    张三,数学,80
    ,数学,80
    张三,,80
    ,,90
    ,语文,abc
    ,英语,75
    ,数学,
    ,语文,101"""
    csv_file.write_text(csv_content,encoding="utf-8")
    file_path_str=str(csv_file)
    main.cal_nums(file_path_str)


if __name__=='__main__':
    test_safe_float()
    test_cal_nums()
