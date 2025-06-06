# modules/parsing/filename_parser.py

import re

def parse_filename(filename: str) -> dict:
    """
    파일명에서 문제 정보를 파싱합니다.
    예: '중학수학1-상_01_12_B_03.png'
    반환: {
        'book': '중학수학1-상',
        'chapter': '01',
        'page': '12',
        'type': 'B',
        'number': '03'
    }
    """
    pattern = r"(?P<book>.+?)_(?P<chapter>\d{2})_(?P<page>\d{2})_(?P<type>[A-Z])_(?P<number>\d{2})\.png"
    match = re.match(pattern, filename)

    if not match:
        raise ValueError(f"파일명 형식이 잘못되었습니다: {filename}")

    return match.groupdict()
