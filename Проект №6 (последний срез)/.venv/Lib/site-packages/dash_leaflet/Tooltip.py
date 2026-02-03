# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class Tooltip(Component):
    """A Tooltip component.
Used to display small texts on top of map layers.

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

- bubblingMouseEvents (boolean; optional):
    When True, a mouse event on this layer will trigger the same event
    on the map (unless L.DomEvent.stopPropagation is used).

- className (string; optional):
    A custom CSS class name to assign to the overlay.

- clickData (dict; optional):
    An object holding data related to the click event. Typing is
    indicative.

    `clickData` is a dict with keys:

    - latlng (list of numbers; required)

    - layerPoint (list of numbers; required)

    - containerPoint (list of numbers; required)

- content (string; optional):
    Sets the HTML content of the overlay while initializing. If a
    function is passed the source layer will be passed to the
    function. The function should return a String or HTMLElement to be
    used in the overlay.

- dblclickData (dict; optional):
    An object holding data related to the double click event. Typing
    is indicative.

    `dblclickData` is a dict with keys:

    - latlng (list of numbers; required)

    - layerPoint (list of numbers; required)

    - containerPoint (list of numbers; required)

- direction (a value equal to: 'center', 'right', 'left', 'top', 'bottom', 'auto'; optional):
    Direction where to open the tooltip. Possible values are: right,
    left, top, bottom, center, auto. auto will dynamically switch
    between right and left according to the tooltip position on the
    map.

- disableDefaultEventHandlers (boolean; optional):
    If set to True, default events handlers are not registered.
    [MUTABLE].

- eventHandlers (dict; optional):
    Object with keys specifying the event type and the value the
    corresponding event handlers. [MUTABLE].

- interactive (boolean; optional):
    If True, the popup/tooltip will listen to the mouse events.

- loading_state (dict; optional):
    Dash loading state information.

- n_clicks (number; optional):
    An integer that represents the number of times that this element
    has been clicked on.

- n_dblclicks (number; optional):
    An integer that represents the number of times that this element
    has been double-clicked on.

- offset (dict; optional):
    The offset of the popup position.

    `offset` is a dict with keys:

    - clone (required)

    - add (required)

    - subtract (required)

    - divideBy (required)

    - multiplyBy (required)

    - scaleBy (required)

    - unscaleBy (required)

    - round (required)

    - floor (required)

    - ceil (required)

    - trunc (required)

    - distanceTo (required)

    - equals (required)

    - contains (required)

    - toString (optional)

    - x (number; required)

    - y (number; required)

- opacity (number; optional):
    Tooltip container opacity.

- pane (string; optional):
    Map pane where the layer will be added.

- permanent (boolean; optional):
    Whether to open the tooltip permanently or only on mouseover.

- position (dict; optional):
    A geographical point in (lat, lon) format. [MUTABLE].

    `position` is a dict with keys:

    - equals (required)

    - toString (optional)

    - distanceTo (required)

    - wrap (required)

    - toBounds (required)

    - clone (required)

    - lat (number; required)

    - lng (number; required)

    - alt (number; optional)

- sticky (boolean; optional):
    If True, the tooltip will follow the mouse instead of being fixed
    at the feature center."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_leaflet'
    _type = 'Tooltip'
    Position = TypedDict(
        "Position",
            {
            "equals": typing.Any,
            "toString": NotRequired[typing.Any],
            "distanceTo": typing.Any,
            "wrap": typing.Any,
            "toBounds": typing.Any,
            "clone": typing.Any,
            "lat": typing.Union[int, float, numbers.Number],
            "lng": typing.Union[int, float, numbers.Number],
            "alt": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    Offset = TypedDict(
        "Offset",
            {
            "clone": typing.Any,
            "add": typing.Any,
            "subtract": typing.Any,
            "divideBy": typing.Any,
            "multiplyBy": typing.Any,
            "scaleBy": typing.Any,
            "unscaleBy": typing.Any,
            "round": typing.Any,
            "floor": typing.Any,
            "ceil": typing.Any,
            "trunc": typing.Any,
            "distanceTo": typing.Any,
            "equals": typing.Any,
            "contains": typing.Any,
            "toString": NotRequired[typing.Any],
            "x": typing.Union[int, float, numbers.Number],
            "y": typing.Union[int, float, numbers.Number]
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
        position: typing.Optional[typing.Union["Position"]] = None,
        opacity: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        className: typing.Optional[str] = None,
        interactive: typing.Optional[bool] = None,
        bubblingMouseEvents: typing.Optional[bool] = None,
        attribution: typing.Optional[str] = None,
        pane: typing.Optional[str] = None,
        content: typing.Optional[typing.Union[str]] = None,
        offset: typing.Optional["Offset"] = None,
        direction: typing.Optional[Literal["center", "right", "left", "top", "bottom", "auto"]] = None,
        permanent: typing.Optional[bool] = None,
        sticky: typing.Optional[bool] = None,
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
        self._prop_names = ['children', 'id', 'attribution', 'bubblingMouseEvents', 'className', 'clickData', 'content', 'dblclickData', 'direction', 'disableDefaultEventHandlers', 'eventHandlers', 'interactive', 'loading_state', 'n_clicks', 'n_dblclicks', 'offset', 'opacity', 'pane', 'permanent', 'position', 'sticky']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'attribution', 'bubblingMouseEvents', 'className', 'clickData', 'content', 'dblclickData', 'direction', 'disableDefaultEventHandlers', 'eventHandlers', 'interactive', 'loading_state', 'n_clicks', 'n_dblclicks', 'offset', 'opacity', 'pane', 'permanent', 'position', 'sticky']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Tooltip, self).__init__(children=children, **args)
