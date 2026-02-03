# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Filter(Component):
    """A Filter component.
Filter is a wrapper for the <filter> SVG element.
For detailed attribute info see:
https://developer.mozilla.org/en-US/docs/Web/SVG/Element/filter

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

- filterRes (string | number; optional):
    Deprecated: This feature is no longer recommended. Though some
    browsers might still support it, it may have already been  removed
    from the relevant web standards, may be in the  process of being
    dropped, or may only be kept for compatibility  purposes. Avoid
    using it, and update existing code if  possible; see the
    compatibility table at the bottom of  this page to guide your
    decision. Be aware that this feature  may cease to work at any
    time.The filterRes attribute  indicates the width and height of
    the intermediate images  in pixels of a filter primitive.Take care
    when assigning  a non-default value to this attribute. Too small
    of a  value may result in unwanted pixelation in the result.  Too
    large of a value may result in slow processing and  large memory
    usage.Note that negative values or zero values  disable the
    rendering of the element which referenced  the filter.You can use
    this attribute with the following  SVG elements:This value takes
    one or two values, the first  one outlining the resolution in
    horizontal direction,  the second one in vertical direction. If
    only one value  is specified, it is used for both directions.BCD
    tables  only load in the browser with JavaScript enabled. Enable
    JavaScript to view data.Last modified: May 13, 2022, by  MDN
    contributors.

- filterUnits (string | number; optional):
    The filterUnits attribute defines the coordinate system for the
    attributes x, y, width and height.You can use this attribute  with
    the following SVG elements:x, y, width and height  represent
    values in the current coordinate system that  results from taking
    the current user coordinate system  in place at the time when the
    <filter> element is referenced  (i.e., the user coordinate system
    for the element referencing  the <filter> element via a filter
    attribute).In that case,  x, y, width and height represent
    fractions or percentages  of the bounding box on the referencing
    element.BCD tables  only load in the browser with JavaScript
    enabled. Enable  JavaScript to view data.Last modified: May 13,
    2022, by  MDN contributors.

- height (string | number; optional):
    width.

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

- primitiveUnits (string | number; optional):
    The primitiveUnits attribute specifies the coordinate system  for
    the various length values within the filter primitives  and for
    the attributes that define the filter primitive  subregion.You can
    use this attribute with the following  SVG elements:This value
    indicates that any length values  within the filter definitions
    represent values in the  current user coordinate system in place
    at the time when  the <filter> element is referenced (i.e., the
    user coordinate  system for the element referencing the <filter>
    element  via a filter attribute).This value indicates that any
    length values within the filter definitions represent  fractions
    or percentages of the bounding box on the referencing  element.BCD
    tables only load in the browser with JavaScript  enabled. Enable
    JavaScript to view data.Last modified:  May 13, 2022, by MDN
    contributors.

- role (string; optional):
    The ARIA role attribute.

- style (dict with strings as keys and values of type string | number; optional):
    CSS style to apply to the element.

- transform (string; optional):
    Transformation to apply to the element.

- width (string | number; optional):
    width.

- x (string | number; optional):
    x position.

- y (string | number; optional):
    y position."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_svg'
    _type = 'Filter'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, n_clicks=Component.UNDEFINED, n_clicks_timestamp=Component.UNDEFINED, key=Component.UNDEFINED, role=Component.UNDEFINED, filterRes=Component.UNDEFINED, filterUnits=Component.UNDEFINED, height=Component.UNDEFINED, primitiveUnits=Component.UNDEFINED, width=Component.UNDEFINED, x=Component.UNDEFINED, y=Component.UNDEFINED, className=Component.UNDEFINED, transform=Component.UNDEFINED, style=Component.UNDEFINED, fill=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'aria-*', 'className', 'data-*', 'fill', 'filterRes', 'filterUnits', 'height', 'key', 'loading_state', 'n_clicks', 'n_clicks_timestamp', 'primitiveUnits', 'role', 'style', 'transform', 'width', 'x', 'y']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['children', 'id', 'aria-*', 'className', 'data-*', 'fill', 'filterRes', 'filterUnits', 'height', 'key', 'loading_state', 'n_clicks', 'n_clicks_timestamp', 'primitiveUnits', 'role', 'style', 'transform', 'width', 'x', 'y']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Filter, self).__init__(children=children, **args)
