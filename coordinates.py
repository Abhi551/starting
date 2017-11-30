def is_valid_coordinates(coordinates):
	flag=1;
	coordinates=coordinates.split(',');
	print coordinates;
	if isinstance(int(coordinates[0]),int) and isinstance(int(coordinartes[1]),int):
		if 0<=int(coordinates[0])<91 and 0<=int(coordinates[1])<181:
			return True;
	else :
		return False;


