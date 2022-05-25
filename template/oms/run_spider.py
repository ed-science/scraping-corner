# Imports
import os
import time
import numpy as np


# To evaluate scraping execution time
def print_execution_time(start):
    now = time.time()
    duree = now - start
    duree_min = np.round(duree / 60, 2)
    print(f'Durée : {duree_min} min.')


if __name__ == "__main__":


    ##################################################
    file_name = 'oms_1.jl'
    ##################################################

    # Start script
    print('Start scrapping. (Be sure that Scrapy is locally installed in your environment)')

    # Prepare storage
    if 'data' not in os.listdir('../'):
        os.mkdir('../data')

    # Start chronometer
    start_time = time.time()

    # Indicate spider name
    spider_name = 'OMS'

    # Run spider
    cmd = f'scrapy crawl {spider_name} -o ../data/{file_name}'
    os.system(cmd)

    # Display execution time
    print_execution_time(start_time)
