import pytest


def test_ss():
    print('dddd')
    assert 5 == 5

if __name__ == "__main__":
    # pytest.main()  # 遍历相同目录下的所以test开头的用例
    pytest.main(['-q /Users/houmj/Documents/py_workplace/test_login.py'])  # 指定测试文件
    #pytest.main()  # 指定测试目录