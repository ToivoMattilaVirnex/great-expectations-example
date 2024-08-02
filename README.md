# Python Data Validation Example with Great Expectations

This project demonstrates how to use Python for data validation using the Great Expectations library.

Great Expectations is an open-source Python library for data validation, documentation, and profiling.
It helps data teams eliminate pipeline debt, through data testing, documentation, and profiling.
With Great Expectations, you can assert what you expect from your data, and automatically catch data issues as they emerge.

## Great Expectations Concepts

![Great Expectations Concepts](Great%20Expectations%20concepts.png)

This diagram outlines the core concepts and workflow in Great Expectations:

Data Source: Represents the origin of your data, which defines how to connect to the data. This includes for example a database URL and credentials. 1 Data Source can have multiple Data Assets.

Checkpoint: The central component where validation occurs, containing:

Data Asset: Represents your data, which can be broken down into batches. Batches are slices of data, i.e. a single file or rows created last week.
Expectation Suite: A collection of individual expectations (e.g., 'no nulls in column') that define data quality rules.


Validation Process: The checkpoint runs to validate the data against the defined expectations.
Data Docs: The output of the validation process, providing documentation and insights into your data's quality.

## Files

- `example.ipynb`: Contains basic expectation suite creation and validation.
- `validation_example.py`: Demonstrates how to validate data using an existing checkpoint.

## Requirements

- Python 3.8+
- Great Expectations library

## Installation

```
pip install great-expectations
```

For more information on Great Expectations, visit: https://greatexpectations.io/