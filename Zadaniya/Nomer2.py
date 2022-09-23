#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    numb = {
        1: 'a',
        2: 'b',
        3: 'c'
    }
    print(numb)
    print({v: k for k, v in numb.items()})

