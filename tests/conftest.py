

def pytest_addoption(parser):
    parser.addoption("--selected", action="store", default="")
    parser.addoption("--report", action="store", default="report.json")
    parser.addoption("--implementation", action="store_true", default=False, help="Run in development tests")
    parser.addoption("--deprecated", action="store_true", default=False, help="Run deprecated tests")

