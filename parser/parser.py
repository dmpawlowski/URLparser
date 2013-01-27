import re

class URLparser(object):

  def __init__(self, url):
    self.url = url

  def scheme(self):
    s = re.search(r'^http://', self.url)
    return s.group()

  def host(self):
    s = re.search(r'//([\w.]+)[:|/]', self.url)
    return s.group(1)

  def port(self):
    s = re.search(r':(..)/', self.url)
    if s:
      return s.group(1)
    else:
      return '80'

  def path(self):
    s = re.search(r'//.*(/[\w.]+);*', self.url)
    return s.group(1)

  def params(self):
    s = re.findall(r';(\w+)=(\w+)', self.url)
    if s:
      return s
    else:
      return None

  def query(self):
    s = re.findall(r'\?(\w+)=(\w+)', self.url)
    if s:
      return s
    else:
      return None

  def frag(self):
    s = re.search(r'#(\w+)', self.url)
    return s.group(1)
