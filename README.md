# Introduction

## Perquisite
- Generate an OpenAI API Key
- Zep
- Langchain (serve)

## Usage

### Generate an OpenAI API Key.
Follow the steps [here](https://gptforwork.com/help/gpt-for-docs/setup/create-openai-api-key) to generate an OpenAI API Key

### Spin up the Zep server locally.
1. **Clone the Zep repo:**
```bash
git clone https://github.com/getzep/zep.git
```
2. **Add your OpenAI API key to a .env file in the root of the repo:**
```bash
ZEP_OPENAI_API_KEY=<your key here>
```

3. **Start the Zep server:** <br />

Go to the directory where the Zep folder is cloned
```bash
cd < zep_local_directory >
```
Open the docker-compose.yaml file in the zep folder
```bash
nano docker-compose.yaml
```
change the local ports
```bash
From "8000:8000" to "<any local port>:8000"
```
run the docker compose file to start the Zep app server running locally
```bash
docker compose pull
docker compose up
```

4. **Zep's Python SDK! :**

```bash
pip install zep-python
```


### Serve langchain rag bot with langserve

<!-- ```bash
pip install langchain
``` -->
<!-- ```bash
poetry add  "langchain-cli[serve]" -G dev
``` -->

To use this package, you should first have the LangChain CLI installed:
```bash
pip install -U "langchain-cli[serve]"
```

To create a new LangChain project and install this as the only package, you can do:
```bash
cd zep-app
```

Inside this directory, spin up a LangServe instance:

```bash
langchain serve
```

<br>
Then access the Zep Web UI at http://localhost:< local port >/admin

We can see the templates at http://127.0.0.1:8000/docs We can access the playground at http://127.0.0.1:8000/playground


