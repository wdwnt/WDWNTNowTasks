import argparse
from models import Attraction
import config

for attraction in config.WAIT_TIMES:
	Attraction.get(attraction)