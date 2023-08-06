from qrunner.case import TestCase
from qrunner.core.android.driver import AndroidDriver
from qrunner.core.api.request import HttpRequest
from qrunner.core.h5.driver import H5Driver
from qrunner.core.ios.driver import IosDriver
from qrunner.core.web.driver import (ChromeConfig, EdgeConfig, FirefoxConfig,
                                     IEConfig, SafariConfig, WebDriver)
from qrunner.page import Page
from qrunner.page import Elem
from qrunner.running.runner import main
from qrunner.utils.config import config
from qrunner.utils.decorate import *
from qrunner.utils.dingtalk import DingTalk
from qrunner.utils.json_utils import get_schema
from qrunner.utils.log import logger
from qrunner.utils.mail import Mail

__version__ = "1.0.43"
__description__ = "Api/Web/App端自动化测试框架"
