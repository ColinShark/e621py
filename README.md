# e621py

An API Wrapper for the [e621.net](https://e621.net) API.

## Usage

For now there is only one functionality: Searching for posts.

```python
import e621py

e6 = e621py.Client("username", "api_key")

e6.index("shark", 1)
```

This code snippet will yield a JSON object containing all information about the found images.

## Future of this project

I plan to make this a full API Wrapper for the e621 API.

## License

There is no License yet, but the project is private anyway :D
