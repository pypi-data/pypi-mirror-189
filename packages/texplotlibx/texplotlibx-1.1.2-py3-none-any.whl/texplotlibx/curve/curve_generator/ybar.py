from .curve_generator import _tpl_curve_generator


class _tpl_curve_generator_ybar(_tpl_curve_generator):
  _identifiers = (
    "bar",
    "ybar",
    "hist",
    "histogram"
  )

  def _get_fill(self):
    color = "=%s" % self.curve.color.get_value() if self.curve.color.get_value() is not None else ""
    return "fill%s,\n  fill opacity=0.3," % color

  def _get_draw(self):
    color = "=%s" % self.curve.color.get_value() if self.curve.color.get_value() is not None else ""
    return "draw%s,\n  draw opacity=0.7," % color

  def _get_errdraw(self):
    return self._get_draw()

  def _get_type(self):
    return "ybar,"

  def _get_marks_active(self):
    return "no marks,"

  def _get_legend_type(self):
    return "ybar legend,"


class _tpl_curve_generator_ybarinterval(_tpl_curve_generator_ybar):
  _identifiers = (
    "interval",
    "ybar interval"
  )

  def _get_type(self):
      return "ybar interval,"
