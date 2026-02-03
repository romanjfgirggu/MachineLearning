# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class LocateControl(Component):
    """A LocateControl component.
A useful control to geolocate the user with many options. Official Leaflet and MapBox plugin.

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- cacheLocation (boolean; optional):
    Keep a cache of the location after the user deactivates the
    control. If set to False, the user has to wait until the locate
    API returns a new location before they see where they are again.

- circlePadding (list of numbers; optional):
    Padding around the accuracy circle.

- circleStyle (dict; optional):
    Accuracy circle style properties.

    `circleStyle` is a dict with keys:

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

- clickBehavior (dict; optional):
    What to do when the user clicks on the control. Has three options
    inView, inViewNotFollowing and outOfView. Possible values are stop
    and setView, or the name of a behaviour to inherit from.

- compassStyle (dict; optional):
    Triangle compass heading marker style properties. Only works if
    your marker class supports setStyle.

    `compassStyle` is a dict with keys:

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

- drawCircle (boolean; optional):
    If set, a circle that shows the location accuracy is drawn.

- drawMarker (boolean; optional):
    If set, the marker at the users' location is drawn.

- flyTo (boolean; optional):
    Smooth pan and zoom to the location of the marker. Only works in
    Leaflet 1.0+.

- followCircleStyle (dict; optional):
    Changes to the accuracy circle while following. Only need to
    provide changes.

    `followCircleStyle` is a dict with keys:

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

- followCompassStyle (dict; optional):
    Changes to the compass marker while following. Only need to
    provide changes.

    `followCompassStyle` is a dict with keys:

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

- followMarkerStyle (dict; optional):
    Changes to the inner marker while following. Only need to provide
    changes.

    `followMarkerStyle` is a dict with keys:

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

- icon (string; optional):
    The CSS class for the icon.

- iconElementTag (string; optional):
    The element to be created for icons.

- iconLoading (string; optional):
    The CSS class for the icon while loading.

- initialZoomLevel (number; optional):
    After activating the plugin by clicking on the icon, zoom to the
    selected zoom level, even when keepCurrentZoomLevel is True. Set
    to False to disable this feature.

- keepCurrentZoomLevel (boolean; optional):
    Only pan when setting the view.

- loading_state (dict; optional):
    Dash loading state information.

- locateOptions (dict; optional):
    The default options passed to leaflets locate method.

    `locateOptions` is a dict with keys:

    - watch (boolean; optional)

    - setView (boolean; optional)

    - maxZoom (number; optional)

    - timeout (number; optional)

    - maximumAge (number; optional)

    - enableHighAccuracy (boolean; optional)

- markerStyle (dict; optional):
    Inner marker style properties. Only works if your marker class
    supports setStyle.

    `markerStyle` is a dict with keys:

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

- metric (boolean; optional):
    Use metric units.

- position (a value equal to: 'topleft', 'topright', 'bottomleft', 'bottomright'; optional):
    Map control position.

- returnToPrevBounds (boolean; optional):
    If set, save the map bounds just before centering to the user's
    location. When control is disabled, set the view back to the
    bounds that were saved.

- setView (optional):
    Set the map view (zoom and pan) to the user's location as it
    updates.

- showCompass (boolean; optional):
    Show the compass bearing on top of the location marker.

- showPopup (boolean; optional):
    Display a pop-up when the user click on the inner marker.

- strings (dict; optional):
    Strings used in the control. Options are title, text, metersUnit,
    feetUnit, popup and outsideMapBoundsMsg.

    `strings` is a dict with keys:

    - title (string; optional)

    - metersUnit (string; optional)

    - feetUnit (string; optional)

    - popup (string; optional)

    - outsideMapBoundsMsg (string; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_leaflet'
    _type = 'LocateControl'
    CircleStyle = TypedDict(
        "CircleStyle",
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

    MarkerStyle = TypedDict(
        "MarkerStyle",
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

    CompassStyle = TypedDict(
        "CompassStyle",
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

    FollowCircleStyle = TypedDict(
        "FollowCircleStyle",
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

    FollowMarkerStyle = TypedDict(
        "FollowMarkerStyle",
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

    FollowCompassStyle = TypedDict(
        "FollowCompassStyle",
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

    Strings = TypedDict(
        "Strings",
            {
            "title": NotRequired[str],
            "metersUnit": NotRequired[str],
            "feetUnit": NotRequired[str],
            "popup": NotRequired[str],
            "outsideMapBoundsMsg": NotRequired[str]
        }
    )

    LocateOptions = TypedDict(
        "LocateOptions",
            {
            "watch": NotRequired[bool],
            "setView": NotRequired[bool],
            "maxZoom": NotRequired[typing.Union[int, float, numbers.Number]],
            "timeout": NotRequired[typing.Union[int, float, numbers.Number]],
            "maximumAge": NotRequired[typing.Union[int, float, numbers.Number]],
            "enableHighAccuracy": NotRequired[bool]
        }
    )

    @_explicitize_args
    def __init__(
        self,
        position: typing.Optional[Literal["topleft", "topright", "bottomleft", "bottomright"]] = None,
        icon: typing.Optional[str] = None,
        setView: typing.Optional[typing.Union[Literal["once"], Literal["always"], Literal["untilPan"], Literal["untilPanOrZoom"]]] = None,
        flyTo: typing.Optional[bool] = None,
        keepCurrentZoomLevel: typing.Optional[bool] = None,
        initialZoomLevel: typing.Optional[typing.Union[typing.Union[int, float, numbers.Number]]] = None,
        clickBehavior: typing.Optional[dict] = None,
        returnToPrevBounds: typing.Optional[bool] = None,
        cacheLocation: typing.Optional[bool] = None,
        showCompass: typing.Optional[bool] = None,
        drawCircle: typing.Optional[bool] = None,
        drawMarker: typing.Optional[bool] = None,
        circleStyle: typing.Optional["CircleStyle"] = None,
        markerStyle: typing.Optional["MarkerStyle"] = None,
        compassStyle: typing.Optional["CompassStyle"] = None,
        followCircleStyle: typing.Optional["FollowCircleStyle"] = None,
        followMarkerStyle: typing.Optional["FollowMarkerStyle"] = None,
        followCompassStyle: typing.Optional["FollowCompassStyle"] = None,
        iconLoading: typing.Optional[str] = None,
        iconElementTag: typing.Optional[str] = None,
        circlePadding: typing.Optional[typing.Sequence[typing.Union[int, float, numbers.Number]]] = None,
        metric: typing.Optional[bool] = None,
        showPopup: typing.Optional[bool] = None,
        strings: typing.Optional["Strings"] = None,
        locateOptions: typing.Optional["LocateOptions"] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        loading_state: typing.Optional[dict] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'cacheLocation', 'circlePadding', 'circleStyle', 'clickBehavior', 'compassStyle', 'drawCircle', 'drawMarker', 'flyTo', 'followCircleStyle', 'followCompassStyle', 'followMarkerStyle', 'icon', 'iconElementTag', 'iconLoading', 'initialZoomLevel', 'keepCurrentZoomLevel', 'loading_state', 'locateOptions', 'markerStyle', 'metric', 'position', 'returnToPrevBounds', 'setView', 'showCompass', 'showPopup', 'strings']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'cacheLocation', 'circlePadding', 'circleStyle', 'clickBehavior', 'compassStyle', 'drawCircle', 'drawMarker', 'flyTo', 'followCircleStyle', 'followCompassStyle', 'followMarkerStyle', 'icon', 'iconElementTag', 'iconLoading', 'initialZoomLevel', 'keepCurrentZoomLevel', 'loading_state', 'locateOptions', 'markerStyle', 'metric', 'position', 'returnToPrevBounds', 'setView', 'showCompass', 'showPopup', 'strings']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(LocateControl, self).__init__(**args)
