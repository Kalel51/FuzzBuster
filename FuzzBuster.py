#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Global vars
version = "1.0"


def banner_intro():
    """Print intro banner
    """

    banner = """\
    ______            ______           _            
    |  ___|           | ___ \         | |           
    | |_ _   _ _______| |_/ /_   _ ___| |_ ___ _ __ 
    |  _| | | |_  /_  / ___ \ | | / __| __/ _ \ '__|
    | | | |_| |/ / / /| |_/ / |_| \__ \ ||  __/ |   
    \_|  \__,_/___/___\____/ \__,_|___/\__\___|_|   
    
                   Developed by Kal3l
    """
    print(banner)


def main():
    # TODO check if config file exist
    banner_intro()


if __name__ == '__main__':
    main()
