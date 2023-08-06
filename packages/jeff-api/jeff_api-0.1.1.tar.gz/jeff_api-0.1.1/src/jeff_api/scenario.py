from . import client, server

class ScenarioTerminatedException(Exception):
  "The scenario is ended by the user forcibly."
  pass

class ScenarioNotStartedException(Exception):
  "The scenario is ended by the user forcibly."
  pass

class Scenario:
  def __init__(self, cli, srv):
    self.cli = cli
    self.srv = srv
    self.init = False
    self.token = None

  def _encode_json(j):
    return json.dumps(j).encode()
  
  def _decode_json(b):
    return json.loads(b.decode())

  def init_scenario(self, j):
    self.srv.server_socket.settimeout(5)
    j2 = j + {"sready": True, "saddr": self.srv.host, "sport": self.srv.port}
    self.cli._send(Scenario._encode_json(j))
    res = Scenario._decode_json(self.srv._waits_for())
    self.srv.server_socket.settimeout(None)
    if "stoken" not in res:
      raise ScenarioNotStartedException
    self.token = res["stoken"]
    self.init = True
 
  def continue_scenario(self, j):
    self.cli._send(Scenario._encode_json(j))

  def send_msg(self, msg):
    j = {"send": msg}
    if self.init:
      self.continue_scenario(j)
    else:
      self.init_scenario(j)

  def send_as_user(self, msg):
    j = {"send_as_user": msg}
    if self.init:
      self.continue_scenario(j)
    else:
      self.init_scenario(j)

  def send_status(self, msg_id, msg):
    j = {"send_status": {"id": msg_id, "msg": msg}}
    if self.init:
      self.continue_scenario(j)
    else:
      self.init_scenario(j)

  def send_error(self, msg):
    j = {"send_warning": msg}
    if self.init:
      self.continue_scenario(j)
    else:
      self.init_scenario(j)

  def store_cells(self, values_dict):
    j = {"store_in_memory": values_dict}
    if self.init:
      self.continue_scenario(j)
    else:
      self.init_scenario(j)
    
  def read_cells(self, keys_arr, buffer_size=8192):
    if not self.init:
      return None
    j = {"memory_cells": keys_arr}
    j = Scenario._decode_json(self._accept(Scenario._encode_json(j), buffer_size))
    if "memory_values" not in j:
      return None
    else:
      return j

  def listen(self):
    if not self.init:
      raise ScenarioNotStartedException
    j = Server._decode_json(self._waits_for())
    if "sfinish" in j:
      if j["sfinish"] is True:
        raise ScenarioTerminatedException
    return j
