import typing as _tp
from .models import ParamOpts
from .engines import tableized as tableized_e


_parametrized = ParamOpts.width, ParamOpts.poly, ParamOpts.seed, ParamOpts.xor, ParamOpts.refin, ParamOpts.refout

# generic/standard/parametrized
generic = *_parametrized,

tableized = ParamOpts.table, *_parametrized

# naive/simple
naive = *_parametrized,

DEFAULT_ENGINE = tableized_e


def new(
        width: int = None, poly: int = None,
        init: int = None, xorout: int = None,
        refin: (bool, int) = None, refout: (bool, int) = None,
        # desc
        name: str = None, aliases: _tp.Sequence[str] = None, desc: str = None,
        # table
        table=None,
        # checks
        check=None,
        residue=None,
):
    r = {
        ParamOpts.width: width, ParamOpts.poly: poly,
        ParamOpts.seed: init, ParamOpts.xor: xorout,
        ParamOpts.refin: refin, ParamOpts.refout: refout,
        ParamOpts.name: name, ParamOpts.aliases: aliases, ParamOpts.desc: desc,
        ParamOpts.table: table,
        ParamOpts.check: check, ParamOpts.residue: residue,
    }
    return dict((k, v) for k, v in r.items() if v is not None)


class Calculator:
    class Calculation:
        def __init__(self, calculator):
            self.calculator = calculator
            self._init = calculator.init
            self._process = calculator.process
            self._final = calculator.final
            self.value = calculator.init()

        def __repr__(self):
            return f""

        def process(self, data):
            self.value = r = self._process(self.value, data)
            return r

        def final(self) -> int:
            return self._final(self.value)

    def __init__(self, init, process, final):
        self.init = init
        self.process = process
        self.final = final

    def __repr__(self):
        return f""

    def __call__(self, *args, **kwargs):
        return self.Calculation(self)

    def calc(self, data) -> int:
        return self.final(self.process(self.init(), data))


def create(params, engine=DEFAULT_ENGINE) -> Calculator:
    init, process, final = engine.new(params)
    r = Calculator(init, process, final)
    return r
