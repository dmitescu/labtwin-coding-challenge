# Description

Here is a service that summarizes some given text. Normally one
would call the bert-summarizer service (shipped with the package)
through REST, but for the purpose of this challenge, it doesn't 
(in this imaginary scenario, I'm processing something inside the
service).

PLEASE NOTE: I was unable to test this locally so all the testing is
done by Travis

# TODO
	- implement result caching

# Improvements

	- as far as I understood, the downloaded content
	done by `sync.py` is the language model; this
	would ideally be mounted as a volume inside the container
	to avoid long build times

# How to build and run the Docker container

To build:

```
docker build . -t labtwin:1.0
```

To run:

```
docker run -dit -p 8000:8000 labtwin:1.0 --name labtwin
```
