# Notebook setup

from dotenv import load_dotenv
import os
from pathlib import Path

# Load the .env file from the project root
project_root = Path(__file__).resolve().parents[1]  # one level up from /scripts
load_dotenv(dotenv_path=project_root / ".env")

# Access and export variables
INPUT_DIR = os.getenv("INPUT_DIR")
OUTPUT_DIR = os.getenv("OUTPUT_DIR")

# Optional: resolve paths relative to project root
INPUT_PATH = project_root / INPUT_DIR if INPUT_DIR else None
OUTPUT_PATH = project_root / OUTPUT_DIR if OUTPUT_DIR else None

# Import libraries
import pandas as pd
import seaborn as sns
from pathlib import Path
from matplotlib import pyplot as plt
from matplotlib import rcParams
import numpy as np
from scripts.helpers import *

SCRIPTS_DIR = os.getenv("SCRIPTS_DIR")
MODELS_DIR = os.getenv("MODELS_DIR")

# Global plot parameters
rcParams['figure.figsize'] = (10, 5) # plot size
sns.set_palette('colorblind') # colour palette
