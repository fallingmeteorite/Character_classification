#!/usr/bin/env python
# -*- coding: utf-8 -*-

from imgutils.metrics import ccip_difference, ccip_clustering, ccip_same


def detect_similarity(base_path, input_path):
    similarity_01 = ccip_difference(base_path, input_path)
    return similarity_01 * 1000
