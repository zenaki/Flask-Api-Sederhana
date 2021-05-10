import sys, os
from flask import Flask

import test_api

from dotenv import load_dotenv
APP_ROOT = os.path.join(os.path.dirname(__file__), '.')  # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

app = Flask(__name__, template_folder='template')
app.register_blueprint(test_api.test_api)

@app.route('/test/<value>')
def test(value):
    return "Hello %s" % value

if __name__ == "__main__":
    # app.run()
    app.run(host=str(os.getenv('APP_WEB_ADDRESS')), port=int(os.getenv('APP_WEB_PORT')), threaded=True, debug=True)