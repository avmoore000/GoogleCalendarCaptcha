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

class node:
	def __init__(self):
		self.data = None # contaiins the data
		self.next = None #  contains the reference to the next node.
		self.date = None # contains the date of the event.
		self.time = None # contains the time of the event

class linkedList:
	def __init__(self):
		self.cur_node = None

	def addNode(self,data,dateInfo):

		new_node = node() # create new node
		new_node.data = data
		new_node.date = dateInfo[0:10]
		new_node.time = dateInfo[12:] 
		new_node.next = self.cur_node # link the new node and the previous node.
		self.cur_node = new_node # set the current node to the new one.

	def printList(self):
		node = self.cur_node
		while node:
			print node.data
			print node.date
			print node.time
			node = node.next

	def sortByDate(self,a,b):
	
			a_date = " ".join(a.date)
			b_date = " ".join(b.date)

			return cmp(a_date,b_date)
	

	def sortByTime(self):
		print 'Coming soon'

class CalendarService:
	
	L = linkedList()
	
	def __init__(self):

		self.username = 'andrewvmoore1985@gmail.com'
		self.visibility = 'private-1789a31d3c48182d5267fc5870bf5dc0'
		self.projection = 'full'
		self.calendar_service = gdata.calendar.service.CalendarService()


	def DateRangeQuery(self,start_date,end_date):

		print 'Date range query for events on Primary Calendar: %s to %s' %(start_date,end_date)

		query = gdata.calendar.service.CalendarEventQuery(self.username,self.visibility,self.projection)
		query.start_min = start_date
		query.start_max = end_date
	
		feed = self.calendar_service.CalendarQuery(query)
		
		for i, an_event in enumerate(feed.entry):
			for a_when in an_event.when:
				temp = '%s. ' %(i) + ' ' + an_event.title.text + '\t\t Start Time:  %s \t\t End Time:  %s\n' %(a_when.start_time,a_when.end_time)
				self.L.addNode(temp,a_when.start_time)
		
		self.L.sortByDate()
		self.L.printList()	

calendar = CalendarService()	
calendar.DateRangeQuery('2009-12-27','2010-01-04')
