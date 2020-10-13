from pathlib import Path

BASE_PATH = Path(__file__).absolute().parent  #工程的绝对路径

p=Path(BASE_PATH)

DATAS_PATH = p.joinpath("datas")  #数据路径
CASE_PATH = p.joinpath('case')   #用例路径
REPORT_PATH = p.joinpath('report')   #报告路径