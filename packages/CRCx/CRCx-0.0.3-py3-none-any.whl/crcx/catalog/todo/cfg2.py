import itertools
import lxml
import lxml.etree
from lxml import etree
import io
import chardet
from lxml import html
import typing as _tp


PATH = r"D:\users\DAS\Mega\Projects\Lib\py\modules\crc\research" \
	r"\Catalogue of parametrised CRC algorithms (1_16_2023 10_43_56 PM).html"


with open(PATH, "rb") as FD:
	HTML_B = FD.read()

# x = chardet.detect(HTML_B)
# print(x)
HTML = HTML_B.decode("utf-8")


def concat(*its):
	"""joins iterables together"""
	for it in its:
		yield from it


def apply(fns):
	def f(it):
		return (fn(x) for fn, x in zip(fns, it))
	return f


def select_els(doc):
	xp = r"/html/body/p/code"
	els = doc.xpath(xp)
	for el in els:
		yield el


def parse_param(s):
	return s.split("=")


def bool_s(s: str):
	s = s.strip().lower()
	if s == "false":
		return False
	if s == "true":
		return True
	return None


class Params(_tp.NamedTuple):
	name: str
	width: int
	poly: int
	init: int
	xorout: int
	refin: bool
	refout: bool
	check: int
	residue: int


def parse_params(text: str):
	params = text.strip().split(" ")
	params = (parse_param(param) for param in params if len(param))
	params = Params(**dict(params))
	params = Params(*apply((eval, int, eval, eval, eval, bool_s, bool_s, eval, eval))(params))
	return params


def get_params(els):
	return (parse_params(el.text) for el in els)


def ssv(tab_stops, sep_char=" ", min_sep=2):
	def f(strs):
		def g():
			i = 0
			for tab_stop, s in zip(tab_stops, strs):
				whitespace_len = max(tab_stop - i, min_sep if i else 0)
				yield from (sep_char for _ in range(whitespace_len))  # negative range is same as zero
				yield s
				i += whitespace_len + len(s)
		return "".join(g())
	return f


class Fn:
	def __new__(cls, fn):
		def f(*args, **kwargs):
			return fn(*args, **kwargs)
		return f


def fjoin(*fns):
	def f(x):
		for fn in reversed(fns):
			x = fn(x)
		return x
	return f


def split_line(line: str):
	line = line.expandtabs(4).strip()
	cols = line.split(" ")
	cols = (col for col in cols if col)
	return cols





def is_comment(s: str):
	return s[:1] == "#"


def trunc_at(pred):
	def f(it):
		for x in it:
			if pred(x):
				break
			yield x

	return f


def cfg_loads(raw: str):
	col_maps = (str, eval, eval, eval, eval, eval, eval, eval, eval)
	lines = raw.split("\n")
	lines = filter(len, (
			tuple(
				apply(col_maps)(
					trunc_at(is_comment)(split_line(line))
				))
			for line in lines
		))
	return lines


def cfg_load(fp):
	with open(fp) as fd:
		lines = cfg_loads(fd.read())
	return lines


def cfg_dumpl(lines):
	col_maps = (str, str, hex, hex, hex, str, str, hex, hex)
	lines = tuple(concat(
		(("#AlgorithmName", "Width", "Poly", "XorIn", "XorOut", "RefIn", "RefOut", "Check", "Residue"), ),
		map(fjoin(tuple, apply(col_maps)), lines),
	))

	col_lens = [0] * len(col_maps)
	for line in lines:
		col_lens = (max(a, b) for a, b in zip(map(len, line), col_lens))

	tab_stops = ((0, ) + tuple(x + 2 for x in col_lens)[:-1])
	tab_stops = tuple(itertools.accumulate(tab_stops))

	lines = (ssv(tab_stops)((str(x) for x in line)) for line in lines)
	return lines


def cfg_dumps(lines):
	lines = cfg_dumpl(lines)
	return "\n".join(lines)


def cfg_dump(fp, lines):
	with open(fp, "w") as fd:
		fd.write(cfg_dumps(lines))
	return lines


def main():
	# write
	parser = etree.HTMLParser()
	doc = etree.parse(io.StringIO(HTML), parser)
	paramsets = tuple(get_params(select_els(doc)))

	fp = r"D:\users\DAS\Mega\Projects\Lib\py\modules\crc\lib\crc_rc2\catalog\cfg2.txt"

	raw = cfg_dumps(paramsets)
	cfg_dump(fp, paramsets)

	print(raw)


def main2():
	# read
	fp = r"D:\users\DAS\Mega\Projects\Lib\py\modules\crc\lib\crc_rc2\catalog\cfg2.txt"
	lines = cfg_load(fp)
	raw = cfg_dumps(lines)
	print(raw)


if __name__ == '__main__':
	main2()
