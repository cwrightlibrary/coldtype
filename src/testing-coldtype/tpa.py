from coldtype import *

tpa_text = "Third Party\nAdministrators"

d_text1 = "Simplifying healthcare,"
d_text2 = "One plan at a time."

dmsans = "src/fonts/DMSans-VariableFont_opsz,wght.ttf"

# Bold to thin, center to left

# @animation((800, 500), timeline=60, bg=hsl(0.5))
# def animate_tpa(f):
#     x_pos = f.e("eeio", 1, rng=(0, -f.a.r.w/4))
#     wght_anim = f.e("eeio", 1, rng=(1, 0))
#     return (StSt(tpa_text, dmsans, 50, wght=wght_anim)
#             .align(f.a.r, th=0)
#             .translate(x_pos, 0)
#             .f(1))

# Center left to top left

# @animation((800, 500), timeline=60, bg=hsl(0.5))
# def animate_tpa2(f):
#     y_pos = f.e("eeio", 1, rng=(0, f.a.r.h/3))
#     return (StSt(tpa_text, dmsans, 50, wght=0)
#             .align(f.a.r, th=0)
#             .translate(-f.a.r.w/4, y_pos)
#             .f(1))

# Second text left to center

# @animation((800, 500), timeline=60, bg=hsl(0.5))
# def animate_tpa3(f):
#     x_pos = f.e("eeio", 1, rng=(-f.a.r.w, -f.a.r.w/8))
#     y_pos = f.a.r.h/12
#     return P(
#         StSt(tpa_text, dmsans, 50, wght=0)
#         .align(f.a.r, th=0)
#         .translate(-f.a.r.w/4, f.a.r.h/3)
#         .f(1),

#         StSt(d_text1, dmsans, 30, wght=0.5)
#         .align(f.a.r, th=0)
#         .translate(x_pos, y_pos)
#         .f(1))

# Third text left to center

@animation((800, 500), timeline=60, bg=hsl(0.5))
def animate_tpa4(f):
    x_pos1 = -f.a.r.w/8
    x_pos2 = f.e("eeio", 0, rng=(-f.a.r.w, -f.a.r.w/6.1))
    y_pos1 = f.a.r.h/12
    y_pos2 = 0
    return P(
        StSt(tpa_text, dmsans, 50, wght=0)
        .align(f.a.r, th=0)
        .translate(-f.a.r.w/4, f.a.r.h/3)
        .f(1),
        
        StSt(d_text1, dmsans, 30, wght=0.5)
        .align(f.a.r, th=0)
        .translate(x_pos1, y_pos1)
        .f(1),
        
        StSt(d_text2, dmsans, 30, wght=0.5)
        .align(f.a.r, th=0)
        .translate(x_pos2, y_pos2)
        .f(1)
        )
