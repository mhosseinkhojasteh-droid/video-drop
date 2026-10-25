"""Machine-specific locations. Override with environment variables on Windows/macOS:
  HIPHOP_VST3_DIR      e.g. C:/Program Files/Common Files/VST3/
  HIPHOP_SURGE_PATCHES e.g. C:/ProgramData/Surge XT/patches_factory/
"""
import os, platform
_win = platform.system() == 'Windows'
VST3_DIR = os.environ.get('HIPHOP_VST3_DIR', 'C:/Program Files/Common Files/VST3/' if _win else '/usr/lib/vst3/')
SURGE_DIR = os.environ.get('HIPHOP_SURGE_PATCHES', 'C:/ProgramData/Surge XT/patches_factory/' if _win else '/usr/share/surge-xt/patches_factory/')
