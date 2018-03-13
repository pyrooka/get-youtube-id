# get-youtube-id
Extract YouTube ID from URLs.  
Based on [jmorrell's code](https://github.com/jmorrell/get-youtube-id)  
Tested with Python 2.7.14 and 3.6.3.

## Usage
```python
from getyoutubeid import get_youtube_id

get_youtube_id('Check [this](http://youtu.be/0zM3nApSvMg) video!', first_match=True, fuzzy=True)
```

The result should be:
```
0zM3nApSvMg
```
