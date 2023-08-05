# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['labos']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.2.2',
 'numpy>=1.21',
 'requests>=2.2',
 'scipy>=1.10.0',
 'sympy>=1.10']

setup_kwargs = {
    'name': 'labos',
    'version': '0.1.2.7',
    'description': 'Paquete para trabajar en el labo',
    'long_description': '# Labos\n\nEste paquete está dedicado principalmente a facilitar el uso de herramientas y paquetes utilizados en la adquisición y procesamiento de datos en el marco de los laboratorios de la carrera en [*Ciencias Físicas de la UBA*](https://www.df.uba.ar/es/).\n\nLos paquetes hasta ahora implementados son de adquisición y análisis de datos.\n\n<!-- headings -->\n## Análisis de datos\n\n### Propagación\nEste paquete está dedicado a propagar errores utilizando una aproximación lineal sobre la formula de covarianza. El paquete está basado en las librerías numpy e sympy.\n```python\nfrom labos.propagacion import Propagacion_errores\nimport numpy as np\n\n# Formula a propagar\nexpr = \'A*cos(f*t) + C\'    \n\n# Las variables dependientes y sus valores\nvariables = [\n    (\'f\', 100), # Hz\n    (\'A\', 2), # Volts\n    (\'t\', 1), # s\n    (\'C\', .5), # Volts\n    ]\n\n# Los errores de las variables\nerrores = np.array(\n    [.0005,\n    .0001, \n    0, \n    .0001]\n    ).reshape(-1,1)\n\n# Instancia de la clase\npropaga = Propagacion_errores(\n    formula = expr,\n    variables = variables,\n    errores = errores)\npropaga.fit()\n>>(2.224637744575368, 0.0005232992460070357)\n```\n### Ajuste\nEste paquete está dedicado a realizar ajustes sobre datos. El paquete está basado en las librerías numpy e sympy.\n\n#### Heading 3\n##### Heading 4\n###### Heading 5\n\n<!-- line breaks -->\n<!-- ENTER -->\n\n<!-- Italics -->\nThis is an *italic* text\n\nThis is an _italic_ text\n\n<!-- Strongs -->\nThis is an **strong** text\n\nThis is an __strong__ text\n\n<!-- StrikeTrough -->\nThis is an ~~striketrogh~~ text\n\n\n\n<!-- UL -->\n* item 1\n* item 2\n* item 3\n    * item 3.1\n    * item 3.2    \n* item 4\n\n<!-- OL -->\n1. item 1\n1. item 2\n1. item 3\n1. item 4\n\n<!-- Links -->\n[Faztweb.com](https://www.faztweb.com)\n\n[Faztweb.com](https://www.faztweb.com "Custom title")\n<!-- Blockquote -->\n> this is a quote\n\n<!-- Horizontal Rule -->\n___\n---\n\n<!-- Inline code -->\n`console.log(\'hello world\')`\n\n`<h1>Hello world</h1>`\n\n<!-- IMAGES -->\n<!-- ![Vscode Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Visual_Studio_Code_1.35_icon.svg/1200px-Visual_Studio_Code_1.35_icon.svg.png) -->\n\n<!-- ![Vscode logo](./vscode.png "vscode") -->\n\n<!-- GITHUB MD -->\n\n```\nfirst line of code\nsecond line of code\n```\n\n```python\nprint("hello world")\n```\n\n```javascript\nconsole.log(\'hello world\')\n\nconst test = (str) => str + \'test\';\n```\n\n```html\n<h1>Hello World</h1>\n```\n\n<!-- TABLES -->\n| Product       | Price         |quantity   |\n| ------------- |:-------------:| :--------:|\n| Laptop        | 3.33          | 2         |\n| Mouse         | 10.33         | 1         |\n\n* [x] task1\n* [] task2\n* [] task3\n* [x] task4\n\n<!-- Mentiosn -->\n@faztweb :+1: :smile:\n',
    'author': 'joctavio287',
    'author_email': 'joctavio287@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
