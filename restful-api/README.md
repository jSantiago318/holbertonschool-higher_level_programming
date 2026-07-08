# RESTful API

This directory covers **RESTful APIs**: consuming web services from the command
line and from Python, and developing APIs with Python's `http.server` and Flask,
including security and authentication.

## Concepts covered

- HTTP/HTTPS fundamentals (methods, status codes, secure vs. non-secure)
- Consuming APIs with `curl` and with Python's `requests` library
- Parsing and transforming JSON, exporting to CSV
- Building APIs with the built-in `http.server` module
- Building APIs with the Flask framework (routing, JSON responses)
- API security and authentication techniques

## Files

| File | Description |
| --- | --- |
| `task_02_requests.py` | Fetch posts from JSONPlaceholder with `requests`; print titles and save to CSV |
| `task_03_http_server.py` | Simple API server with `http.server` (`/`, `/data`, `/status`, `/info`, 404) |
| `task_04_flask.py` | Flask API with routing, JSON responses, dynamic routes, and POST `/add_user` |

## Requirements

- Scripts are tested with **Python 3.9**
- The `requests` and `Flask` libraries are used in later tasks
  (`pip install requests Flask`)
- Code follows `pycodestyle`
- All modules and functions are documented

## Author

Holberton School / Higher-Level Programming track
