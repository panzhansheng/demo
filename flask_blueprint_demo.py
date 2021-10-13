from flask import Flask
from example_blueprint import example_blueprint, example_blueprint2
#from example_blueprint2 import example_blueprint2
import sys

"""
Why Blueprints?
Blueprints in Flask are intended for these cases:

* Factor an application into a set of blueprints. This is ideal for larger applications; a project could instantiate an application object, initialize several extensions, and register a collection of blueprints.
* Register a blueprint on an application at a URL prefix and/or subdomain. Parameters in the URL prefix/subdomain become common view arguments (with defaults) across all view functions in the blueprint.
* Register a blueprint multiple times on an application with different URL rules.
* Provide template filters, static files, templates, and other utilities through blueprints. A blueprint does not have to implement applications or view functions.
* Register a blueprint on an application for any of these cases when initializing a Flask extension.
"""
sys.path.append('./')
app = Flask(__name__)
app.register_blueprint(example_blueprint)
app.register_blueprint(example_blueprint2)

app.run("0.0.0.0", port="8000")
