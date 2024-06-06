try:
	from xml.etree import ElementTree
except ImportError:
	from elementtree import ElementTree
import gdata.calendar.service
import gdata.service
import atom.service
import gdata.calendar
import atom
import getopt
import sys
import string
import time
import operator


class CalendarService:

	L = list()
	out = list()
	def __init__(self):

		self.username = 'andrewvmoore1985@gmail.com'
		self.visibility = 'private-1789a31d3c48182d5267fc5870bf5dc0'
		self.projection = 'full'
		self.calendar_service = gdata.calendar.service.CalendarService()

	def compare2 (self,a,b,date):

		a_name = " ".join(a.date)
		b_name = " ".join(b.date)

		return cmp(a_name,b_name)
	
	def myCompare (self,a,b):
		a_name = " ".join(a.split()[8:10])
		b_name = " ".join(b.split()[8:10])

		#print "A name is " + a_name
		#print "B name is " +  b_name

		return cmp(a_name,b_name)

	def DateRangeQuery(self,start_date,end_date):

		print 'Date range query for events on Primary Calendar: %s to %s' %(start_date,end_date)

		query = gdata.calendar.service.CalendarEventQuery(self.username,self.visibility,self.projection)
		query.start_min = start_date
		query.start_max = end_date
	
		feed = self.calendar_service.CalendarQuery(query)
		
		for i, an_event in enumerate(feed.entry):
			for a_when in an_event.when:
				temp = '%s. ' %(i) + ' ' + an_event.title.text + '\t\t Start Time:  %s \t\t End Time:  %s\n' %(a_when.start_time,a_when.end_time)
				self.L.append(temp)

	#	self.out.append(sorted(self.L,key=operator.itemgetter(3)))	


		self.L.sort(self.myCompare)

		for item in self.L:

			print "".join(item)	

calendar = CalendarService()	
calendar.DateRangeQuery('2009-12-27','2010-01-04')
