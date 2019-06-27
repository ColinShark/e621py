# e621py

<img src="https://i.imgur.com/BIIQQRI.png" width="250" align="right" alt="e621 mascot, Esix">

<big>An API Wrapper for the [e621.net](https://e621.net) [API](https://e621.net/help/show/api).</big>

## Usage

Currently there is full funcationality for `/posts/` endpoints. For some API
calls authentication is required. To get an API Key, head to
[your API Access page](https://e621.net/user/api_key) and enable it.

```python
>>> import e621py
>>> e6 = e621py.Client()
>>> for result in e6.index("shark", 2):
...     print(result)
{'id': 1914785, ...}
{'id': 1914718, ...}
```

The above code snippet will yield JSON objects containing all information
about the found posts. The example doesn't show all information for the sake
of brevity.

## License

There is no License yet, but the repo is private anyway :D
