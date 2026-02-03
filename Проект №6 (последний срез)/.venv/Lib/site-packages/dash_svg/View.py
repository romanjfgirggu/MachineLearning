# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class View(Component):
    """A View component.
View is a wrapper for the <view> SVG element.
For detailed attribute info see:
https://developer.mozilla.org/en-US/docs/Web/SVG/Element/view

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

- preserveAspectRatio (string; optional):
    The preserveAspectRatio attribute indicates how an element with  a
    viewBox providing a given aspect ratio must fit into  a viewport
    with a different aspect ratio.Because the aspect  ratio of an SVG
    image is defined by the viewBox attribute,  if this attribute
    isn't set, the preserveAspectRatio attribute  has no effect (with
    one exception, the <image> element,  as described below).Its value
    is made of one or two keywords:  A required alignment value and an
    optional \"meet or slice\"  reference as described below:The
    alignment value indicates  whether to force uniform scaling and,
    if so, the alignment  method to use in case the aspect ratio of
    the viewBox  doesn't match the aspect ratio of the viewport. The
    alignment  value must be one of the following keywords:The meet or
    slice reference is optional and, if provided, must be  one of the
    following keywords:You can use this attribute  with the following
    SVG elements:For <feImage>, preserveAspectRatio  defines how the
    referenced image should fit in the rectangle  define by the
    <feImage> element.For <image>, preserveAspectRatio  defines how
    the referenced image should fit in the rectangle  define by the
    <image> element.For <marker>, preserveAspectRatio  indicates if a
    uniform scaling must be performed to fit  the element viewport.For
    <pattern>, preserveAspectRatio  indicates if a uniform scaling
    must be performed to fit  the element viewport.For <svg>,
    preserveAspectRatio indicates  if a uniform scaling must be
    performed to fit the element  viewport.For <symbol>,
    preserveAspectRatio indicates if  a uniform scaling must be
    performed to fit the element  viewport.For <view>,
    preserveAspectRatio indicates if  a uniform scaling must be
    performed to fit the element  viewport.Last modified: May 13,
    2022, by MDN contributors.

- role (string; optional):
    The ARIA role attribute.

- style (dict with strings as keys and values of type string | number; optional):
    CSS style to apply to the element.

- transform (string; optional):
    Transformation to apply to the element.

- viewBox (string; optional):
    The viewBox attribute defines the position and dimension, in  user
    space, of an SVG viewport.The value of the viewBox  attribute is a
    list of four numbers: min-x, min-y, width  and height. The
    numbers, which are separated by whitespace  and/or a comma,
    specify a rectangle in user space which  is mapped to the bounds
    of the viewport established for  the associated SVG element (not
    the browser viewport).You  can use this attribute with the
    following SVG elements:The  exact effect of this attribute is
    influenced by the preserveAspectRatio  attribute.Note: Values for
    width or height lower or equal  to 0 disable rendering of the
    element.For <marker>, viewBox  defines the position and dimension
    for the content of  the <marker> element.For <pattern>, viewBox
    defines the  position and dimension for the content of the pattern
    tile.For <svg>, viewBox defines the position and dimension  for
    the content of the <svg> element.For <symbol>, viewBox  defines
    the position and dimension for the content of  the <symbol>
    element.For <view>, viewBox defines the position  and dimension
    for the content of the <view> element.Last  modified: May 13,
    2022, by MDN contributors.

- viewTarget (string | number; optional):
    Deprecated: This feature is no longer recommended. Though some
    browsers might still support it, it may have already been  removed
    from the relevant web standards, may be in the  process of being
    dropped, or may only be kept for compatibility  purposes. Avoid
    using it, and update existing code if  possible; see the
    compatibility table at the bottom of  this page to guide your
    decision. Be aware that this feature  may cease to work at any
    time.The viewTarget attribute  indicates the target object
    associated with the view.You  can use this attribute with the
    following SVG elements:This  value specifies the name of the
    object associated with  the view.BCD tables only load in the
    browser with JavaScript  enabled. Enable JavaScript to view
    data.Last modified:  May 13, 2022, by MDN contributors.

- x (string | number; optional):
    x position.

- y (string | number; optional):
    y position.

- zoomAndPan (string; optional):
    Deprecated: This feature is no longer recommended. Though some
    browsers might still support it, it may have already been  removed
    from the relevant web standards, may be in the  process of being
    dropped, or may only be kept for compatibility  purposes. Avoid
    using it, and update existing code if  possible; see the
    compatibility table at the bottom of  this page to guide your
    decision. Be aware that this feature  may cease to work at any
    time.The zoomAndPan attribute  specifies whether the SVG document
    can be magnified and  panned.Magnification in this context means
    the effect  of a supplemental scale and translate transformation
    on  the outermost SVG document fragment.Panning represents  a
    translation (i.e., a shift) transformation on an SVG  document
    fragment in response to a user interface action.You  can use this
    attribute with the following SVG elements:BCD  tables only load in
    the browser with JavaScript enabled.  Enable JavaScript to view
    data.Last modified: May 13,  2022, by MDN contributors."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_svg'
    _type = 'View'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, n_clicks=Component.UNDEFINED, n_clicks_timestamp=Component.UNDEFINED, key=Component.UNDEFINED, role=Component.UNDEFINED, preserveAspectRatio=Component.UNDEFINED, viewBox=Component.UNDEFINED, viewTarget=Component.UNDEFINED, zoomAndPan=Component.UNDEFINED, className=Component.UNDEFINED, transform=Component.UNDEFINED, style=Component.UNDEFINED, x=Component.UNDEFINED, y=Component.UNDEFINED, fill=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'aria-*', 'className', 'data-*', 'fill', 'key', 'loading_state', 'n_clicks', 'n_clicks_timestamp', 'preserveAspectRatio', 'role', 'style', 'transform', 'viewBox', 'viewTarget', 'x', 'y', 'zoomAndPan']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['children', 'id', 'aria-*', 'className', 'data-*', 'fill', 'key', 'loading_state', 'n_clicks', 'n_clicks_timestamp', 'preserveAspectRatio', 'role', 'style', 'transform', 'viewBox', 'viewTarget', 'x', 'y', 'zoomAndPan']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(View, self).__init__(children=children, **args)
