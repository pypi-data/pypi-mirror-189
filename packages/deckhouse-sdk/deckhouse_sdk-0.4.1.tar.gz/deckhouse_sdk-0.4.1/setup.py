# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['deckhouse_sdk']

package_data = \
{'': ['*']}

install_requires = \
['dictdiffer>=0.9.0,<0.10.0']

setup_kwargs = {
    'name': 'deckhouse-sdk',
    'version': '0.4.1',
    'description': 'Python SDK for Shell Operator hooks',
    'long_description': '# Deckhouse module SDK\n\nDeckhouse module SDK simplifies writing module hooks for operators:\n\n- [Deckhouse](https://github.com/deckhouse/deckhouse)\n- [Addon Operator](https://github.com/flant/addon-operator)\n- [Shell Operator](https://github.com/flant/shell-operator) (values are unaccessable)\n\n**NOTE**:\n- The API is in alpha stage\n\n\n## Install\n\n```bash\npip install deckhouse-sdk\n```\n\n## Sample hook\n\n```python\n# hello.py\nfrom deckhouse_sdk import hook\n\ndef main(ctx: hook.Context):\n    # Manipulate kubernetes state\n    # ... object = { "kind" : "Pod", "apiVersion" : "v1", ... }\n    ctx.kubernetes.create_or_update(object)\n\n    # Export metrics\n    # ... metric = { "name" : "power", "group": "my_hook", "set" : 9000, ... }\n    ctx.metrics.collect(metric)\n\n    # Use in-memory values for helm chart. Shell Operator does not support values, but Addon Operator and Deckhouse do.\n    ctx.values.myModule.deployment.replicas = 5\n\n\nif __name__ == "__main__":\n    hook.run(main, configpath="hello.yaml") # \'config\' arg is also supported for raw string\n```\n\n```yaml\n# hello.yaml\nconfigVersion: v1\nonStartup: 10\n```\n\n## How to test\n\nAn example for pytest\n\n```python\n# hello_test.py\n\nfrom hello import main\nfrom deckhouse_sdk import hook\n\n# Inputs\n#   initial_values = { ... }\n#   binding_context = [ { ... } ]\n# Outputs\n#   expected_metrics = [ ... ]\n#   expected_kube_operations = [ ... ]\n#   expected_values_patches = [ ... ]\n#   expected_values = { ... }\n\ndef test_hello():\n    out = hook.testrun(main, binding_context, initial_values)\n\n    assert out.metrics.data == expected_metrics\n    assert out.kube_operations.data == expected_kube_operations\n    assert out.values_patches.data == expected_values_patches\n\n    assert out.values.myModule.deployment.repicas == 5\n```\n',
    'author': 'Eugene Shevchenko',
    'author_email': 'evgeny.shevchenko@flant.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.2,<4.0.0',
}


setup(**setup_kwargs)
