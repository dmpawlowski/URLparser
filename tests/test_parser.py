from nose.tools import *
from parser.parser import *

url = "http://www.dmpawlowski.com:80/index.html;params"

def test_scheme():
  c = URLparser(url)
  assert_equal(c.scheme(),'http://')

def test_host():
  c=URLparser(url)
  assert_equal(c.host(),'www.dmpawlowski.com')

def test_port():
  c = URLparser(url)
  assert_equal(c.port(),'80')

def test_path():
  c = URLparser(url)
  assert_equal(c.path(),'/index.html')

def test_params():
  c = URLparser(url)
  assert_equal(c.params(),'params')
