from __future__ import annotations

__all__ = ("GradientEffect",)

from typing import Any

from kivy.clock import Clock
from kivy.event import EventDispatcher
from kivy.graphics import RenderContext
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    ListProperty,
    NumericProperty,
    OptionProperty,
)
from kivy.utils import get_color_from_hex

GRADIENT_FS = """
$HEADER$
uniform vec2 u_size;
uniform vec2 u_pos;
uniform float u_time;
uniform float u_wave_height;
uniform float u_wave_count;
uniform vec4 u_color_top;
uniform vec4 u_color_bottom;
uniform float u_grad_type;
uniform vec2 u_linear_bounds;
uniform float u_radial_radius;
uniform vec2 u_radial_center;

void main(void) {
    vec2 uv = (gl_FragCoord.xy - u_pos) / u_size;

    if (uv.x < 0.0 || uv.x > 1.0 || uv.y < 0.0 || uv.y > 1.0) {
        discard;
    }

    float wave_offset = sin(u_time + uv.x * u_wave_count) * u_wave_height;
    vec2 animated_uv = vec2(uv.x, uv.y + wave_offset);

    float mix_value = 0.0;

    if (u_grad_type < 0.5) {
        float range = u_linear_bounds.y - u_linear_bounds.x;
        if (abs(range) < 0.0001) {
            mix_value = step(u_linear_bounds.x, animated_uv.y);
        } else {
            mix_value = smoothstep(u_linear_bounds.x, u_linear_bounds.y, animated_uv.y);
        }
    } else {
        float dist = distance(animated_uv, u_radial_center);
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
    gradient_animated = BooleanProperty(True)
    gradient_speed = NumericProperty(1.0)
    gradient_wave_height = NumericProperty(0.05)
    gradient_wave_count = NumericProperty(4.0)
    render_fps = NumericProperty(60.0)

    def __init__(self, **kwargs):
        self.canvas = RenderContext(
            use_parent_projection=True, use_parent_modelview=True
        )
        self.canvas.shader.fs = GRADIENT_FS
        self.time = 0.0

        super().__init__(**kwargs)

        Clock.schedule_once(self._init_gradient, 0)

    def _init_gradient(self, dt: float | int) -> None:
        self.canvas["u_color_top"] = list(self.gradient_color_top)
        self.canvas["u_color_bottom"] = list(self.gradient_color_bottom)
        self.canvas["u_grad_type"] = 0.0 if self.gradient_type == "linear" else 1.0
        self.canvas["u_linear_bounds"] = list(self.gradient_linear_bounds)
        self.canvas["u_radial_radius"] = float(self.gradient_radial_radius)
        self.canvas["u_radial_center"] = list(self.gradient_radial_center)
        self.canvas["u_wave_height"] = float(self.gradient_wave_height)
        self.canvas["u_wave_count"] = float(self.gradient_wave_count)
        self.canvas["u_time"] = 0.0

        self._update_uniforms(None, None)
        self.bind(size=self._update_uniforms, pos=self._update_uniforms)

        Clock.schedule_interval(self._update_time, 1.0 / self.render_fps)

    def _update_time(self, dt: float | int) -> None:
        if self.gradient_animated and hasattr(self, "canvas"):
            self.time += dt * self.gradient_speed
            self.canvas["u_time"] = float(self.time)
            self.canvas.ask_update()

    def on_gradient_wave_height(self, instance: object, value: Any) -> None:
        if hasattr(self, "canvas"):
            self.canvas["u_wave_height"] = float(value)

    def on_gradient_wave_count(self, instance: object, value: Any) -> None:
        if hasattr(self, "canvas"):
            self.canvas["u_wave_count"] = float(value)

    def on_gradient_color_top(self, instance: object, value: Any) -> None:
        self.canvas["u_color_top"] = list(value)

    def on_gradient_color_bottom(self, instance: object, value: Any) -> None:
        self.canvas["u_color_bottom"] = list(value)

    def on_gradient_type(self, instance: object, value: Any) -> None:
        self.canvas["u_grad_type"] = 0.0 if value == "linear" else 1.0

    def on_gradient_linear_bounds(self, instance: object, value: Any) -> None:
        self.canvas["u_linear_bounds"] = list(value)

    def on_gradient_radial_radius(self, instance: object, value: Any) -> None:
        self.canvas["u_radial_radius"] = float(value)

    def on_gradient_radial_center(self, instance: object, value: Any) -> None:
        self.canvas["u_radial_center"] = list(value)

    def _update_uniforms(self, instance: object, value: Any) -> None:
        if (
            not hasattr(self, "size")
            or not hasattr(self, "pos")
            or not hasattr(self, "to_window")
        ):
            return

        win_x, win_y = self.to_window(*self.pos)
        self.canvas["u_size"] = [float(v) for v in self.size]
        self.canvas["u_pos"] = [float(win_x), float(win_y)]
