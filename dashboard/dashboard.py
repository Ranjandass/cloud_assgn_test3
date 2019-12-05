# Copyright Google Inc. 2017
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import logging
import concurrent
import time
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.io import curdoc

# Hide some noisy warnings
logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)


def modify_doc(doc):
    """Add a plotted function to the document.

    Arguments:
        doc: A bokeh document to which elements can be added.
    """
    x_values = range(10)
    y_values = [x ** 2 for x in x_values]
    data_source = ColumnDataSource(data=dict(x=x_values, y=y_values))
    plot = figure(title="plot title ca675",
                  tools="crosshair,pan,reset,save,wheel_zoom", )
    plot.line('x', 'y', source=data_source, line_width=3, line_alpha=0.6)
    doc.add_root(plot)
    doc.title = "doc title CA675"


def main():
    modify_doc(curdoc())


main()
