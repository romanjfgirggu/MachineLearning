# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class Rectangle(Component):
    """A Rectangle component.
A class for drawing rectangle overlays on a map.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Children [MUTABLE].

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- attribution (string; optional):
    String to be shown in the attribution control, e.g. \"©
    OpenStreetMap contributors\". It describes the layer data and is
    often a legal obligation towards copyright holders and tile
    providers. [MUTABLE].

- bounds (dict; required):
    Geographical bounds.

    `bounds` is a dict with keys:

    - extend (required)

    - pad (required)

    - getCenter (required)

    - getSouthWest (required)

    - getNorthEast (required)

    - getNorthWest (required)

    - getSouthEast (required)

    - getWest (required)

    - getSouth (required)

    - getEast (required)

    - getNorth (required)

    - contains (required)

    - intersects (required)

    - overlaps (required)

    - toBBoxString (required)

    - equals (required)

    - isValid (required)

- bubblingMouseEvents (boolean; optional):
    When True, a mouse event on this layer will trigger the same event
    on the map (unless L.DomEvent.stopPropagation is used).

- className (string; optional):
    Custom class name set on an element. Only for SVG renderer.

- clickData (dict; optional):
    An object holding data related to the click event. Typing is
    indicative.

    `clickData` is a dict with keys:

    - latlng (list of numbers; required)

    - layerPoint (list of numbers; required)

    - containerPoint (list of numbers; required)

- color (string; optional):
    Stroke color.

- dashArray (string; optional):
    A string that defines the stroke dash pattern. Doesn't work on
    Canvas-powered layers in some old browsers.

- dashOffset (string; optional):
    A string that defines the distance into the dash pattern to start
    the dash. Doesn't work on Canvas-powered layers in some old
    browsers.

- dblclickData (dict; optional):
    An object holding data related to the double click event. Typing
    is indicative.

    `dblclickData` is a dict with keys:

    - latlng (list of numbers; required)

    - layerPoint (list of numbers; required)

    - containerPoint (list of numbers; required)

- disableDefaultEventHandlers (boolean; optional):
    If set to True, default events handlers are not registered.
    [MUTABLE].

- eventHandlers (dict; optional):
    Object with keys specifying the event type and the value the
    corresponding event handlers. [MUTABLE].

- fill (boolean; optional):
    Whether to fill the path with color. Set it to False to disable
    filling on polygons or circles.

- fillColor (string; optional):
    Fill color. Defaults to the value of the color option.

- fillOpacity (number; optional):
    Fill opacity.

- fillRule (a value equal to: 'inherit', 'nonzero', 'evenodd'; optional):
    A string that defines how the inside of a shape is determined.

- interactive (boolean; optional):
    If False, the layer will not emit mouse events and will act as a
    part of the underlying map.

- lineCap (a value equal to: 'butt', 'round', 'square', 'inherit'; optional):
    A string that defines shape to be used at the end of the stroke.

- lineJoin (a value equal to: 'round', 'inherit', 'miter', 'bevel'; optional):
    A string that defines shape to be used at the corners of the
    stroke.

- loading_state (dict; optional):
    Dash loading state information.

- n_clicks (number; optional):
    An integer that represents the number of times that this element
    has been clicked on.

- n_dblclicks (number; optional):
    An integer that represents the number of times that this element
    has been double-clicked on.

- noClip (boolean; optional):
    Disable clipping.

- opacity (number; optional):
    Stroke opacity.

- pane (string; optional):
    Map pane where the layer will be added.

- pathOptions (dict; optional):
    Path options. Use this prop, if you want to modify path options
    through callbacks. [MUTABLE].

    `pathOptions` is a dict with keys:

    - stroke (boolean; optional):
        Whether to draw stroke along the path. Set False to disable
        borders on polygons or circles.

    - color (string; optional):
        Stroke color.

    - weight (number; optional):
        Stroke width in pixels.

    - opacity (number; optional):
        Stroke opacity.

    - lineCap (a value equal to: 'butt', 'round', 'square', 'inherit'; optional):
        A string that defines shape to be used at the end of the
        stroke.

    - lineJoin (a value equal to: 'round', 'inherit', 'miter', 'bevel'; optional):
        A string that defines shape to be used at the corners of the
        stroke.

    - dashArray (string; optional):
        A string that defines the stroke dash pattern. Doesn't work on
        Canvas-powered layers in some old browsers.

    - dashOffset (string; optional):
        A string that defines the distance into the dash pattern to
        start the dash. Doesn't work on Canvas-powered layers in some
        old browsers.

    - fill (boolean; optional):
        Whether to fill the path with color. Set it to False to
        disable filling on polygons or circles.

    - fillColor (string; optional):
        Fill color. Defaults to the value of the color option.

    - fillOpacity (number; optional):
        Fill opacity.

    - fillRule (a value equal to: 'inherit', 'nonzero', 'evenodd'; optional):
        A string that defines how the inside of a shape is determined.

    - className (string; optional):
        Custom class name set on an element. Only for SVG renderer.

    - interactive (boolean; optional):
        If False, the layer will not emit mouse events and will act as
        a part of the underlying map.

    - bubblingMouseEvents (boolean; optional):
        When True, a mouse event on this layer will trigger the same
        event on the map (unless L.DomEvent.stopPropagation is used).

    - attribution (string; optional):
        String to be shown in the attribution control, e.g. \"©
        OpenStreetMap contributors\". It describes the layer data and
        is often a legal obligation towards copyright holders and tile
        providers.

    - pane (string; optional):
        Map pane where the layer will be added.

- smoothFactor (number; optional):
    How much to simplify the shape on each zoom level. More means
    better performance and smoother look, and less means more accurate
    representation.

- stroke (boolean; optional):
    Whether to draw stroke along the path. Set False to disable
    borders on polygons or circles.

- weight (number; optional):
    Stroke width in pixels."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_leaflet'
    _type = 'Rectangle'
    PathOptions = TypedDict(
        "PathOptions",
            {
            "stroke": NotRequired[bool],
            "color": NotRequired[str],
            "weight": NotRequired[typing.Union[int, float, numbers.Number]],
            "opacity": NotRequired[typing.Union[int, float, numbers.Number]],
            "lineCap": NotRequired[Literal["butt", "round", "square", "inherit"]],
            "lineJoin": NotRequired[Literal["round", "inherit", "miter", "bevel"]],
            "dashArray": NotRequired[str],
            "dashOffset": NotRequired[str],
            "fill": NotRequired[bool],
            "fillColor": NotRequired[str],
            "fillOpacity": NotRequired[typing.Union[int, float, numbers.Number]],
            "fillRule": NotRequired[Literal["inherit", "nonzero", "evenodd"]],
            "className": NotRequired[str],
            "interactive": NotRequired[bool],
            "bubblingMouseEvents": NotRequired[bool],
            "attribution": NotRequired[str],
            "pane": NotRequired[str]
        }
    )

    Bounds = TypedDict(
        "Bounds",
            {
            "extend": typing.Any,
            "pad": typing.Any,
            "getCenter": typing.Any,
            "getSouthWest": typing.Any,
            "getNorthEast": typing.Any,
            "getNorthWest": typing.Any,
            "getSouthEast": typing.Any,
            "getWest": typing.Any,
            "getSouth": typing.Any,
            "getEast": typing.Any,
            "getNorth": typing.Any,
            "contains": typing.Any,
            "intersects": typing.Any,
            "overlaps": typing.Any,
            "toBBoxString": typing.Any,
            "equals": typing.Any,
            "isValid": typing.Any
        }
    )

    ClickData = TypedDict(
        "ClickData",
            {
            "latlng": typing.Sequence[typing.Union[int, float, numbers.Number]],
            "layerPoint": typing.Sequence[typing.Union[int, float, numbers.Number]],
            "containerPoint": typing.Sequence[typing.Union[int, float, numbers.Number]]
        }
    )

    DblclickData = TypedDict(
        "DblclickData",
            {
            "latlng": typing.Sequence[typing.Union[int, float, numbers.Number]],
            "layerPoint": typing.Sequence[typing.Union[int, float, numbers.Number]],
            "containerPoint": typing.Sequence[typing.Union[int, float, numbers.Number]]
        }
    )

    @_explicitize_args
    def __init__(
        self,
        children: typing.Optional[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]] = None,
        stroke: typing.Optional[bool] = None,
        color: typing.Optional[str] = None,
        weight: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        opacity: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        lineCap: typing.Optional[Literal["butt", "round", "square", "inherit"]] = None,
        lineJoin: typing.Optional[Literal["round", "inherit", "miter", "bevel"]] = None,
        dashArray: typing.Optional[str] = None,
        dashOffset: typing.Optional[str] = None,
        fill: typing.Optional[bool] = None,
        fillColor: typing.Optional[str] = None,
        fillOpacity: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        fillRule: typing.Optional[Literal["inherit", "nonzero", "evenodd"]] = None,
        className: typing.Optional[str] = None,
        interactive: typing.Optional[bool] = None,
        bubblingMouseEvents: typing.Optional[bool] = None,
        attribution: typing.Optional[str] = None,
        pane: typing.Optional[str] = None,
        pathOptions: typing.Optional["PathOptions"] = None,
        bounds: typing.Optional[typing.Union["Bounds"]] = None,
        smoothFactor: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        noClip: typing.Optional[bool] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        loading_state: typing.Optional[dict] = None,
        eventHandlers: typing.Optional[dict] = None,
        disableDefaultEventHandlers: typing.Optional[bool] = None,
        n_clicks: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        clickData: typing.Optional["ClickData"] = None,
        n_dblclicks: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        dblclickData: typing.Optional["DblclickData"] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'attribution', 'bounds', 'bubblingMouseEvents', 'className', 'clickData', 'color', 'dashArray', 'dashOffset', 'dblclickData', 'disableDefaultEventHandlers', 'eventHandlers', 'fill', 'fillColor', 'fillOpacity', 'fillRule', 'interactive', 'lineCap', 'lineJoin', 'loading_state', 'n_clicks', 'n_dblclicks', 'noClip', 'opacity', 'pane', 'pathOptions', 'smoothFactor', 'stroke', 'weight']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'attribution', 'bounds', 'bubblingMouseEvents', 'className', 'clickData', 'color', 'dashArray', 'dashOffset', 'dblclickData', 'disableDefaultEventHandlers', 'eventHandlers', 'fill', 'fillColor', 'fillOpacity', 'fillRule', 'interactive', 'lineCap', 'lineJoin', 'loading_state', 'n_clicks', 'n_dblclicks', 'noClip', 'opacity', 'pane', 'pathOptions', 'smoothFactor', 'stroke', 'weight']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['bounds']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Rectangle, self).__init__(children=children, **args)
