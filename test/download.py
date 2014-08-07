import urllib2
import socket

try:
  f = urllib2.urlopen('http://sports.qq.com/d/f_teams/1/42/', timeout = 10)
  code = f.getcode()
  if code < 200 or code >= 300:
    print 'Not 200'
  else:
    print code
except Exception, e:
  if isinstance(e, urllib2.HTTPError):
    print 'http error: {0}'.format(e.code)
  elif isinstance(e, urllib2.URLError) and isinstance(e.reason, socket.timeout):
    print 'url error: socket timeout {0}'.format(e.__str__())
  else:
    print 'misc error: ' + e.__str__()
