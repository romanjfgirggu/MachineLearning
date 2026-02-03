# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class VideoOverlay(Component):
    """A VideoOverlay component.
Used to load and display a video player over specific bounds of the map. Uses the <video> HTML5 element.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Children [MUTABLE].

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- alt (string; optional):
    Text for the alt attribute of the image (useful for
    accessibility).

- attribution (string; optional):
    String to be shown in the attribution control, e.g. \"©
    OpenStreetMap contributors\". It describes the layer data and is
    often a legal obligation towards copyright holders and tile
    providers. [MUTABLE].

- autoplay (boolean; optional):
    Whether the video starts playing automatically when loaded. On
    some browsers autoplay will only work with muted: True.

- bounds (dict; required):
    The geographical bounds that the overlay is tied to. [MUTABLE].

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
    A custom class name to assign to the image. Empty by default.

- clickData (dict; optional):
    An object holding data related to the click event. Typing is
    indicative.

    `clickData` is a dict with keys:

    - latlng (list of numbers; required)

    - layerPoint (list of numbers; required)

    - containerPoint (list of numbers; required)

- crossOrigin (optional):
    Whether the crossOrigin attribute will be added to the image. If a
    String is provided, the image will have its crossOrigin attribute
    set to the String provided. This is needed if you want to access
    image pixel data. Refer to CORS Settings for valid String values.

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

- errorOverlayUrl (string; optional):
    URL to the overlay image to show in place of the overlay that
    failed to load.

- eventHandlers (dict; optional):
    Object with keys specifying the event type and the value the
    corresponding event handlers. [MUTABLE].

- interactive (boolean; optional):
    If True, the image overlay will emit mouse events when clicked or
    hovered.

- keepAspectRatio (boolean; optional):
    Whether the video will save aspect ratio after the projection.

- loading_state (dict; optional):
    Dash loading state information.

- loop (boolean; optional):
    Whether the video will loop back to the beginning when played.

- muted (boolean; default True):
    Whether the video starts on mute when loaded.

- n_clicks (number; optional):
    An integer that represents the number of times that this element
    has been clicked on.

- n_dblclicks (number; optional):
    An integer that represents the number of times that this element
    has been double-clicked on.

- n_loads (number; optional):
    An integer that represents the number of times that the load event
    has fired.

- opacity (number; optional):
    The overlay opacity. [MUTABLE].

- pane (string; optional):
    Map pane where the layer will be added.

- play (boolean; optional):
    Set to True/False to start/stop video playback. [MUTABLE].

- playsInline (boolean; optional):
    Mobile browsers will play the video right where it is instead of
    open it up in fullscreen mode.

- url (string; required):
    The video URL. [MUTABLE].

- zIndex (number; optional):
    The overlay zIndex. [MUTABLE]."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_leaflet'
    _type = 'VideoOverlay'
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
        opacity: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        className: typing.Optional[str] = None,
        interactive: typing.Optional[bool] = None,
        bubblingMouseEvents: typing.Optional[bool] = None,
        attribution: typing.Optional[str] = None,
        pane: typing.Optional[str] = None,
        alt: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        crossOrigin: typing.Optional[typing.Union[Literal["anonymous"], Literal["use-credentials"]]] = None,
        errorOverlayUrl: typing.Optional[str] = None,
        zIndex: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        bounds: typing.Optional[typing.Union["Bounds"]] = None,
        autoplay: typing.Optional[bool] = None,
        loop: typing.Optional[bool] = None,
        keepAspectRatio: typing.Optional[bool] = None,
        muted: typing.Optional[bool] = None,
        playsInline: typing.Optional[bool] = None,
        play: typing.Optional[bool] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        loading_state: typing.Optional[dict] = None,
        eventHandlers: typing.Optional[dict] = None,
        disableDefaultEventHandlers: typing.Optional[bool] = None,
        n_clicks: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        clickData: typing.Optional["ClickData"] = None,
        n_dblclicks: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        dblclickData: typing.Optional["DblclickData"] = None,
        n_loads: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'alt', 'attribution', 'autoplay', 'bounds', 'bubblingMouseEvents', 'className', 'clickData', 'crossOrigin', 'dblclickData', 'disableDefaultEventHandlers', 'errorOverlayUrl', 'eventHandlers', 'interactive', 'keepAspectRatio', 'loading_state', 'loop', 'muted', 'n_clicks', 'n_dblclicks', 'n_loads', 'opacity', 'pane', 'play', 'playsInline', 'url', 'zIndex']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'alt', 'attribution', 'autoplay', 'bounds', 'bubblingMouseEvents', 'className', 'clickData', 'crossOrigin', 'dblclickData', 'disableDefaultEventHandlers', 'errorOverlayUrl', 'eventHandlers', 'interactive', 'keepAspectRatio', 'loading_state', 'loop', 'muted', 'n_clicks', 'n_dblclicks', 'n_loads', 'opacity', 'pane', 'play', 'playsInline', 'url', 'zIndex']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['bounds', 'url']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(VideoOverlay, self).__init__(children=children, **args)
