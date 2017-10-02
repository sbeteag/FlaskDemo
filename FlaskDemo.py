from flask import Flask, render_template
from static.page import Page
from webargs import fields
from webargs.flaskparser import use_args

app = Flask(__name__)

index = Page("index",
             "Home Page",
             "Here's a sample home page. I can add anything here, including "
             "<strong>HTML</strong><i>Tags</i><br>Line<br>Breaks<hr>Horizontal Lines<hr>And extra images<br>"
             "<img class='img-responsive' src='static/community.png'>",
             img="static/flask.png")

what = Page("what",
            "What is Flask?",
            "Flask is a Python web framework. It is considered a micro-framework, meaning that it has little to no"
            " dependencies on external libraries. It is used to build web applications.<br><br>It was initially "
            "released April 1, 2010, but it still on version 0.12.2. As of mid 2016, it was the most popular Python web development framework on GitHub.<br><br><a href='http://flask.pocoo.org/community/poweredby/'>Powered by Flask</a>",
            img="static/flask.png")

why = Page("why",
           "Why Flask?",
           "Flask allows you to create web apps very quickly. You can use templates to create consistent pages very "
           "quickly. You can tie it to existing Python code fairly simply.",
           img="static/flask.png",
           list=["<b>Rapid Development</b> - Flask allows you to create web apps very quickly", "<b>Lightweight</b> - "
                                                                                                "Has minimal dependencies",
                 "<b>HTML Templates</b> - reuse old templates", "Easily connects to existing Python code",
                 "Easier to use than some larger frameworks", "It works with standard CSS, HTML, jQuery, etc."])

jinja = Page("jinja",
             "Jinja2 Template System",
             "Flask uses a template system called Jinja. It was developed specifically for Flask. It allows you to "
             "easily pass and display variables, execute loops, run functions, and is very easy to debug.<br><br>"
             "Using a base template (base.jinja2), we can pass new values to the template to render unique pages. "
             "Every page on this demo site is using the same base and secondary template - "
             "just 2 files for multiple pages.",
             img="static/jinja-logo.png")

django = Page("django",
              "Flask vs Django",
              "Django is another popular Python framework. Flask is much more 'modular', meaning that it is pretty "
              "bare but has modules that can be added as they're needed. Django is used on bigger projects (Pinterest, NASA, instagram) but many sites use Flask for their APIs.<hr>Django Hello World"
              "<img class='img-responsive' src='static/djangoHello.PNG'><hr>Flask Hello World"
              "<img class='img-responsive' src='static/flaskHello.PNG'>",
              img="static/flask.png")

p404 = Page("missing",
            "Page not found",
            "The URL you entered does not exist.")

pages = {"what": what,
         "why": why,
         "jinja": jinja,
         "home": index,
         "django": django}

nav = ['Home', 'What', 'Why', 'Jinja', 'Django']  # , 'Hello']


@app.route('/')
def home():
    return render_template('main.jinja2', page=index, nav=nav)


@app.route('/<string:name>')
def load_page(name):
    try:
        page = pages[name]
        return render_template('main.jinja2', page=page, nav=nav)
    except KeyError:
        return render_template("main.jinja2", page=p404, nav=nav)


@app.route('/hello/<string:name>')
def hello_page(name):
    if name == "":
        name = "World"
    hello = Page(name, 'Hello!', "Hello, {}!".format(name))
    return render_template("main.jinja2", page=hello, nav=nav)


@app.route('/hello/')
def blank_hello():
    name = "World"
    hello = Page(name, 'Hello!', "Hello, {}!".format(name))
    return render_template("main.jinja2", page=hello, nav=nav)


area_args = {
    'height': fields.Int(validate=lambda val: val > 0),
    'width': fields.Int(validate=lambda val: val > 0)
}


@app.route('/area/')
@use_args(area_args)
def area(args):
    print(args['height'])
    rectangle = Page('Your Rectangle', 'Your rectangle', '', img='/static/blue.png')
    rectangle.height = args['height']
    rectangle.width = args['width']
    return render_template('area.jinja2', page=rectangle, nav=nav)


if __name__ == '__main__':
    app.run(debug=True)
