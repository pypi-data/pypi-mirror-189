from collections.abc import Iterable
import csv
import subprocess

from .annotations.label import _tpl_label
from .curve.curve import _tpl_curve
from .annotations.legend import _tpl_legend
from .strutils import _savetext, _compactify
from .logmodes import _tpl_logmodes
from .annotations.ticklabel import _tpl_ticklabel
from .cycle_list import _tpl_cycle_list
from .limits import _tpl_limits
from .attribute import _tpl_attribute_variable
from .annotations.annotation import _tpl_annotation


class figure:
  PDF_COMPILE_CMD = "pdflatex -halt-on-error -interaction nonstopmode TEXFILE | grep '^!.*' -A200 --color=always"

  def __init__(self, figsize: tuple = None, name: str = None):
    if figsize is None:
      figsize = (8, 5)
    self.__name: str = name if name is not None else 'tplaxis'
    self.__figsize: tuple = figsize
    self.__curves: list[_tpl_curve] = []
    self.__xlabel: _tpl_label = _tpl_label(token="xlabel")
    self.__ylabel: _tpl_label = _tpl_label(token="ylabel")
    self.__xticklabel: _tpl_ticklabel = _tpl_ticklabel("x")
    self.__yticklabel: _tpl_ticklabel = _tpl_ticklabel("y")
    self.__legend: _tpl_legend = _tpl_legend()
    self.__type: str = "xy"
    self.__logmodes: _tpl_logmodes = _tpl_logmodes()
    self.__additional_axis_cmds: list[str] = []
    self.__cycle_list: _tpl_cycle_list = _tpl_cycle_list("multi")
    self.__limits: _tpl_limits = _tpl_limits()
    self.__title: _tpl_attribute_variable = _tpl_attribute_variable(token="title")
    self.__annotations: _tpl_annotation = []

  def plot(self, x: Iterable, y: Iterable, xerror: Iterable = None, yerror: Iterable = None,
           *args, **kwargs):
    if len(x) != len(y):
      print("x and y must be of same length (%d != %d)" % (len(x), len(y)))
      return
    self.__curves.append(_tpl_curve(x, y, xerror, yerror, *args, **kwargs))

  def plotcsv(self, filename: str, xcolname: str, ycolname: str, xerrcolname: str = None, yerrcolname: str = None,
              *args, **kwargs):
    with open(filename, "r") as f:
      csvreader = csv.reader(f)
      data = dict()
      for d in list(map(list, zip(*([x for x in csvreader if x != []])))):
        data[d[0]] = d[1:]

      def error(axis: str, v: str):
        print("Cannot find %s-key \"%s\" in csv file %s" % (axis, v, filename))
        print("Found the following data:")
        print(data)
      if xcolname not in data.keys():
        error("x", xcolname)
        return
      if ycolname not in data.keys():
        error("y", ycolname)
        return
      if xerrcolname is not None and xerrcolname not in data.keys():
        error("x error", xerrcolname)
        return
      if yerrcolname is not None and yerrcolname not in data.keys():
        error("y error", yerrcolname)
        return
      xerr = data[xerrcolname] if xerrcolname in data.keys() else None
      yerr = data[yerrcolname] if yerrcolname in data.keys() else None

      self.__curves.append(_tpl_curve(data[xcolname], data[ycolname], xerr, yerr, *args, **kwargs))

  def savefig(self, filename: str):
    DEFAULT_SUFFIX = "tex"
    splitfile = filename.split(".")
    suffix = splitfile[-1] if len(splitfile) != 1 else None
    if suffix is None:
      suffix = DEFAULT_SUFFIX
      filename += "." + DEFAULT_SUFFIX
      print(f"No file-suffix specified. Assuming {DEFAULT_SUFFIX}.")
    if suffix.lower() == "tex":
      texstr = self.__create_tex()
      _savetext(filename, texstr)
    elif suffix.lower() == "tikz":
      tikzstr = self.__create_tikz()
      _savetext(filename, tikzstr)
    elif suffix.lower() == "pdf":
      texfilename = ".".join(filename.split(".")[:-1]) + ".tex"
      texstr = self.__create_tex()
      _savetext(texfilename, texstr)
      subprocess.run(self.__class__.PDF_COMPILE_CMD.replace("TEXFILE", texfilename).split())
    else:
      print("File type \"%s\" not supported!" % suffix)

  def set_xlabel(self, label: str):
    self.__xlabel.text.set_value(label)

  def set_ylabel(self, label: str):
    self.__ylabel.text.set_value(label)

  def set_title(self, title: str):
    fulltitle = '{' + title + '}' if title is not None else None
    self.__title.set_value(fulltitle)

  def set_xprecision(self, precision: int):
    self.__xticklabel._set_precision(precision)
    self.set_fixed_x_ticks(True)

  def set_yprecision(self, precision: int):
    self.__yticklabel._set_precision(precision)
    self.set_fixed_y_ticks(True)

  def set_fixed_x_ticks(self, fixed: bool = True):
    self.__xticklabel._set_fixed(fixed)
    self.__xticklabel._set_zerofill(fixed)

  def set_fixed_y_ticks(self, fixed: bool = True):
    self.__yticklabel._set_fixed(fixed)
    self.__yticklabel._set_zerofill(fixed)

  def set_scaled_x_ticks(self, scaled_ticks: bool = True):
    self.__xticklabel._set_scaled(scaled_ticks)

  def set_scaled_y_ticks(self, scaled_ticks: bool = True):
    self.__yticklabel._set_scaled(scaled_ticks)

  def set_x_ticks(self, data: list[float] = None):
    self.__xticklabel._set_ticks(data)

  def set_y_ticks(self, data: list[float] = None):
    self.__yticklabel._set_ticks(data)

  def set_x_ticks_from_data(self, use_data: bool = True):
    self.__xticklabel._set_ticks_use_data(use_data)

  def set_y_ticks_from_data(self, use_data: bool = True):
    self.__yticklabel._set_ticks_use_data(use_data)

  def set_x_tick_labels(self, labels: list[str] = None):
    self.__xticklabel._set_tick_labels(labels)

  def set_y_tick_labels(self, labels: list[str] = None):
    self.__yticklabel._set_tick_labels(labels)

  def set_xlim(self, left: float = None, right: float = None):
    self.__limits.set_xlim(left, right)

  def set_ylim(self, left: float = None, right: float = None):
    self.__limits.set_ylim(left, right)

  def set_legend_position(self, pos: str):
    self.__legend._set_position(pos)

  def set_plottype(self, type: str = 'xy', idx: int = -1):
    self.__curves[idx]._set_plottype(type)

  def set_logmode(self, mode: str = None):
    self.__logmodes.set_mode(mode)

  def add_axis_command(self, cmd: str):
    self.__additional_axis_cmds.append(cmd)

  def repeat_style(self, ntimes: int = None):
    self.__cycle_list.repeat_style(ntimes)

  def add_annotation(self, pos: str, label: str, xshift: str = None, yshift: str = None):
    self.__annotations.append(_tpl_annotation(pos, label, self.__name, xshift, yshift))

  def __create_tex(self):
    preable_cmd = """\\documentclass[tikz]{standalone}\n
\\usepackage{pgfplots}
\\pgfplotsset{compat=newest}\n
\\begin{document}\n\n"""

    tikz_cmd = self.__create_tikz(True)

    end_cmd = "\n\\end{document}"

    return preable_cmd + tikz_cmd + end_cmd

  def __create_tikz(self, include_begintikz: bool = True):
    begintikz_cmd = "\\begin{tikzpicture}\n" if include_begintikz else ""

    body_cmd = f"""\\begin{{axis}}[
  name={self.__name},
  label style={{
    font=\\large
  }},
  {self.__xlabel.text}
  {self.__ylabel.text}
  tick label style={{
    font=\\large
  }},
  {self.__title}
  {self.__xticklabel}
  {self.__yticklabel}
  {self.__legend.pos}
  legend cell align={{left}},
  grid=minor,
  grid style=dotted,
  scale only axis,
  {self.__logmodes.x}
  {self.__logmodes.y}
  {self.__limits}
  {self.__cycle_list}"""
    body_cmd += ''.join(["\n  " + x + "," for x in self.__additional_axis_cmds])
    body_cmd += "\n]\n\n"

    plot_cmd = [c._get_addplot_code() for c in self.__curves]

    post_cmd = "\n\\end{axis}\n"

    annotations = "".join(str(a) + "\n" for a in self.__annotations)

    endtikz_cmd = "\\end{tikzpicture}\n" if include_begintikz else ""

    return begintikz_cmd \
      + body_cmd \
      + "\n".join([_compactify(pc) for pc in plot_cmd]) \
      + post_cmd \
      + annotations \
      + endtikz_cmd
