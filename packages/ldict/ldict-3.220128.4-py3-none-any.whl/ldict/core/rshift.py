#  Copyright (c) 2021. Davi Pereira dos Santos
#  This file is part of the ldict project.
#  Please respect the license - more about this in the section (*) below.
#
#  ldict is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  ldict is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with ldict.  If not, see <http://www.gnu.org/licenses/>.
#
#  (*) Removing authorship by any means, e.g. by distribution of derived
#  works or verbatim, obfuscated, compiled or rewritten versions of any
#  part of this work is illegal and unethical regarding the effort and
#  time spent here.
#
#  ldict is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  ldict is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with ldict.  If not, see <http://www.gnu.org/licenses/>.
#
#  (*) Removing authorship by any means, e.g. by distribution of derived
#  works or verbatim, obfuscated, compiled or rewritten versions of any
#  part of this work is illegal and unethical regarding the effort and
#  time spent here.
from inspect import signature
from types import FunctionType
from typing import Union

from lange import AP, GP

from ldict.core.inspection import (
    extract_dynamic_input,
    extract_output,
    extract_body,
    CodeExtractionException,
)
from ldict.core.inspection import extract_input
from ldict.exception import InconsistentLange, UndefinedSeed, DependenceException
from ldict.lazyval import LazyVal
from ldict.parameter.let import AbstractLet


def handle_dict(data, dictlike, rnd):
    """
    >>> from ldict import ldict
    >>> d = ldict(x=5, y=7, z=8)
    >>> di = handle_dict(d.frozen.data, {"y":None}, None)
    >>> di
    {'x': 5, 'z': 8}
    >>> handle_dict(di, {"w":lambda x,z: x**z}, None)
    {'x': 5, 'z': 8, 'w': →(x z)}
    """
    data = data.copy()
    for k, v in dictlike.items():
        if v is None:
            del data[k]
        else:
            from ldict.core.ldict_ import Ldict

            if callable(v):
                if (r := lazify(data, k, v, rnd, is_multi_output=False)) is not None:
                    data[k] = r
            elif isinstance(v, Ldict):
                data[k] = v.frozen
            else:
                data[k] = v
    return data


def lazify(data, output_field: Union[list, str], f, rnd, is_multi_output) -> Union[dict, LazyVal]:
    """Create lazy values and handle metafields.
    >>> from ldict import ldict, let
    >>> from random import Random
    >>> (d := ldict(x=5) >> Random(0) >> (lambda x, a=1, b=[1, 2, 3, ... , 8]: {"y": a*x + b, "_parameters": ...}))
    {
        "x": 5,
        "y": "→(a b x)",
        "_parameters": {
            "a": 1,
            "b": 7
        }
    }
    >>> d.y
    12
    >>> d = ldict(x=5) >> Random(0) >> let(
    ...     (lambda x, a=1, b=[1, 2, 3, ... , 8]: {"y": a*x + b, "_parameters": ...}),
    ...     a=3, b=5
    ... )
    >>> d
    {
        "x": 5,
        "y": "→(a b x)",
        "_parameters": {
            "a": 3,
            "b": 5
        }
    }
    >>> d.y
    20
    >>> def f(input="a", output="b", **kwargs):
    ...     return {output: kwargs[input], "_history": ...}
    >>> f.metadata = {"id": "fffffff----------------------------fffff",
    ...             "name": "f",
    ...             "description": "Copy.",
    ...             "code": ...,
    ...             "parameters": ...}
    >>> d = ldict(a=5) >> let(f, output="b")
    >>> d.b
    5
    >>> d
    {
        "a": 5,
        "b": 5,
        "_history": {
            "fffffff----------------------------fffff": {
                "name": "f",
                "description": "Copy.",
                "code": "def f(input='a', output='b', **kwargs):\\nreturn {output: kwargs[input], '_history': ...}",
                "parameters": {
                    "input": "a",
                    "output": "b"
                }
            }
        }
    }
    >>> def f(input=["a", "b"], output=None, **kwargs):
    ...     return {output: kwargs[input[0]] * kwargs[input[1]]}
    >>> d = ldict(a=5, b=7) >> let(f, output="c")
    >>> d.c
    35
    >>> d
    {
        "a": 5,
        "b": 7,
        "c": 35
    }
    """

    """
    >>> def f(input=["a", "b"], output=None, **kwargs):
    ...     return {kwargs[output[0]]: kwargs[input[0]], kwargs[output[1]]: kwargs[input[1]]}
    >>> d = ldict(a=5, b=7) >> let(f, output=["c", "d"])
    >>> d.c
    35
    >>> d
    {
        "a": 5,
        "b": 7,
        "c": 35
    }
    """
    # TODO (minor): simplify to improve readability of this function
    config, f = (f.config, f.f) if isinstance(f, AbstractLet) else ({}, f)
    input_fields, parameters, optional = extract_input(f)
    noop = False
    if "_" in input_fields:
        noop = True
        del input_fields["_"]
        if isinstance(f, AbstractLet):  # pragma: no cover
            raise Exception("Cannot let parameters have values for a noop function")
    for k, v in config.items():
        parameters[k] = v
    if isinstance(f, FunctionType):
        try:
            body = extract_body(f)
        except CodeExtractionException as e:
            body = f"<{e}>"
        dynamic_input = extract_dynamic_input("".join(body))
    else:
        body = None
        if not (hasattr(f, "metadata") and "input" in f.metadata and "output" in f.metadata):  # pragma: no cover
            raise Exception(f"Missing 'metadata' containing 'input' and 'output' keys for custom callable '{type(f)}'")
        dynamic_input = []
    dynamic_output = []
    if hasattr(f, "metadata"):
        if not dynamic_input and "input" in f.metadata and "dynamic" in f.metadata["input"]:
            dynamic_input = f.metadata["input"]["dynamic"]
        if "output" in f.metadata and "dynamic" in f.metadata["output"]:
            dynamic_output = f.metadata["output"]["dynamic"]

    # Process dynamic_input.
    multidynamicinput = set()
    for par in dynamic_input:
        if par not in parameters:  # pragma: no cover
            raise Exception(f"Parameter '{par}' value is not available:", parameters)
        if parameters[par] == "[]":
            parameters[par] = []
        if isinstance(parameters[par], list):
            for k in parameters[par]:
                input_fields[k] = None
            multidynamicinput.add(par)
        elif isinstance(parameters[par], dict):
            for k in parameters[par]:
                input_fields[k] = None
            multidynamicinput.add(par)
        else:
            input_fields[parameters[par]] = None

    dynio = multidynamicinput | set(dynamic_output)
    deps = prepare_deps(data, input_fields, parameters, rnd, dynio, optional)
    for k, v in parameters.items():
        parameters[k] = deps[k]
    if noop:

        def la(**deps_out):
            f(**deps_out)
            return deps_out

        lazies = []
        # REMINDER: noop uses input fields as output
        dic = {k: LazyVal(k, la, deps, data, lazies) for k in input_fields}
        lazies.extend(dic.values())
        deps["_"] = None
        return dic

    newidx = 0
    if hasattr(f, "metadata"):
        step = f.metadata.copy()
        if "id" in step:
            newidx = step.pop("id")
            if "_" in newidx:  # pragma: no cover
                raise Exception(f"'id' cannot have '_': {newidx}")
        for k in ["input", "output", "function"]:
            if k in step:
                del step[k]
        if "code" in f.metadata and f.metadata["code"] is ...:
            if body is None:  # pragma: no cover
                raise Exception(f"Cannot autofill 'metadata.code' for custom callable '{type(f)}'")
            head = f"def f{str(signature(f))}:"
            code = head + "\n" + "\n".join(body)
            f.metadata["code"] = code
            step["code"] = code
        if "parameters" in f.metadata and f.metadata["parameters"] is ...:
            step["parameters"] = parameters
        if "function" in f.metadata and f.metadata["function"] is ...:
            # REMINDER: it is not clear yet whether somebody wants this...
            if hasattr(f, "pickle_dump"):
                f.metadata["function"] = f.pickle_dump
            else:
                import dill

                dump = dill.dumps(f, protocol=5)
                f.metadata["function"] = dump
                f.pickle_dump = dump  # Memoize
    else:
        step = {}
    if output_field == "extract":
        explicit, meta, meta_ellipsed = extract_output(f, body, deps, is_multi_output, dynamic_output)
        lazies = []
        dic = {k: LazyVal(k, f, deps, data, lazies) for k in explicit + meta}
        lazies.extend(dic.values())
        for metaf in meta_ellipsed:
            if metaf == "_code":
                if hasattr(f, "metadata") and "code" in f.metadata:
                    dic["_code"] = f.metadata["code"]
                else:
                    if body is None:  # pragma: no cover
                        raise Exception(f"Missing 'metadata' containing 'code' key for custom callable '{type(f)}'")
                    head = f"def f{str(signature(f))}:"
                    dic["_code"] = head + "\n" + "\n".join(body)
            elif metaf == "_parameters":
                dic["_parameters"] = parameters
            elif metaf == "_function":
                # REMINDER: it even more unclear whether somebody wants this...
                if hasattr(f, "pickle_dump"):
                    dic["_function"] = f.pickle_dump
                else:
                    import dill

                    dump = dill.dumps(f, protocol=5)
                    dic["_function"] = dump
                    f.pickle_dump = dump  # Memoize
            elif metaf == "_history":
                if "_history" in data:
                    if isinstance(data["_history"], LazyVal):
                        data["_history"] = data["_history"]()
                    last = list(data["_history"].keys())[-1]
                    if isinstance(last, int):
                        newidx = last + 1
                    elif newidx == 0:
                        newidx = ...
                    dic["_history"] = data["_history"].copy()
                else:
                    dic["_history"] = {}
                dic["_history"][newidx] = step
            else:  # pragma: no cover
                raise Exception(f"'...' is not defined for '{metaf}'.")
        return dic
    else:
        return LazyVal(output_field, f, deps, data, None)


def prepare_deps(data, input, parameters, rnd, multi, optional):
    """Build a dict containing all needed dependencies (values) to apply a function:
        input fields and parameters.

    Parameter values are given in let() or sampled according to a range using a random number generator that provides a 'choice' method.
    A range is specified as the default value of the parameter in the function signature.
    """
    deps = {}
    for k, v in parameters.items():
        # TODO existence of multidynamic output is raising exception here
        #  because it will only be extracted at the end of lazify
        #  A workaround is to declare multidynamic output at f.metadata, instead of detecting it.
        if isinstance(v, list) and k not in multi and k not in optional:
            if rnd is None:
                raise UndefinedSeed(
                    "\nMissing Random object (or some object with the method 'choice') "
                    "before parameterized function application.\n"
                    "Example: ldict(x=5) >> Random(42) >> (lambda x, a=[1,2,3]: {'y': a * x**2})\n"
                    f"field={k}\n"
                    f"values={v}\n{parameters=}\n{multi=}\n"
                    f"Another possible cause: Multidynamic output cannot be detected by now, "
                    f"please declare multidynamic output at f.metadata['output']"
                )
            deps[k] = rnd.choice(expand(v))
        elif v is None:
            raise DependenceException(f"'None' value for parameter '{k}'.", deps.keys())
        else:
            deps[k] = v
    for k in input:
        if k in data:
            deps[k] = data[k]
        if k not in optional:
            if k not in deps:
                raise DependenceException(f"Missing field '{k}'.", data.keys())
            if deps[k] is None:
                raise DependenceException(f"'None' value for field '{k}'.", data.keys())
    return deps


def expand(lst):
    """Evaluate list representing A. or G. progression

    >>> expand([1,2,3,...,9])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> expand([1,2,4,...,20])
    [1, 2, 4, 8, 16]

    Parameters
    ----------
    lst

    Returns
    -------

    """
    return list(list2progression(lst)) if Ellipsis in lst else lst


def list2progression(lst):
    """Convert list representing A. or G. progression to lange

    >>> list2progression([1,2,3,...,9])
    [1 2 .+. 9]
    >>> list2progression([1,2,4,...,16])
    [1 2 .*. 16]

    Parameters
    ----------
    lst

    Returns
    -------

    """
    # TODO move this to lange package
    try:
        diff1 = lst[1] - lst[0]
        diff2 = lst[2] - lst[1]
        ratio1 = lst[1] / lst[0]
        ratio2 = lst[2] / lst[1]
    except:
        raise InconsistentLange(f"Cannot identify whether this is a G. or A. progression: {lst}")
    newlst = [lst[0], lst[1], ..., lst[-1]]
    if diff1 == diff2:
        return AP(*newlst)
    elif ratio1 == ratio2:
        return GP(*newlst)
    else:
        raise InconsistentLange(f"Cannot identify whether this is a G. or A. progression: {lst}")
