# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FeOffset(Component):
    """A FeOffset component.
FeOffset is a wrapper for the <feOffset> SVG element.
For detailed attribute info see:
https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feOffset

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

- dx (string | number; optional):
    The dx attribute indicates a shift along the x-axis on the
    position  of an element or its content.You can use this attribute
    with the following SVG elements:Warning: As of SVG2 <altGlyph>  is
    deprecated and shouldn't be used.For <altGlyph>, if  it contains a
    single value, dx defines a shift along the  x-axis for all
    alternate glyph.If there are multiple values,  dx defines a shift
    along the x-axis for each individual  glyph relative to the
    preceding glyph. If there are less  values than glyphs, the
    remaining glyphs use a value of  0. If there are more values than
    glyphs, extra values  are ignored.For <feDropShadow>, dx defines
    the x offset  of the dropped shadow. The unit used to resolve the
    value  of the attribute is set by the primitiveUnits attribute  of
    the <filter> element.For <feOffset>, dx defines the  x offset of
    the filter input graphic. The unit used to  resolve the value of
    the attribute is set by the primitiveUnits  attribute of the
    <filter> element.Warning: As of SVG2  <glyphRef> is deprecated and
    shouldn't be used.For <glyphRef>,  dx defines the x offset of the
    glyph, in the font metric  system.For <text>, if it contains a
    single value, dx defines  a shift along the x-axis for all
    glyphs.If there are multiple  values, dx defines a shift along the
    x-axis for each individual  glyph relative to the preceding glyph.
    If there are less  values than glyphs, the remaining glyphs use a
    value of  0. If there are more values than glyphs, extra values
    are ignored.Warning: As of SVG2 <tref> is deprecated and
    shouldn't be used.For <tref>, if it contains a single  value, dx
    defines a shift along the x-axis for all glyphs.If  there are
    multiple values, dx defines a shift along the  x-axis for each
    individual glyph relative to the preceding  glyph. If there are
    less values than glyphs, the remaining  glyphs use a value of 0.
    If there are more values than  glyphs, extra values are
    ignored.For <tspan>, if it contains  a single value, dx defines a
    shift along the x-axis for  all alternate glyph.If there are
    multiple values, dx defines  a shift along the x-axis for each
    individual glyph relative  to the preceding glyph. If there are
    less values than  glyphs, the remaining glyphs use a value of 0.
    If there  are more values than glyphs, extra values are
    ignored.Last  modified: May 13, 2022, by MDN contributors.

- dy (string | number; optional):
    The dy attribute indicates a shift along the y-axis on the
    position  of an element or its content.You can use this attribute
    with the following SVG elements:Warning: As of SVG2 <altGlyph>  is
    deprecated and shouldn't be used.For <altGlyph>, if  it contains a
    single value, dy defines a shift along the  y-axis for all
    alternate glyph.If there are multiple values,  dy defines a shift
    along the y-axis for each individual  glyph relative to the
    preceding glyph. If there are less  values than glyphs, the
    remaining glyphs use a value of  0. If there are more values than
    glyphs, extra values  are ignored.For <feDropShadow>, dy defines
    the y offset  of the dropped shadow. The unit used to resolve the
    value  of the attribute is set by the primitiveUnits attribute  of
    the <filter> element.For <feOffset>, dy defines the  y offset of
    the filter input graphic. The unit used to  resolve the value of
    the attribute is set by the primitiveUnits  attribute of the
    <filter> element.Warning: As of SVG2  <glyphRef> is deprecated and
    shouldn't be used.For <glyphRef>,  dy defines the y offset of the
    glyph, in the font metric  system.For <text>, if it contains a
    single value, dy defines  a shift along the y-axis for all
    glyphs.If there are multiple  values, dy defines a shift along the
    y-axis for each individual  glyph relative to the preceding glyph.
    If there are less  values than glyphs, the remaining glyphs use a
    value of  0. If there are more values than glyphs, extra values
    are ignored.Warning: As of SVG2 <tref> is deprecated and
    shouldn't be used.For <tref>, if it contains a single  value, dy
    defines a shift along the y-axis for all glyphs.If  there are
    multiple values, dy defines a shift along the  y-axis for each
    individual glyph relative to the preceding  glyph. If there are
    less values than glyphs, the remaining  glyphs use a value of 0.
    If there are more values than  glyphs, extra values are
    ignored.For <tspan>, if it contains  a single value, dy defines a
    shift along the y-axis for  all alternate glyph.If there are
    multiple values, dy defines  a shift along the y-axis for each
    individual glyph relative  to the preceding glyph. If there are
    less values than  glyphs, the remaining glyphs use a value of 0.
    If there  are more values than glyphs, extra values are
    ignored.Last  modified: May 13, 2022, by MDN contributors.

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
    _type = 'FeOffset'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, n_clicks=Component.UNDEFINED, n_clicks_timestamp=Component.UNDEFINED, key=Component.UNDEFINED, role=Component.UNDEFINED, colorInterpolationFilters=Component.UNDEFINED, dx=Component.UNDEFINED, dy=Component.UNDEFINED, height=Component.UNDEFINED, result=Component.UNDEFINED, width=Component.UNDEFINED, x=Component.UNDEFINED, y=Component.UNDEFINED, className=Component.UNDEFINED, transform=Component.UNDEFINED, style=Component.UNDEFINED, fill=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'aria-*', 'className', 'colorInterpolationFilters', 'data-*', 'dx', 'dy', 'fill', 'height', 'in', 'key', 'loading_state', 'n_clicks', 'n_clicks_timestamp', 'result', 'role', 'style', 'transform', 'width', 'x', 'y']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['children', 'id', 'aria-*', 'className', 'colorInterpolationFilters', 'data-*', 'dx', 'dy', 'fill', 'height', 'in', 'key', 'loading_state', 'n_clicks', 'n_clicks_timestamp', 'result', 'role', 'style', 'transform', 'width', 'x', 'y']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FeOffset, self).__init__(children=children, **args)
