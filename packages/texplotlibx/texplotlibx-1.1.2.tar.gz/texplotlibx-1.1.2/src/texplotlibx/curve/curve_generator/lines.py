from .curve_generator import _tpl_curve_generator


class _tpl_curve_generator_lines(_tpl_curve_generator):
  _identifiers = (
    "lines",
    "line",
    "continuous"
  )

  def _get_draw(self):
    color = "=%s" % self.curve.color.get_value() if self.curve.color.get_value() is not None else ""
    return "draw%s," % color

  def _get_marks_active(self):
    return "no marks,"
