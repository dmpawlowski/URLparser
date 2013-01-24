import re

class URLparser(object):

  def __init__(self, url):
    self.url = url

  def scheme(self):
    s = re.search(r'^http://', self.url)
    return s.group()

  def host(self):
    s = re.search(r'//(.+):', self.url)
    return s.group(1)

  def port(self):
    s = re.search(r':(..)/', self.url)
    return s.group(1)

  def path(self):
    s = re.search(r'//.*(/.*);', self.url)
    return s.group(1)

  def params(self):
    s = re.search(r';(.+)', self.url)
    return s.group(1)