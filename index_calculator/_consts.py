_freq = {"year": "YS", "sem": "QS-DEC", "mon": "MS", "day": "D"}

_tfreq = {
    "year": ["YS", "Y"],
    "sem": ["QS-DEC", "Q-FEB"],
    "mon": ["MS", "M"],
    "day": "D",
}

_bounds = {
    "day": {
        "start": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        "end": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    },
    "year": {"start": [1], "end": [12]},
    "sem": {"start": [3, 6, 9, 12], "end": [2, 5, 8, 11]},
    "month": {
        "start": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        "end": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    },
    "fx": {
        "start": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        "end": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    },
}

_fmt = {
    "day": "%Y%m%d",
    "year": "%Y",
    "month": "%Y%m",
    "sem": "%Y%m",
    "fx": "%Y%m%d",
}