# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class PolylineDecorator(Component):
    """A PolylineDecorator component.
Polyline is a wrapper of Polyline in react-leaflet. It takes similar properties to its react-leaflet counterpart.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The children of this component. If positions are not specified, an
    attempt is made to read them from the children property. In this
    case, the children must be a single PolyLine or a single Polygon.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- clickData (dict; optional):
    An object holding data related to the click event. Typing is
    indicative.

    `clickData` is a dict with keys:

    - latlng (list of numbers; required)

    - layerPoint (list of numbers; required)

    - containerPoint (list of numbers; required)

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

- loading_state (dict; optional):
    Dash loading state information.

- n_clicks (number; optional):
    An integer that represents the number of times that this element
    has been clicked on.

- n_dblclicks (number; optional):
    An integer that represents the number of times that this element
    has been double-clicked on.

- patterns (list of dicts; required):
    List of patterns to be added.

    `patterns` is a list of dicts with keys:

    - offset (string; required)

    - endOffset (string; required)

    - repeat (string; required)

    - dash (dict; required)

        `dash` is a dict with keys:

        - pixelSize (number; required)

        - pathOptions (dict; required)

    - arrowHead (dict; required)

        `arrowHead` is a dict with keys:

        - polygon (boolean; required)

        - pixelSize (number; required)

        - headAngle (number; required)

        - pathOptions (dict; required)

    - marker (dict; required)

        `marker` is a dict with keys:

        - markerOptions (dict; required)

        - rotate (boolean; required)

- positions (list of list of numberss | list of list of list of numbersss; optional):
    An array of geographical points (lat, lon)."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_leaflet'
    _type = 'PolylineDecorator'
    PatternsDash = TypedDict(
        "PatternsDash",
            {
            "pixelSize": typing.Union[int, float, numbers.Number],
            "pathOptions": dict
        }
    )

    PatternsArrowHead = TypedDict(
        "PatternsArrowHead",
            {
            "polygon": bool,
            "pixelSize": typing.Union[int, float, numbers.Number],
            "headAngle": typing.Union[int, float, numbers.Number],
            "pathOptions": dict
        }
    )

    PatternsMarker = TypedDict(
        "PatternsMarker",
            {
            "markerOptions": dict,
            "rotate": bool
        }
    )

    Patterns = TypedDict(
        "Patterns",
            {
            "offset": str,
            "endOffset": str,
            "repeat": str,
            "dash": "PatternsDash",
            "arrowHead": "PatternsArrowHead",
            "marker": "PatternsMarker"
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
        positions: typing.Optional[typing.Union[typing.Sequence[typing.Sequence[typing.Union[int, float, numbers.Number]]], typing.Sequence[typing.Sequence[typing.Sequence[typing.Union[int, float, numbers.Number]]]]]] = None,
        patterns: typing.Optional[typing.Sequence["Patterns"]] = None,
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
        self._prop_names = ['children', 'id', 'clickData', 'dblclickData', 'disableDefaultEventHandlers', 'eventHandlers', 'loading_state', 'n_clicks', 'n_dblclicks', 'patterns', 'positions']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'clickData', 'dblclickData', 'disableDefaultEventHandlers', 'eventHandlers', 'loading_state', 'n_clicks', 'n_dblclicks', 'patterns', 'positions']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['patterns']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(PolylineDecorator, self).__init__(children=children, **args)
