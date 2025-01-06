############################################
#                 Animation                #
############################################

from coldtype import *

# A circle moving


# @animation((540, 540), timeline=60, bg=1)
# def circle(f):
#     return (
#         P()
#         .oval(
#             f.a.r.inset(120).offset(f.e("eei", 1, rng=(-f.a.r.w / 2, f.a.r.w / 2)), 0)
#         )
#         .f(hsl(0.7))
#     )

# A letter flying


# @animation((540, 540), bg=0, timeline=24)
# def flying(f):
#     return P(
#         P().rect(f.a.r).f(hsl(f.e("qeio", 0))),
#         StSt("A", Font.MutatorSans(), 50, wght=0.2)
#         .align(f.a.r)
#         .scale(f.e("eei", 0, rng=(1, 120)))
#         .rotate(f.e("qeio", 0, rng=(0, 360)))
#         .f(1),
#     )

# Simple variation


# @animation((1080, 540), timeline=50, bg=hsl(0.4))
# def vari(f):
#     return (
#         StSt("CDELOPTY", Font.ColdtypeObviously(), 200, wdth=f.e("eeio", 1))
#         .align(f.a.r)
#         .f(1)
#     )

# A variable wave


@animation((1080, 540), timeline=50, bg=hsl(0.6))
def wave(f):
    return (
        Glyphwise(
            "COLDTYPE",
            lambda g: Style(
                Font.ColdtypeObviously(), 200, wdth=f.adj(-g.i * 3).e("seio", 1)
            ),
        )
        .align(f.a.r)
        .f(1)
    )
