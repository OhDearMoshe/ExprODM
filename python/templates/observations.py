from jinja2 import Environment, PackageLoader
# -*- coding: utf-8 -*-
class Observation:
    welcome = ""
    date = ""
    weather = ""
    pic_title = ""
    pic_link = ""
    pic_contributor = ""
# 'yourapplication', 'templates'
env = Environment(loader=PackageLoader('observations', '.'))

obs = Observation()
obs.welcome = "Hello /r/London! Good morning,"
obs.date = "Saturday, the 26th of November. "
obs.weather = "Today`s weather will be cloudy, maybe a bit foggy, with highs of 9C"
obs.pic_title= "Here is a pic of the day"
obs.pic_link = "https://i.imgur.com/UsSFndm.jpg"
obs.pic_contributor = "/u/Fwoggie2"

template = env.get_template('template.txt')
print template.render(observation=obs)
