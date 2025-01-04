############################################
#                   Text                   #
############################################

from coldtype import *

# A few common variables we'll be using
# throughout

r = Rect(1000, 250)
co = Font.ColdtypeObviously()

############################################
#                Basic Text                #
############################################

# Let's start with a "Hello World" except in
# this case let's say COLDTYPE.


# @renderable((800, 150))
# def text1(r):
#     return StSt("COLDTYPE", co, 150).align(r)


# The blue color is the default fill for any
# text. Let's change some settings


# @renderable((800, 150))
# def text2(r):
#     return StSt("CDELOPTY", co, 150, wdth=0.5).f(hsl(0.8, s=0.75)).align(r)

# We can also track out the letters and rotate them


# @renderable((800, 150))
# def text3(r):
#     return (
#         StSt("CDELOPTY", co, 150, wdth=0.5, rotate=10, tu=150)
#         .f(hsl(0.9, s=0.75))
#         .align(r)
#     )

