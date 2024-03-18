from versions import python_version, requests_version, pytest_version

def python_version():
 
    return sys.version_info

def requests_version():
    return requests.__version__

def pytest_version():
    return pytest.__version__
