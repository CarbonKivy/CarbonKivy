__app_name__ = "CarbonKivy"
__version__ = "0.0.4"

from kivy.logger import Logger

import carbonkivy.factory_registers
from carbonkivy.config import ROOT

Logger.info(f"{__app_name__}: {__version__}")
Logger.info(f"{__app_name__}: Installed at {ROOT}")
