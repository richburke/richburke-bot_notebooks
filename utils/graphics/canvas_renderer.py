"""
Provides a class that contains convenience methods for a ipycanvas.
"""

from operator import itemgetter


class CanvasRenderer:
    """
    Convenience methods for a Canvas.
    """

    __canvas = None
    __defaults = None

    @classmethod
    def set_canvas(cls, canvas):
        """
        Applies the relevant canvas. This needs to be called before other
        class methods.
        """
        cls.__canvas = canvas
        return cls

    @classmethod
    def set_defaults(cls, default_canvas_settings):
        """
        Applies the canvas's defaults. This needs to be called before other
        class methods.
        """
        cls.__defaults = default_canvas_settings
        return cls

    @classmethod
    def defaults(cls):
        """
        Returns the existing list of canvas defaults.
        """
        return cls.__defaults

    @classmethod
    def clear(cls, dimensions=None):
        """
        Clears a rectangle of the supplied dimensions. If no dimensions are
        supplied, the whole canvas is cleared.
        """
        if dimensions is None:
            cls.__canvas.clear()
            return cls

        x, y, width, height = itemgetter("x", "y", "width", "height")(dimensions)
        cls.__canvas.clear_rect(x, y, width, height)
        return cls

    @classmethod
    def restore(cls, settings):
        """
        Restores a canvas to its default settings.
        """
        cls.__canvas.font = settings["font"]
        cls.__canvas.fill_style = settings["fill_style"]
        cls.__canvas.stroke_style = settings["stroke_style"]
        return cls

    @classmethod
    def fill_rect(cls, settings):
        """
        Fills a rectangle of the supplied color and dimensions. It stashes and
        restores existing canvas values.

        The properties of the settings are "color", "x", "y", "width", "height".
        """
        color, x, y, width, height = itemgetter(
            "color",
            "x",
            "y",
            "width",
            "height",
        )(settings)
        original_fill_style = cls.__canvas.fill_style
        cls.__canvas.fill_style = color
        cls.__canvas.fill_rect(x, y, width, height)
        cls.__canvas.fill_style = original_fill_style
        return cls

    @classmethod
    def stroke_rect(cls, settings):
        """
        Strokes a rectangle of the supplied color and dimensions. It stashes and
        restores existing canvas values.

        The properties of the settings are "color", "x", "y", "width", "height".
        """
        color, x, y, width, height = itemgetter("color", "x", "y", "width", "height")(
            settings
        )
        original_stroke_style = cls.__canvas.stroke_style
        cls.__canvas.stroke_style = color
        cls.__canvas.stroke_rect(x, y, width, height)
        cls.__canvas.stroke_style = original_stroke_style
        return cls

    @classmethod
    def fill_polygon(cls, settings):
        """
        Fills a polygon of supplied points/vertices with the supplied color. It
        stashes and restores existing canvas values.

        The properties of the settings are "color" and "points". The points
        property is a list of two-value tuples.
        """
        color, points = itemgetter("color", "points")(settings)
        original_fill_style = cls.__canvas.fill_style
        cls.__canvas.fill_style = color
        cls.__canvas.fill_polygon(points)
        cls.__canvas.fill_style = original_fill_style
        return cls

    @classmethod
    def stroke_polygon(cls, settings):
        """
        Strokes a polygon of supplied points/vertices with the supplied color.
        It stashes and restores existing canvas values.

        The properties of the settings are "color" and "points". The points
        property is a list of two-value tuples.
        """
        color, points = itemgetter("color", "points")(settings)
        original_stroke_style = cls.__canvas.stroke_style
        cls.__canvas.stroke_style = color
        cls.__canvas.stroke_polygon(points)
        cls.__canvas.stroke_style = original_stroke_style
        return cls

    @classmethod
    def stroke_line(cls, settings):
        """
        Strokes a line with the supplied color and dash style. It stashes and
        restores existing canvas values.

        The properties of the settings are "color", "line_dash", "x1", "y1",
        "x2", "y2".
        """
        color, line_dash, x1, y1, x2, y2 = itemgetter(
            "color", "line_dash", "x1", "y1", "x2", "y2"
        )(settings)
        original_stroke_style = cls.__canvas.stroke_style
        original_line_dash = cls.__canvas.get_line_dash()
        cls.__canvas.stroke_style = color
        cls.__canvas.set_line_dash(line_dash)
        cls.__canvas.stroke_line(x1, y1, x2, y2)
        cls.__canvas.stroke_style = original_stroke_style
        cls.__canvas.set_line_dash(original_line_dash)
        return cls

    @classmethod
    def stroke_lines(cls, settings):
        """
        Strokes line segments with the supplied color and dash style. It stashes
        and restores existing canvas values.

        The properties of the settings are "color", "line_dash", and
        "line_segments".
        """
        color, line_dash, line_segments = itemgetter(
            "color", "line_dash", "line_segments"
        )(settings)
        original_stroke_style = cls.__canvas.stroke_style
        original_line_dash = cls.__canvas.get_line_dash()
        cls.__canvas.stroke_style = color
        cls.__canvas.set_line_dash(line_dash)
        cls.__canvas.stroke_lines(line_segments)
        cls.__canvas.stroke_style = original_stroke_style
        cls.__canvas.set_line_dash(original_line_dash)
        return cls

    @classmethod
    def label(cls, label, settings):
        """
        Draws a label with the supplied settings. It stashes and restores
        existing canvas values.

        The properties of the label are "text", "x", and "y". The properties of
        the settings are "font", "font_color" and "filter.
        """
        if "filter" not in settings:
            settings["filter"] = "none"
        font, font_color, flter = itemgetter("font", "font_color", "filter")(settings)
        text, x, y = itemgetter("text", "x", "y")(label)

        original_fill_style = cls.__canvas.fill_style
        original_font = cls.__canvas.font
        original_filter = cls.__canvas.filter
        cls.__canvas.font = font
        cls.__canvas.fill_style = font_color
        cls.__canvas.filter = flter
        cls.__canvas.fill_text(text, x, y)
        cls.__canvas.fill_style = original_fill_style
        cls.__canvas.font = original_font
        cls.__canvas.filter = original_filter

        return cls
