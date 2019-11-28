---
title: "A title"
author: "An author"
date: "2019-09-28"
site: bookdown::bookdown_site
output: bookdown::gitbook
documentclass: book
bibliography: [book.bib, packages.bib]
biblio-style: apalike
link-citations: yes
description: "An example"
---

# A markdown page

(ref:bar) Some *text*

Now test the reference with (ref:bar)

Soon we will see a Python plot:

<!--- nb:first_notebook.ipynb

This is some explanation about the notebook.

It can use macros: Python.



```python
import matplotlib.pyplot as plt
plt.plot([0, 2, 1, 4])
plt.show()
```

A normal paragraph.

nb -->

Some more text.

<!--- nb:second_notebook.ipynb

This is some explanation about the second notebook.


```python
import matplotlib.pyplot as plt
plt.plot(range(10))
plt.show()
```

Some unrelated text.

```python
a = 1
a
```

nb -->
