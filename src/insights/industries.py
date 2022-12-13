from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs = read(path)
    industries_list = []
    for job in jobs:
        if (job['industry'] != ''):
            industries_list.append(job['industry'])
    return set(industries_list)


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    return [
        job for job in jobs
        if job['industry'] == industry
    ]
