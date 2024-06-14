# Setup

Configure poetry with access to our private gitlab repo.

```
poetry config http-basic.whylabs_container_gitlab __token__ <gitlab api token>
```

# Run

You have to also supply the whylabs api key as an env var until the next release. The `demo/app.py` shows all of the reuqired code
otherwise.

```
WHYLABS_API_KEY=key make install run
```
