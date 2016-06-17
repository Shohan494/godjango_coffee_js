# A file that contains a Class withn a function that converts coffee-script file to Javascript file
# File destination -- from static/coffee/main.coffeee to static/js/app.js

from django.core.management.base import NoArgsCommand, CommandError
import os

class Command(NoArgsCommand):
    help = "Compiles Coffee-Script into JavaScript"
    
    def handle(self, **options):
        f = os.popen("coffee --join static/js/app.js --compile static/coffee/*.coffee")
        for i in f.readlines():
            print i
        
