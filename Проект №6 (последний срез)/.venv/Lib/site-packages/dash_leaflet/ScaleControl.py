# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class ScaleControl(Component):
    """A ScaleControl component.
A simple scale control that shows the scale of the current center of screen in metric (m/km) and imperial (mi/ft) systems.

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- imperial (boolean; optional):
    Whether to show the imperial scale line (mi/ft).

- loading_state (dict; optional):
    Dash loading state information.

- maxWidth (number; optional):
    Maximum width of the control in pixels. The width is set
    dynamically to show round values (e.g. 100, 200, 500).

- metric (boolean; optional):
    Whether to show the metric scale line (m/km).

- position (a value equal to: 'topleft', 'topright', 'bottomleft', 'bottomright'; optional):
    Map control position. [MUTABLE].

- updateWhenIdle (boolean; optional):
    If True, the control is updated on moveend, otherwise it's always
    up-to-date (updated on move)."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_leaflet'
    _type = 'ScaleControl'

    @_explicitize_args
    def __init__(
        self,
        position: typing.Optional[Literal["topleft", "topright", "bottomleft", "bottomright"]] = None,
        metric: typing.Optional[bool] = None,
        maxWidth: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        imperial: typing.Optional[bool] = None,
        updateWhenIdle: typing.Optional[bool] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        loading_state: typing.Optional[dict] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'imperial', 'loading_state', 'maxWidth', 'metric', 'position', 'updateWhenIdle']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'imperial', 'loading_state', 'maxWidth', 'metric', 'position', 'updateWhenIdle']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(ScaleControl, self).__init__(**args)
