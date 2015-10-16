#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import cherrypy

from mako.template import Template
from mako.lookup import TemplateLookup

from api import open_events_global, open_events
from presets import presets, presets_by_name

lookup = TemplateLookup(directories=['html'], output_encoding='utf-8', encoding_errors='replace')

# filter out events that are obviously not social
# change favicon

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
			query_string = vpath.pop(0).decode("utf8")
			preset = query_string in presets_by_name and presets_by_name[query_string]
			if preset:
				cherrypy.request.params['query'] = query_string.encode("utf8")
				cherrypy.request.params['use_preset'] = preset
				return self.query
			else:
				return self
		return vpath

	@cherrypy.expose
	def index(self):
		return render_index()

class ProstQuery(object):
	@cherrypy.expose
	def index(self, query=None, use_preset=None, useGeo=False, lat=None, lon=None):
		if useGeo:
			res = open_events(query, lat, lon, 100).results
		else:
			res = open_events_global(query).results
		return render_index(results=res, use_preset=use_preset, query=query.decode("utf8"))

if __name__ == '__main__':
	cherrypy.quickstart(Prost(), "/", "conf/server.conf")
