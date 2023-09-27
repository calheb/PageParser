# PageParser

A script to search web directories for keywords. 

This script is currently set up to search for a few font files located in various directories on https://mirrors.kernel.org/gentoo/distfiles/

## Using
- Install [python](https://www.python.org/downloads/)

Clone the repo.
```
git clone https://github.com/calheb/PageParser.git
```
Modify the script for the page you'd like to search and the keywords to search for.
You can also specify the depth (how many directory levels to traverse when searching).

`keywords`

`base_url`

`max_depth`

```
python3 search.py
```
<div class='container' align='left'>
  <img src="https://caleb.foo/img/misc/pysearch_terminal.png">
</div>
