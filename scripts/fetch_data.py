#!/usr/bin/env python
import pandas as pd
from io import StringIO
import requests

def fetch_public_data(source_url):
    response = requests.get(source_url)
    data = response.text
    return pd.read_csv(StringIO(data))

def main():
    public_source_url = 'https://example.com/public/data.csv'
    df = fetch_public_data(public_source_url)
    print(df.head())

if __name__ == '__main__':
    main()
