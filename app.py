import json
import falcon
import pos


class Debit(object):
    def on_post(self, req, resp):
        """Handles POST requests"""
        data = json.load(req.stream)
        amount = data['amount']
        r = pos.pos_debit(amount)
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = json.dumps({"state": r[0], "message ": r[1]})


# falcon.API instances are callable WSGI apps
app = falcon.App()

# Resources are represented by long-lived class instances
debit = Debit()

# things will handle all requests to the '/things' URL path
app.add_route('/debit', debit)

