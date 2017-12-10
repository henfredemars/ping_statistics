
import json

STAT_FILE = 'stats.json'

class StatWriter:

  def __init__(self, file_path=STAT_FILE):
    self.file_path = file_path
    self.host_times = {}  # host: [time, time...]

  def write(self):
    with open(self.file_path, 'w') as fd:
      json.dump(self.host_times, fd, sort_keys=True, indent=4)

  def record(self, host, time):
    if host in self.host_times.keys():
      self.host_times[host].append(time)
    else:
      self.host_times[host] = [time]

  def __iter__(self):
    return iter(self.hosts)

  def __in__(self, v):
    return v in self.hosts
