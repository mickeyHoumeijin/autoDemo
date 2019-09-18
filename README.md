# py_workplace
三种执行方式
1.单个用例里面，运行 __name__==__main__
2.运行runcase.py
3.命令行运行
 python3 -m pytest -n 3 --alluredir ./reports/xml        ====>执行用例，生成xml

allure generate --clean  reports/xml -o  reports/html     =====》生成html
