# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class WMSTileLayer(Component):
    """A WMSTileLayer component.
Used to display WMS services as tile layers on the map.

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- attribution (string; optional):
    String to be shown in the attribution control, e.g. \"©
    OpenStreetMap contributors\". It describes the layer data and is
    often a legal obligation towards copyright holders and tile
    providers.

- bounds (dict; optional):
    If set, tiles will only be loaded inside the set LatLngBounds.

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

- className (string; optional):
    A custom class name to assign to the tile layer. Empty by default.

- crossOrigin (optional):
    Whether the crossOrigin attribute will be added to the tiles. If a
    String is provided, all tiles will have their crossOrigin
    attribute set to the String provided. This is needed if you want
    to access tile pixel data. Refer to CORS Settings for valid String
    values.

- crs (string; optional):
    The Coordinate Reference System to use. Don't change this if
    you're not sure what it means. [DL].

- detectRetina (boolean; optional):
    If True and user is on a retina display, it will request four
    tiles of half the specified size and a bigger zoom level in place
    of one to utilize the high resolution.

- disableDefaultEventHandlers (boolean; optional):
    If set to True, default events handlers are not registered.
    [MUTABLE].

- errorTileUrl (string; optional):
    URL to the tile image to show in place of the tile that failed to
    load.

- eventHandlers (dict; optional):
    Object with keys specifying the event type and the value the
    corresponding event handlers. [MUTABLE].

- format (string; optional):
    WMS image format (use 'image/png' for layers with transparency).

- keepBuffer (number; optional):
    When panning the map, keep this many rows and columns of tiles
    before unloading them.

- layers (string; required):
    Comma-separated list of WMS layers to show.

- loading_state (dict; optional):
    Dash loading state information.

- maxNativeZoom (number; optional):
    Maximum zoom number the tile source has available. If it is
    specified, the tiles on all zoom levels higher than maxNativeZoom
    will be loaded from maxNativeZoom level and auto-scaled.

- maxZoom (number; optional):
    The maximum zoom level up to which this layer will be displayed
    (inclusive).

- minNativeZoom (number; optional):
    Minimum zoom number the tile source has available. If it is
    specified, the tiles on all zoom levels lower than minNativeZoom
    will be loaded from minNativeZoom level and auto-scaled.

- minZoom (number; optional):
    The minimum zoom level down to which this layer will be displayed
    (inclusive).

- n_loads (number; optional):
    An integer that represents the number of times that the load event
    has fired.

- noWrap (boolean; optional):
    Whether the layer is wrapped around the antimeridian. If True, the
    GridLayer will only be displayed once at low zoom levels. Has no
    effect when the map CRS doesn't wrap around. Can be used in
    combination with bounds to prevent requesting tiles outside the
    CRS limits.

- opacity (number; optional):
    The layer opacity. [MUTABLE].

- pane (string; optional):
    Map pane where the layer will be added.

- params (dict; optional):
    WMS parameters. [MUTABLE].

    `params` is a dict with keys:

    - format (string; optional)

    - layers (string; required)

    - request (string; optional)

    - service (string; optional)

    - styles (string; optional)

    - version (string; optional)

    - transparent (boolean; optional)

    - width (number; optional)

    - height (number; optional)

- referrerPolicy (optional):
    Whether the referrerPolicy attribute will be added to the tiles.
    If a String is provided, all tiles will have their referrerPolicy
    attribute set to the String provided. This may be needed if your
    map's rendering context has a strict default but your tile
    provider expects a valid referrer (e.g. to validate an API token).
    Refer to HTMLImageElement.referrerPolicy for valid String values.

- styles (string; optional):
    Comma-separated list of WMS styles.

- subdomains (string | list of strings; optional):
    Subdomains of the tile service. Can be passed in the form of one
    string (where each letter is a subdomain name) or an array of
    strings.

- tileSize (number; optional):
    Width and height of tiles in the grid. Use a number if width and
    height are equal, or L.point(width, height) otherwise.

- tms (boolean; optional):
    If True, inverses Y axis numbering for tiles (turn this on for TMS
    services).

- transparent (boolean; optional):
    If True, the WMS service will return images with transparency.

- updateInterval (number; optional):
    Tiles will not update more than once every updateInterval
    milliseconds when panning.

- updateWhenIdle (boolean; optional):
    Load new tiles only when panning ends. True by default on mobile
    browsers, in order to avoid too many requests and keep smooth
    navigation. False otherwise in order to display new tiles during
    panning, since it is easy to pan outside the keepBuffer option in
    desktop browsers.

- updateWhenZooming (boolean; optional):
    By default, a smooth zoom animation (during a touch zoom or a
    flyTo()) will update grid layers every integer zoom level. Setting
    this option to False will update the grid layer only when the
    smooth animation ends.

- uppercase (boolean; optional):
    If True, WMS request parameter keys will be uppercase.

- url (string; required):
    The URL template.

- version (string; optional):
    Version of the WMS service to use.

- zIndex (number; optional):
    The layer zIndex. [MUTABLE].

- zoomOffset (number; optional):
    The zoom number used in tile URLs will be offset with this value.

- zoomReverse (boolean; optional):
    If set to True, the zoom number used in tile URLs will be reversed
    (maxZoom - zoom instead of zoom)."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_leaflet'
    _type = 'WMSTileLayer'
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

    Params = TypedDict(
        "Params",
            {
            "format": NotRequired[str],
            "layers": str,
            "request": NotRequired[str],
            "service": NotRequired[str],
            "styles": NotRequired[str],
            "version": NotRequired[str],
            "transparent": NotRequired[bool],
            "width": NotRequired[typing.Union[int, float, numbers.Number]],
            "height": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    @_explicitize_args
    def __init__(
        self,
        opacity: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        className: typing.Optional[str] = None,
        attribution: typing.Optional[str] = None,
        pane: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
        crossOrigin: typing.Optional[typing.Union[Literal["anonymous"], Literal["use-credentials"]]] = None,
        zIndex: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        bounds: typing.Optional["Bounds"] = None,
        minZoom: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        maxZoom: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        updateWhenIdle: typing.Optional[bool] = None,
        subdomains: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        errorTileUrl: typing.Optional[str] = None,
        zoomOffset: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        tms: typing.Optional[bool] = None,
        zoomReverse: typing.Optional[bool] = None,
        detectRetina: typing.Optional[bool] = None,
        referrerPolicy: typing.Optional[typing.Union[Literal["no-referrer"], Literal["no-referrer-when-downgrade"], Literal["origin"], Literal["origin-when-cross-origin"], Literal["same-origin"], Literal["strict-origin"], Literal["strict-origin-when-cross-origin"], Literal["unsafe-url"]]] = None,
        tileSize: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        updateWhenZooming: typing.Optional[bool] = None,
        updateInterval: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        maxNativeZoom: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        minNativeZoom: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        noWrap: typing.Optional[bool] = None,
        keepBuffer: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        layers: typing.Optional[str] = None,
        styles: typing.Optional[str] = None,
        transparent: typing.Optional[bool] = None,
        version: typing.Optional[str] = None,
        uppercase: typing.Optional[bool] = None,
        params: typing.Optional["Params"] = None,
        crs: typing.Optional[str] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        loading_state: typing.Optional[dict] = None,
        eventHandlers: typing.Optional[dict] = None,
        disableDefaultEventHandlers: typing.Optional[bool] = None,
        n_loads: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'attribution', 'bounds', 'className', 'crossOrigin', 'crs', 'detectRetina', 'disableDefaultEventHandlers', 'errorTileUrl', 'eventHandlers', 'format', 'keepBuffer', 'layers', 'loading_state', 'maxNativeZoom', 'maxZoom', 'minNativeZoom', 'minZoom', 'n_loads', 'noWrap', 'opacity', 'pane', 'params', 'referrerPolicy', 'styles', 'subdomains', 'tileSize', 'tms', 'transparent', 'updateInterval', 'updateWhenIdle', 'updateWhenZooming', 'uppercase', 'url', 'version', 'zIndex', 'zoomOffset', 'zoomReverse']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'attribution', 'bounds', 'className', 'crossOrigin', 'crs', 'detectRetina', 'disableDefaultEventHandlers', 'errorTileUrl', 'eventHandlers', 'format', 'keepBuffer', 'layers', 'loading_state', 'maxNativeZoom', 'maxZoom', 'minNativeZoom', 'minZoom', 'n_loads', 'noWrap', 'opacity', 'pane', 'params', 'referrerPolicy', 'styles', 'subdomains', 'tileSize', 'tms', 'transparent', 'updateInterval', 'updateWhenIdle', 'updateWhenZooming', 'uppercase', 'url', 'version', 'zIndex', 'zoomOffset', 'zoomReverse']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['layers', 'url']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(WMSTileLayer, self).__init__(**args)
