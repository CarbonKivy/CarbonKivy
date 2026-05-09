from __future__ import annotations

__all__ = ("ShimmerEffect",)

from typing import Any

from kivy.clock import Clock
from kivy.properties import BooleanProperty, ColorProperty, NumericProperty
from kivy.graphics import RenderContext


SHIMMER_FS = """
$HEADER$
uniform float time;
uniform vec2 widget_size;
uniform vec2 widget_pos;
uniform vec4 shimmer_color;
uniform vec4 shine_color;
uniform float do_shimmer; 

void main(void) {
    if (do_shimmer > 0.5) {
        vec2 uv = -(gl_FragCoord.xy - widget_pos.xy) / widget_size.xy;
        float slant = uv.x - uv.y;

        float highlight = (sin(slant * 2.0 + time * 5.0) + 1.0) * 0.5;
        
        gl_FragColor = mix(shimmer_color, shine_color, highlight * 0.6);
    } else {
        gl_FragColor = frag_color * texture2D(texture0, tex_coord0);
    }
}
"""


class ShimmerEffect:

    shimmering = BooleanProperty(False)

    shimmer_speed = NumericProperty(1.5)

    shimmer_base_color = ColorProperty([0.6, 0.6, 0.6, 1])

    shimmer_shine_color = ColorProperty([0.9, 0.9, 0.9, 1])

    def __init__(self, **kwargs):
        self.canvas = RenderContext(
            use_parent_projection=True, use_parent_modelview=True
        )
        self.canvas.shader.fs = SHIMMER_FS
        super().__init__(**kwargs)

        self.bind(shimmering=self._update_glsl_state)
        Clock.schedule_once(self._init_shimmer, 0)

    def _init_shimmer(self, dt: float | int) -> None:
        self.canvas["shimmer_color"] = list(self.shimmer_base_color)
        self.canvas["shine_color"] = list(self.shimmer_shine_color)
        self.canvas["widget_size"] = [float(v) for v in self.size]
        self.canvas["widget_pos"] = [float(v) for v in self.to_window(*self.pos)]
        self.canvas["time"] = 0.0
        self.canvas["do_shimmer"] = 1.0 if self.shimmering else 0.0
        self.bind(size=self._update_uniforms, pos=self._update_uniforms)

    def _update_uniforms(self, instance: object, value: Any) -> None:
        self.canvas["widget_size"] = [float(v) for v in self.size]
        self.canvas["widget_pos"] = [float(v) for v in self.to_window(*self.pos)]

    def _update_glsl_state(self, instance: object, value: Any) -> None:
        self.canvas["do_shimmer"] = 1.0 if value else 0.0
        if value:
            Clock.schedule_interval(self._update_time, 1 / 60.0)
        else:
            Clock.unschedule(self._update_time)
            self.canvas["time"] = 0.0

    def _update_time(self, dt: float | int) -> None:
        self.canvas["time"] += dt * float(self.shimmer_speed)
