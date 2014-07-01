#web programming - Cherrypy framework

import cherrypy

class FirstPage(object):
    def index(self):
        return "Test String"
    index.exposed = True

#Starting the cherrypy and loading the class firstpafe
cherrypy.quickstart(FirstPage())
