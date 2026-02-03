# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class MeasureControl(Component):
    """A MeasureControl component.
Coordinate, linear, and area measure control for Leaflet maps.

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- activeColor (string; optional):
    The color to use for map features rendered while actively
    performing a measurement.

- captureZIndex (number; optional):
    The Z-index of the marker used to capture measure clicks.

- completedColor (string; optional):
    The color to use for features generated from a completed
    measurement.

- decPoint (string; optional):
    The decimal point separator used when displaying measurements.

- loading_state (dict; optional):
    Dash loading state information.

- popupOptions (dict; optional):
    The options applied to the popup of the resulting measure feature.

    `popupOptions` is a dict with keys:

    - maxWidth (number; optional)

    - minWidth (number; optional)

    - maxHeight (number; optional)

    - keepInView (boolean; optional)

    - closeButton (boolean; optional)

    - autoPan (boolean; optional)

    - autoPanPaddingTopLeft (boolean | number | string | dict | list; optional)

    - autoPanPaddingBottomRight (boolean | number | string | dict | list; optional)

    - autoPanPadding (boolean | number | string | dict | list; optional)

    - autoClose (boolean; optional)

    - closeOnClick (boolean; optional)

    - closeOnEscapeKey (boolean; optional)

    - offset (boolean | number | string | dict | list; optional)

    - className (string; optional)

    - pane (string; optional)

    - interactive (boolean; optional)

    - content (string; optional)

- position (a value equal to: 'topleft', 'topright', 'bottomleft', 'bottomright'; optional):
    Map control position.

- primaryAreaUnit (string; default 'sqmeters'):
    The primary units used to display area results.

- primaryLengthUnit (string; default 'meters'):
    The primary units used to display length results.

- secondaryAreaUnit (string; optional):
    The secondary units used to display area results.

- secondaryLengthUnit (string; optional):
    The secondary units used to display length results.

- thousandsSep (string; optional):
    The thousands separator used when displaying measurements.

- units (dict; optional):
    Custom units to make available to the measurement calculator.
    Packaged units are feet, meters, miles, and kilometers for length
    and acres, hectares, sqfeet, sqmeters, and sqmiles for areas.
    Additional unit definitions can be added to the packaged units
    using this option.

    `units` is a dict with keys:

    - string (dict; required)

        `string` is a dict with keys:

        - factor (number; required)

        - display (string; required)

        - decimals (number; required)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_leaflet'
    _type = 'MeasureControl'
    PopupOptions = TypedDict(
        "PopupOptions",
            {
            "maxWidth": NotRequired[typing.Union[int, float, numbers.Number]],
            "minWidth": NotRequired[typing.Union[int, float, numbers.Number]],
            "maxHeight": NotRequired[typing.Union[int, float, numbers.Number]],
            "keepInView": NotRequired[bool],
            "closeButton": NotRequired[bool],
            "autoPan": NotRequired[bool],
            "autoPanPaddingTopLeft": NotRequired[typing.Any],
            "autoPanPaddingBottomRight": NotRequired[typing.Any],
            "autoPanPadding": NotRequired[typing.Any],
            "autoClose": NotRequired[bool],
            "closeOnClick": NotRequired[bool],
            "closeOnEscapeKey": NotRequired[bool],
            "offset": NotRequired[typing.Any],
            "className": NotRequired[str],
            "pane": NotRequired[str],
            "interactive": NotRequired[bool],
            "content": NotRequired[typing.Union[str, typing.Any]]
        }
    )

    UnitsString = TypedDict(
        "UnitsString",
            {
            "factor": typing.Union[int, float, numbers.Number],
            "display": str,
            "decimals": typing.Union[int, float, numbers.Number]
        }
    )

    Units = TypedDict(
        "Units",
            {
            "string": "UnitsString"
        }
    )

    @_explicitize_args
    def __init__(
        self,
        position: typing.Optional[Literal["topleft", "topright", "bottomleft", "bottomright"]] = None,
        primaryLengthUnit: typing.Optional[str] = None,
        secondaryLengthUnit: typing.Optional[str] = None,
        primaryAreaUnit: typing.Optional[str] = None,
        secondaryAreaUnit: typing.Optional[str] = None,
        activeColor: typing.Optional[str] = None,
        completedColor: typing.Optional[str] = None,
        popupOptions: typing.Optional["PopupOptions"] = None,
        units: typing.Optional["Units"] = None,
        captureZIndex: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        decPoint: typing.Optional[str] = None,
        thousandsSep: typing.Optional[str] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        loading_state: typing.Optional[dict] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'activeColor', 'captureZIndex', 'completedColor', 'decPoint', 'loading_state', 'popupOptions', 'position', 'primaryAreaUnit', 'primaryLengthUnit', 'secondaryAreaUnit', 'secondaryLengthUnit', 'thousandsSep', 'units']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'activeColor', 'captureZIndex', 'completedColor', 'decPoint', 'loading_state', 'popupOptions', 'position', 'primaryAreaUnit', 'primaryLengthUnit', 'secondaryAreaUnit', 'secondaryLengthUnit', 'thousandsSep', 'units']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(MeasureControl, self).__init__(**args)
