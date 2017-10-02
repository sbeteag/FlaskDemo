class Page():
    def __init__(self, url, title, body, img=None, list=None):
        self.url = url
        self.title = title
        self.body = body
        self.img = img
        self.list = list

    def __repr__(self):
        return "<Page object with title: {}>".format(self.title)
