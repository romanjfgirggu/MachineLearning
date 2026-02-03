# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FeFuncR(Component):
    """A FeFuncR component.
FeFuncR is a wrapper for the <feFuncR> SVG element.
For detailed attribute info see:
https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feFuncR

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The children of this component.

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- amplitude (string | number; optional):
    The amplitude attribute controls the amplitude of the gamma
    function  of a component transfer element when its type attribute
    is gamma.You can use this attribute with the following  SVG
    elements:Last modified: May 13, 2022, by MDN contributors.

- aria-* (string; optional):
    A wildcard aria attribute.

- className (string; optional):
    Often used with CSS to style elements with common properties.

- data-* (string; optional):
    A wildcard data attribute.

- exponent (string | number; optional):
    The exponent attribute defines the exponent of the gamma
    function.You  can use this attribute with the following SVG
    elements:If  the type attribute of the component element is set to
    gamma, this value specifies the exponent of the gamma
    functionLast modified: May 13, 2022, by MDN contributors.

- fill (string; optional):
    fill color.

- intercept (string | number; optional):
    The intercept attribute defines the intercept of the linear
    function  of color component transfers when the type attribute is
    set to linear.You can use this attribute with the following  SVG
    elements:Last modified: May 13, 2022, by MDN contributors.

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

- tableValues (string | number; optional):
    The tableValues attribute defines a list of numbers defining  a
    lookup table of values for a color component transfer
    function.You can use this attribute with the following  SVG
    elements:This value holds a comma- and/or space-separated  list of
    <number>s, which define a lookup table for the  color component
    transfer function. Each number can be  between 0 and 1.An empty
    list results in an identity transfer  function.Last modified: Jul
    1, 2022, by MDN contributors.

- transform (string; optional):
    Transformation to apply to the element.

- x (string | number; optional):
    x position.

- y (string | number; optional):
    y position."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_svg'
    _type = 'FeFuncR'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, n_clicks=Component.UNDEFINED, n_clicks_timestamp=Component.UNDEFINED, key=Component.UNDEFINED, role=Component.UNDEFINED, amplitude=Component.UNDEFINED, exponent=Component.UNDEFINED, intercept=Component.UNDEFINED, tableValues=Component.UNDEFINED, x=Component.UNDEFINED, y=Component.UNDEFINED, className=Component.UNDEFINED, transform=Component.UNDEFINED, style=Component.UNDEFINED, fill=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'amplitude', 'aria-*', 'className', 'data-*', 'exponent', 'fill', 'intercept', 'key', 'loading_state', 'n_clicks', 'n_clicks_timestamp', 'role', 'style', 'tableValues', 'transform', 'x', 'y']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['children', 'id', 'amplitude', 'aria-*', 'className', 'data-*', 'exponent', 'fill', 'intercept', 'key', 'loading_state', 'n_clicks', 'n_clicks_timestamp', 'role', 'style', 'tableValues', 'transform', 'x', 'y']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FeFuncR, self).__init__(children=children, **args)
