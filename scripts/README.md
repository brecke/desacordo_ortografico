# Script Desacordo Ortográfico

## What it does?

1. For each character in the alphabet
    1. Get list of words affected by the new AO
    2. Add the verbal conjugations of each word
    3. Add the feminine form of each word
    4. Add the plural form of each word

## Intall requirements

> pip install -r requirements.pip

## Launch script

> python script.py

### Arguments

> python script.py --help

- **--priberam**: ask first to *priberam.pt* before trying to guess (defaults to True)
- **--dont-ask**: ask the user for the right plural/feminine form in case of doubt (defaults to False)
- **--verbose**: keep the user informed of what is happening (defaults to False)
- **--lazy**: add a 1second interval between request to *priberam.pt* (defaults to False)
