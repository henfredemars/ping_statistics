
import asyncio
import aioping

from HostManager import HostManager
from SettingManager import SettingManager
from StatWriter import StatWriter


class PingStats:

  def __init__(self):
    self.host_manager = HostManager()
    self.settings = SettingManager()
    self.stat_writer = StatWriter()

    self.host_manager.read()
    self.settings.read()

    self.ping_interval = self.settings['PING_INTERVAL_S']
    self.ping_timeout = self.settings['PING_TIMEOUT_MS']

  async def ping_host(self, host):
    while True:
      try:
        latency = await aioping.ping(host, timeout=self.ping_timeout/1000) * 1000
        self.stat_writer.record(host, latency)
        await asyncio.sleep(self.ping_interval)
      except TimeoutError:
        self.stat_writer.record(host, self.ping_timeout)

  async def await_run(self):
    # register all the hosts
    for host in self.host_manager:
      self.loop.create_task(self.ping_host(host))
      print('Querying %s every %s seconds...' % (host, self.ping_interval))

    if not self.host_manager:
      print('No hosts defined')

    print('All ping tasks scheduled.')


  def run(self):
    self.loop = asyncio.get_event_loop()
    self.loop.create_task(self.await_run())

    try:
     self.loop.run_forever()
    except KeyboardInterrupt:
      print('Logging terminated!')
      self.stat_writer.write()


