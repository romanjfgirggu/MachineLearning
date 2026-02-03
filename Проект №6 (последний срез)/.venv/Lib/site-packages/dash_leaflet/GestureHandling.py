# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class GestureHandling(Component):
    """A GestureHandling component.
GestureHandling is a light wrapper of https://github.com/elmarquis/Leaflet.GestureHandling

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- loading_state (dict; optional):
    Dash loading state information."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_leaflet'
    _type = 'GestureHandling'

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        loading_state: typing.Optional[dict] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(GestureHandling, self).__init__(**args)
