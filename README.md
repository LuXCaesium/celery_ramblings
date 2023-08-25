# Celery Ramblings

This repo will demonstate some of the key compoents for Celery. This is by no means a production ready "nice" bit of code, its quite terrible and should not be used lightly.

## Setting up redis broker

Install redis for whatever operating system you are on.
Then in a terminal call an instance of the server.

For redis support in celery install these packages in your environment,

```bash
pip install -U "celery[redis]"
```

A nice way to run this backend redis server is using docker. Simply run
```bash
docker run -d -p 6379:6379 redis
```
and everything will be taken care of.

## setup celery backend
To run the celery backend, run the following command. 

```bash
celery -A tasks worker --loglevel=DEBUG
```

Then simply run the `run.py` file and you should see the task sent to the worker queue.
