
import json

HOSTS_FILE = 'hosts.json'

class HostManager:

  def __init__(self, file_path=HOSTS_FILE):
    self.file_path = file_path
    self.hosts = []

  def read(self):
    with open(self.file_path) as fd:
      self.hosts = json.load(fd)

  def write(self):
    with open(self.file_path, 'w') as fd:
      json.dump(self.hosts, fd, sort_keys=True, indent=4)

  def add_host(self, host):
    self.hosts.append(host)

  def __iter__(self):
    return iter(self.hosts)

  def __in__(self, v):
    return v in self.hosts

  def __bool__(self):
    return bool(self.hosts)
