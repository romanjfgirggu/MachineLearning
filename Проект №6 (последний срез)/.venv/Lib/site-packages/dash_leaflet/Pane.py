# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class Pane(Component):
    """A Pane component.
Panes are DOM elements used to control the ordering of layers on the map.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Children [MUTABLE].

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- className (string; optional):
    CSS class(es).

- loading_state (dict; optional):
    Dash loading state information.

- name (string; required):
    The name must be unique to the pane and different from the default
    Leaflet pane names.

- pane (string; optional):
    Map pane where the layer will be added."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_leaflet'
    _type = 'Pane'

    @_explicitize_args
    def __init__(
        self,
        children: typing.Optional[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]] = None,
        name: typing.Optional[str] = None,
        className: typing.Optional[str] = None,
        pane: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        loading_state: typing.Optional[dict] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'loading_state', 'name', 'pane', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'loading_state', 'name', 'pane', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['name']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Pane, self).__init__(children=children, **args)
