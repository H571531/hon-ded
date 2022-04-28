#!/usr/bin/python3

import datetime
import time

def main():  

    idag=datetime.datetime.now()
    honded=datetime.datetime(2022,6,20,0,1)
    start=datetime.datetime(2010,5,10,0,1)
    tidTilded=(honded-idag).total_seconds()
    totTidded=(honded-start).total_seconds()
    gamesTilDed=tidTilded/(30*60)
    prs=(tidTilded/totTidded)*100
    prosess=100-prs
    print('\n\n')
    print(r"""
            _   _ _____ _   _
           | | | |  _  | \ | |
           | |_| | | | |  \| |
           |  _  | | | | . ` |
           | | | \ \_/ / |\  |
           \_| |_/\___/\_| \_/

        """)

    
    printProgressBar(prosess,100,prefix='Hon Lifespan',suffix='{:.1f} 30 min games igjen '.format(gamesTilDed),length=50) 
    while tidTilded>0:
        idag=datetime.datetime.now()
        tidTilded=(honded-idag).total_seconds()
        gamesTilDed=tidTilded/(30*60)
        prs=(tidTilded/totTidded)*100
        prosess=100-prs
        printProgressBar(prosess,100,prefix='Hon Lifespan',suffix='{:.1f} 30 min games igjen '.format(gamesTilDed),length=50)
        time.sleep(1)
        

def printProgressBar(iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

if __name__ == '__main__':
    main()
