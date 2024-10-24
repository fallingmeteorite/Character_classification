import logging as log_use
import colorlog

from imgutils.metrics import ccip_difference, ccip_clustering, ccip_same
from log import get_logger

logging = get_logger(log_use.INFO)

def detect_similarity(base_path, input_path):
    similarity_01 = ccip_difference(base_path, input_path)
    # logging.info(similarity_01)
    return similarity_01 * 1000
