#!/usr/bin/env python
# coding: utf8

import pyautogui

from auto_lianliankan import AutoClick, AutoLianLianKan




def main():
    AutoLianLianKan().run()
    # AutoClick().run()
    for i in range(1, 4):
        for j in range(i):
            print(i, j)


if __name__ == "__main__":
    main()

