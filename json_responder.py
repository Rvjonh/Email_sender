from flask import json

class JsonResponse:
    """ A wrapper to send json responses """

    def __init__(self, app=None):
        if not app:
            raise("App needed")
        self.app = app

    def Response(self, dict=None, status=200):
        """ dumps dict to json and give a status response """
        return self.app.response_class(
                    response=json.dumps(dict),
                    status=status,
                    mimetype='application/json'
                )