# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Stop(Component):
    """A Stop component.
Stop is a wrapper for the <stop> SVG element.
For detailed attribute info see:
https://developer.mozilla.org/en-US/docs/Web/SVG/Element/stop

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The children of this component.

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- aria-* (string; optional):
    A wildcard aria attribute.

- className (string; optional):
    Often used with CSS to style elements with common properties.

- data-* (string; optional):
    A wildcard data attribute.

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

- stopColor (string; optional):
    The stop-color attribute indicates what color to use at a gradient
    stop.Note: With respect to gradients, SVG treats the transparent
    keyword differently than CSS. SVG does not calculate gradients  in
    pre-multiplied space, so transparent really means transparent
    black. So, specifying a stop-color with the value transparent  is
    equivalent to specifying a stop-color with the value  black and a
    stop-opacity with the value 0.Note: As a presentation  attribute,
    stop-color can be used as a CSS property.You  can use this
    attribute with the following SVG elements:This  keyword denotes
    the current fill color and can be specified  in the same manner as
    within a <paint> specification for  the fill and stroke
    attributes.This value indicates a  color value.This value refers
    to an ICC color profile.BCD  tables only load in the browser with
    JavaScript enabled.  Enable JavaScript to view data.Last modified:
    May 13,  2022, by MDN contributors.

- stopOpacity (string | number; optional):
    The stop-opacity attribute defines the opacity of a given color
    gradient stop.The opacity value used for the gradient  calculation
    is the product of the value of stop-opacity  and the opacity of
    the value of the stop-color attribute.  For stop-color values that
    don't include explicit opacity  information, the opacity is
    treated as 1.Note: As a presentation  attribute, stop-opacity can
    be used as a CSS property.You  can use this attribute with the
    following SVG elements:This  value is either a <number> between 0
    and 1 or a <percentage>  value specifying the opacity of the color
    gradient stop.BCD  tables only load in the browser with JavaScript
    enabled.  Enable JavaScript to view data.Last modified: May 13,
    2022, by MDN contributors.

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
    _type = 'Stop'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, n_clicks=Component.UNDEFINED, n_clicks_timestamp=Component.UNDEFINED, key=Component.UNDEFINED, role=Component.UNDEFINED, stopColor=Component.UNDEFINED, stopOpacity=Component.UNDEFINED, className=Component.UNDEFINED, transform=Component.UNDEFINED, style=Component.UNDEFINED, x=Component.UNDEFINED, y=Component.UNDEFINED, fill=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'aria-*', 'className', 'data-*', 'fill', 'key', 'loading_state', 'n_clicks', 'n_clicks_timestamp', 'role', 'stopColor', 'stopOpacity', 'style', 'transform', 'x', 'y']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['children', 'id', 'aria-*', 'className', 'data-*', 'fill', 'key', 'loading_state', 'n_clicks', 'n_clicks_timestamp', 'role', 'stopColor', 'stopOpacity', 'style', 'transform', 'x', 'y']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Stop, self).__init__(children=children, **args)
