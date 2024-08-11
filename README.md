# Katabatic Model

This repository contains a simple implementation of the Katabatic model framework.

## Files

- `model.py`: Abstract base Model class
- `dummy_model.py`: DummyModel implementation
- `mock_adapter.py`: MockAdapter class
- `requirements.txt`: Python dependencies
- `Dockerfile`: Instructions for building the Docker container

## Getting Started

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the dummy model: `python dummy_model.py`

## Docker

To build and run the Docker container:

1. Build: `docker build -t katabatic-model .`
2. Run: `docker run katabatic-model`

