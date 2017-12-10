
import json

from collections import ChainMap


SETTING_FILE = 'settings.json'

DEFAULTS = {
  'PING_INTERVAL_S': 180,
  'PING_TIMEOUT_MS': 10000,
}

class SettingManager:

  def __init__(self, file_path=SETTING_FILE):
    self.map = ChainMap(DEFAULTS)
    self.file_path = file_path

  def __getitem__(self, k):
    return self.map[k]

  def read(self):
    try:
      with open(self.file_path) as fd:
        self.map = self.map.new_child(json.load(fd))
    except FileNotFoundError:
      print("No settings file found. Using default settings.")

  def write(self):
    with open(self.file_path, 'w') as fd:
      json.dump(self.map.maps[0], fd, sort_keys=True, indent=4)

