from api import open_events

import argparse

def main():
	parser = argparse.ArgumentParser(description="Query open_events")
	parser.add_argument("query", metavar="q", type=str, help="Query string to use")

	args = parser.parse_args()

	if args.query:
		res = open_events(args.query, 40.7127, -74.0059, 100)
		for r in res.results:
			print "%s: %s, %s - DISTANCE %s" % (r.name, r.lat,r.lon, r.distance)
	else:
		print "A query argument must be provided!"


if __name__ == "__main__":
	main()
