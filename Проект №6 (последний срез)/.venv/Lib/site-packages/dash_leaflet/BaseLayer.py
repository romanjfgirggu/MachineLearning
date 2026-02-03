# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class BaseLayer(Component):
    """A BaseLayer component.
BaseLayer is a wrapper of LayersControl.BaseLayer in react-leaflet. It takes similar properties to its react-leaflet counterpart.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Children [MUTABLE].

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- checked (boolean; optional):
    If True, the layer is shown, otherwise it's hidden. [MUTABLE].

- loading_state (dict; optional):
    Dash loading state information.

- name (boolean; required):
    Name of the layer, used for the label in the LayersControl."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_leaflet'
    _type = 'BaseLayer'

    @_explicitize_args
    def __init__(
        self,
        children: typing.Optional[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]] = None,
        name: typing.Optional[bool] = None,
        checked: typing.Optional[bool] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        loading_state: typing.Optional[dict] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'checked', 'loading_state', 'name']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'checked', 'loading_state', 'name']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['name']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(BaseLayer, self).__init__(children=children, **args)
