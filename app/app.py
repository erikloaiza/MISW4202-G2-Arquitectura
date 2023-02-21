import time
import random

from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
PrometheusMetrics(app)

endpoints=("recalculate")

@app.route("/recalculate")
def recalculate():
    nterms = random.randint(-1000,10000)
    # first two terms
    n1, n2 = 0, 1
    count = 0

    # check if the number of terms is valid
    if nterms <= 0:
        return ":C", 400
    # if there is only one term, return n1
    elif nterms == 1:
        return n1
    #probability of 15% to be an error
    elif random.random()<0.15:
        return 'Service Unavailable',503
    # generate fibonacci sequence
    while count < nterms:
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1
    return str(n1)

if __name__ == "__main__":
    app.run("0.0.0.0", 5000, threaded=True)
