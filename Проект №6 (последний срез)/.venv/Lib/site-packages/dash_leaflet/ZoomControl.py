# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class ZoomControl(Component):
    """A ZoomControl component.
A basic zoom control with two buttons (zoom in and zoom out). It is put on the map by default unless you set its zoomControl option to false.

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- loading_state (dict; optional):
    Dash loading state information.

- position (a value equal to: 'topleft', 'topright', 'bottomleft', 'bottomright'; optional):
    Map control position. [MUTABLE]."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_leaflet'
    _type = 'ZoomControl'

    @_explicitize_args
    def __init__(
        self,
        position: typing.Optional[Literal["topleft", "topright", "bottomleft", "bottomright"]] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        loading_state: typing.Optional[dict] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'loading_state', 'position']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'loading_state', 'position']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(ZoomControl, self).__init__(**args)
