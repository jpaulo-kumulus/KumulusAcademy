import json
j1 = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
print(j1)

print(json.dumps("\"foo\bar"))

print(json.dumps('\u1234'))

print(json.dumps('\\'))

print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))

from io import StringIO
io = StringIO()
json.dump(['streaming API'], io)
print(io.getvalue())

# ***************************************************************************************

print(json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':')))

# ***************************************************************************************

print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))

# **************************************************************************************

print(json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]'))

print(json.loads('"\\"foo\\bar"'))

from io import StringIO
io = StringIO('["streaming API"]')
print(json.load(io))

# **************************************************************************************

def as_complex(dct):
    if '__complex__' in dct:
        return complex(dct['real'], dct['imag'])
    return dct

print(json.loads('{"__complex__": true, "real": 1, "imag": 2}',
    object_hook=as_complex))

import decimal
print(json.loads('1.1', parse_float=decimal.Decimal))

# ***************************************************************************************

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return [obj.real, obj.imag]
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)

print(json.dumps(2 + 1j, cls=ComplexEncoder))

print(ComplexEncoder().encode(2 + 1j))

print(list(ComplexEncoder().iterencode(2 + 1j)))

# *****************************************************************************************

