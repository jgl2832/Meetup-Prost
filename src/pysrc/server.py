import cherrypy

from mako.template import Template
from mako.lookup import TemplateLookup

from api import open_events_global

lookup = TemplateLookup(directories=['html'])

class Root(object):
	@cherrypy.expose
	def index(self, query="prost"):
		tmpl = lookup.get_template("index.html")
		res = open_events_global(query).results
		return tmpl.render(results=res, query=query)

if __name__ == '__main__':
	cherrypy.quickstart(Root(), '/')
