try:
	from key import key
except ImportError:
	print "Must define key.py according to readme"
	exit(1)

from datetime import date
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

category_ids="1,2,3,4,5,6,8,10,11,13,15,16,12,17,18,20,21,22,23,24,25,27,29,30,31,32,33,34,35"

### Endpoints ###
def open_events_global(query):
	return ApiResult(_fetch_from_api(path=OPEN_EVENTS, category=category_ids, and_text="true", text=query, fields="group_photo,category"), EventResult)
def open_events(query, lat, lon, radius):
	return ApiResult(_fetch_from_api(path=OPEN_EVENTS, category=category_ids, and_text="true", text=query, fields="group_photo,category", lat=lat, lon=lon, radius=radius), EventResult)

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
		self.description = "description" in json and json["description"]
		self.group_name = group_json["name"]

		self.photo_url = "group_photo" in group_json and group_json["group_photo"]["photo_link"]
		self.thumb_url = "group_photo" in group_json and group_json["group_photo"]["thumb_link"]

		self.time = date.fromtimestamp(json["time"] / 1000)
		self.month = self.time.strftime("%b")
		self.day = self.time.strftime("%d")

		self.category_id = group_json["category"]["id"]
		self.category_name = group_json["category"]["name"]

		self.url = json["event_url"]

		if "venue" in json:
			venue_json = json["venue"]
			self.lat = venue_json["lat"]
			self.lon = venue_json["lon"]
			self.city = venue_json["city"]
			self.state = "state" in venue_json and venue_json["state"]
			self.country = venue_json["country"]

			state_string = ", %s" % self.state if self.state else ""
			self.loc_string = "%s%s, %s" % (self.city, state_string, self.country.upper())
		else:
			self.lat = group_json["group_lat"]
			self.lon = group_json["group_lon"]
			self.loc_string = None

