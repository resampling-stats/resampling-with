""" Redirect pages to their python- r- repo equivalents
"""

import os
from os.path import relpath, join as pjoin
import sys

TEMPLATE = r"""
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html lang="en">
    <head>
    <title>Redirect</title>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <!--Redirect browser, 3 indicates number of seconds before redirect-->
    <meta http-equiv="refresh" content="3;URL={new_path}">
    </head>
    <body>
        <p>Redirecting to: <a href="{new_path}">
        {new_path}</a></p>
    </body>
</html>
"""

ROOT_PATH = 'http://resampling-stats.github.io'

start_dir = '.' if len(sys.argv) < 2 else sys.argv[1]

for dirpath, dirnames, filenames in os.walk(start_dir):
    for filename in filenames:
        if not filename.endswith('.html'):
            continue
        file_path = pjoin(dirpath, filename)
        rel_path = relpath(file_path, start_dir)
        new_path = f'{ROOT_PATH}/{rel_path}'
        with open(file_path, 'wt') as fobj:
            fobj.write(TEMPLATE.format(new_path=new_path))

