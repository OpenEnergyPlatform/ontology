

def pytest_addoption(parser):
    parser.addoption("--selected", action="store", default="")
    parser.addoption("--report", action="store", default="report.json")
    parser.addoption("--deprecated", action="store_true", default=False, help="Run deprecated tests")