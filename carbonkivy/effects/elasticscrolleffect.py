import math
from kivy.animation import Animation
from kivy.effects.scroll import ScrollEffect


class ElasticScrollEffect(ScrollEffect):

    minimum_absorbed_velocity = 0
    maximum_velocity = 10000
    stretch_intensity = 0.016
    exponential_scalar = math.e / (1 / 3)
    scroll_friction = 0.05
    approx_normailzer = 2e5

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.friction = self.scroll_friction
        self._should_absorb = True
        self.scroll_view = None
        self.scroll_scale = None
        self.scale_axis = "y"
        self.last_touch_pos = None

    def clamp(self, value, min_val, max_val):
        return max(min_val, min(value, max_val))

    def is_top_or_bottom(self):
        if not self.scroll_view:
            return False

        val = getattr(self.scroll_view, f"scroll_{self.scale_axis}")
        return math.isclose(val, 1.0, abs_tol=1e-3) or math.isclose(
            val, 0.0, abs_tol=1e-3
        )

    def on_value(self, stencil, scroll_distance):
        super().on_value(stencil, scroll_distance)

        if self.target_widget:
            if not self.scroll_view or not self.scroll_scale:
                self.scroll_view = self.target_widget.parent
                self.scroll_scale = self.scroll_view._internal_scale

            if self.is_top_or_bottom():
                if (
                    abs(self.velocity) > self.minimum_absorbed_velocity
                    and self._should_absorb
                ):
                    self.absorb_impact()
                self._should_absorb = False
            else:
                self._should_absorb = True

    def get_hw(self):
        return "height" if self.scale_axis == "y" else "width"

    def set_scale_origin(self):
        if not self.scroll_view or not self.target_widget:
            return False

        if getattr(self.target_widget, self.get_hw()) < getattr(self.scroll_view, self.get_hw()):
            return False

        self.scroll_scale.origin = [
            self.scroll_view.right if self.scroll_view.scroll_x > 0.5 else self.scroll_view.x,
            self.scroll_view.top if self.scroll_view.scroll_y > 0.5 else self.scroll_view.y,
        ]
        return True

    def absorb_impact(self):
        if not self.set_scale_origin():
            return

        sanitized_velocity = self.clamp(abs(self.velocity), 1, self.maximum_velocity)
        new_scale = 1 + min((sanitized_velocity / self.approx_normailzer), 1 / 3)

        Animation.cancel_all(self.scroll_scale)

        anim = Animation(
            **{self.scale_axis: new_scale},
            d=(sanitized_velocity * 4) / 1e6,
            t="out_quad",
        )
        anim.bind(on_complete=self.reset_scale)
        anim.start(self.scroll_scale)

    def get_component(self, pos):
        return pos[-1 if self.scale_axis == "y" else 0]

    def convert_overscroll(self, touch):
        if not (self.scroll_view and self.is_top_or_bottom() and self.last_touch_pos):
            return

        if (
            getattr(self.scroll_view, f"do_scroll_{self.scale_axis}")
            and self.velocity == 0
        ):
            if self.set_scale_origin():
                current_pos = self.get_component(touch.pos)
                last_pos = self.get_component(self.last_touch_pos)
                scroll_size = getattr(self.scroll_view, self.get_hw())

                distance = abs(current_pos - last_pos) / scroll_size

                linear_intensity = self.stretch_intensity * distance
                exponential_intensity = self.stretch_intensity * (
                    1 - math.exp(-distance * self.exponential_scalar)
                )
                new_scale = 1 + exponential_intensity + linear_intensity

                new_scale = self.clamp(new_scale, 1.0, 1.3)
                setattr(self.scroll_scale, self.scale_axis, new_scale)

    def reset_scale(self, *args):
        if not self.scroll_scale:
            return

        _scale = getattr(self.scroll_scale, self.scale_axis)
        if _scale > 1.0:
            Animation.cancel_all(self.scroll_scale)
            anim = Animation(**{self.scale_axis: 1.0}, d=0.25, t="out_bounce")
            anim.start(self.scroll_scale)
