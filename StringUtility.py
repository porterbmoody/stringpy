import pandas as pd
import numpy as np
import re
from termcolor import colored

class StringUtility:

    float_regex = r'([-+]?\d*)\.?(\d*)'

    @staticmethod
    def str_detect(string, regex, ignore_case = False):
        """ regex detects if 
            
        Args:
            string (str)
            regex (str)
        
        Returns:
            boolean
        """
        if ignore_case:
            return bool(re.search(regex, string, re.IGNORECASE))
    
        return bool(re.search(regex, string))

    @staticmethod
    def join_words_to_regex(words):
        """
        Args:
            words (list): list of words to join
        Returns:
            ex: (word1)|(word2)|(word3)
        """
        return '(' + ')|('.join(words) + ')'
    
    @staticmethod
    def str_extract(string, regex, ignore_case = False):
        if ignore_case:
            match = re.search(regex, string, re.IGNORECASE)
        else:
            match = re.search(regex, string)
        if match is None:
            return
        return match.group(0)

    @staticmethod
    def str_extract_all(string, regex, ignore_case=False):
        if ignore_case:
            return re.findall(regex, string, re.IGNORECASE)
        else:
            return re.findall(regex, string)

    @staticmethod
    def str_replace(string, regex_search_term, regex_replacement):
        
        return re.sub(regex_search_term, regex_replacement, string)

    @staticmethod
    def str_combine_all(words):
        words = ("".join(x) for x in words)
        return ''.join(words)

    @staticmethod
    def str_split(string, regex, strip = False):
        print([string.strip() for string in re.split(regex, string)])
        if strip:
            return [string.strip() for string in re.split(regex, string)]
        else:
            return re.split(regex, string)
