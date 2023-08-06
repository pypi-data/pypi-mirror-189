# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['misprint']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'misprint',
    'version': '0.1.1',
    'description': "A logging filter that 'misprints' your secrets",
    'long_description': 'misprint\n========\n\nA logging filter that hides your secrets. Integrates with Python\'s ``logging`` module.\n\nInstallation\n------------\n\n.. code-block:: bash\n\n    pip install misprint\n\nUsage\n-----\n\n``misprint.Misprinter``\n"""""""""""""""""""""""\n\n\nYou can use the ``Misprinter`` class to redact exact string matches or regular expressions\nwithin a string:\n\n.. code-block:: python\n\n    misprinter = Misprinter(token=["my_secret_token", re.compile(r"^ghp_\\w+")])\n\n    assert misprinter.mask("this is my_secret_token") == "this is ****"\n    assert (\n        misprinter.make("github tokens: ghp_abc123 ghp_def456")\n        == "github tokens: **** ****"\n    )\n\nIf you need to add a mask for new data to an existing instance then you can use the\n``add_mask_for`` method:\n\n.. code-block:: python\n\n    misprinter = Misprinter()\n    assert misprinter.mask("a secret1234") == "a secret1234"\n\n    misprinter.add_mask_for("secret1234")\n    assert misprinter.mask("a secret1234") == "a ****"\n\nYou can also initialise your ``Misprinter`` instance with ``use_named_masks=True`` if you would\nlike to be able to identify what data has been masked more easily:\n\n.. code-block:: python\n\n    misprinter = Misprinter(use_named_masks=True)\n    misprinter.add_mask_for("another_secret", name="database password")\n\n    assert (\n        misprinter.mask("printing another_secret")\n        == "printing <\'database password\' (value removed)>"\n    )\n\n``misprint.MisprintFilter``\n"""""""""""""""""""""""""""\n\n``misprint`` also provides a ``logging.Filter`` subclass, which integrates with the\nPython standard library\'s ``logging`` module to enable redaction of log messages.\n\n``MisprintFilter`` is a subclass of ``Misprinter``, so inherits all of the methods detailed above.\nThis is useful, as the filter can be connected to the loggers that are configured for a\nprogram at startup, and new secrets can be conveniently added to the filter to be\nredacted in the logs:\n\n.. code-block:: python\n\n    import logging\n    import sys\n\n    import misprint\n\n    logging.basicConfig(\n        datefmt="[%X]",\n        handlers=[logging.StreamHandler(sys.stderr)],  # plus others\n    )\n\n    misprinter = misprint.MisprintFilter()\n\n    for handler in logging.getLogger().handlers:\n        handler.addFilter(misprinter)\n\n    A_TOKEN = "asdf1234"\n\n    misprinter.add_mask_for(A_TOKEN)\n\n    log.error("Bad token: %s", A_TOKEN)\n',
    'author': 'Bernard Cooke',
    'author_email': 'bernard-cooke@hotmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
