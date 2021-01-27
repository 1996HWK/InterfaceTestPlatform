from datetime import datetime
import pytest
from py._xmlgen import html

def pytest_configure(config):
    # 添加接口地址与项目名称
    config._metadata["项目名称"] = "接口自动化"
    config._metadata['接口地址'] = 'https://www.cnblogs.com/linuxchao/'


    # 删除Java_Home
    config._metadata.pop("JAVA_HOME")
    config._metadata.pop("Packages")
    config._metadata.pop("Platform")
    config._metadata.pop("Plugins")
    config._metadata.pop("Python")

@pytest.mark.optionalhook
def pytest_html_results_summary(prefix):
    prefix.extend([html.p("所属部门: xx测试中心")])
    prefix.extend([html.p("测试人员: Linux超")])



@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(report)
    report.nodeid = report.nodeid.encode("utf-8").decode("utf-8")  # 设置编码显示中文



def pytest_html_report_title(report):

    report.title = "My very own title!"

def pytest_html_results_table_header(cells):
    cells.insert(2, html.th("Description"))
    cells.insert(1, html.th("Time", class_="sortable time", col="time"))
    cells.pop()


def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report))
    cells.insert(1, html.td(datetime.utcnow(), class_="col-time"))
    cells.pop()