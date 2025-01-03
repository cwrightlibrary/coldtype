############################################
#            Learning Coldtype             #
############################################

############################################
#                  Basics                  #
############################################

# When run locally with the coldtype viewer,
# the *.py file is the coldtype program
# source file

# In order to work, it must Import the
# library and define a renderable function

from coldtype import *

# Next we **define a renderable function**


# def show_something(r: Rect):
#     return P().rect(r)


# After setting up a venv using python
# 3.11.6 and running
# pip3 install coldtype[viewer],  we can run
# the coldtype program by running:
# coldtype anatomy.py in the terminal

# If we do this now, we'll get a popup that
# says "Nothing found." This is because we
# need to tell coldtype that the file is
# renderable with @renderable


# @renderable()
# def show_something(r: Rect):
#     return P().rect(r)


# When running the file you'll see a giant
# pink rectangle. We can make changes to
# it likeso:


# @renderable()
# def show_something(r: Rect):
#     return P().rect(r).f(hsl(random()))


# We can also change the rectangle to an
# oval like this


# @renderable()
# def show_something(r: Rect):
#     return P().oval(r).f(hsl(random()))


# Here's an example on rendering text


@renderable((800, 300))
def sample_text(r):
    return P(
        P().oval(r.inset(20)).f(hsl(random())),
        StSt("COLDTYPE", Font.ColdtypeObviously(), 200, wdth=0, tu=100, rotate=10)
        .align(r)
        .f(1),
    )


# A lot of the weird args are confusing
# but are covered in the text tutorial
# in the documentation:
# https://coldtype.goodhertz.com/tutorials/text.html

############################################
#                 Workflow                 #
############################################

# To save the file, all we have to do is
# hit the [a] key on the keyboard

# To show the saved file, press [s]

# To play the file, press [space]

# To open the file in the editor, press [o]

# To exit the renderer, press [q]
