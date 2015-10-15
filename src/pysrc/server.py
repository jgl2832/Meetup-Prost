import cherrypy
from api import open_events_global

class Root(object):
	@cherrypy.expose
	def index(self):
		res = open_events_global("prost").results
		return str([r.name for r in res])

if __name__ == '__main__':
	cherrypy.quickstart(Root(), '/')
