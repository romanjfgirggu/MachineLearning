# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FeConvolveMatrix(Component):
    """A FeConvolveMatrix component.
FeConvolveMatrix is a wrapper for the <feConvolveMatrix> SVG element.
For detailed attribute info see:
https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feConvolveMatrix

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The children of this component.

- id (string; optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app.

- aria-* (string; optional):
    A wildcard aria attribute.

- bias (string | number; optional):
    The bias attribute shifts the range of the filter. After applying
    the kernelMatrix of the <feConvolveMatrix> element to  the input
    image to yield a number and applied the divisor  attribute, the
    bias attribute is added to each component.  This allows
    representation of values that would otherwise  be clamped to 0 or
    1.You can use this attribute with the  following SVG elements:One
    application of bias is when  it is desirable to have 0.5 gray
    value be the zero response  of the filter.BCD tables only load in
    the browser with  JavaScript enabled. Enable JavaScript to view
    data.Last  modified: May 13, 2022, by MDN contributors.

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

- divisor (string | number; optional):
    The divisor attribute specifies the value by which the resulting
    number of applying the kernelMatrix of a <feConvolveMatrix>
    element to the input image color value is divided to yield  the
    destination color value.A divisor that is the sum  of all the
    matrix values tends to have an evening effect  on the overall
    color intensity of the result.You can use  this attribute with the
    following SVG elements:This value  defines the divisor. If the
    specified divisor is 0 then  the default value will be used
    instead.BCD tables only  load in the browser with JavaScript
    enabled. Enable JavaScript  to view data.Last modified: May 13,
    2022, by MDN contributors.

- edgeMode (string | number; optional):
    The edgeMode attribute determines how to extend the input image
    as necessary with color values so that the matrix operations  can
    be applied when the kernel is positioned at or near  the edge of
    the input image.You can use this attribute  with the following SVG
    elements:For <feConvolveMatrix>,  edgeMode determines how to
    extend the input image as necessary  with color values so that the
    matrix operations can be  applied when the kernel is positioned at
    or near the edge  of the input image.This value indicates that the
    input  image is extended along each of its borders as necessary
    by duplicating the color values at the given edge of the  input
    image.This value indicates that the input image  is extended by
    taking the color values from the opposite  edge of the image.This
    value indicates that the input  image is extended with pixel
    values of zero for R, G,  B and A.For <feGaussianBlur>, edgeMode
    determines how  to extend the input image as necessary with color
    values  so that the matrix operations can be applied when the
    kernel is positioned at or near the edge of the input  image.This
    value indicates that the input image is extended  along each of
    its borders as necessary by duplicating  the color values at the
    given edge of the input image.This  value indicates that the input
    image is extended by taking  the color values from the opposite
    edge of the image.This  value indicates that the input image is
    extended with  pixel values of zero for R, G, B and A.Last
    modified:  May 13, 2022, by MDN contributors.

- fill (string; optional):
    fill color.

- height (string | number; optional):
    width.

- in (string | number; optional):
    The in attribute identifies input for the given filter
    primitive.The  value can be either one of the six keywords defined
    below,  or a string which matches a previous result attribute
    value within the same <filter> element. If no value is  provided
    and this is the first filter primitive, then  this filter
    primitive will use SourceGraphic as its input.  If no value is
    provided and this is a subsequent filter  primitive, then this
    filter primitive will use the result  from the previous filter
    primitive as its input.If the  value for result appears multiple
    times within a given  <filter> element, then a reference to that
    result will  use the closest preceding filter primitive with the
    given  value for attribute result.You can use this attribute  with
    the following SVG elements:This keyword represents  the graphics
    elements that were the original input into  the <filter>
    element.This keyword represents the graphics  elements that were
    the original input into the <filter>  element. SourceAlpha has all
    of the same rules as SourceGraphic  except that only the alpha
    channel is used.This keyword  represents an image snapshot of the
    SVG document under  the filter region at the time that the
    <filter> element  was invoked.Same as BackgroundImage except only
    the alpha  channel is used.This keyword represents the value of
    the  fill property on the target element for the filter effect.
    In many cases, the FillPaint is opaque everywhere, but  that might
    not be the case if a shape is painted with  a gradient or pattern
    which itself includes transparent  or semi-transparent parts.This
    keyword represents the  value of the stroke property on the target
    element for  the filter effect. In many cases, the StrokePaint is
    opaque  everywhere, but that might not be the case if a shape  is
    painted with a gradient or pattern which itself includes
    transparent or semi-transparent parts.This value is an  assigned
    name for the filter primitive in the form of  a <custom-ident>. If
    supplied, then graphics that result  from processing this filter
    primitive can be referenced  by an in attribute on a subsequent
    filter primitive within  the same filter element. If no value is
    provided, the  output will only be available for re-use as the
    implicit  input into the next filter primitive if that filter
    primitive  provides no value for its in attribute.BackgroundImage
    is not supported as a filter source in modern browsers  (see the
    feComposite compatibility table). We therefore  need to import one
    of the images to blend inside the filter  itself, using an
    <feImage> element.Note: Firefox Bug 455986  means that feImage
    cannot load partial images, including  circles, rectangles, paths
    or other fragments defined  in the document. So that this example
    works on more browsers,  a full external image of the logo is
    loaded.Last modified:  Jul 1, 2022, by MDN contributors.

- kernelMatrix (string | number; optional):
    The kernelMatrix attribute defines the list of numbers that make
    up the kernel matrix for the <feConvolveMatrix> element.Values
    are separated by space characters and/or a comma. The  number of
    entries in the list must equal to <orderX> by  <orderY> as defined
    in the order attribute.You can use  this attribute with the
    following SVG elements:The list  of <number>s that make up the
    kernel matrix for the convolution.  Values are separated by space
    characters and/or a comma.  The number of entries in the list must
    equal <orderX>  times <orderY>.If the result of orderX * orderY is
    not  equal to the number of entries in the value list, the  filter
    primitive acts as a pass through filter.BCD tables  only load in
    the browser with JavaScript enabled. Enable  JavaScript to view
    data.Last modified: May 13, 2022, by  MDN contributors.

- kernelUnitLength (string | number; optional):
    Deprecated: This feature is no longer recommended. Though some
    browsers might still support it, it may have already been  removed
    from the relevant web standards, may be in the  process of being
    dropped, or may only be kept for compatibility  purposes. Avoid
    using it, and update existing code if  possible; see the
    compatibility table at the bottom of  this page to guide your
    decision. Be aware that this feature  may cease to work at any
    time.The kernelUnitLength attribute  has two meanings based on the
    context it's used in. For  lighting filter primitives, it
    indicates the intended  distance for the x and y coordinates, for
    <feConvolveMatrix>,  it indicates the intended distance between
    successive  columns and rows in the kernel matrix.You can use this
    attribute with the following SVG elements:For the
    <feConvolveMatrix>,  kernelUnitLength indicates the intended
    distance in current  filter units (i.e., units as determined by
    the value of  primitiveUnits attribute) between successive columns
    and  rows, respectively, in the kernelMatrix. By specifying
    value(s) for kernelUnitLength, the kernel becomes defined  in a
    scalable, abstract coordinate system. If the attribute  is not
    specified, the default value is one pixel in the  offscreen
    bitmap, which is a pixel-based coordinate system,  and thus
    potentially not scalable.If a negative or zero  value is specified
    the default value will be used instead.The  first number is the x
    value. The second number is the  y value. If the x value is not
    specified, it defaults  to the same value as x.For the
    <feDiffuseLighting>, kernelUnitLength  indicates the intended
    distance in current filter units  (i.e., units as determined by
    the value of attribute primitiveUnits)  for the x and y
    coordinate, respectively, in the surface  normal calculation
    formulas.The first number is the x  value. The second number is
    the y value. If the y value  is not specified, it defaults to the
    same value as x.  By specifying value(s) for kernelUnitLength, the
    kernel  becomes defined in a scalable, abstract coordinate system.
    If the attribute is not specified, the x and y values  represent
    very small deltas relative to a given position,  which might be
    implemented in some cases as one pixel  in the intermediate image
    offscreen bitmap, which is a  pixel-based coordinate system, and
    thus potentially not  scalable.If a negative or zero value is
    specified the  default value will be used instead.For the
    <feSpecularLighting>,  kernelUnitLength indicates the intended
    distance in current  filter units (i.e., units as determined by
    the value of  attribute primitiveUnits) for the x and y
    coordinate,  respectively, in the surface normal calculation
    formulas.The  first number is the x value. The second number is
    the  y value. If the y value is not specified, it defaults  to the
    same value as x. By specifying value(s) for kernelUnitLength,  the
    kernel becomes defined in a scalable, abstract coordinate  system.
    If the attribute is not specified, the x and y  values represent
    very small deltas relative to a given  position, which might be
    implemented in some cases as  one pixel in the intermediate image
    offscreen bitmap,  which is a pixel-based coordinate system, and
    thus potentially  not scalable.If a negative or zero value is
    specified  the default value will be used instead.Last modified:
    May 13, 2022, by MDN contributors.

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

- order (a value equal to: "no", "yes"; optional):
    The order attribute indicates the size of the matrix to be used
    by a <feConvolveMatrix> element.You can use this attribute  with
    the following SVG elements:This value indicates the  number of
    cells in each dimension for the kernel matrix.  The values
    provided must be <integer>s greater than zero.  Values that are
    not integers will be truncated, i.e. rounded  to the closest
    integer value towards zero. The first number,  indicates the
    number of columns in the matrix. The second  number, indicates the
    number of rows in the matrix. If  no second number is not
    provided, it defaults to the first  number.It is recommended that
    only small values (e.g.,  3) be used; higher values may result in
    very high CPU  overhead and usually do not produce results that
    justify  the impact on performance.BCD tables only load in the
    browser with JavaScript enabled. Enable JavaScript to  view
    data.Last modified: Jun 12, 2022, by MDN contributors.

- preserveAlpha (a value equal to: 'true', 'false'; optional):
    the preserveAlpha attribute indicates how a <feConvolveMatrix>
    element handled alpha transparency.You can use this attribute
    with the following SVG elements:This value indicates that  the
    convolution will only apply to the color channels.  In this case,
    the filter will temporarily unpremultiply  the color component
    values and apply the kernel.This value  indicates that the
    convolution will apply to all channels,  including the alpha
    channel.BCD tables only load in the  browser with JavaScript
    enabled. Enable JavaScript to  view data.Last modified: May 13,
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

- targetX (string | number; optional):
    The targetX attribute determines the positioning in horizontal
    direction of the convolution matrix relative to a given  target
    pixel in the input image. The leftmost column of  the matrix is
    column number zero. The value must be such  that: 0 <= targetX <
    orderX.You can use this attribute  with the following SVG
    elements:This value indicates the  positioning in horizontal
    direction of the convolution  matrix relative to a given target
    pixel in the input image.BCD  tables only load in the browser with
    JavaScript enabled.  Enable JavaScript to view data.Last modified:
    May 13,  2022, by MDN contributors.

- targetY (string | number; optional):
    The targetY attribute determines the positioning in vertical
    direction of the convolution matrix relative to a given  target
    pixel in the input image. The topmost row of the  matrix is row
    number zero. The value must be such that:  0 <= targetY <
    orderY.You can use this attribute with  the following SVG
    elements:This value indicates the positioning  in vertical
    direction of the convolution matrix relative  to a given target
    pixel in the input image.BCD tables  only load in the browser with
    JavaScript enabled. Enable  JavaScript to view data.Last modified:
    May 13, 2022, by  MDN contributors.

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
    _type = 'FeConvolveMatrix'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, n_clicks=Component.UNDEFINED, n_clicks_timestamp=Component.UNDEFINED, key=Component.UNDEFINED, role=Component.UNDEFINED, bias=Component.UNDEFINED, colorInterpolationFilters=Component.UNDEFINED, divisor=Component.UNDEFINED, edgeMode=Component.UNDEFINED, height=Component.UNDEFINED, kernelMatrix=Component.UNDEFINED, kernelUnitLength=Component.UNDEFINED, order=Component.UNDEFINED, preserveAlpha=Component.UNDEFINED, result=Component.UNDEFINED, targetX=Component.UNDEFINED, targetY=Component.UNDEFINED, width=Component.UNDEFINED, x=Component.UNDEFINED, y=Component.UNDEFINED, className=Component.UNDEFINED, transform=Component.UNDEFINED, style=Component.UNDEFINED, fill=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'aria-*', 'bias', 'className', 'colorInterpolationFilters', 'data-*', 'divisor', 'edgeMode', 'fill', 'height', 'in', 'kernelMatrix', 'kernelUnitLength', 'key', 'loading_state', 'n_clicks', 'n_clicks_timestamp', 'order', 'preserveAlpha', 'result', 'role', 'style', 'targetX', 'targetY', 'transform', 'width', 'x', 'y']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['children', 'id', 'aria-*', 'bias', 'className', 'colorInterpolationFilters', 'data-*', 'divisor', 'edgeMode', 'fill', 'height', 'in', 'kernelMatrix', 'kernelUnitLength', 'key', 'loading_state', 'n_clicks', 'n_clicks_timestamp', 'order', 'preserveAlpha', 'result', 'role', 'style', 'targetX', 'targetY', 'transform', 'width', 'x', 'y']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FeConvolveMatrix, self).__init__(children=children, **args)
