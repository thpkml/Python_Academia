class Staff:
    # following 3 are class variables, not dependent on any specific instance
    schoolName = 'St Patricks College'
    numOfStaff = 0
    staffList = []

    # the following lines initializes the 'instance variables'. 
    def __init__(self, staffId, staffFname, staffLname, staffPass, jobTitle):
        self.id = staffId
        self.name = staffFname
        self.surname = staffLname
        self.password = staffPass
        self.job = jobTitle

        # every time a new object is instantiated, numOfStaff will increase by 1. 
        Staff.numOfStaff += 1
        Staff.staffList.append

    def getName(self):
        return '{} {}'.format(self.name, self.surname)
    
    def addStaff(self):
        print('Enter Your Details:')
        self.id = input('ID: ')
        self.name = input('First Name: ')
        self.surname = input('Last Name: ')
        self.password = input('Password: ')
        self.job = input('Job Title: ')

    def getStaff(self):
        print('ID: ' + str(self.id))
        print('First Name: ' + self.name)
        print('Last Name: ' + self.surname)
        print('Job Title: ' + self.job)

    # the following method does not require an instance of the Staff class
    # so, we define it as a 'class method' and pass 'cls' as it parameter.
    # it can be called from anywhere E.g. Staff.howManyStaff()
    # Note that since it is a class method, intances can make use of it by
    # e.g. staff_1.howManyStaff()
    @classmethod
    def howManyStaff(cls):
        print('The number of staff registered in this system is: ')
        print(cls.numOfStaff)

staff_1 = Staff(100, 'Kamal', 'Thapa', 'pass1', 'lecturer')
staff_2 = Staff(200, 'Arkan', 'Tujilo', 'pass2', 'lecturer')
staff_3 = Staff(300, 'Kyle', 'Black', 'pass3', 'course leader')
staff_4 = Staff(400, 'Rylie', 'Chan', 'pass4', 'lecturer')
staff_5 = Staff(500, 'Katie', 'Adams', 'pass5', 'researcher')
staff_6 = Staff(600, 'Thomas', 'Bravas', 'pass6', 'researcher')
staff_7 = Staff(700, 'Malcolm', 'May', 'pass6', 'vice principal - research')
staff_8 = Staff(800, 'Theresa', 'Thompson', 'pass7', 'vice principal - research') 

# creating subclass 'Investigator' from the superclass 'Staff'
class Investigator(Staff):
    def __init__(self, staffId, staffFname, staffLname, staffPass, jobTitle, deptName,
                 isFullTime, dateJoined, noOfActivities):
        # the following line will inherit variables from superclass
        super().__init__(staffId, staffFname, staffLname, staffPass, jobTitle)
        # the rest are declared below
        self.department = deptName
        self.fulltime = isFullTime
        self.start = dateJoined
        self.activities = noOfActivities

inv_1 = Investigator(500, 'Katie', 'Adams', 'pass5', 'researcher', 'IT',
                     True, '12/01/2015', 2)
inv_2 = Investigator(600, 'Thomas', 'Bravas', 'pass6', 'researcher', 'Business Studies',
                     False, '18/05/2018', 1)
inv_3 = Investigator(200, 'Arkan', 'Tujilo', 'pass2', 'lecturer', 'Social Care',
                     False, '01/03/2016', 2)
inv_4 = Investigator(400, 'Rylie', 'Chan', 'pass4', 'lecturer', 'IT',
                     True, '09/12/2012', 2)
inv_5 = Investigator(300, 'Kyle', 'Black', 'pass3', 'course leader', 'IT',
                     True, '02/02/2011', 2)

# class ScholarlyActivity (Activity - for brevity)

class IterateActivity(type): # this class will iterate the instances of Activity class
    def __iter__(cls):
        return iter(cls.allActivity)
    
class Activity(metaclass = IterateActivity):
    allActivity = []
    
    def __init__(self, activityId, activityTitle, activityDate, progressPercent, staffId):
        self.activityId = activityId
        self.activityTitle = activityTitle
        self.activityDate = activityDate
        self.progressPercent = progressPercent
        self.staffId = staffId
        self.allActivity.append(self)
        
    def addActivity(self):
        print('Enter Activity Details:')
        self.activityId = input('Activity ID: ')
        self.activityTitle = input('Activity Title: ')
        self.activityDate = input('Start Date: ')
        self.progressPercent = input('Progress Percent')
        self.staffId = input('Staff ID: ')
    def setProgress(self):
        print('What is the progress of your research activity?')
        self.progressPercent = input('Progress Percent (do not write "%" sign): ')
    def getProgress(self):
        print('The progress for the chosen actvity is: ' + str(self.progressPercent) + ' %')
        
    @classmethod   
    def listActivity(cls):
        for act in Activity:
            print(act.activityTitle + ' -- by staffID -- ' + str(act.staffId)
                  + '-- Progress: -- '+ str(act.progressPercent) + '%') 

if __name__ == '__main__':
    act_1 = Activity(1, 'Future of IoT', '02/02/2019', 30, inv_1.id)
    act_2 = Activity(2, 'Cybersecurity in Schools', '17/11/2018', 100, inv_1.id)
    act_3 = Activity(3, 'For-Profit Education System', '23/08/2018', 92, inv_2.id)
    act_4 = Activity(4, 'Ageing Workforce in the UK', '12/02/2017', 100, inv_3.id)
    act_5 = Activity(5, 'NHS Struggles vs Immigration', '06/01/2019', 23, inv_3.id)
    act_6 = Activity(6, 'Object Oriented Thinking', '02/03/2013', 100, inv_4.id)
    act_7 = Activity(7, 'Why Should You Code', '02/02/2019', 45, inv_4.id)
    act_8 = Activity(8, 'The Dark Side of Web', '15/01/2019', 85, inv_5.id)
    act_9 = Activity(9, 'The Online Generation', '25/02/2012', 100, inv_5.id)

# class Resource
class IterResource(type): # this iter.. class will iterate the instances of class Resource
    def __iter__(cls):
        return iter(cls.allResource)
class Resource(metaclass = IterResource):
    allResource = []
    
    def __init__(self, resourceId, resourceName, numberAvailable, onLoan):
        self.resourceId = resourceId
        self.resourceName = resourceName
        self.numberAvailable = numberAvailable
        self.onLoan = onLoan
        self.allResource.append(self)
    def addResource(self):
        print('Enter Resource Details')
        self.resourceId = input('Resource ID: ')
        self.resourceName = input('Resource Title: ')
        self.numberAvailable = input('Number Available: ')
        self.onLoan = input('Number On Loan: ')
    def setNumberAvailable(self):
        self.numberAvailable = input('Number of Copies Available: ')
    def getTotalNumber(self):
        return(self.numberAvailable + self.onLoan)
    @classmethod # class method to iterate the instances using the Iter.. class
    def listResource(cls):
        for res in Resource:
            print('Title: ' + res.resourceName + ' ==> Available: ' + str(res.numberAvailable)
                  + ' ==> On Loan: ' + str(res.onLoan))
            
if __name__ == '__main__':
    res_1 = Resource(1, 'Internet of Things', 5, 2)
    res_2 = Resource(2, 'Safety on the Internet', 4, 4)
    res_3 = Resource(3, 'States with Free Education', 6, 2)
    res_4 = Resource(4, 'The World is Getting Older', 5, 3)
    res_5 = Resource(5, 'NHS Statistics 2018', 9, 1)
    res_6 = Resource(6, 'OOP and Life', 2, 4)
    res_7 = Resource(7, 'The Digitised World', 5, 2)
    res_8 = Resource(8, 'The Darknet', 4, 6)
    res_9 = Resource(9, 'Internet and the Millenials', 8, 2)
    res_10 = Resource(10, 'Teaching Children to Code', 7, 3)
    res_11 = Resource(11, 'Should Universities be Subsidised', 3, 9)
    res_12 = Resource(12, 'Surviving without Internet for a Year', 5, 1)
    res_13 = Resource(13, 'Surviving without Internet for a Year', 5, 1)

# class ResourceRequest ('Request' - for brevity)
class IterRequest(type):
    def __iter__(cls):
        return iter(cls.allRequest)
class Request(metaclass = IterRequest):
    allRequest = []
    
    def __init__(self, requestId, resourceId, staffId, activityId, requestDate, status):
        self.requestId = requestId
        self.resourceId = resourceId
        self.staffId = staffId
        self.activityId = activityId
        self.requestDate = requestDate
        self.status = status
        self.allRequest.append(self)
    def addRequest(self):
        print('Enter details of resource you want to request')
        self.resourceId = input('Resource Id: ')
        self.staffId = input('Staff Id: ')
        self.activityId = input('Activity Id: ')
        self.requestDate = input('Todays Date: ')
    def getRequest(self):
        print('The request details are as follows: ')
        print('Request Id: ' + self.requestId)
    def setStatus(self):
        self.status = input('Set status to pending/fulfilled: ')
    def getStatus(self):
        print(self.status)
    @classmethod
    def listRequest(cls):
        for req in Request:
            print('RequestID: ' + str(req.requestId) + ' ==> ResourceID: ' + str(req.resourceId)
                  + ' ==> StaffID: ' + str(req.staffId) + ' ==> ActivityID: ' + str(req.activityId)
                  + ' ==> RequestDate: ' + req.requestDate + ' ==> Status: ' + req.status)

req_1 = Request(1, 1, 500, 1, '06/02/2019', 'fulfilled')
req_2 = Request(2, 2, 500, 2, '06/02/2019', 'pending')
req_3 = Request(3, 3, 600, 3, '06/02/2019', 'fulfilled')
req_4 = Request(4, 4, 200, 4, '06/02/2019', 'fulfilled')
req_5 = Request(5, 5, 200, 5, '06/02/2019', 'pending')
req_6 = Request(6, 6, 400, 6, '06/02/2019', 'pending')
req_7 = Request(7, 7, 400, 7, '06/02/2019', 'fulfilled')
req_8 = Request(8, 8, 300, 8, '06/02/2019', 'fulfilled')
req_9 = Request(9, 9, 300, 9, '06/02/2019', 'pending')
req_10 = Request(10, 10, 400, 7, '06/02/2019', 'fulfilled')

# creating subclass 'Admin' from the superclass 'Staff'
class Admin(Staff):
    def __init__(self, staffId, staffFname, staffLname, staffPass, jobTitle, staff=None):
        super().__init__(staffId, staffFname, staffLname, staffPass, jobTitle)
        if staff is None:
            self.staff = []
        else:
            self.staff = staff
    def addStaff(self, stf):
        if stf not in self.staff:
            self.staff.append(stf)
    def removeStaff(self, stf):
        if stf in self.staff:
            self.staff.remove(stf)
    def listStaff(self):
        for stf in self.staff:
            print('-->', stf.getName())
    def getRequest(self):
        Request.listRequest()
    def getProgress(self, act):
        Activity.getProgress(act)
adm_1 = Admin(700, 'Theresa', 'Thompson', 'pass7', 'vice principal - research', [inv_2])
adm_2 = Admin(800, 'Malcolm', 'May', 'pass6', 'vice principal - research', [inv_3])

