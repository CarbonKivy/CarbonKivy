from __future__ import annotations

__all__ = ("GradientEffect",)

from typing import Any

from kivy.clock import Clock
from kivy.event import EventDispatcher
from kivy.graphics import Fbo, Color, Rectangle
from kivy.properties import ColorProperty, ListProperty, NumericProperty, OptionProperty
from kivy.utils import get_color_from_hex

GRADIENT_FS = """
$HEADER$
uniform vec2 u_size;
uniform vec4 u_color_top;    
uniform vec4 u_color_bottom; 
uniform float u_grad_type;      
uniform vec2  u_linear_bounds;  
uniform float u_radial_radius;  
uniform vec2  u_radial_center;  

void main(void) {
    vec2 uv = gl_FragCoord.xy / u_size;
    
    if (uv.x < 0.0 || uv.x > 1.0 || uv.y < 0.0 || uv.y > 1.0) {
        discard;
    }
    
    float mix_value = 0.0;
    
    if (u_grad_type < 0.5) {
        float range = u_linear_bounds.y - u_linear_bounds.x;
        if (abs(range) < 0.0001) {
            mix_value = step(u_linear_bounds.x, uv.y);
        } else {
            mix_value = smoothstep(u_linear_bounds.x, u_linear_bounds.y, uv.y);
        }
    } else {
        float dist = distance(uv, u_radial_center);
        mix_value = smoothstep(0.0, u_radial_radius, dist);
    }
    
    mix_value = clamp(mix_value, 0.0, 1.0);
    gl_FragColor = mix(u_color_bottom, u_color_top, mix_value);
}
"""


class GradientEffect(EventDispatcher):

    gradient_color_top = ColorProperty([1.0, 1.0, 1.0, 1.0])
    gradient_color_bottom = ColorProperty(get_color_from_hex("#0F62FE"))
    gradient_type = OptionProperty("linear", options=["linear", "radial"])
    gradient_linear_bounds = ListProperty([0.0, 1.0])
    gradient_radial_radius = NumericProperty(0.7)
    gradient_radial_center = ListProperty([0.5, 0.5])

    def __init__(self, **kwargs):
        super(GradientEffect, self).__init__(**kwargs)

        init_size = getattr(self, "size", (100, 100))
        init_pos = getattr(self, "pos", (0, 0))

        self._fbo = Fbo(size=init_size, with_depthbuffer=False)
        self._fbo.shader.fs = GRADIENT_FS

        with self._fbo:
            self._fbo_rect = Rectangle(size=init_size)

        if hasattr(self, "canvas"):
            with self.canvas.before:
                Color(1, 1, 1, 1)
                self._bg_rect = Rectangle(
                    pos=init_pos, size=init_size, texture=self._fbo.texture
                )

        Clock.schedule_once(self._init_gradient, 0)

    def _init_gradient(self, dt: float | int) -> None:
        self._fbo["u_color_top"] = list(self.gradient_color_top)
        self._fbo["u_color_bottom"] = list(self.gradient_color_bottom)
        self._fbo["u_grad_type"] = 0.0 if self.gradient_type == "linear" else 1.0
        self._fbo["u_linear_bounds"] = list(self.gradient_linear_bounds)
        self._fbo["u_radial_radius"] = float(self.gradient_radial_radius)
        self._fbo["u_radial_center"] = list(self.gradient_radial_center)

        self._update_uniforms(None, None)

        self.bind(size=self._update_uniforms, pos=self._update_uniforms)

    def on_gradient_color_top(self, instance: object, value: Any) -> None:
        self._fbo["u_color_top"] = list(value)
        self._fbo.draw()

    def on_gradient_color_bottom(self, instance: object, value: Any) -> None:
        self._fbo["u_color_bottom"] = list(value)
        self._fbo.draw()

    def on_gradient_type(self, instance: object, value: Any) -> None:
        self._fbo["u_grad_type"] = 0.0 if value == "linear" else 1.0
        self._fbo.draw()

    def on_gradient_linear_bounds(self, instance: object, value: Any) -> None:
        self._fbo["u_linear_bounds"] = list(value)
        self._fbo.draw()

    def on_gradient_radial_radius(self, instance: object, value: Any) -> None:
        self._fbo["u_radial_radius"] = float(value)
        self._fbo.draw()

    def on_gradient_radial_center(self, instance: object, value: Any) -> None:
        self._fbo["u_radial_center"] = list(value)
        self._fbo.draw()

    def _update_uniforms(self, instance: object, value: Any) -> None:
        if not hasattr(self, "size") or not hasattr(self, "pos"):
            return

        w, h = self.size
        if w <= 0 or h <= 0:
            w, h = 1, 1

        self._fbo.size = (w, h)
        self._fbo_rect.size = (w, h)

        if hasattr(self, "_bg_rect"):
            self._bg_rect.size = (w, h)
            self._bg_rect.pos = self.pos

        self._fbo["u_size"] = [float(w), float(h)]

        self._fbo.draw()
