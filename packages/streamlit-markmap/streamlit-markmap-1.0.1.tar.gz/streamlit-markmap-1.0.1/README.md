## Markmap Component for Streamlit

---

Visualize your Markdown as mindmaps.

This project is heavily inspired by  [markmap](https://github.com/markmap/markmap).

---

### Installation

```
pip install streamlit-markmap
```

### Example

![image-20230202215117681](https://cdn.jsdelivr.net/gh/echoopen/echoimage/img/image-20230202215117681.png)

~~~python
import streamlit as st
from streamlit_markmap import markmap

st.set_page_config(page_title="markmap", layout="wide")

data = '''
---
markmap:
  colorFreezeLevel: 2
---

# markmap

## Links

- <https://markmap.js.org/>
- [GitHub](https://github.com/gera2ld/markmap)

## Related Projects

- [coc-markmap](https://github.com/gera2ld/coc-markmap)
- [gatsby-remark-markmap](https://github.com/gera2ld/gatsby-remark-markmap)

## Features

- links
- **strong** ~~del~~ *italic* ==highlight==
- multiline
  text
- `inline code`
-
    ```js
    console.log('code block');
    ```
- Katex
  - $x = {-b \pm \sqrt{b^2-4ac} \over 2a}$
  - [More Katex Examples](#?d=gist:af76a4c245b302206b16aec503dbe07b:katex.md)
- Now we can wrap very very very very long text based on `maxWidth` option

'''

markmap(data, height=400)
~~~

