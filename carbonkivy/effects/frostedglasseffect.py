"""
==================
FrostedGlassEffect
==================

Features golden-angle spiral blurring, vibrancy (saturation), and film grain.
"""

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import (
    BindTexture,
    ClearBuffers,
    ClearColor,
    Color,
    Fbo,
    RenderContext,
    RoundedRectangle,
    Scale,
    SmoothLine,
    Translate,
)
from kivy.properties import ColorProperty, ListProperty, NumericProperty, ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.modalview import ModalView
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView

macos_shader = """
#ifdef GL_ES
    precision highp float;
#endif
$HEADER$

uniform float opacity;
uniform float blur_size;
uniform float saturation;
uniform vec2 position;
uniform vec2 resolution;
uniform vec4 color_overlay;
uniform sampler2D texture1;

float hash(vec2 p) {
    return fract(sin(dot(p, vec2(12.9898, 78.233))) * 43758.5453);
}

void main(void)
{
    vec2 uv = (gl_FragCoord.xy - position.xy) / resolution.xy;
    uv = clamp(uv, 0.0, 1.0);
    vec4 blurred_color = vec4(0.0);
    float weight_sum = 0.0;
    float golden_angle = 2.39996323; 
    const float ITERATIONS = 128.0; 
    
    for (float i = 0.0; i < ITERATIONS; i++) {
        float r = sqrt(i + 0.5) / sqrt(ITERATIONS);
        float theta = i * golden_angle;
        vec2 offset = vec2(cos(theta), sin(theta)) * (r * blur_size);
        offset.x *= resolution.y / resolution.x;
        float weight = exp(-r * r * 4.0); 
        blurred_color += texture2D(texture1, clamp(uv + offset, 0.0, 1.0)) * weight;
        weight_sum += weight;
    }

    blurred_color /= weight_sum;

    const vec3 W = vec3(0.2125, 0.7154, 0.0721);
    float luminance = dot(blurred_color.rgb, W);
    vec3 vibrant_color = mix(vec3(luminance), blurred_color.rgb, saturation);

    float noise = (hash(gl_FragCoord.xy) - 0.5) * 0.03; 
    vibrant_color += noise * (0.5 + luminance * 0.5);
    vec4 final_color = vec4(vibrant_color, 1.0);
    final_color.rgb = mix(final_color.rgb, color_overlay.rgb, color_overlay.a);
    gl_FragColor = vec4(final_color.rgb, opacity);
}
"""


class BackgroundCaptureFbo(Fbo):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        with self:
            ClearColor(0, 0, 0, 0)
            ClearBuffers()
            self.fbo_scale = Scale(1, 1, 1)
            self.fbo_translate = Translate(0, 0)


class FrostedGlassEffect(Widget):
    background = ObjectProperty(None, allownone=True)
    blur_size = NumericProperty(0.03)
    saturation = NumericProperty(1.8)
    overlay_color = ColorProperty([0.1, 0.1, 0.1, 0.35])
    border_radius = ListProperty([0, 0, 0, 0])
    outline_color = ColorProperty([1.0, 1.0, 1.0, 0.4])
    outline_width = NumericProperty(1)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        fbind = self.fbind
        fbind("outline_width", self._update_canvas)
        fbind("outline_color", self._update_canvas)
        fbind("border_radius", self._update_canvas)
        fbind("overlay_color", self.update_effect)
        fbind("blur_size", self.update_effect)
        fbind("saturation", self.update_effect)

        self.glass_effect = RenderContext(
            use_parent_projection=True, use_parent_modelview=True, fs=macos_shader
        )
        with self.glass_effect:
            self.bt_1 = BindTexture(index=1)
            self.fbo_rect = RoundedRectangle(
                size=self.size, pos=self.pos, radius=self.border_radius
            )

        self.glass_effect["texture1"] = 1
        self.canvas.add(self.glass_effect)

        with self.canvas:
            self._outline_color = Color(rgba=self.outline_color)
            self.outline = SmoothLine(
                width=1,
                overdraw_width=2,
                rounded_rectangle=(
                    self.x,
                    self.y,
                    self.width,
                    self.height,
                    1,
                    1,
                    1,
                    1,
                    45,
                ),
            )

        self.capture_fbo = BackgroundCaptureFbo(size=(250, 250))

        self._pos = [0, 0]
        self.parent_screen = None
        self.parents_list = []
        self._last_background_canvas = None
        self.is_movable = False

        self._update_glsl_ev = Clock.create_trigger(self._update_glsl, 0)
        self._update_fbo_ev = Clock.create_trigger(self._update_fbo_effect, 0)
        self._update_texture_ev = Clock.create_trigger(self._set_final_texture, 0)

    def update_effect(self, *args):
        self._update_glsl_ev()

    def refresh_effect(self, *args):
        self._update_fbo_ev()
        self._update_glsl_ev()

    def _update_glsl(self, *args):
        self._pos = self.to_window(*self.pos)
        if self.not_current_screen or (
            self.out_of_the_window and self.background_loaded
        ):
            return

        effect = self.glass_effect
        effect["position"] = [float(v) for v in self._pos]
        effect["resolution"] = [float(v) for v in self.size]
        effect["blur_size"] = float(self.blur_size)
        effect["saturation"] = float(self.saturation)
        effect["color_overlay"] = [float(v) for v in self.overlay_color]

        if self.is_movable:
            self.refresh_effect()
            self.capture_fbo.fbo_translate.x = -self._pos[0]
            self.capture_fbo.fbo_translate.y = -self._pos[1]

        self._update_texture_ev()

    def _set_final_texture(self, pos):
        if not self.background:
            return

        if self._last_background_canvas not in self.capture_fbo.children:
            self.capture_fbo.add(self._last_background_canvas)

        self.capture_fbo.draw()
        self.capture_fbo.ask_update()
        self.bt_1.texture = self.capture_fbo.texture

    def _update_fbo_effect(self, *args):
        fbo_size = (min(self.width, 250), min(self.height, 250))
        size = max(1, self.width), max(1, self.height)
        fbo_size = max(1, fbo_size[0]), max(1, fbo_size[1])

        self.capture_fbo.size = fbo_size
        pos = self.to_window(*self.pos)

        self.capture_fbo.fbo_scale.x = 1 / (size[0] / fbo_size[0])
        self.capture_fbo.fbo_scale.y = 1 / (size[1] / fbo_size[1])

        self.capture_fbo.fbo_translate.x = -pos[0]
        self.capture_fbo.fbo_translate.y = -pos[1]

    def on_size(self, instance, size):
        self._update_canvas()
        self.refresh_effect()

    def on_pos(self, *args):
        self._update_canvas()
        self.refresh_effect()

    def _update_canvas(self, *args):
        border_radius = list(
            map(
                lambda x: max(1, min(min(self.width, self.height) / 2, x)),
                self.border_radius,
            )
        )
        self.fbo_rect.size = self.size
        self.fbo_rect.pos = self.pos
        self.fbo_rect.radius = border_radius

        self._outline_color.rgba = self.outline_color
        self.outline.width = self.outline_width
        self.outline.rounded_rectangle = (
            self.x,
            self.y,
            self.width,
            self.height,
            *border_radius,
            45,
        )

    def on_background(self, _, background):
        if not background:
            return
        if self._last_background_canvas in self.capture_fbo.children:
            self.capture_fbo.remove(self._last_background_canvas)
            self._unbind_parent_properties(self.background_parents_list)

        self._last_background_canvas = background.canvas
        self.background_parents_list = self._get_all_parents(self.background)
        self._bind_parent_properties(self.background_parents_list)
        self.update_effect()

    def on_parent(self, _, parent):
        if not parent:
            return
        self.parents_list = self._get_all_parents(parent)
        for p in self.parents_list:
            if isinstance(p, Screen):
                self.parent_screen = p
            if isinstance(p, ScrollView):
                self.is_movable = True
        self._bind_parent_properties(self.parents_list)

    def _get_all_parents(self, widget):
        widgets_list = []
        parent = widget
        while True:
            widgets_list.append(parent)
            if parent.parent and parent != parent.parent:
                parent = parent.parent
            else:
                break
        return widgets_list

    def _bind_parent_properties(self, parents_list):
        for widget in parents_list:
            if isinstance(widget, ScrollView):
                widget.bind(
                    size=self._trigger_update,
                    pos=self._trigger_update,
                    scroll_x=self._trigger_update,
                    scroll_y=self._trigger_update,
                )
            elif isinstance(widget, Screen):
                pass
            else:
                widget.bind(size=self._trigger_update)
                try:
                    widget.bind(pos=self._trigger_update)
                except Exception:
                    pass

    def _unbind_parent_properties(self, parents_list):
        for widget in parents_list:
            if isinstance(widget, ScrollView):
                widget.unbind(
                    size=self._trigger_update,
                    pos=self._trigger_update,
                    scroll_x=self._trigger_update,
                    scroll_y=self._trigger_update,
                )
            elif isinstance(widget, Screen):
                pass
            else:
                widget.unbind(size=self._trigger_update)
                try:
                    widget.unbind(pos=self._trigger_update)
                except Exception:
                    pass

    def _trigger_update(self, widget, value=None):
        self.update_effect()

    @property
    def not_current_screen(self):
        if self.parent_screen is None or self.parent_screen.manager is None:
            return False
        return self.parent_screen.manager.current != self.parent_screen.name

    @property
    def out_of_the_window(self):
        x, y = self.to_window(self.x, self.y)
        right, top = self.to_window(self.right, self.top)
        return right < 0 or top < 0 or x > Window.width or y > Window.height

    @property
    def background_loaded(self):
        if not self.background:
            return False
        return self.background.canvas in self.capture_fbo.children
