############################################
#                  Shapes                  #
############################################

# Let's draw a rectangle

from coldtype import *

# @renderable((300, 300))
# def rectangle(r):
#     return P().rect(r.inset(50)).f(hsl(0.9, 0.75))

# This is how we draw a rectangle with 50px
# padding around the edges (the padding
# coming from the r.inset(50) call)

# Similarly, an oval would look like this

# @renderable((300, 300))
# def oval(r):
#     return P().oval(r.inset(45)).f(hsl(0.6))

# To combine an oval and a rect, we'd do this

# @renderable((300, 300))
# def ovalrect(r):
#     return (P()
#             .oval(r.inset(60))
#             .translate(30, 30)
#             .union(P()
#                    .rect(r.inset(65))
#                    .translate(-30, -30))
#             .f(hsl(0.05, l=0.6, s=0.75)))

# To show only the parts that don't overlap,
# (difference) fill with a gradient and
# rotate the rect, we'd do this


# @renderable((300, 300))
# def ovalrect_diff(r):
#     return (
#         P()
#         .oval(r.inset(60))
#         .translate(30, 30)
#         .xor(P().rect(r.inset(65)).translate(-30, -30).rotate(-5))
#         .f(Gradient.Horizontal(r, hsl(0.05, l=0.6, s=0.75), hsl(0.8, l=0.6, s=0.5)))
#         .translate(7)
#     )

############################################
#             Modifying Shapes             #
############################################

# Here we build up a chain of effects to
# modify a simple vector shape

from coldtype.fx.skia import phototype


@renderable((300, 300))
def ovalmod(r):
    return (
        P()
        .oval(r.inset(60))
        .flatten(5)  # breaks the oval into non-curves, segment length being 5
        .roughen(50)  # randomizes the vertices of the shape
        .f(1)
        .ch(phototype(r, blur=5, cut=100, cutw=5, fill=hsl(0.07, 1, 0.6)))
    )
