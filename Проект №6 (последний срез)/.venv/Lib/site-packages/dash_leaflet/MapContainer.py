# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class MapContainer(Component):
    """A MapContainer component.
The MapContainer component is responsible for creating the Leaflet Map instance and providing it to its child components, using a React Context.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Map components [MUTABLE].

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- attributionControl (boolean; optional):
    Whether a attribution control is added to the map by default.

- bounceAtZoomLimits (boolean; optional):
    Set it to False if you don't want the map to zoom beyond min/max
    zoom and then bounce back when pinch-zooming.

- bounds (dict; optional):
    Initial map bounds.

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

- boundsOptions (dict; optional):
    Options for initial map bounds.

    `boundsOptions` is a dict with keys:

    - paddingTopLeft (boolean | number | string | dict | list; optional)

    - paddingBottomRight (boolean | number | string | dict | list; optional)

    - padding (boolean | number | string | dict | list; optional)

    - maxZoom (number; optional)

    - animate (boolean; optional)

    - duration (number; optional)

    - easeLinearity (number; optional)

    - noMoveStart (boolean; optional)

- boxZoom (boolean; optional):
    Whether the map can be zoomed to a rectangular area specified by
    dragging the mouse while pressing the shift key.

- center (dict; optional):
    Initial geographic center of the map.

    `center` is a dict with keys:

    - equals (required)

    - toString (optional)

    - distanceTo (required)

    - wrap (required)

    - toBounds (required)

    - clone (required)

    - lat (number; required)

    - lng (number; required)

    - alt (number; optional)

- className (string; optional):
    Extra CSS classes to add to the map.

- clickData (dict; optional):
    An object holding data related to the click event. Typing is
    indicative.

    `clickData` is a dict with keys:

    - latlng (list of numbers; required)

    - layerPoint (list of numbers; required)

    - containerPoint (list of numbers; required)

- closePopupOnClick (boolean; optional):
    Set it to False if you don't want popups to close when user clicks
    the map.

- crs (string; default 'EPSG3857'):
    The Coordinate Reference System to use. Don't change this if
    you're not sure what it means. [DL].

- dblclickData (dict; optional):
    An object holding data related to the double click event. Typing
    is indicative.

    `dblclickData` is a dict with keys:

    - latlng (list of numbers; required)

    - layerPoint (list of numbers; required)

    - containerPoint (list of numbers; required)

- doubleClickZoom (optional):
    Whether the map can be zoomed in by double clicking on it and
    zoomed out by double clicking while holding shift. If passed
    'center', double-click zoom will zoom to the center of the view
    regardless of where the mouse was.

- dragging (boolean; optional):
    Whether the map is draggable with mouse/touch or not.

- easeLinearity (number; optional):
    Defaults to 0.2.

- eventHandlers (dict; optional):
    Object with keys specifying the event type and the value the
    corresponding event handlers. [MUTABLE].

    `eventHandlers` is a dict with keys:

    - baselayerchange (dict; optional)

        `baselayerchange` is a dict with keys:


    - overlayadd (dict; optional)

        `overlayadd` is a dict with keys:


    - overlayremove (dict; optional)

        `overlayremove` is a dict with keys:


    - layeradd (dict; optional)

        `layeradd` is a dict with keys:


    - layerremove (dict; optional)

        `layerremove` is a dict with keys:


    - zoomlevelschange (dict; optional)

        `zoomlevelschange` is a dict with keys:


    - unload (dict; optional)

        `unload` is a dict with keys:


    - viewreset (dict; optional)

        `viewreset` is a dict with keys:


    - load (dict; optional)

        `load` is a dict with keys:


    - zoomstart (dict; optional)

        `zoomstart` is a dict with keys:


    - movestart (dict; optional)

        `movestart` is a dict with keys:


    - zoom (dict; optional)

        `zoom` is a dict with keys:


    - move (dict; optional)

        `move` is a dict with keys:


    - zoomend (dict; optional)

        `zoomend` is a dict with keys:


    - moveend (dict; optional)

        `moveend` is a dict with keys:


    - autopanstart (dict; optional)

        `autopanstart` is a dict with keys:


    - dragstart (dict; optional)

        `dragstart` is a dict with keys:


    - drag (dict; optional)

        `drag` is a dict with keys:


    - add (dict; optional)

        `add` is a dict with keys:


    - remove (dict; optional)

        `remove` is a dict with keys:


    - loading (dict; optional)

        `loading` is a dict with keys:


    - error (dict; optional)

        `error` is a dict with keys:


    - update (dict; optional)

        `update` is a dict with keys:


    - down (dict; optional)

        `down` is a dict with keys:


    - predrag (dict; optional)

        `predrag` is a dict with keys:


    - resize (dict; optional)

        `resize` is a dict with keys:


    - popupopen (dict; optional)

        `popupopen` is a dict with keys:


    - popupclose (dict; optional)

        `popupclose` is a dict with keys:


    - tooltipopen (dict; optional)

        `tooltipopen` is a dict with keys:


    - tooltipclose (dict; optional)

        `tooltipclose` is a dict with keys:


    - locationerror (dict; optional)

        `locationerror` is a dict with keys:


    - locationfound (dict; optional)

        `locationfound` is a dict with keys:


    - click (dict; optional)

        `click` is a dict with keys:


    - dblclick (dict; optional)

        `dblclick` is a dict with keys:


    - mousedown (dict; optional)

        `mousedown` is a dict with keys:


    - mouseup (dict; optional)

        `mouseup` is a dict with keys:


    - mouseover (dict; optional)

        `mouseover` is a dict with keys:


    - mouseout (dict; optional)

        `mouseout` is a dict with keys:


    - mousemove (dict; optional)

        `mousemove` is a dict with keys:


    - contextmenu (dict; optional)

        `contextmenu` is a dict with keys:


    - preclick (dict; optional)

        `preclick` is a dict with keys:


    - keypress (dict; optional)

        `keypress` is a dict with keys:


    - keydown (dict; optional)

        `keydown` is a dict with keys:


    - keyup (dict; optional)

        `keyup` is a dict with keys:


    - zoomanim (dict; optional)

        `zoomanim` is a dict with keys:


    - dragend (dict; optional)

        `dragend` is a dict with keys:


    - tileunload (dict; optional)

        `tileunload` is a dict with keys:


    - tileloadstart (dict; optional)

        `tileloadstart` is a dict with keys:


    - tileload (dict; optional)

        `tileload` is a dict with keys:


    - tileabort (dict; optional)

        `tileabort` is a dict with keys:


    - tileerror (dict; optional)

        `tileerror` is a dict with keys:


- fadeAnimation (boolean; optional):
    Whether the tile fade animation is enabled. By default it's
    enabled in all browsers that support CSS3 Transitions except
    Android.

- inertia (boolean; optional):
    If enabled, panning of the map will have an inertia effect where
    the map builds momentum while dragging and continues moving in the
    same direction for some time. Feels especially nice on touch
    devices. Enabled by default.

- inertiaDeceleration (number; optional):
    The rate with which the inertial movement slows down, in
    pixels/second².

- inertiaMaxSpeed (number; optional):
    Max speed of the inertial movement, in pixels/second.

- invalidateSize (string | number | dict; optional):
    Change the value to force map size invalidation. [DL].

- keyboard (boolean; optional):
    Makes the map focusable and allows users to navigate the map with
    keyboard arrows and +/- keys.

- keyboardPanDelta (number; optional):
    Amount of pixels to pan when pressing an arrow key.

- keydownData (dict; optional):
    An object holding data related to the keydown event. Typing is
    indicative.

    `keydownData` is a dict with keys:

    - key (string; required)

    - ctrlKey (boolean; required)

    - metaKey (boolean; required)

    - shiftKey (boolean; required)

    - repeat (boolean; required)

- loading_state (dict; optional):
    Dash loading state information.

- markerZoomAnimation (boolean; optional):
    Whether markers animate their zoom with the zoom animation, if
    disabled they will disappear for the length of the animation. By
    default it's enabled in all browsers that support CSS3 Transitions
    except Android.

- maxBounds (dict; optional):
    When this option is set, the map restricts the view to the given
    geographical bounds, bouncing the user back if the user tries to
    pan outside the view. To set the restriction dynamically, use
    setMaxBounds method.

    `maxBounds` is a dict with keys:

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

- maxBoundsViscosity (number; optional):
    If maxBounds is set, this option will control how solid the bounds
    are when dragging the map around. The default value of 0.0 allows
    the user to drag outside the bounds at normal speed, higher values
    will slow down map dragging outside bounds, and 1.0 makes the
    bounds fully solid, preventing the user from dragging outside the
    bounds.

- maxZoom (number; optional):
    Maximum zoom level of the map. If not specified and at least one
    GridLayer or TileLayer is in the map, the highest of their maxZoom
    options will be used instead.

- minZoom (number; optional):
    Minimum zoom level of the map. If not specified and at least one
    GridLayer or TileLayer is in the map, the lowest of their minZoom
    options will be used instead.

- n_clicks (number; optional):
    An integer that represents the number of times that this element
    has been clicked on.

- n_dblclicks (number; optional):
    An integer that represents the number of times that this element
    has been double-clicked on.

- n_keydowns (number; optional):
    An integer that represents the number of times that the keyboard
    has been pressed.

- n_loads (number; optional):
    An integer that represents the number of times that the load event
    has fired.

- placeholder (a list of or a singular dash component, string or number; optional):
    Component to be shown instead of the map.

- preferCanvas (boolean; optional):
    Whether Paths should be rendered on a Canvas renderer. By default,
    all Paths are rendered in a SVG renderer.

- renderer (dict; default undefined):
    The default method for drawing vector layers on the map. L.SVG or
    L.Canvas by default depending on browser support. [DL].

    `renderer` is a dict with keys:

    - method (a value equal to: 'svg', 'canvas'; required)

    - options (dict; required)

- scrollWheelZoom (optional):
    Whether the map can be zoomed by using the mouse wheel. If passed
    'center', it will zoom to the center of the view regardless of
    where the mouse was.

- tapHold (boolean; optional):
    Enables simulation of contextmenu event, default is True for
    mobile Safari.

- tapTolerance (number; optional):
    The max number of pixels a user can shift his finger during touch
    for it to be considered a valid tap.

- touchZoom (optional):
    Whether the map can be zoomed by touch-dragging with two fingers.
    If passed 'center', it will zoom to the center of the view
    regardless of where the touch events (fingers) were. Enabled for
    touch-capable web browsers.

- trackResize (boolean; optional):
    Whether the map automatically handles browser window resize to
    update itself.

- trackViewport (boolean; default True):
    If True (default), zoom, center, and bounds properties are updated
    on whenReady/moveend. [DL].

- transform3DLimit (number; optional):
    Defines the maximum size of a CSS translation transform. The
    default value should not be changed unless a web browser positions
    layers in the wrong place after doing a large panBy.

- viewport (dict; optional):
    This property can be used to manipulate the viewport after
    initializing the map. Set either \"center\"/\"zoom\", or bounds.
    If both are set, \"bounds\" takes precedence. Default value for
    transition is \"setView\" for \"center\"/ \"zoom\", and
    \"fitBounds\" for \"bounds\". [DL].

    `viewport` is a dict with keys:

    - center (list of numbers; optional)

    - zoom (number; optional)

    - transition (a value equal to: 'setView', 'flyTo', 'panTo', 'fitBounds', 'flyToBounds', 'panInsideBounds'; optional)

    - bounds (list of list of numberss; optional)

    - options (dict; optional)

        `options` is a dict with keys:

        - animate (boolean; optional)

        - duration (number; optional)

        - easeLinearity (number; optional)

        - noMoveStart (boolean; optional)

        - paddingTopLeft (list of numbers; optional)

        - paddingBottomRight (list of numbers; optional)

        - padding (list of numbers; optional)

- wheelDebounceTime (number; optional):
    Limits the rate at which a wheel can fire (in milliseconds). By
    default user can't zoom via wheel more often than once per 40 ms.

- wheelPxPerZoomLevel (number; optional):
    How many scroll pixels (as reported by L.DomEvent.getWheelDelta)
    mean a change of one full zoom level. Smaller values will make
    wheel-zooming faster (and vice versa).

- worldCopyJump (boolean; optional):
    With this option enabled, the map tracks when you pan to another
    \"copy\" of the world and seamlessly jumps to the original one so
    that all overlays like markers and vector layers are still
    visible.

- zoom (number; optional):
    Initial map zoom level.

- zoomAnimation (boolean; optional):
    Whether the map zoom animation is enabled. By default it's enabled
    in all browsers that support CSS3 Transitions except Android.

- zoomAnimationThreshold (number; optional):
    Won't animate zoom if the zoom difference exceeds this value.

- zoomControl (boolean; optional):
    Whether a zoom control is added to the map by default.

- zoomDelta (number; optional):
    Controls how much the map's zoom level will change after a
    zoomIn(), zoomOut(), pressing + or - on the keyboard, or using the
    zoom controls. Values smaller than 1 (e.g. 0.5) allow for greater
    granularity.

- zoomSnap (number; optional):
    Forces the map's zoom level to always be a multiple of this,
    particularly right after a fitBounds() or a pinch-zoom. By
    default, the zoom level snaps to the nearest integer; lower values
    (e.g. 0.5 or 0.1) allow for greater granularity. A value of 0
    means the zoom level will not be snapped after fitBounds or a
    pinch-zoom."""
    _children_props = ['placeholder']
    _base_nodes = ['placeholder', 'children']
    _namespace = 'dash_leaflet'
    _type = 'MapContainer'
    Center = TypedDict(
        "Center",
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

    EventHandlersBaselayerchange = TypedDict(
        "EventHandlersBaselayerchange",
            {

        }
    )

    EventHandlersOverlayadd = TypedDict(
        "EventHandlersOverlayadd",
            {

        }
    )

    EventHandlersOverlayremove = TypedDict(
        "EventHandlersOverlayremove",
            {

        }
    )

    EventHandlersLayeradd = TypedDict(
        "EventHandlersLayeradd",
            {

        }
    )

    EventHandlersLayerremove = TypedDict(
        "EventHandlersLayerremove",
            {

        }
    )

    EventHandlersZoomlevelschange = TypedDict(
        "EventHandlersZoomlevelschange",
            {

        }
    )

    EventHandlersUnload = TypedDict(
        "EventHandlersUnload",
            {

        }
    )

    EventHandlersViewreset = TypedDict(
        "EventHandlersViewreset",
            {

        }
    )

    EventHandlersLoad = TypedDict(
        "EventHandlersLoad",
            {

        }
    )

    EventHandlersZoomstart = TypedDict(
        "EventHandlersZoomstart",
            {

        }
    )

    EventHandlersMovestart = TypedDict(
        "EventHandlersMovestart",
            {

        }
    )

    EventHandlersZoom = TypedDict(
        "EventHandlersZoom",
            {

        }
    )

    EventHandlersMove = TypedDict(
        "EventHandlersMove",
            {

        }
    )

    EventHandlersZoomend = TypedDict(
        "EventHandlersZoomend",
            {

        }
    )

    EventHandlersMoveend = TypedDict(
        "EventHandlersMoveend",
            {

        }
    )

    EventHandlersAutopanstart = TypedDict(
        "EventHandlersAutopanstart",
            {

        }
    )

    EventHandlersDragstart = TypedDict(
        "EventHandlersDragstart",
            {

        }
    )

    EventHandlersDrag = TypedDict(
        "EventHandlersDrag",
            {

        }
    )

    EventHandlersAdd = TypedDict(
        "EventHandlersAdd",
            {

        }
    )

    EventHandlersRemove = TypedDict(
        "EventHandlersRemove",
            {

        }
    )

    EventHandlersLoading = TypedDict(
        "EventHandlersLoading",
            {

        }
    )

    EventHandlersError = TypedDict(
        "EventHandlersError",
            {

        }
    )

    EventHandlersUpdate = TypedDict(
        "EventHandlersUpdate",
            {

        }
    )

    EventHandlersDown = TypedDict(
        "EventHandlersDown",
            {

        }
    )

    EventHandlersPredrag = TypedDict(
        "EventHandlersPredrag",
            {

        }
    )

    EventHandlersResize = TypedDict(
        "EventHandlersResize",
            {

        }
    )

    EventHandlersPopupopen = TypedDict(
        "EventHandlersPopupopen",
            {

        }
    )

    EventHandlersPopupclose = TypedDict(
        "EventHandlersPopupclose",
            {

        }
    )

    EventHandlersTooltipopen = TypedDict(
        "EventHandlersTooltipopen",
            {

        }
    )

    EventHandlersTooltipclose = TypedDict(
        "EventHandlersTooltipclose",
            {

        }
    )

    EventHandlersLocationerror = TypedDict(
        "EventHandlersLocationerror",
            {

        }
    )

    EventHandlersLocationfound = TypedDict(
        "EventHandlersLocationfound",
            {

        }
    )

    EventHandlersClick = TypedDict(
        "EventHandlersClick",
            {

        }
    )

    EventHandlersDblclick = TypedDict(
        "EventHandlersDblclick",
            {

        }
    )

    EventHandlersMousedown = TypedDict(
        "EventHandlersMousedown",
            {

        }
    )

    EventHandlersMouseup = TypedDict(
        "EventHandlersMouseup",
            {

        }
    )

    EventHandlersMouseover = TypedDict(
        "EventHandlersMouseover",
            {

        }
    )

    EventHandlersMouseout = TypedDict(
        "EventHandlersMouseout",
            {

        }
    )

    EventHandlersMousemove = TypedDict(
        "EventHandlersMousemove",
            {

        }
    )

    EventHandlersContextmenu = TypedDict(
        "EventHandlersContextmenu",
            {

        }
    )

    EventHandlersPreclick = TypedDict(
        "EventHandlersPreclick",
            {

        }
    )

    EventHandlersKeypress = TypedDict(
        "EventHandlersKeypress",
            {

        }
    )

    EventHandlersKeydown = TypedDict(
        "EventHandlersKeydown",
            {

        }
    )

    EventHandlersKeyup = TypedDict(
        "EventHandlersKeyup",
            {

        }
    )

    EventHandlersZoomanim = TypedDict(
        "EventHandlersZoomanim",
            {

        }
    )

    EventHandlersDragend = TypedDict(
        "EventHandlersDragend",
            {

        }
    )

    EventHandlersTileunload = TypedDict(
        "EventHandlersTileunload",
            {

        }
    )

    EventHandlersTileloadstart = TypedDict(
        "EventHandlersTileloadstart",
            {

        }
    )

    EventHandlersTileload = TypedDict(
        "EventHandlersTileload",
            {

        }
    )

    EventHandlersTileabort = TypedDict(
        "EventHandlersTileabort",
            {

        }
    )

    EventHandlersTileerror = TypedDict(
        "EventHandlersTileerror",
            {

        }
    )

    EventHandlers = TypedDict(
        "EventHandlers",
            {
            "baselayerchange": NotRequired["EventHandlersBaselayerchange"],
            "overlayadd": NotRequired["EventHandlersOverlayadd"],
            "overlayremove": NotRequired["EventHandlersOverlayremove"],
            "layeradd": NotRequired["EventHandlersLayeradd"],
            "layerremove": NotRequired["EventHandlersLayerremove"],
            "zoomlevelschange": NotRequired["EventHandlersZoomlevelschange"],
            "unload": NotRequired["EventHandlersUnload"],
            "viewreset": NotRequired["EventHandlersViewreset"],
            "load": NotRequired["EventHandlersLoad"],
            "zoomstart": NotRequired["EventHandlersZoomstart"],
            "movestart": NotRequired["EventHandlersMovestart"],
            "zoom": NotRequired["EventHandlersZoom"],
            "move": NotRequired["EventHandlersMove"],
            "zoomend": NotRequired["EventHandlersZoomend"],
            "moveend": NotRequired["EventHandlersMoveend"],
            "autopanstart": NotRequired["EventHandlersAutopanstart"],
            "dragstart": NotRequired["EventHandlersDragstart"],
            "drag": NotRequired["EventHandlersDrag"],
            "add": NotRequired["EventHandlersAdd"],
            "remove": NotRequired["EventHandlersRemove"],
            "loading": NotRequired["EventHandlersLoading"],
            "error": NotRequired["EventHandlersError"],
            "update": NotRequired["EventHandlersUpdate"],
            "down": NotRequired["EventHandlersDown"],
            "predrag": NotRequired["EventHandlersPredrag"],
            "resize": NotRequired["EventHandlersResize"],
            "popupopen": NotRequired["EventHandlersPopupopen"],
            "popupclose": NotRequired["EventHandlersPopupclose"],
            "tooltipopen": NotRequired["EventHandlersTooltipopen"],
            "tooltipclose": NotRequired["EventHandlersTooltipclose"],
            "locationerror": NotRequired["EventHandlersLocationerror"],
            "locationfound": NotRequired["EventHandlersLocationfound"],
            "click": NotRequired["EventHandlersClick"],
            "dblclick": NotRequired["EventHandlersDblclick"],
            "mousedown": NotRequired["EventHandlersMousedown"],
            "mouseup": NotRequired["EventHandlersMouseup"],
            "mouseover": NotRequired["EventHandlersMouseover"],
            "mouseout": NotRequired["EventHandlersMouseout"],
            "mousemove": NotRequired["EventHandlersMousemove"],
            "contextmenu": NotRequired["EventHandlersContextmenu"],
            "preclick": NotRequired["EventHandlersPreclick"],
            "keypress": NotRequired["EventHandlersKeypress"],
            "keydown": NotRequired["EventHandlersKeydown"],
            "keyup": NotRequired["EventHandlersKeyup"],
            "zoomanim": NotRequired["EventHandlersZoomanim"],
            "dragend": NotRequired["EventHandlersDragend"],
            "tileunload": NotRequired["EventHandlersTileunload"],
            "tileloadstart": NotRequired["EventHandlersTileloadstart"],
            "tileload": NotRequired["EventHandlersTileload"],
            "tileabort": NotRequired["EventHandlersTileabort"],
            "tileerror": NotRequired["EventHandlersTileerror"]
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

    MaxBounds = TypedDict(
        "MaxBounds",
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

    BoundsOptions = TypedDict(
        "BoundsOptions",
            {
            "paddingTopLeft": NotRequired[typing.Any],
            "paddingBottomRight": NotRequired[typing.Any],
            "padding": NotRequired[typing.Any],
            "maxZoom": NotRequired[typing.Union[int, float, numbers.Number]],
            "animate": NotRequired[bool],
            "duration": NotRequired[typing.Union[int, float, numbers.Number]],
            "easeLinearity": NotRequired[typing.Union[int, float, numbers.Number]],
            "noMoveStart": NotRequired[bool]
        }
    )

    Renderer = TypedDict(
        "Renderer",
            {
            "method": Literal["svg", "canvas"],
            "options": dict
        }
    )

    ViewportOptions = TypedDict(
        "ViewportOptions",
            {
            "animate": NotRequired[bool],
            "duration": NotRequired[typing.Union[int, float, numbers.Number]],
            "easeLinearity": NotRequired[typing.Union[int, float, numbers.Number]],
            "noMoveStart": NotRequired[bool],
            "paddingTopLeft": NotRequired[typing.Sequence[typing.Union[int, float, numbers.Number]]],
            "paddingBottomRight": NotRequired[typing.Sequence[typing.Union[int, float, numbers.Number]]],
            "padding": NotRequired[typing.Sequence[typing.Union[int, float, numbers.Number]]]
        }
    )

    Viewport = TypedDict(
        "Viewport",
            {
            "center": NotRequired[typing.Sequence[typing.Union[int, float, numbers.Number]]],
            "zoom": NotRequired[typing.Union[int, float, numbers.Number]],
            "transition": NotRequired[Literal["setView", "flyTo", "panTo", "fitBounds", "flyToBounds", "panInsideBounds"]],
            "bounds": NotRequired[typing.Sequence[typing.Sequence[typing.Union[int, float, numbers.Number]]]],
            "options": NotRequired["ViewportOptions"]
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

    KeydownData = TypedDict(
        "KeydownData",
            {
            "key": str,
            "ctrlKey": bool,
            "metaKey": bool,
            "shiftKey": bool,
            "repeat": bool
        }
    )

    @_explicitize_args
    def __init__(
        self,
        children: typing.Optional[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]] = None,
        className: typing.Optional[str] = None,
        center: typing.Optional["Center"] = None,
        eventHandlers: typing.Optional["EventHandlers"] = None,
        style: typing.Optional[typing.Any] = None,
        keyboard: typing.Optional[bool] = None,
        bounds: typing.Optional[typing.Union["Bounds"]] = None,
        preferCanvas: typing.Optional[bool] = None,
        attributionControl: typing.Optional[bool] = None,
        zoomControl: typing.Optional[bool] = None,
        closePopupOnClick: typing.Optional[bool] = None,
        boxZoom: typing.Optional[bool] = None,
        doubleClickZoom: typing.Optional[typing.Union[Literal["center"]]] = None,
        dragging: typing.Optional[bool] = None,
        zoomSnap: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        zoomDelta: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        trackResize: typing.Optional[bool] = None,
        inertia: typing.Optional[bool] = None,
        inertiaDeceleration: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        inertiaMaxSpeed: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        easeLinearity: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        worldCopyJump: typing.Optional[bool] = None,
        maxBoundsViscosity: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        keyboardPanDelta: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        scrollWheelZoom: typing.Optional[typing.Union[Literal["center"]]] = None,
        wheelDebounceTime: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        wheelPxPerZoomLevel: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        tapHold: typing.Optional[bool] = None,
        tapTolerance: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        touchZoom: typing.Optional[typing.Union[Literal["center"]]] = None,
        bounceAtZoomLimits: typing.Optional[bool] = None,
        zoom: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        minZoom: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        maxZoom: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        maxBounds: typing.Optional["MaxBounds"] = None,
        zoomAnimation: typing.Optional[bool] = None,
        zoomAnimationThreshold: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        fadeAnimation: typing.Optional[bool] = None,
        markerZoomAnimation: typing.Optional[bool] = None,
        transform3DLimit: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        boundsOptions: typing.Optional["BoundsOptions"] = None,
        placeholder: typing.Optional[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]] = None,
        crs: typing.Optional[str] = None,
        renderer: typing.Optional["Renderer"] = None,
        invalidateSize: typing.Optional[typing.Union[str, typing.Union[int, float, numbers.Number], dict]] = None,
        viewport: typing.Optional["Viewport"] = None,
        trackViewport: typing.Optional[bool] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        loading_state: typing.Optional[dict] = None,
        n_clicks: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        clickData: typing.Optional["ClickData"] = None,
        n_dblclicks: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        dblclickData: typing.Optional["DblclickData"] = None,
        n_loads: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        n_keydowns: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        keydownData: typing.Optional["KeydownData"] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'attributionControl', 'bounceAtZoomLimits', 'bounds', 'boundsOptions', 'boxZoom', 'center', 'className', 'clickData', 'closePopupOnClick', 'crs', 'dblclickData', 'doubleClickZoom', 'dragging', 'easeLinearity', 'eventHandlers', 'fadeAnimation', 'inertia', 'inertiaDeceleration', 'inertiaMaxSpeed', 'invalidateSize', 'keyboard', 'keyboardPanDelta', 'keydownData', 'loading_state', 'markerZoomAnimation', 'maxBounds', 'maxBoundsViscosity', 'maxZoom', 'minZoom', 'n_clicks', 'n_dblclicks', 'n_keydowns', 'n_loads', 'placeholder', 'preferCanvas', 'renderer', 'scrollWheelZoom', 'style', 'tapHold', 'tapTolerance', 'touchZoom', 'trackResize', 'trackViewport', 'transform3DLimit', 'viewport', 'wheelDebounceTime', 'wheelPxPerZoomLevel', 'worldCopyJump', 'zoom', 'zoomAnimation', 'zoomAnimationThreshold', 'zoomControl', 'zoomDelta', 'zoomSnap']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'attributionControl', 'bounceAtZoomLimits', 'bounds', 'boundsOptions', 'boxZoom', 'center', 'className', 'clickData', 'closePopupOnClick', 'crs', 'dblclickData', 'doubleClickZoom', 'dragging', 'easeLinearity', 'eventHandlers', 'fadeAnimation', 'inertia', 'inertiaDeceleration', 'inertiaMaxSpeed', 'invalidateSize', 'keyboard', 'keyboardPanDelta', 'keydownData', 'loading_state', 'markerZoomAnimation', 'maxBounds', 'maxBoundsViscosity', 'maxZoom', 'minZoom', 'n_clicks', 'n_dblclicks', 'n_keydowns', 'n_loads', 'placeholder', 'preferCanvas', 'renderer', 'scrollWheelZoom', 'style', 'tapHold', 'tapTolerance', 'touchZoom', 'trackResize', 'trackViewport', 'transform3DLimit', 'viewport', 'wheelDebounceTime', 'wheelPxPerZoomLevel', 'worldCopyJump', 'zoom', 'zoomAnimation', 'zoomAnimationThreshold', 'zoomControl', 'zoomDelta', 'zoomSnap']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(MapContainer, self).__init__(children=children, **args)
