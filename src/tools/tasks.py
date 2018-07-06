from celery import shared_task
import requests
import json


@shared_task
def create_tool_from_suggestion():
    """ 
        Task to attempt creating Tools from suggestions
    """
    pass