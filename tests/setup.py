import os
import shutil
import pytest
from functional import seq
import src.config as config
from src.config import Settings

config.settings = Settings('../../.test.env')

settings = config.settings
