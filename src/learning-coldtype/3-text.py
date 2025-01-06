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

# We can also track and rotate the letters


# @renderable((800, 150))
# def text3(r):
#     return (
#         StSt("CDELOPTY", co, 150, wdth=0.5, rotate=10, tu=150)
#         .f(hsl(0.9, s=0.75))
#         .align(r)
#     )

# With coldtype, we aren't drawing text, we are
# getting information about individual glyphs
# and their location, with StSt

# When we call StSt we get a rich set of data
# that can be inspected and manipulated


# @renderable((800, 150))
# def text4(r):
#     pens = (
#         StSt("COLDTYPE", co, 150, wdth=0.5, rotate=10, tu=150)
#         .f(Gradient.Vertical(r, hsl(0.5, s=0.8), hsl(0.8, s=0.75)))
#         .align(r)
#     )

#     pens[0].rotate(180)
#     pens[-1].rotate(180)
#     pens[-2].rotate(10)
#     return pens

# @renderable((800, 150))
# def text_print(r):
#     pens = (StSt("COLD", co, 150).align(r))
#     print(pens.tree())
#     return pens

# We can also use .indices and .index to
# target elements of the tree and do
# what we want with letters that way


# @renderable((800, 150))
# def text4_more_coldtypey(r):
#     return (
#         StSt("COLDTYPE", co, 150, wdth=0.5, rotate=10, tu=150)
#         .align(r)
#         .indices([0, -1], lambda p: p.rotate(180))
#         .index(-2, lambda p: p.rotate(10))
#         .ch(lambda p: p.f(Gradient.V(p.ambit(), hsl(0.55, 1), hsl(0.45, 1))))
#     )


