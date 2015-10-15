#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import cherrypy

from mako.template import Template
from mako.lookup import TemplateLookup

from api import open_events_global, open_events

lookup = TemplateLookup(directories=['html'], output_encoding='utf-8', encoding_errors='replace')

presets = [u"prost", u"kanpai", u"sláinte"]

def render_index(**kwargs):
	tmpl = lookup.get_template("index.html")

	all_params = {"presets" : presets}
	all_params.update(kwargs)
	return tmpl.render_unicode(**all_params)

class Prost(object):
	def __init__(self):
		self.query = ProstQuery()

	def _cp_dispatch(self, vpath):
		if len(vpath) == 1:
			query_string = vpath.pop(0)
			cherrypy.request.params['query'] = query_string
			return self.query
		return vpath

	@cherrypy.expose
	def index(self):
		return render_index()

class ProstQuery(object):
	@cherrypy.expose
	def index(self, query=None, useGeo=False, lat=None, lon=None):
		if useGeo:
			res = open_events(query, lat, lon, 100).results
		else:
			res = open_events_global(query).results
		return render_index(results=res, query=query.decode("utf8"))

if __name__ == '__main__':
	cherrypy.quickstart(Prost(), "/", "conf/server.conf")
