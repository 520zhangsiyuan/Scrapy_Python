import os
import sys
import time
import random
import unittest

from settings import IPPOOL;
from threading import Thread
from datetime import datetime
if __name__ == '__main__':
	startscrapy = 'scrapy crawl icautos'
IPPOOL='221.2.120.211:23721'
time.sleep(2)
os.system(startscrapy)

