from operator import itemgetter
from enum import Enum
from ipywidgets import FloatSlider, HBox, Label, Layout
from .constants import UIContainerProp

class SliderProp(Enum):
    DESCRIPTION = 'description'
    VALUE = 'value'
    MIN = 'minimum'
    MAX = 'maximum'
    STEP = 'step'

def _update_label(label, label_precision):
    def fn(change):
        value = change['new']
        label.value = f"{value:.{label_precision}f}"
    return fn

def define_slider(options, key='slider', label_precision=0):
    description, value, minimum, maximum, step = itemgetter(
        SliderProp.DESCRIPTION,
        SliderProp.VALUE,
        SliderProp.MIN,
        SliderProp.MAX,
        SliderProp.STEP,
    )(options)

    slider = FloatSlider(
        value=value,
        min=minimum,
        max=maximum,
        step=step,
        orientation='horizontal',
        readout=False,
        continuous_update=False
    )

    label = Label(
        value=description,
        layout=Layout(width='8rem'),
    )
    label_min = Label(
        value=f"{minimum:.{label_precision}f}",
        style={
            'text_color': 'gray'
        },
    )
    label_max = Label(
        value=f"{maximum:.{label_precision}f}",
        style={
            'text_color': 'gray'
        },
    )

    label_value = Label(
        value=f"{value:.{label_precision}f}",
        layout=Layout(
            width='3rem',
            margin='2px 0 0 1rem',
            justify_content='flex-end',
        ),
    )
    slider.observe(_update_label(label_value, label_precision), names="value")

    return {
        UIContainerProp.CONTROLS: {
            key: slider,
        },
        UIContainerProp.CONTAINER: HBox(
            children=[
                label,
                HBox(
                    children=[label_min, slider, label_max],
                    layout=Layout(justify_content='center'),
                ),
                label_value
            ],
            layout=Layout(
                justify_content='space-between'
            ))
    }
