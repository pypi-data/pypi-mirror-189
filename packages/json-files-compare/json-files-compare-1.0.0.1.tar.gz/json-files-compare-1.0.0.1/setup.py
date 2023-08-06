# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['json_compare']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'json-files-compare',
    'version': '1.0.0.1',
    'description': 'Simple but powerfull JSON-files comparator',
    'long_description': '# json-compare\nJson-compare is a simple package that allows you to easily and fastly compare two .json files. Support key and multi-key comparison.\nYou can also ignore certain fields\' values or perform comparison insensitive to data types.\n\n[![made-with-python](https://img.shields.io/badge/python-3.10%2B-brightgreen)](https://www.python.org/)\n\nUsage\n---\nCompare files just as they are:\n\n```python\nfrom json_compare import JSONComparator\n\ncomparator = JSONComparator(\n    left_file_path="expected.json",\n    right_file_path="actual.json",\n)\n\n# compare "actual.json" from the perspective of "expected.json"\'s structure\ncomparator.compare_with_right()  # / compare_with_left() / full_compare()\n\n# save diff logs to ".comparison_logs" folder\ncomparator.save_diff_logs(path="comparison_logs")\n\n# or print them into stdout\ndiffs = comparator.diff_log.log\nprint("\\n".join(diffs))\n\n# or print only summary. Here\'s an example:\n---------------------\nTOTAL: 4 differences\n-missing_obj_property: 3\n-unequal_value: 4\n```\nSet key property to perform more accurate comparisons of objects in arrays:\n\n```python\n# expected.json: {"cats": [{"id": 4, "name": "Nyan"}, {"id": 2, "name": "Marx"}, {"id": 8, "name": "Flake"}]}\n# actual.json: {"cats": [{"id": 2, "name": "Marx"}, {"id": 4, "name": "Naan"}]}\n\ncomparator = JSONComparator(\n    left_file_path="expected.json",\n    right_file_path="actual.json",\n    key="DATA//cats//<array>//id",  # <----- just pass a "path" to needed property with following keywords: \n)                                            # DATA - points to the root of file \n                                             # <array> - indicates array with key property\'s object\n```\nIn this case, saved diff log would look like that:\n```text\nactual.json//cats//<array>\nlack of items in array: expected 3 items, got only 2\nactual.json//cats//<array>//[0]//name\nunequal values: expected "Nyan", got "Naan" instead\nactual.json//cats//<array>//[2]\nmissing array item: expected <object> with "id"=8\n```\nYou can go further and add non-important fields to `ignore` parameter:\n```python\n# expected.json: [{"id": 4, "name": "Nyan", "age": 2}, {"id": 2, "name": "Marx", "age": 7}, {"id": 8, "name": "Flake", "age": 4}]\n# actual.json: [{"id": 2, "name": "Marx", "age": 7}, {"id": 4, "name": "Naan", "age": "two"}, {"id": 9, "name": "Lol", "age": 1}]\n\ncomparator = JSONComparator(\n    left_file_path="expected.json",\n    right_file_path="actual.json",\n    key="DATA//<array>//id",\n    ignore="DATA//<array>//age"  # <-------\n)  \n```\nAnd here the result:\n```text\nactual.json//<array>//[0]//name\nunequal values: expected "Nyan", got "Naan" instead\nactual.json//<array>//[2]\nmissing array item: expected <object> with "id"=8\n```\nIf you want to compare ignoring type-differences between similar values\n like `"1.4"` vs `1.4` or `"[\\"New Age №1\\"]"` vs `["New Age №1"]` - just add `ignore_types=True` \n param to JSONComparator:\n```python\ncomparator = JSONComparator(\n    left_file_path="expected.json",\n    right_file_path="actual.json",\n    key="DATA//<array>//id",\n    ignore_types=True,  # <-------\n)  \n```',
    'author': 'Alexey Novikov',
    'author_email': 'lexutka@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
