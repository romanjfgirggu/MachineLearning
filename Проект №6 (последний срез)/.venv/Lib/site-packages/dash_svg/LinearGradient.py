# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class LinearGradient(Component):
    """A LinearGradient component.
LinearGradient is a wrapper for the <linearGradient> SVG element.
For detailed attribute info see:
https://developer.mozilla.org/en-US/docs/Web/SVG/Element/linearGradient

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

- colorInterpolation (string | number; optional):
    The color-interpolation attribute specifies the color space for
    gradient interpolations, color animations, and alpha
    compositing.Note:  For filter effects, the
    color-interpolation-filters property  controls which color space
    is used.The color-interpolation  property chooses between color
    operations occurring in  the sRGB color space or in a (light
    energy linear) linearized  RGB color space. Having chosen the
    appropriate color space,  component-wise linear interpolation is
    used.When a child  element is blended into a background, the value
    of the  color-interpolation property on the child determines the
    type of blending, not the value of the color-interpolation  on the
    parent. For gradients which make use of the href  or the
    deprecated xlink:href attribute to reference another  gradient,
    the gradient uses the property's value from  the gradient element
    which is directly referenced by the  fill or stroke property. When
    animating colors, color  interpolation is performed according to
    the value of the  color-interpolation property on the element
    being animated.Note:  As a presentation attribute,
    color-interpolation can be  used as a CSS property.You can use
    this attribute with  the following SVG elements:Indicates that the
    user agent  can choose either the sRGB or linearRGB spaces for
    color  interpolation. This option indicates that the author
    doesn't  require that color interpolation occur in a particular
    color space.Indicates that color interpolation should  occur in
    the sRGB color space.Indicates that color interpolation  should
    occur in the linearized RGB color space as described  in the sRGB
    specification.BCD tables only load in the  browser with JavaScript
    enabled. Enable JavaScript to  view data.Last modified: May 13,
    2022, by MDN contributors.

- data-* (string; optional):
    A wildcard data attribute.

- fill (string; optional):
    fill color.

- gradientTransform (string; optional):
    The gradientTransform attribute contains the definition of an
    optional additional transformation from the gradient coordinate
    system onto the target coordinate system (i.e., userSpaceOnUse  or
    objectBoundingBox). This allows for things such as  skewing the
    gradient. This additional transformation matrix  is
    post-multiplied to (i.e., inserted to the right of)  any
    previously defined transformations, including the  implicit
    transformation necessary to convert from object  bounding box
    units to user space.You can use this attribute  with the following
    SVG elements:A list of transformation  functions specifying some
    additional transformation from  the gradient coordinate system
    onto the target coordinate  system.BCD tables only load in the
    browser with JavaScript  enabled. Enable JavaScript to view
    data.Last modified:  May 13, 2022, by MDN contributors.

- gradientUnits (string; optional):
    The gradientUnits attribute defines the coordinate system used
    for attributes specified on the gradient elements.You  can use
    this attribute with the following SVG elements:For
    <linearGradient>, gradientUnits defines the coordinate  system
    used for the attributes x1, y1, x2, and y2.        This value
    indicates that the attributes represent  values in the coordinate
    system that results from taking  the current user coordinate
    system in place at the time  when the gradient element is
    referenced (i.e., the user  coordinate system for the element
    referencing the gradient  element via a fill or stroke property)
    and then applying  the transform specified by attribute
    gradientTransform.        Percentages represent values relative to
    the current  SVG viewport.     This value indicates that the user
    coordinate  system for the attributes is established using the
    bounding  box of the element to which the gradient is applied and
    then applying the transform specified by attribute
    gradientTransform.Percentages  represent values relative to the
    bounding box for the  object.With this value and gradientTransform
    being the  identity matrix, the normal of the linear gradient is
    perpendicular to the gradient vector in object bounding  box space
    (i.e., the abstract coordinate system where  (0,0) is at the
    top/left of the object bounding box and  (1,1) is at the
    bottom/right of the object bounding box).  When the object's
    bounding box is not square, the gradient  normal which is
    initially perpendicular to the gradient  vector within object
    bounding box space may render non-perpendicular  relative to the
    gradient vector in user space. If the  gradient vector is parallel
    to one of the axes of the  bounding box, the gradient normal will
    remain perpendicular.  This transformation is due to application
    of the non-uniform  scaling transformation from bounding box space
    to user  space.For <radialGradient>, gradientUnits defines the
    coordinate system used for the attributes cx, cy, r, fx,  fy, and
    fr.cx, cy, r, fx, fy, and fr represent values  in the coordinate
    system that results from taking the  current user coordinate
    system in place at the time when  the gradient element is
    referenced (i.e., the user coordinate  system for the element
    referencing the gradient element  via a fill or stroke property)
    and then applying the transform  specified by attribute
    gradientTransform.       for <radialGradient>:  the user
    coordinate system for attributes cx, cy, r, fx,  fy, and fr is
    established using the bounding box of the  element to which the
    gradient is applied (see Object bounding  box units) and then
    applying the transform specified by  attribute gradientTransform.
    With this value and  gradientTransform being the identity matrix,
    the rings  of the radial gradient are circular with respect to the
    object bounding box space (i.e., the abstract coordinate  system
    where (0,0) is at the top/left of the object bounding  box and
    (1,1) is at the bottom/right of the object bounding  box). When
    the object's bounding box is not square, the  rings that are
    conceptually circular within object bounding  box space will
    render as elliptical due to application  of the non-uniform
    scaling transformation from bounding  box space to user space.
    Last modified: May 13, 2022,  by MDN contributors.

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

- spreadMethod (string; optional):
    The spreadMethod attribute determines how a shape is filled beyond
    the defined edges of a gradient.You can use this attribute  with
    the following SVG elements:This value indicates that  the final
    color of the gradient fills the shape beyond  the gradient's
    edges.This value indicates that the gradient  repeats in reverse
    beyond its edges.This value specifies  that the gradient repeats
    in the original order beyond  its edges.By default, a gradient
    reaches to the edges  of the shape being filled. To see the
    effects of this  attribute, you will need to set the size of the
    gradient  smaller than the shape.In the case of a linear gradient,
    the edges may be defined as a rectangle by the x1, x2,  y1 and y2
    attributes. In the case of a radial gradient,  the edges may be
    defined as outer and inner circles by  the cx, cy and r (outer)
    and fx, fy and fr (inner) attributes.Notice  that the middle third
    of each gradient is the same. The  outer thirds show the
    difference between the three spread  methods.BCD tables only load
    in the browser with JavaScript  enabled. Enable JavaScript to view
    data.Last modified:  May 13, 2022, by MDN contributors.

- style (dict with strings as keys and values of type string | number; optional):
    CSS style to apply to the element.

- transform (string; optional):
    Transformation to apply to the element.

- x (string | number; optional):
    x position.

- x1 (string | number; optional):
    The x1 attribute is used to specify the first x-coordinate for
    drawing an SVG element that requires more than one coordinate.
    Elements that only need one coordinate use the x attribute
    instead.You can use this attribute with the following  SVG
    elements:For <line>, x1 defines the x coordinate of  the starting
    point of the line.For <linearGradient>, x1  defines the x
    coordinate of the starting point of the  gradient vector used to
    map the gradient stop values.  The exact behavior of this
    attribute is influenced by  the gradientUnits attributesLast
    modified: May 13, 2022,  by MDN contributors.

- x2 (string | number; optional):
    The x2 attribute is used to specify the second x-coordinate for
    drawing an SVG element that requires more than one coordinate.
    Elements that only need one coordinate use the x attribute
    instead.You can use this attribute with the following  SVG
    elements:For <line>, x2 defines the x coordinate of  the ending
    point of the line.For <linearGradient>, x2  defines the x
    coordinate of the ending point of the gradient  vector used to map
    the gradient stop values. The exact  behavior of this attribute is
    influenced by the gradientUnits  attributesLast modified: May 13,
    2022, by MDN contributors.

- y (string | number; optional):
    y position.

- y1 (string | number; optional):
    The y1 attribute is used to specify the first y-coordinate for
    drawing an SVG element that requires more than one coordinate.
    Elements that only need one coordinate use the y attribute
    instead.You can use this attribute with the following  SVG
    elements:For <line>, y1 defines the y coordinate of  the starting
    point of the line.For <linearGradient>, y1  defines the y
    coordinate of the starting point of the  gradient vector used to
    map the gradient stop values.  The exact behavior of this
    attribute is influenced by  the gradientUnits attributesLast
    modified: May 13, 2022,  by MDN contributors.

- y2 (string | number; optional):
    The y2 attribute is used to specify the second y-coordinate for
    drawing an SVG element that requires more than one coordinate.
    Elements that only need one coordinate use the y attribute
    instead.You can use this attribute with the following  SVG
    elements:For <line>, y2 defines the y coordinate of  the ending
    point of the line.For <linearGradient>, y2  defines the y
    coordinate of the ending point of the gradient  vector used to map
    the gradient stop values. The exact  behavior of this attribute is
    influenced by the gradientUnits  attributesLast modified: May 13,
    2022, by MDN contributors."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_svg'
    _type = 'LinearGradient'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, n_clicks=Component.UNDEFINED, n_clicks_timestamp=Component.UNDEFINED, key=Component.UNDEFINED, role=Component.UNDEFINED, colorInterpolation=Component.UNDEFINED, gradientTransform=Component.UNDEFINED, gradientUnits=Component.UNDEFINED, spreadMethod=Component.UNDEFINED, x1=Component.UNDEFINED, x2=Component.UNDEFINED, y1=Component.UNDEFINED, y2=Component.UNDEFINED, className=Component.UNDEFINED, transform=Component.UNDEFINED, style=Component.UNDEFINED, x=Component.UNDEFINED, y=Component.UNDEFINED, fill=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'aria-*', 'className', 'colorInterpolation', 'data-*', 'fill', 'gradientTransform', 'gradientUnits', 'key', 'loading_state', 'n_clicks', 'n_clicks_timestamp', 'role', 'spreadMethod', 'style', 'transform', 'x', 'x1', 'x2', 'y', 'y1', 'y2']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['children', 'id', 'aria-*', 'className', 'colorInterpolation', 'data-*', 'fill', 'gradientTransform', 'gradientUnits', 'key', 'loading_state', 'n_clicks', 'n_clicks_timestamp', 'role', 'spreadMethod', 'style', 'transform', 'x', 'x1', 'x2', 'y', 'y1', 'y2']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(LinearGradient, self).__init__(children=children, **args)
