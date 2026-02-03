# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class GeoJSON(Component):
    """A GeoJSON component.
The GeoJSON component is based on the Leaflet counterpart, https://leafletjs.com/reference.html#geojson, but with
extra functionality (e.g. marker clustering via supercluster https://github.com/mapbox/supercluster) added on top.
Marker cluster styles are based on https://github.com/Leaflet/Leaflet.markercluster

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

- clickData (dict; optional):
    An object holding data related to the click event. Typing is
    indicative.

    `clickData` is a dict with keys:

    - latlng (list of numbers; required)

    - layerPoint (list of numbers; required)

    - containerPoint (list of numbers; required)

- cluster (boolean; optional):
    If True, marker clustering will be performed. [MUTABLE, DL].

- clusterToLayer (string | dict; optional):
    Function that determines how a cluster is drawn. [MUTABLE, DL].

- coordsToLatLng (string | dict; optional):
    A Function that will be used for converting GeoJSON coordinates to
    LatLngs. The default is the coordsToLatLng static method.
    [MUTABLE, DL].

- data (dict; optional):
    Data (consider using url for better performance). One of data/url
    must be set. [MUTABLE, DL].

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

- filter (string | dict; optional):
    A Function that will be used to decide whether to include a
    feature or not. The default is to include all features: function
    (geoJsonFeature) {     return True; } [MUTABLE, DL].

- format (a value equal to: 'geojson', 'geobuf', 'flatgeobuf'; default 'geojson'):
    Format of the data, applies both to url/data properties. Defaults
    to \"geojson\". [MUTABLE, DL].

- formatOptions (dict; optional):
    Format options, currently only used for \"flatgeobuf\". [MUTABLE,
    DL].

    `formatOptions` is a dict with keys:

    - rect (dict; required)

        `rect` is a dict with keys:

        - minX (number; required)

        - minY (number; required)

        - maxX (number; required)

        - maxY (number; required)

- hideout (string | dict; optional):
    Object intended for passing variables to functional properties,
    i.e. clusterToLayer, hoverStyle and (options) pointToLayer, style,
    filter, and onEachFeature functions. [MUTABLE, DL].

- hoverStyle (string | dict; optional):
    Style function applied on hover. [MUTABLE, DL].

- interactive (boolean; optional):
    If False, the layer will not emit mouse events and will act as a
    part of the underlying map.

- loading_state (dict; optional):
    Dash loading state information.

- markersInheritOptions (boolean; optional):
    Whether default Markers for \"Point\" type Features inherit from
    group options. [MUTABLE, DL].

- n_clicks (number; optional):
    An integer that represents the number of times that this element
    has been clicked on.

- n_dblclicks (number; optional):
    An integer that represents the number of times that this element
    has been double-clicked on.

- onEachFeature (string | dict; optional):
    A Function that will be called once for each created Feature,
    after it has been created and styled. Useful for attaching events
    and popups to features. The default is to do nothing with the
    newly created layers: function (feature, layer) {} [MUTABLE, DL].

- options (dict; optional):
    Options for the GeoJSON object (see
    https://leafletjs.com/reference-1.6.0.html#geojson-option for
    details). [DEPRECATED].

- pane (string; optional):
    Map pane where the layer will be added.

- pointToLayer (string | dict; optional):
    Function defining how GeoJSON points spawn Leaflet layers. It is
    internally called when data is added, passing the GeoJSON point
    feature and its LatLng. The default is to spawn a default Marker:
    function(geoJsonPoint, latlng) {     return L.marker(latlng); }
    [MUTABLE, DL].

- spiderfyOnMaxZoom (boolean; default True):
    If True, markers that are not resolved at max zoom level will be
    spiderfied on click. [MUTABLE, DL].

- superClusterOptions (dict; optional):
    Options for the SuperCluster object (see
    https://github.com/mapbox/supercluster for details). [MUTABLE,
    DL].

- url (string; optional):
    Url to data (use instead of data for better performance). One of
    data/url must be set. [MUTABLE, DL].

- zoomToBounds (boolean; optional):
    If True, zoom bounds when data are set. [MUTABLE, DL].

- zoomToBoundsOnClick (boolean; optional):
    If True, zoom to feature bounds on click. [MUTABLE, DL]."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_leaflet'
    _type = 'GeoJSON'
    FormatOptionsRect = TypedDict(
        "FormatOptionsRect",
            {
            "minX": typing.Union[int, float, numbers.Number],
            "minY": typing.Union[int, float, numbers.Number],
            "maxX": typing.Union[int, float, numbers.Number],
            "maxY": typing.Union[int, float, numbers.Number]
        }
    )

    FormatOptions = TypedDict(
        "FormatOptions",
            {
            "rect": "FormatOptionsRect"
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
        interactive: typing.Optional[bool] = None,
        bubblingMouseEvents: typing.Optional[bool] = None,
        attribution: typing.Optional[str] = None,
        pane: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        pointToLayer: typing.Optional[typing.Union[str, dict]] = None,
        onEachFeature: typing.Optional[typing.Union[str, dict]] = None,
        filter: typing.Optional[typing.Union[str, dict]] = None,
        coordsToLatLng: typing.Optional[typing.Union[str, dict]] = None,
        markersInheritOptions: typing.Optional[bool] = None,
        data: typing.Optional[dict] = None,
        url: typing.Optional[str] = None,
        zoomToBoundsOnClick: typing.Optional[bool] = None,
        zoomToBounds: typing.Optional[bool] = None,
        hoverStyle: typing.Optional[typing.Union[str, dict]] = None,
        hideout: typing.Optional[typing.Union[str, dict]] = None,
        format: typing.Optional[Literal["geojson", "geobuf", "flatgeobuf"]] = None,
        formatOptions: typing.Optional["FormatOptions"] = None,
        cluster: typing.Optional[bool] = None,
        clusterToLayer: typing.Optional[typing.Union[str, dict]] = None,
        spiderfyOnMaxZoom: typing.Optional[bool] = None,
        superClusterOptions: typing.Optional[dict] = None,
        options: typing.Optional[dict] = None,
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
        self._prop_names = ['children', 'id', 'attribution', 'bubblingMouseEvents', 'clickData', 'cluster', 'clusterToLayer', 'coordsToLatLng', 'data', 'dblclickData', 'disableDefaultEventHandlers', 'eventHandlers', 'filter', 'format', 'formatOptions', 'hideout', 'hoverStyle', 'interactive', 'loading_state', 'markersInheritOptions', 'n_clicks', 'n_dblclicks', 'onEachFeature', 'options', 'pane', 'pointToLayer', 'spiderfyOnMaxZoom', 'style', 'superClusterOptions', 'url', 'zoomToBounds', 'zoomToBoundsOnClick']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'attribution', 'bubblingMouseEvents', 'clickData', 'cluster', 'clusterToLayer', 'coordsToLatLng', 'data', 'dblclickData', 'disableDefaultEventHandlers', 'eventHandlers', 'filter', 'format', 'formatOptions', 'hideout', 'hoverStyle', 'interactive', 'loading_state', 'markersInheritOptions', 'n_clicks', 'n_dblclicks', 'onEachFeature', 'options', 'pane', 'pointToLayer', 'spiderfyOnMaxZoom', 'style', 'superClusterOptions', 'url', 'zoomToBounds', 'zoomToBoundsOnClick']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(GeoJSON, self).__init__(children=children, **args)
