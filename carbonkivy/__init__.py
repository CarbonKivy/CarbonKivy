__app_name__ = "CarbonKivy"
__version__ = "0.0.1.dev"

from kivy.logger import Logger

from carbonkivy.config import ROOT

Logger.info(f"{__app_name__}: {__version__}")
Logger.info(f"{__app_name__}: Installed at {ROOT}")

import carbonkivy.factory_registers
