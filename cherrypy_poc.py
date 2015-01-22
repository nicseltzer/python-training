#!/usr/bin/python

'''
To get to this point I needed to install cherrypy through:
Scripts\pip install cherrypy
'''

import json
import cherrypy

json_data = {
                "nic":
                    {
                        "title": "Professional Keyboardist",
                        "dept": "The Typing Dept."
                    },
                "jimmy":
                    {
                        "title": "Architect",
                        "dept": "Global Architecting"
                    }
            }


class ExampleREST:
    exposed = True

    def GET(self, user_id=None):
        if user_id is None:
            return(json.dumps(json_data))
        elif user_id in json_data:
            return(json.dumps({"success": True, user_id: json_data[user_id]}))
        else:
            return(json.dumps({"success": False, "user_id": user_id,
                "error": "No user found with user_id {0}.".format(user_id)}))

    def PUT(self, user_id=None, dept=None, title=None):
        if user_id in json_data:
            user = json_data[user_id]
            user['dept'] = dept or user['dept']
            user['title'] = title or user['title']
            return(json.dumps({"success": True, "path": user_id}))
        else:
            return(json.dumps({"success": False, "path": user_id}))

    def DELETE(self, user_id=None):
        if user_id in json_data:
            try:
                del json_data[user_id]
                return({"success": True, "path": user_id})
            except:
                return({"success": False, "path": user_id})

if __name__ == "__main__":
    cherrypy.tree.mount(
        ExampleREST(), "/api",
        {
            '/':
            {
                'request.dispatch': cherrypy.dispatch.MethodDispatcher()
            },
        }
    )

    cherrypy.engine.start()
    cherrypy.engine.block()
