# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FeDistantLight(Component):
    """A FeDistantLight component.
FeDistantLight is a wrapper for the <feDistantLight> SVG element.
For detailed attribute info see:
https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feDistantLight

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The children of this component.

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- aria-* (string; optional):
    A wildcard aria attribute.

- azimuth (string | number; optional):
    The azimuth attribute specifies the direction angle for the light
    source on the XY plane (clockwise), in degrees from the  x
    axis.You can use this attribute with the following SVG
    elements:BCD tables only load in the browser with JavaScript
    enabled. Enable JavaScript to view data.Last modified:  May 13,
    2022, by MDN contributors.

- className (string; optional):
    Often used with CSS to style elements with common properties.

- data-* (string; optional):
    A wildcard data attribute.

- elevation (string | number; optional):
    The elevation attribute specifies the direction angle for the
    light source from the XY plane towards the Z-axis, in  degrees.
    Note that the positive Z-axis points towards  the viewer of the
    content.You can use this attribute with  the following SVG
    elements:BCD tables only load in the  browser with JavaScript
    enabled. Enable JavaScript to  view data.Last modified: May 13,
    2022, by MDN contributors.

- fill (string; optional):
    fill color.

- key (string; optional):
    A unique identifier for the component, used to improve performance
    by React.js while rendering components See
    https://reactjs.org/docs/lists-and-keys.html for more info.

- loading_state (dict; optional):
    Object that holds the loading state object coming from
    dash-renderer.

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- n_clicks (number; default 0):
    An integer that represents the number of times that this element
    has been clicked on.

- n_clicks_timestamp (number; default -1):
    An integer that represents the time (in ms since 1970) at which
    n_clicks changed. This can be used to tell which button was
    changed most recently.

- role (string; optional):
    The ARIA role attribute.

- style (dict with strings as keys and values of type string | number; optional):
    CSS style to apply to the element.

- transform (string; optional):
    Transformation to apply to the element.

- x (string | number; optional):
    x position.

- y (string | number; optional):
    y position."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_svg'
    _type = 'FeDistantLight'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, n_clicks=Component.UNDEFINED, n_clicks_timestamp=Component.UNDEFINED, key=Component.UNDEFINED, role=Component.UNDEFINED, azimuth=Component.UNDEFINED, elevation=Component.UNDEFINED, className=Component.UNDEFINED, transform=Component.UNDEFINED, style=Component.UNDEFINED, x=Component.UNDEFINED, y=Component.UNDEFINED, fill=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'aria-*', 'azimuth', 'className', 'data-*', 'elevation', 'fill', 'key', 'loading_state', 'n_clicks', 'n_clicks_timestamp', 'role', 'style', 'transform', 'x', 'y']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['children', 'id', 'aria-*', 'azimuth', 'className', 'data-*', 'elevation', 'fill', 'key', 'loading_state', 'n_clicks', 'n_clicks_timestamp', 'role', 'style', 'transform', 'x', 'y']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FeDistantLight, self).__init__(children=children, **args)
