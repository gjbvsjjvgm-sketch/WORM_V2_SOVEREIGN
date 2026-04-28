#!/usr/bin/env python

import sys
import platform

def main():
    print("Linux Development Environment on Android is working!")
    print(f"Python version: {sys.version}")
    print(f"Platform: {platform.platform()}")
    print(f"System: {platform.system()} {platform.release()}")
    
if __name__ == "__main__":
    main()

