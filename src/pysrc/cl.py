from api import open_events, open_events_global

import argparse

def main():
	parser = argparse.ArgumentParser(description="Query open_events")
	parser.add_argument("query", metavar="q", type=str, help="Query string to use")
	parser.add_argument("--local", action="store_true")

	args = parser.parse_args()

	if args.query:
		if args.local:
			print args.local
			res = open_events(args.query, 40.7127, -74.0059, 1000)
			for r in res.results:
				print "%s: %s, %s - DISTANCE %s" % (r.name, r.lat,r.lon, r.distance)
		else:
			res = open_events_global(args.query)
			for r in res.results:
				print "%s: %s, %s" % (r.name, r.lat, r.lon)
	else:
		print "A query argument must be provided!"

if __name__ == "__main__":
	main()
