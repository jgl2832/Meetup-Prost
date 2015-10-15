try:
	from key import key
except ImportError:
	print "Must define key.py according to readme"
	exit(1)

import urllib, urllib2

ROOT = "https://api.meetup.com"
OPEN_EVENTS = "/2/open_events"

def _params_dict(**kwargs):
	params = kwargs
	params["key"] = key
	return params

def _params_string(**kwargs):
	param_dict = _params_dict(**kwargs)
	return urllib.urlencode(param_dict)

def _make_path(root, path, query):
	return "%s%s?%s" % (root, path, query)

def _fetch_from_api(root=ROOT, path="/", **kwargs):
	full_path = _make_path(root, path, _params_string(**kwargs))
	try:
		response = urllib2.urlopen(full_path)
		html = response.read()
		return html
	except urllib2.HTTPError, e:
		print "Unable to fetch from %s: %s" % (full_path, e)
		return None


### Endpoints ###
def open_events(query):
	return _fetch_from_api(path=OPEN_EVENTS, text=query)
