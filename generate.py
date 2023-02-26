"""
We are setting up this redirect by autogenerated 35K pages with this redirect

https://trac.sagemath.org/ticket/[number] -->
https://github.com/sagemath/sage/issues/[number]


"""

import os
from pathlib import Path

def mkdir(d):
    Path(d).mkdir(parents=True, exist_ok=True)

mkdir('ticket')


def redirect(n):
    return f"""<!DOCTYPE html>
<html>
  <body style="margin: 30px">
    <p>This ticket is now <a href="https://github.com/sagemath/sage/issues/{n}">hosted on GitHub</a>.</p>

<p>
    There is also <a href="https://web.archive.org/web/20230130064641/https://trac.sagemath.org/ticket/{n}">a read-only archive of the original trac ticket at trac.sagemath.org</a>.
    </p>
  </body>
</html>
"""


for n in range(1, 5):
    mkdir(f'ticket/{n}')
    open(f"ticket/{n}/index.html", 'w').write(redirect(n))
