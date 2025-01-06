# Coldtype: Detailed Documentation

## Overview

[Coldtype](https://github.com/coldtype/coldtype) is a Python library designed for programmatically creating and animating text and design elements. It supports vector-based workflows and provides robust tools for working with type, including animations and variable fonts. Coldtype integrates with libraries like PIL, Skia, and FontTools to provide a seamless experience for typography and animation enthusiasts. Additionally, it enables advanced workflows that allow users to create typographic art, motion graphics, and even interactive animations with precision and control.

Coldtype focuses on flexibility and creativity, empowering designers and developers to push the boundaries of generative design. With a rich ecosystem of functions and decorators, users can craft everything from static layouts to dynamic, timeline-driven animations.

---

## Installation

Install Coldtype using `pip`:

```bash
pip install coldtype
```

Ensure you have the required dependencies, including Python 3.8+ and a modern graphics environment. For a complete setup, consider installing development tools like Skia and FontTools, which enhance Coldtype’s capabilities. If you encounter issues during installation, refer to the [official documentation](https://github.com/coldtype/coldtype) for troubleshooting and environment setup tips.

## Basic Usage

A Simple Text Example

Here’s a quick example of rendering static text:

```python
from coldtype import *

@renderable()
def simple_text(r):
    return (StSt("Hello, Coldtype!", "YourFont.ttf", 100)
        .align(r)
        .f(hsl(0.7)))
```

This script generates a simple, visually appealing text layout. The text is styled using a specific font, aligned within the rendering rectangle, and filled with a vibrant hue from the HSL color space.

### Key Components

- `renderable()`: Marks a function as a renderable object, allowing it to be processed and displayed by Coldtype.
- `StSt`: Creates styled text with various customization options such as font, size, and variable axes.
- .`align(r)`: Aligns text within the provided rectangle, supporting vertical and horizontal centering.
- `.f()`: Sets the fill color using various color models like RGB, HSL, or gradients.

---

## Animating Text Location

Animating text in Coldtype involves the use of the animation decorator. Here's an example of moving text horizontally across the canvas:

```python
from coldtype import *

@animation(timeline=60, bg=hsl(0.9))
def animate_text(f):
    x_position = f.e("eeio", 1, rng=(0, f.a.r.w))
    return (StSt("Move Me!", "YourFont.ttf", 150)
        .align(f.a.r)
        .translate(x_position, 0)
        .f(0))
```

### Explanation

- `@animation`: Creates an animation with a specified timeline (60 frames in this example).
- `f.e()`: Eases between values (e.g., `0` to `canvas width`) using an easing function (e.g., "eeio", an ease-in-out cubic).
- `.translate(x, y)`: Moves the text by `x` and `y` units, supporting dynamic and fluid motion.

By leveraging the `f.e()` function, you can create sophisticated animations with precise control over the timing and interpolation of movements. Experiment with different easing functions to achieve unique effects.

---

## Variable Font Settings

Coldtype supports variable fonts, allowing fine-tuned control over axes such as weight, width, or optical size. This makes it an ideal tool for exploring the full potential of modern typefaces.

### Using Variable Fonts

```python
from coldtype import *

@renderable()
def variable_font(r):
    return (StSt("Variable", "YourVariableFont.ttf", 150,
        wdth=0.75, wght=0.3)
        .align(r)
        .f(0))
```

In this example, the `wdth` (width) and `wght` (weight) axes are adjusted to customize the appearance of the text. Variable fonts provide unparalleled flexibility, enabling designs that were previously time-consuming to achieve.

### Animating Font Properties

Variable font properties like `wdth` (width) and `wght` (weight) can be animated:

```python
@animation(timeline=60, bg=hsl(0.2))
def animate_variable_font(f):
    width_value = f.e("linear", 1, rng=(0, 1))
    weight_value = f.e("eeio", 2, rng=(0.2, 0.8))

    return (StSt("Dynamic Font", "YourVariableFont.ttf", 200,
        wdth=width_value, wght=weight_value)
        .align(f.a.r)
        .f(hsl(0.6)))
```

### Explanation

- `wdth`: Controls font width, allowing for condensed or expanded letterforms.
- `wght`: Controls font weight, adjusting the thickness of the strokes.
- `f.e()`: Eases the properties across frames, providing smooth transitions.

By combining variable font properties with animations, designers can create responsive and adaptive typographic experiences.

---

## Advanced Text Animations

### Animating Along a Path

Text can animate along a custom path, such as a curve:

```python
from coldtype import *

@animation(timeline=120)
def text_on_path(f):
    path = (P().oval(f.a.r.inset(100)))
    return (StSt("Around the Path", "YourFont.ttf", 100)
        .align(f.a.r)
        .pen()
        .follow(path, f.i/120)
        .f(hsl(0.5)))
```

### Explanation

- `P().oval()`: Creates a circular path that serves as the trajectory for the text.
- `.pen()`: Converts text to a pen (path representation), making it compatible with path-following functions.
- `.follow(path, progress)`: Animates text along the given path, with `progress` determining the position on the path.

Using path animations, you can craft intricate motion graphics and layouts, where text seamlessly flows along complex trajectories.

---

## Styling Text

### Colors and Gradients

Set fill colors or gradients for your text:

```python
@renderable()
def colorful_text(r):
    return (StSt("Colors!", "YourFont.ttf", 150)
        .align(r)
        .f(Gradient.Horizontal(r, hsl(0.1), hsl(0.8))))
```

Gradients add depth and vibrancy to your designs. Coldtype supports linear, radial, and custom gradient styles, ensuring versatility for any project.

### Stroke and Fill

You can use `.f()` for fills and `.s()` for strokes:

```python
@renderable()
def stroke_text(r):
    return (StSt("Stroke", "YourFont.ttf", 150)
        .align(r)
        .f(None)
        .s(hsl(0.3))
        .sw(5))
```

The `.sw()` method sets the stroke width, giving you full control over the appearance of outlined text. Combining fills and strokes can produce striking effects that elevate your compositions.

---

## Keyboard and Interaction

Coldtype supports interactive development and previewing, enhancing the design process with real-time feedback.

- Press `r` to refresh renderables, instantly applying changes to your scripts.
- Press `space` to toggle animation playback, enabling seamless previewing of motion effects.
- Use the `coldtype run` command in the terminal to start the live preview environment, a powerful tool for iterative workflows.

Interactive features like these make Coldtype an excellent choice for prototyping and refining complex animations.

---

## Resources

- [Official GitHub Repository](https://github.com/coldtype/coldtype): The source code and documentation for Coldtype.
- [Coldtype Examples](https://github.com/coldtype/coldtype): A collection of scripts and projects showcasing the library’s capabilities.

For further exploration, refer to the extensive examples and documentation provided in the repository. Coldtype’s flexibility and power make it a valuable tool for anyone interested in generative design and animated typography.