# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class AttributionControl(Component):
    """An AttributionControl component.
The attribution control allows you to display attribution data in a small text box on a map. It is put on the map by default unless you set its attributionControl option to false, and it fetches attribution texts from layers with the getAttribution method automatically.

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- loading_state (dict; optional):
    Dash loading state information.

- position (a value equal to: 'topleft', 'topright', 'bottomleft', 'bottomright'; optional):
    Map control position. [MUTABLE].

- prefix (string; optional):
    The HTML text shown before the attributions. Pass False to
    disable."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_leaflet'
    _type = 'AttributionControl'

    @_explicitize_args
    def __init__(
        self,
        prefix: typing.Optional[typing.Union[str]] = None,
        position: typing.Optional[Literal["topleft", "topright", "bottomleft", "bottomright"]] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        loading_state: typing.Optional[dict] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'loading_state', 'position', 'prefix']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'loading_state', 'position', 'prefix']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(AttributionControl, self).__init__(**args)
