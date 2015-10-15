try:
	from key import key
except ImportError:
	print "Must define key.py according to readme"
	exit(1)

import json
import urllib
import urllib2

ROOT = "https://api.meetup.com"
OPEN_EVENTS = "/2/open_events"

def _params_dict(**kwargs):
	params = kwargs
	params["key"] = key
	params["page"] = 20
	return params

def _params_string(**kwargs):
	param_dict = _params_dict(**kwargs)
	return urllib.urlencode(param_dict)

def _make_path(root, path, query):
	return "%s%s?%s" % (root, path, query)

def _fetch_raw_from_api(root=ROOT, path="/", **kwargs):
	full_path = _make_path(root, path, _params_string(**kwargs))
	try:
		response = urllib2.urlopen(full_path)
		html = response.read()
		return html
	except urllib2.HTTPError, e:
		print "Unable to fetch from %s: %s" % (full_path, e)
		return None


def _fetch_from_api(root=ROOT, path="/", **kwargs):
	raw = _fetch_raw_from_api(root, path, **kwargs)
	return raw and json.loads(raw)

### Endpoints ###
def open_events_global(query):
	return ApiResult(_fetch_from_api(path=OPEN_EVENTS, and_text="true", text=query), EventResult)
def open_events(query, lat, lon, radius):
	return ApiResult(_fetch_from_api(path=OPEN_EVENTS, and_text="true", text=query, lat=lat, lon=lon, radius=radius), EventResult)

### Codecs ###

class ApiResult():
	def __init__(self, json, result_serializer):
		self.results = [result_serializer(r) for r in json["results"]]
		self.meta = json["meta"]
	def __str__(self):
		return "Results: %s, Meta: %s" % (str(self.results), str(self.meta))

class EventResult():
	attrs_to_grab = ["name"]
	def __init__(self, json):
		group_json = json["group"]

		self.name = json["name"]
		self.distance = json["distance"] if "distance" in json else None

		if "venue" in json:
			venue_json = json["venue"]
			self.lat = venue_json["lat"]
			self.lon = venue_json["lon"]
		else:
			self.lat = group_json["group_lat"]
			self.lon = group_json["group_lon"]
