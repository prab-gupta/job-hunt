# TypeScript -> Python, for a live coding round

Bubble/N8N anchor first, then TS you know, then Python.

| Concept | Bubble / N8N | TypeScript | Python |
|---|---|---|---|
| Record / object | a Thing / one N8N item | `{name: "a", n: 1}` | `{"name": "a", "n": 1}` (dict) |
| Read field | Thing's name | `obj.name` | `obj["name"]` or `obj.get("name")` (no KeyError) |
| List | list of Things | `[1,2,3]` | `[1, 2, 3]` |
| Length | :count | `arr.length` | `len(arr)` |
| Loop | repeating group / Loop node | `for (const x of arr)` | `for x in arr:` |
| Loop with index | | `arr.forEach((x,i)=>)` | `for i, x in enumerate(arr):` |
| map | :each item's field | `arr.map(x => x*2)` | `[x*2 for x in arr]` |
| filter | :filtered | `arr.filter(x => x>1)` | `[x for x in arr if x > 1]` |
| find first | :first item | `arr.find(f)` | `next((x for x in arr if f(x)), None)` |
| sum | :sum | `reduce` | `sum(arr)` |
| sort | :sorted by | `arr.sort((a,b)=>a.n-b.n)` | `sorted(arr, key=lambda x: x["n"])` (`reverse=True` for desc) |
| unique | :unique elements | `new Set(arr)` | `set(arr)` (order lost) or `dict.fromkeys(arr)` (order kept) |
| group by | | manual reduce | `defaultdict(list)` then `groups[key].append(x)` |
| count occurrences | | manual | `Counter(arr)`, `.most_common(3)` |
| string join | :join with | `arr.join(",")` | `",".join(arr)` (strings only) |
| template | Insert dynamic data | `` `Hi ${n}` `` | `f"Hi {n}"` |
| null / empty | is empty | `null` / `undefined` | `None`; test with `is None` |
| truthy | | `if (x)` | `if x:` (empty list, "", 0, None are falsy) |
| and / or / not | | `&& \|\| !` | `and or not` |
| equality | | `===` | `==` (`is` only for None) |
| int division | :floor | `Math.floor(a/b)` | `a // b`, remainder `a % b` |
| increment | | `i++` | `i += 1` |
| function | reusable workflow | `function f(a, b=1) {}` | `def f(a, b=1):` |
| arrow fn | | `x => x+1` | `lambda x: x + 1` |
| try/catch | Error Trigger workflow | `try {} catch (e) {}` | `try: ... except KeyError as e: ...` |
| class | custom data type | `class A { constructor() }` | `class A:` with `def __init__(self, ...)` |
| typed record | data type with fields | `interface` | `@dataclass class Row: name: str; n: int = 0` |
| JSON | Parse JSON node | `JSON.parse(s)` / `JSON.stringify(o)` | `json.loads(s)` / `json.dumps(o)` |
| read file | | fs.readFileSync | `with open(p) as f: data = f.read()` |
| slice | :items from #a until #b | `arr.slice(1,3)` | `arr[1:3]` (end exclusive), `arr[-1]` last, `arr[::-1]` reversed |
| range | | `[...Array(n).keys()]` | `range(n)`, `range(1, n+1)` |
| dict loop | | `Object.entries(o)` | `for k, v in d.items():` |
| in | contains | `arr.includes(x)` / `k in obj` | `x in arr` / `k in d` |
| print | debug alert | `console.log` | `print(x)` |

## Traps for a TS brain
- Indentation IS the block. 4 spaces. No braces, colon at end of `if/for/def/class` line.
- `d["k"]` on missing key raises `KeyError`. Use `d.get("k", default)`.
- `for x in arr` gives values, not indexes.
- Mutable default arg `def f(x=[])` is shared across calls. Use `None` and create inside.
- `sorted()` returns new list, `arr.sort()` sorts in place and returns `None`.
- Strings are immutable. `s.upper()` returns new string.
- Integer math is exact and unbounded. `/` always gives float.
- snake_case for names. `True/False/None` capitalised.

## Live-round protocol (say it out loud)
1. Repeat the problem, ask about input shape and edge cases (empty, duplicates, None).
2. Write the signature and one example as an `assert` first.
3. Brute force that passes. Say "I will optimise if needed".
4. Run it. Then talk about complexity and what you would change.
