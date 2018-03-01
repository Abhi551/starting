#namedtuple are also similiar to tuple and are immutable

Point =namedtuple('Point',list('abcd'))
new=Point(1,5,1,6)

print (type(new),new)

#printing fields in namedtuple

print (new._fields)

#converting namedtuple to ordereddict

print (new._asdict())

#new._replace to replace the values in namedtuple

print (new._replace(d=78))

#new namedtuple

color=namedtuple('color','red green blue')
print (color._fields)

##merging to namedtuples

pixel=namedtuple('pixel',color._fields+new._fields)
new_pixel=pixel(1,5,1,2,0,0,255)
print (new_pixel)

##dictionary to namedtuple

dict={'a':5,'b':8,'c':1,'d':6}
tup=Point(**dict)

## namedtuple with classes 

class point(namedtuple('point','x y')):
	@property
	def hypot(self):
		return (self.x**2+self.y**2)**.5
	def __str__(self):
		return "Point x = %f y = %f z = %f "%(self.x,self.y,self.hypot)
print (point(3.0,4.0));
