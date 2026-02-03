# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FeImage(Component):
    """A FeImage component.
FeImage is a wrapper for the <feImage> SVG element.
For detailed attribute info see:
https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feImage

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

- colorInterpolationFilters (a value equal to: "auto", "inherit", "linearRGB", "sRGB"; optional):
    The color-interpolation-filters attribute specifies the color
    space for imaging operations performed via filter effects.Note:
    This property just has an affect on filter operations.  Therefore,
    it has no effect on filter primitives like  <feOffset>, <feImage>,
    <feTile> or <feFlood>.color-interpolation-filters  has a different
    initial value than color-interpolation.
    color-interpolation-filters has an initial value of linearRGB,
    whereas color-interpolation has an initial value of sRGB.  Thus,
    in the default case, filter effects operations occur  in the
    linearRGB color space, whereas all other color  interpolations
    occur by default in the sRGB color space.It  has no affect on
    filter functions, which operate in the  sRGB color space.Note: As
    a presentation attribute, color-interpolation-filters  can be used
    as a CSS property.You can use this attribute  with the following
    SVG elements:Indicates that the user  agent can choose either the
    sRGB or linearRGB spaces for  color interpolation. This option
    indicates that the author  doesn't require that color
    interpolation occur in a particular  color space.Indicates that
    color interpolation should  occur in the sRGB color
    space.Indicates that color interpolation  should occur in the
    linearized RGB color space as described  in the sRGB
    specification.BCD tables only load in the  browser with JavaScript
    enabled. Enable JavaScript to  view data.Last modified: May 13,
    2022, by MDN contributors.

- data-* (string; optional):
    A wildcard data attribute.

- fill (string; optional):
    fill color.

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

- result (string; optional):
    The result attribute defines the assigned name for this filter
    primitive. If supplied, then graphics that result from  processing
    this filter primitive can be referenced by  an in attribute on a
    subsequent filter primitive within  the same <filter> element. If
    no value is provided, the  output will only be available for
    re-use as the implicit  input into the next filter primitive if
    that filter primitive  provides no value for its in attribute.You
    can use this  attribute with the following SVG elements:This value
    is  a <custom-ident> and defines the name for the filter
    primitive.  It is only meaningful within a given <filter> element
    and thus has only local scope. It is legal for the same
    <filter-primitive-reference> to appear multiple times  within the
    same <filter> element. When referenced, this  value will use the
    closest preceding filter primitive  with the given result.Last
    modified: May 13, 2022, by  MDN contributors.

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
    _type = 'FeImage'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, n_clicks=Component.UNDEFINED, n_clicks_timestamp=Component.UNDEFINED, key=Component.UNDEFINED, role=Component.UNDEFINED, colorInterpolationFilters=Component.UNDEFINED, height=Component.UNDEFINED, preserveAspectRatio=Component.UNDEFINED, result=Component.UNDEFINED, width=Component.UNDEFINED, x=Component.UNDEFINED, y=Component.UNDEFINED, className=Component.UNDEFINED, transform=Component.UNDEFINED, style=Component.UNDEFINED, fill=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'aria-*', 'className', 'colorInterpolationFilters', 'data-*', 'fill', 'height', 'key', 'loading_state', 'n_clicks', 'n_clicks_timestamp', 'preserveAspectRatio', 'result', 'role', 'style', 'transform', 'width', 'x', 'y']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['children', 'id', 'aria-*', 'className', 'colorInterpolationFilters', 'data-*', 'fill', 'height', 'key', 'loading_state', 'n_clicks', 'n_clicks_timestamp', 'preserveAspectRatio', 'result', 'role', 'style', 'transform', 'width', 'x', 'y']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FeImage, self).__init__(children=children, **args)
