# Agentic SI Summarizer

A multi-agent AI pipeline that ingests data, processes it, and generates structured executive summaries.

## Features

- Multi-agent architecture
- Context-aware memory system
- Structured Markdown reporting
- Modular ingestion pipeline
- Configurable agent memory

## Project Structure

src/
  brain.py        # core agent orchestration
  ingestor.py     # data ingestion
  memory_mgr.py   # memory handling
  formatter.py    # report formatting

## Installation

Clone the repo

git clone https://github.com/YOUR_USERNAME/agentic-si-summarizer.git

Install dependencies

pip install -r requirements.txt

## Run

python main.py

## Future Improvements

- Add LLM integration
- Add streaming data ingestion
- Deploy as microservice