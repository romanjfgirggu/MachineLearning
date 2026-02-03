# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class Colorbar(Component):
    """A Colorbar component.
Color bar control component for Leaflet. Most of the functionality is
delegated to chroma-js (see the docs for that module). For creating your
own color schemes for maps, have a look at http://colorbrewer2.org.

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- className (string; optional):
    Any CSS classes to appy.

- classes (number | list of numbers; optional):
    The number or positions of discrete classes in the colorbar. If
    not set the colorbar will be continuous, which is the default.

- colorscale (string | list of strings; optional):
    Chroma-js colorscale. Either a colorscale name, e.g. \"Viridis\",
    or a list of colors, e.g. [\"black\", \"#fdd49e\",
    \"rgba(255,0,0,0.35)\"]. The predefined colorscales are listed
    here:
    https://github.com/gka/chroma.js/blob/master/src/colors/colorbrewer.js.

- height (number; optional):
    Height in pixels.

- loading_state (dict; optional):
    Dash loading state information.

- max (number; optional):
    Domain maximum of the colorbar. Translates to the last color of
    the colorscale.

- min (number; optional):
    Domain minimum of the colorbar. Translates to the first color of
    the colorscale.

- nTicks (number; optional):
    Number of ticks on the colorbar.

- opacity (number; optional):
    Opacity of the colorbar. Use it to match the perceived colors from
    an overlay with opacity.

- position (a value equal to: 'topleft', 'topright', 'bottomleft', 'bottomright'; optional):
    Map control position.

- tickDecimals (number; optional):
    If set, fixes the tick decimal points to the given number.

- tickText (list of numbers; optional):
    If set, this text will be used instead of the data values.

- tickValues (list of numbers; optional):
    If set, these values are used for ticks (rather than the ones
    genrated based on nTicks).

- tooltip (boolean; optional):
    If True, the value will be shown as tooltip on hover.

- unit (string; optional):
    Optional text to append to the colorbar ticks.

- width (number; optional):
    Width in pixels."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_leaflet'
    _type = 'Colorbar'

    @_explicitize_args
    def __init__(
        self,
        position: typing.Optional[Literal["topleft", "topright", "bottomleft", "bottomright"]] = None,
        opacity: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        className: typing.Optional[str] = None,
        colorscale: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        width: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        height: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        min: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        max: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        classes: typing.Optional[typing.Union[typing.Union[int, float, numbers.Number], typing.Sequence[typing.Union[int, float, numbers.Number]]]] = None,
        unit: typing.Optional[str] = None,
        nTicks: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        tickDecimals: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        tickValues: typing.Optional[typing.Sequence[typing.Union[int, float, numbers.Number]]] = None,
        tickText: typing.Optional[typing.Sequence[typing.Union[int, float, numbers.Number]]] = None,
        tooltip: typing.Optional[bool] = None,
        style: typing.Optional[typing.Any] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        loading_state: typing.Optional[dict] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'className', 'classes', 'colorscale', 'height', 'loading_state', 'max', 'min', 'nTicks', 'opacity', 'position', 'style', 'tickDecimals', 'tickText', 'tickValues', 'tooltip', 'unit', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'classes', 'colorscale', 'height', 'loading_state', 'max', 'min', 'nTicks', 'opacity', 'position', 'style', 'tickDecimals', 'tickText', 'tickValues', 'tooltip', 'unit', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(Colorbar, self).__init__(**args)
