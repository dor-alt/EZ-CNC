import _winreg
import os


def query_reg(value_to_query):
    registry_path = "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion"
    try:
        key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, registry_path, 0, _winreg.KEY_ALL_ACCESS)
        path = _winreg.QueryValueEx(key, value_to_query)[0]
        _winreg.CloseKey(key)
        return str(path.lower())
    except Exception, e:
        return ""

def check_bit_architecure():
    try:
        os.environ["PROGRAMFILES(x86)"]
    except KeyError:
        return "Architecture: 32"
    return "Architecture: 64"


def get_windows_type():
    windows_product = query_reg("ProductName")
    return "Windows: " + windows_product


def get_windows_10_release():
    win_10_versions = {"1507": "Threshold 1", "1511": "Threshold 2 (November Update)", "1607": "Redstone 1 (Anniversary Update)",
                       "1703": "Redstone 2 (Creators Update)", "1709": "Redstone 3 (Fall Creators Update)", "1803": "Redstone 4 (April 2018 Update)",
                       "1809": "Redstone 5"}
    win_version = query_reg("ReleaseId")
    try:
        return win_version + " - " + win_10_versions[win_version]
    except KeyError:
        return ""



if __name__ == "__main__":
    # Use these functions to get thw windows version, architecure and for windows 10 - the release id
    print check_bit_architecure()
    print get_windows_type()
    print get_windows_10_release()