#!/usr/bin/python3

from pprint import pprint
import requests

def main():
    req = requests.get('https://www.anapioficeandfire.com/api')
    pprint(req.json())

main()
