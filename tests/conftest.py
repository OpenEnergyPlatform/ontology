

def pytest_addoption(parser):
    parser.addoption("--selected", action="store", default="")
    parser.addoption("--report", action="store", default="report.json")