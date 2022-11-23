_freq = {
    "fx": None,
    "day": "D",
    "week": "7D",
    "mon": "MS",
    "sem": "QS-DEC",
    "year": "YS",
}

_tfreq = {
    "fx": None,
    "day": "D",
    "week": "7D",
    "mon": ["MS", "M"],
    "sem": ["QS-DEC", "Q-FEB"],
    "year": ["AS", "A"],
}

_bounds = {
    "fx": {
        "start": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        "end": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    },
    "day": {
        "start": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        "end": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    },
    "week": {
        "start": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        "end": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    },
    "month": {
        "start": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        "end": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    },
    "sem": {"start": [3, 6, 9, 12], "end": [2, 5, 8, 11]},
    "year": {"start": [1], "end": [12]},
}

_fmt = {
    "fx": "%Y%m%d",
    "day": "%Y%m%d",
    "week": "%Y%m%d",
    "month": "%Y%m",
    "sem": "%Y%m",
    "year": "%Y",
}

_split = {
    "fx": False,
    "day": "5A",
    "week": "10A",
    "month": "10A",
    "sem": "10A",
    "year": "20A",
}
