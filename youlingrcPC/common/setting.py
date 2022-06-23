import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

# 测试用例目录
TEST_DIR = os.path.join(BASE_DIR, "report")
# 日志目录
LOG_DIR = os.path.join(BASE_DIR, "log")
# 元素控件
TEST_Element_YAML = os.path.join(BASE_DIR, "pages/company")
