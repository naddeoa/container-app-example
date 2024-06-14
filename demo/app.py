from whylogs_container.whylabs.container.startup import ServerConfig
from whylogs_container import Server


if __name__ == "__main__":
    # These settings can be set via env as well
    # LLM_CONTAINER=True WHYLABS_API_KEY=my-api-key CONTAINER_PASSWORD=password
    # WHYLABS_API_KEY has to be an env var at the moment until its fixed in our next release.
    # You can omit this config entirely and just use env vars for everything as well.
    config = ServerConfig(whylabs_api_key="your_whylabs_api_key", container_password="password", llm_container=True)
    server = Server(overide_config=config)
    server.start(port=8000)
