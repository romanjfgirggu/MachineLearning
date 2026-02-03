# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FeMergeNode(Component):
    """A FeMergeNode component.
FeMergeNode is a wrapper for the <feMergeNode> SVG element.
For detailed attribute info see:
https://developer.mozilla.org/en-US/docs/Web/SVG/Element/feMergeNode

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
    _type = 'FeMergeNode'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, n_clicks=Component.UNDEFINED, n_clicks_timestamp=Component.UNDEFINED, key=Component.UNDEFINED, role=Component.UNDEFINED, x=Component.UNDEFINED, y=Component.UNDEFINED, className=Component.UNDEFINED, transform=Component.UNDEFINED, style=Component.UNDEFINED, fill=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'aria-*', 'className', 'data-*', 'fill', 'in', 'key', 'loading_state', 'n_clicks', 'n_clicks_timestamp', 'role', 'style', 'transform', 'x', 'y']
        self._valid_wildcard_attributes =            ['data-', 'aria-']
        self.available_properties = ['children', 'id', 'aria-*', 'className', 'data-*', 'fill', 'in', 'key', 'loading_state', 'n_clicks', 'n_clicks_timestamp', 'role', 'style', 'transform', 'x', 'y']
        self.available_wildcard_properties =            ['data-', 'aria-']
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(FeMergeNode, self).__init__(children=children, **args)
