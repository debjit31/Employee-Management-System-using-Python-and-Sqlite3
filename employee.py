class Employee:
    def __init__(self, uid, fname, lname, job, pay, address):
        self.__uid = uid
        self.__fname = fname
        self.__lname = lname
        self.__pay = pay
        self.__job = job
        self.__address = address

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.__fname, self.__lname)

    @property
    def fullname(self):
        return '{} {}'.format(self.__fname, self.__lname)

    def getUID(self):
        return self.__uid

    def getfname(self):
        return self.__fname

    def getlname(self):
        return self.__lname

    def getPay(self):
        return self.__pay

    def getJob(self):
        return self.__job

    def getAddress(self):
        return self.__address






