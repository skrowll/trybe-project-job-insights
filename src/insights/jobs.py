from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path) as csv_file:
        jobs = csv.DictReader(csv_file)
        # jobs_list = []
        # for job in jobs:
        #     jobs_list.append(job)
        # return jobs_list
        return [job for job in jobs]


def get_unique_job_types(path: str) -> List[str]:
    jobs = read(path)
    jobs_list = []
    for job in jobs:
        jobs_list.append(job['job_type'])
    return set(jobs_list)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    return [
        job for job in jobs
        if job['job_type'] == job_type
    ]