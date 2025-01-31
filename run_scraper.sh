#!/bin/bash
source /home/elias/miniconda/etc/profile.d/conda.sh  # Load conda
conda activate eda  # Activate the 'eda' environment

# Set environment variables explicitly
export TG_API_ID=21429245
export TG_API_HASH=7cca92e3c0c480235c4cd818f9c638fe
export phone=+251714058387

# Run the script
/home/elias/miniconda/envs/eda/bin/python /home/elias/Documents/data_collection/Telegram_scrapper/tl_scrape.py
