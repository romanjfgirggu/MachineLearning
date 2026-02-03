# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class FullScreenControl(Component):
    """A FullScreenControl component.
A basic FullScreen control with two buttons (FullScreen in and FullScreen out). It is put on the map by default unless you set its FullScreenControl option to false.

Keyword arguments:

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- content (string; optional):
    Content of the button, can be HTML, default 'None'.

- forcePseudoFullscreen (boolean; optional):
    Force use of pseudo full screen even if full screen API is
    available, default 'False'.

- forceSeparateButton (boolean; optional):
    Force separate button to detach from zoom buttons, default
    'False'.

- fullscreenElement (boolean | number | string | dict | list; optional):
    Dom element to render in full screen, False by default, fallback
    to 'map._container'.

- loading_state (dict; optional):
    Dash loading state information.

- position (a value equal to: 'topleft', 'topright', 'bottomleft', 'bottomright'; optional):
    Map control position.

- title (string; optional):
    Title of the button, default 'Full Screen'.

- titleCancel (string; optional):
    Title of the button when fullscreen is on, default 'Exit Full
    Screen'."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_leaflet'
    _type = 'FullScreenControl'

    @_explicitize_args
    def __init__(
        self,
        position: typing.Optional[Literal["topleft", "topright", "bottomleft", "bottomright"]] = None,
        title: typing.Optional[str] = None,
        content: typing.Optional[str] = None,
        titleCancel: typing.Optional[str] = None,
        forceSeparateButton: typing.Optional[bool] = None,
        forcePseudoFullscreen: typing.Optional[bool] = None,
        fullscreenElement: typing.Optional[typing.Any] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        loading_state: typing.Optional[dict] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'content', 'forcePseudoFullscreen', 'forceSeparateButton', 'fullscreenElement', 'loading_state', 'position', 'title', 'titleCancel']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'content', 'forcePseudoFullscreen', 'forceSeparateButton', 'fullscreenElement', 'loading_state', 'position', 'title', 'titleCancel']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FullScreenControl, self).__init__(**args)
