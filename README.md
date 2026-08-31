# RAG system

Let's implement a RAG system

## Requirements

- python 3.8 or later

#### install python using MiniConda
1) Download and install Miniconda from [here](https://www.anaconda.com/docs/getting-started/miniconda/system-requirements)
2) Create a new conda environment using the following comand
```bash
$ conda create -n rag-system python=3.8
```
3) Activate the environment
```bash
$ conda activate rag-system
```

### (optional) setup CLI inference for better readiability
```bash
$ export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```

## Installations

### Install the required packages

```bash
$ pip install -r requirements.txt
```

### setup the environment variables

```bash
$ cp .env.example .env
```

set your environment variables in the `.env` file. like `OPEN_AI_KEY` value.

## Run the FastAPI server

```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000  
```

## POSTMAN Collection

Download the POSTMAN collection from [/assets/mini-rag-app.postman_collection.json](/assets/mini-rag-app.postman_collection.json)