=====
gogpy
=====

Communicate with a `gog`_ server for data visualization independent of
Python.

.. _gog: https://github.com/ajschumacher/gog

The ``gog`` function sends data from a `pandas`_ DataFrame to a gog
server such as `gogd`_. The gog server is responsible for passing the
data to a gog frontend such as `gogi`_ for visualization.

.. _pandas: http://pandas.pydata.org/
.. _gogd: https://github.com/ajschumacher/gogd
.. _gogi: https://github.com/ajschumacher/gogi


Usage
-----

::

  > import pandas as pd
  > my_data = pd.DataFrame({'x': [1, 2, 3], 'y': [3, 1, 1]})
  > from gogpy import gog
  > gog(my_data)
