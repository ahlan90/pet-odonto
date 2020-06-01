from rest_framework import serializers

class Anchor(object):

    def __init__(self, classes, url, text):
        self.classes, self.url, self.text = classes, url, text

    def __str__(self):
        return "<a class='{}' href='{}'>{}</a>".format(self.classes, self.url, self.text)