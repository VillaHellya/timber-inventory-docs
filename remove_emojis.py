#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Remove emojis from HTML files"""

import re

def remove_emojis(text):
    """Remove common emojis"""
    emoji_pattern = re.compile(
        "["
        "\U0001F300-\U0001F9FF"  # symbols & pictographs
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F680-\U0001F6FF"  # transport & map
        "\U00002600-\U000026FF"  # misc symbols
        "\U00002700-\U000027BF"  # dingbats
        "\U0000FE00-\U0000FE0F"  # variation selectors
        "\u2600-\u26FF"  # more symbols
        "\u2700-\u27BF"  # more dingbats
        "\u2B50"  # star
        "\u2705"  # checkmark
        "\u274C"  # X mark
        "\u231A-\u231B"  # watch
        "\u23E9-\u23F3"  # media buttons
        "\u25AA-\u25AB"  # squares
        "\u25B6"  # play button
        "\u25C0"  # reverse button
        "\u25FB-\u25FE"  # more squares
        "\u2934-\u2935"  # arrows
        "\u2B05-\u2B07"  # more arrows
        "\u3030"  # wavy dash
        "\u303D"  # part alternation mark
        "\u3297"  # Japanese congratulations
        "\u3299"  # Japanese secret
        "]+",
        flags=re.UNICODE
    )
    return emoji_pattern.sub('', text)

# Process privacy-policy.html
with open('privacy-policy.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = remove_emojis(content)

with open('privacy-policy.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Emojis removed successfully")
