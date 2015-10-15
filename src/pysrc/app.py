from api import open_events

def main():
	res = open_events("prost", 40.7127, -74.0059, 100)
	for r in res.results:
		print "%s: %s, %s - DISTANCE %s" % (r.name, r.lat,r.lon, r.distance)


if __name__ == "__main__":
	main()
