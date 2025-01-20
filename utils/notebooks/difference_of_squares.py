"""
Provides a utility class, a Color enum, and constants, all for use in "A Visual
Proof: Difference of Squares".
"""

from enum import Enum
from operator import itemgetter
from utils.graphics.canvas_renderer import CanvasRenderer


class Color(Enum):
    """An enumeration of Colors used in "A Difference of Squares"."""

    BLACK = "#000022"
    WHITE = "#ffffff"
    GRAY = "#555555"
    LIGHT_GRAY = "#999999"
    LIGHTER_GRAY = "#dddddd"
    BLUE = "#1b9ce5"


MARGIN_LEFT = 60
MARGIN_TOP = 60
PLOT_CONTENT_A_DIMENSION = 280
PLOT_CONTENT_B_DIMENSION = 80
PLOT_CONTENT_WIDTH = PLOT_CONTENT_A_DIMENSION + PLOT_CONTENT_B_DIMENSION
PLOT_CONTENT_HEIGHT = PLOT_CONTENT_A_DIMENSION
CANVAS_WIDTH = MARGIN_LEFT * 2 + PLOT_CONTENT_WIDTH + 30
CANVAS_HEIGHT = MARGIN_TOP * 2 + PLOT_CONTENT_HEIGHT + 30
DEFAULT_LABEL_SETTINGS = {
    "font": "18px sans-serif",
    "font_color": Color.BLACK.value,
}


class RenderUtils:
    """A class the provides utility methods for use in "A Difference of Squares"
    notebook.

    The class methods make extensive use of a supplied CanvasRenderer class.
    """

    __renderer: CanvasRenderer = None
    __dimensions = {
        "a": PLOT_CONTENT_A_DIMENSION,
        "b": PLOT_CONTENT_B_DIMENSION,
        "left_margin": MARGIN_LEFT,
        "top_margin": MARGIN_TOP,
        "a_plus_b": PLOT_CONTENT_A_DIMENSION + PLOT_CONTENT_B_DIMENSION,
        "a_minus_b": PLOT_CONTENT_A_DIMENSION - PLOT_CONTENT_B_DIMENSION,
        "center_a": PLOT_CONTENT_A_DIMENSION / 2,
        "center_b": PLOT_CONTENT_B_DIMENSION / 2,
        "center_a_plus_b": (PLOT_CONTENT_A_DIMENSION + PLOT_CONTENT_B_DIMENSION) / 2,
        "center_a_minus_b": (PLOT_CONTENT_A_DIMENSION - PLOT_CONTENT_B_DIMENSION) / 2,
    }

    @classmethod
    def set_renderer(cls, renderer):
        """Applies the CanvasRenderer. This needs to be called before other class
        methods.
        """
        cls.__renderer = renderer
        return cls

    @classmethod
    def clear(cls):
        """A convenience method for clearing the whole canvas."""
        cls.__renderer.clear()
        return cls

    @classmethod
    def label(cls, label, settings=None):
        """A convenience method for drawing a label."""
        if settings is None:
            settings = DEFAULT_LABEL_SETTINGS
        cls.__renderer.label(label, settings)
        return cls

    @classmethod
    def a_rect(cls):
        """Fills the "a" area of the canvas."""
        color = Color.LIGHT_GRAY.value
        a, left_margin, top_margin = itemgetter("a", "left_margin", "top_margin")(
            cls.__dimensions
        )

        cls.__renderer.fill_rect(
            {
                "color": color,
                "x": left_margin,
                "y": top_margin,
                "width": a,
                "height": a,
            }
        )
        return cls

    @classmethod
    def a_plus_b_rect(cls):
        """Fills and strokes a rectangle with dimensions of "a+b" as the width
        and "a-b" as the height.
        """
        color = Color.LIGHT_GRAY.value
        left_margin, top_margin, a_plus_b, a_minus_b = itemgetter(
            "left_margin",
            "top_margin",
            "a_plus_b",
            "a_minus_b",
        )(cls.__dimensions)

        (
            cls.__renderer.fill_rect(
                {
                    "color": color,
                    "x": left_margin,
                    "y": top_margin,
                    "width": a_plus_b,
                    "height": a_minus_b,
                }
            ).stroke_rect(
                {
                    "color": color,
                    "x": left_margin,
                    "y": top_margin,
                    "width": a_plus_b,
                    "height": a_minus_b,
                }
            )
        )
        return cls

    @classmethod
    def a_minus_b_rect(cls):
        """Fills and strokes a rectangle with dimensions of "a" as the width and
        "a-b" as the height.
        """
        color = Color.LIGHT_GRAY.value
        a, left_margin, top_margin, a_minus_b = itemgetter(
            "a",
            "left_margin",
            "top_margin",
            "a_minus_b",
        )(cls.__dimensions)

        (
            cls.__renderer.fill_rect(
                {
                    "color": color,
                    "x": left_margin,
                    "y": top_margin,
                    "width": a,
                    "height": a_minus_b,
                }
            ).stroke_rect(
                {
                    "color": color,
                    "x": left_margin,
                    "y": top_margin,
                    "width": a,
                    "height": a_minus_b,
                }
            )
        )
        return cls

    @classmethod
    def b_rect(cls):
        """Fills a square of the "b" dimension."""
        color = Color.LIGHTER_GRAY.value
        b, left_margin, top_margin, a_minus_b = itemgetter(
            "b",
            "left_margin",
            "top_margin",
            "a_minus_b",
        )(cls.__dimensions)

        (
            cls.__renderer.clear(
                {
                    "x": left_margin + a_minus_b,
                    "y": top_margin + a_minus_b,
                    "width": b,
                    "height": b,
                }
            ).fill_rect(
                {
                    "color": color,
                    "x": left_margin + a_minus_b + 2,
                    "y": top_margin + a_minus_b + 2,
                    "width": b - 6,
                    "height": b - 6,
                }
            )
        )
        return cls

    @classmethod
    def b_rect_horizontal(cls, offset=0):
        """Fills and strokes a rectangle with dimensions of "a-b" as the width
        and "b" as the height.
        """
        color = Color.LIGHT_GRAY.value
        b, left_margin, top_margin, a_minus_b = itemgetter(
            "b",
            "left_margin",
            "top_margin",
            "a_minus_b",
        )(cls.__dimensions)

        (
            cls.__renderer.fill_rect(
                {
                    "color": color,
                    "x": left_margin,
                    "y": top_margin + a_minus_b + offset,
                    "width": a_minus_b,
                    "height": b,
                }
            ).stroke_rect(
                {
                    "color": color,
                    "x": left_margin,
                    "y": top_margin + a_minus_b + offset,
                    "width": a_minus_b,
                    "height": b,
                }
            )
        )
        return cls

    @classmethod
    def b_rect_vertical(cls, offset=0):
        """Fills and strokes a rectangle with dimensions of "b" as the width
        and "a-b" as the height.
        """
        color = Color.LIGHT_GRAY.value
        a, b, left_margin, top_margin, a_minus_b = itemgetter(
            "a",
            "b",
            "left_margin",
            "top_margin",
            "a_minus_b",
        )(cls.__dimensions)

        (
            cls.__renderer.fill_rect(
                {
                    "color": color,
                    "x": left_margin + a + offset,
                    "y": top_margin,
                    "width": b,
                    "height": a_minus_b,
                }
            ).stroke_rect(
                {
                    "color": color,
                    "x": left_margin + a + offset,
                    "y": top_margin,
                    "width": b,
                    "height": a_minus_b,
                }
            )
        )
        return cls

    @classmethod
    def a_bar(cls):
        """Draws the "a" label bar in the left margin."""
        color = Color.GRAY.value
        a, left_margin, top_margin = itemgetter(
            "a",
            "left_margin",
            "top_margin",
        )(cls.__dimensions)

        (
            cls.__renderer.stroke_line(
                {
                    "color": color,
                    "line_dash": [],
                    "x1": left_margin - 40,
                    "y1": top_margin,
                    "x2": left_margin - 20,
                    "y2": top_margin,
                }
            )
            .stroke_line(
                {
                    "color": color,
                    "line_dash": [],
                    "x1": left_margin - 30,
                    "y1": top_margin,
                    "x2": left_margin - 30,
                    "y2": top_margin + a,
                }
            )
            .stroke_line(
                {
                    "color": color,
                    "line_dash": [],
                    "x1": left_margin - 40,
                    "y1": top_margin + a,
                    "x2": left_margin - 20,
                    "y2": top_margin + a,
                }
            )
        )
        return cls

    @classmethod
    def b_border(cls):
        """Draws a dashed line around the "b" section of the total area."""
        color = Color.GRAY.value
        a, left_margin, top_margin, a_minus_b = itemgetter(
            "a",
            "left_margin",
            "top_margin",
            "a_minus_b",
        )(cls.__dimensions)

        cls.__renderer.stroke_lines(
            {
                "color": color,
                "line_dash": [5, 10],
                "line_segments": [
                    (left_margin + a_minus_b, top_margin + a),
                    (left_margin + a_minus_b, top_margin + a_minus_b),
                    (left_margin + a, top_margin + a_minus_b),
                ],
            }
        )
        return cls

    ####
    @classmethod
    def a_plus_b_border(cls):
        """Strokes a rectangle of the "a" dimension."""
        color = Color.LIGHT_GRAY.value
        a, left_margin, top_margin = itemgetter(
            "a",
            "left_margin",
            "top_margin",
        )(cls.__dimensions)
        cls.__renderer.stroke_rect(
            {
                "color": color,
                "x": left_margin,
                "y": top_margin,
                "width": a,
                "height": a,
            }
        )
        return cls

    @classmethod
    def a_minus_b(cls):
        """Fills and strokes a polygon of "b" subtracted from "a"."""
        color = Color.LIGHT_GRAY.value
        a, left_margin, top_margin, a_minus_b = itemgetter(
            "a",
            "left_margin",
            "top_margin",
            "a_minus_b",
        )(cls.__dimensions)
        points = [
            (left_margin, top_margin),
            (left_margin + a, top_margin),
            (left_margin + a, top_margin + a_minus_b),
            (left_margin + a_minus_b, top_margin + a_minus_b),
            (left_margin + a_minus_b, top_margin + a),
            (left_margin, top_margin + a),
        ]

        (
            cls.__renderer.fill_polygon(
                {
                    "color": color,
                    "points": points,
                }
            ).stroke_polygon(
                {
                    "color": color,
                    "points": points,
                }
            )
        )
        return cls

    @classmethod
    def a_plus_b_line(cls):
        """Draws a dashed line along the right border of "a", where it will be
        combined with "b"."""
        color = Color.GRAY.value
        a, left_margin, top_margin, a_minus_b = itemgetter(
            "a",
            "left_margin",
            "top_margin",
            "a_minus_b",
        )(cls.__dimensions)

        cls.__renderer.stroke_line(
            {
                "color": color,
                "line_dash": [5, 10],
                "x1": left_margin + a,
                "y1": top_margin,
                "x2": left_margin + a,
                "y2": top_margin + a_minus_b,
            }
        )
        return cls

    @classmethod
    def a_minus_b_line(cls):
        """Draws a dashed line along the bottom of "a-b", where "b" will be
        removed from "a"."""
        color = Color.GRAY.value
        b, left_margin, top_margin, a_minus_b = itemgetter(
            "b",
            "left_margin",
            "top_margin",
            "a_minus_b",
        )(cls.__dimensions)

        cls.__renderer.stroke_line(
            {
                "color": color,
                "line_dash": [5, 10],
                "x1": left_margin,
                "y1": top_margin + a_minus_b,
                "x2": left_margin + a_minus_b,
                "y2": top_margin + a_minus_b,
            }
        )
        return cls

    @classmethod
    def label_a_left(cls):
        """Draws the "a" label along the left margin."""
        left_margin, top_margin, center_a = itemgetter(
            "left_margin",
            "top_margin",
            "center_a",
        )(cls.__dimensions)

        cls.label(
            {
                "text": "a",
                "x": left_margin - 48,
                "y": top_margin + center_a,
            }
        )
        return cls

    @classmethod
    def label_a_top(cls):
        """Draws the "a" label along the top margin."""
        left_margin, top_margin, center_a = itemgetter(
            "left_margin",
            "top_margin",
            "center_a",
        )(cls.__dimensions)

        cls.label(
            {
                "text": "a",
                "x": left_margin + center_a,
                "y": top_margin - 10,
            }
        )
        return cls

    @classmethod
    def label_a_bottom(cls):
        """Draws the "a" label along the bottom of "a", after "b" has been
        removed."""
        left_margin, top_margin, center_a, a_minus_b = itemgetter(
            "left_margin",
            "top_margin",
            "center_a",
            "a_minus_b",
        )(cls.__dimensions)

        cls.label(
            {
                "text": "a",
                "x": left_margin + center_a,
                "y": top_margin + a_minus_b + 18,
            }
        )
        return cls

    @classmethod
    def label_b_box_right(cls):
        """Draws the "b" label along the right side of the "b" square area."""
        a, left_margin, top_margin, center_b = itemgetter(
            "a",
            "left_margin",
            "top_margin",
            "center_b",
        )(cls.__dimensions)

        cls.label(
            {
                "text": "b",
                "x": left_margin + a + 15,
                "y": top_margin + a - center_b + 2,
            }
        )
        return cls

    @classmethod
    def label_b_box_bottom(cls):
        """Draws the "b" label along the bottom of the "b" square area."""
        a, left_margin, top_margin, center_b = itemgetter(
            "a",
            "left_margin",
            "top_margin",
            "center_b",
        )(cls.__dimensions)

        cls.label(
            {
                "text": "b",
                "x": left_margin + a - center_b - 2,
                "y": top_margin + a + 22,
            }
        )
        return cls

    @classmethod
    def label_b_left(cls, vertical_offset=0):
        """Draws the "b" label in the left margin, where "b" will be removed
        from "a"."""
        a, left_margin, top_margin, center_b = itemgetter(
            "a",
            "left_margin",
            "top_margin",
            "center_b",
        )(cls.__dimensions)

        cls.label(
            {
                "text": "b",
                "x": left_margin - 18,
                "y": top_margin + a - center_b + 2 + vertical_offset,
            }
        )
        return cls

    @classmethod
    def label_b_right(cls, vertical_offset=0):
        """Draws the "b" label along the right side of where the "b" area has
        been removed from "a"."""
        a, left_margin, top_margin, a_minus_b, center_b = itemgetter(
            "a",
            "left_margin",
            "top_margin",
            "a_minus_b",
            "center_b",
        )(cls.__dimensions)

        cls.label(
            {
                "text": "b",
                "x": left_margin + a_minus_b + 10,
                "y": top_margin + a - center_b + 2 + vertical_offset,
            }
        )
        return cls

    @classmethod
    def label_b_top(cls, horizontal_offset=0):
        """Draws the "b" label in the top margin where the "b" will be added to
        "a"."""
        a, left_margin, top_margin, center_b = itemgetter(
            "a",
            "left_margin",
            "top_margin",
            "center_b",
        )(cls.__dimensions)

        cls.label(
            {
                "text": "b",
                "x": left_margin + a + center_b - 7 + horizontal_offset,
                "y": top_margin - 10,
            }
        )
        return cls

    @classmethod
    def label_b_bottom(cls, horizontal_offset=0):
        """Draws the "b" label along the bottom where the "b" will be added to
        "a"."""
        a, left_margin, top_margin, center_b, a_minus_b = itemgetter(
            "a",
            "left_margin",
            "top_margin",
            "center_b",
            "a_minus_b",
        )(cls.__dimensions)

        cls.label(
            {
                "text": "b",
                "x": left_margin + a + center_b - 7 + horizontal_offset,
                "y": top_margin + a_minus_b + 18,
            }
        )
        return cls

    @classmethod
    def label_a_minus_b_left(cls):
        """Draws the "a - b" label in the left margin."""
        left_margin, top_margin, center_a = itemgetter(
            "left_margin",
            "top_margin",
            "center_a",
        )(cls.__dimensions)

        cls.label(
            {
                "text": "a - b",
                "x": left_margin - 44,
                "y": top_margin + center_a - 30,
            }
        )
        return cls

    @classmethod
    def label_a_minus_b_right(cls, horizontal_offset=0):
        """Draws the "a - b" label along the right side of "a"."""
        a, left_margin, top_margin, center_a = itemgetter(
            "a",
            "left_margin",
            "top_margin",
            "center_a",
        )(cls.__dimensions)

        cls.label(
            {
                "text": "a - b",
                "x": left_margin + a + 8 + horizontal_offset,
                "y": top_margin + center_a - 30,
            }
        )
        return cls

    @classmethod
    def label_a_minus_b_bottom(cls, vertical_offset=0):
        """Draws the "a - b" label along the bottom."""
        a, left_margin, top_margin, center_a_minus_b = itemgetter(
            "a",
            "left_margin",
            "top_margin",
            "center_a_minus_b",
        )(cls.__dimensions)

        cls.label(
            {
                "text": "a - b",
                "x": left_margin + center_a_minus_b - 20,
                "y": top_margin + a + 22 + vertical_offset,
            }
        )
        return cls

    @classmethod
    def label_a_plus_b_top(cls):
        """Draws the "a + b" label in the top margin."""
        left_margin, top_margin, center_a_plus_b = itemgetter(
            "left_margin",
            "top_margin",
            "center_a_plus_b",
        )(cls.__dimensions)

        cls.label(
            {
                "text": "a + b",
                "x": left_margin + center_a_plus_b - 20,
                "y": top_margin - 8,
            }
        )
        return cls

    @classmethod
    def label_a_plus_b_bottom(cls):
        """Draws the "a + b" label along the bottom of the plot."""
        left_margin, top_margin, center_a_plus_b, a_minus_b = itemgetter(
            "left_margin",
            "top_margin",
            "center_a_plus_b",
            "a_minus_b",
        )(cls.__dimensions)

        cls.label(
            {
                "text": "a + b",
                "x": left_margin + center_a_plus_b - 20,
                "y": top_margin + a_minus_b + 20,
            }
        )
        return cls

    @classmethod
    def b_box_snip(cls):
        """Draws the "snip" label before removing the "b" area from "a"."""
        color = Color.BLACK.value
        a, left_margin, top_margin, center_b, a_minus_b = itemgetter(
            "a",
            "left_margin",
            "top_margin",
            "center_b",
            "a_minus_b",
        )(cls.__dimensions)

        # cls.__renderer.clear(
        #     {
        #         "x": left_margin + a_minus_b - 22,
        #         "y": top_margin + a - center_b - 14,
        #         "width": 46,
        #         "height": 22,
        #     }
        # )
        color = Color.WHITE.value
        label = {
            "text": "[snip]",
            "x": left_margin + a_minus_b - 15,
            "y": top_margin + a - center_b + 1,
        }
        settings = {
            "font": "14px serif",
            "font_color": color,
        }
        cls.label(label, settings)

        color = Color.BLACK.value
        label = {
            "text": "[snip]",
            "x": left_margin + a_minus_b - 15 + 2,
            "y": top_margin + a - center_b + 1 + 2,
        }
        settings = {
            "font": "14px serif",
            "font_color": color,
        }
        cls.label(label, settings)
        return cls

    @classmethod
    def a_minus_b_snip(cls):
        """Draws the "snip" label before removing the "b" rectangle from "a"."""
        color = Color.BLACK.value
        left_margin, top_margin, a_minus_b, center_a_minus_b = itemgetter(
            "left_margin",
            "top_margin",
            "a_minus_b",
            "center_a_minus_b",
        )(cls.__dimensions)

        cls.__renderer.clear(
            {
                "x": left_margin + center_a_minus_b - 20,
                "y": top_margin + a_minus_b - 12,
                "width": 46,
                "height": 22,
            }
        )
        label = {
            "text": "[snip]",
            "x": left_margin + center_a_minus_b - 14,
            "y": top_margin + a_minus_b + 3,
        }
        settings = {
            "font": "14px serif",
            "font_color": color,
        }
        cls.label(label, settings)
        return cls

    @classmethod
    def a_plus_b_paste(cls):
        """Draws the "paste" label before adding the "b" rectangle to "a"."""
        color = Color.BLACK.value
        a, left_margin, top_margin, center_a = itemgetter(
            "a",
            "left_margin",
            "top_margin",
            "center_a",
        )(cls.__dimensions)

        cls.__renderer.clear(
            {
                "x": left_margin + a - 22,
                "y": top_margin + center_a - 48,
                "width": 46,
                "height": 22,
            }
        )
        label = {
            "text": "[paste]",
            "x": left_margin + a - 18,
            "y": top_margin + center_a - 33,
        }
        settings = {
            "font": "14px serif",
            "font_color": color,
        }
        cls.label(label, settings)
        return cls
