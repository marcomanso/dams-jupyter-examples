import logging
import traceback
import datetime

import requests

import json

##
from requests import HTTPError

SOCKET_TIMEOUT = 90

##

def to_timestamp(naive_time):
    return datetime.datetime.strptime(naive_time, '%Y-%m-%d %H:%M:%S').timestamp()


def to_iso_format(naive_time):
    return datetime.datetime.strptime(naive_time, '%Y-%m-%d %H:%M:%S').isoformat()+'Z'

#

def read_file(file):
    with open(file, encoding='utf-8') as json_file:
        content = json.load(json_file)
    return content


def get_double_or_zero(data, key):
    if key in data:
        return data[key]
    else:
        return 0.0


def print_exception(e: Exception):
    logging.error("Error ...")
    print(e)
    traceback.print_exc()

def print_http_error(e: HTTPError):
    logging.error("Error ...")
    print(e)
    print(e.response.content)
    traceback.print_exc()


##


def authorise(endpoint, username, password):
    if not username and not password:
        raise Exception("No username or password specified")
    headers = {
        "Content-Type": "application/json;charset=utf-8"
    }
    try:
        data = {
            "username": username,
            "password": password
        }
        myResponse = requests.post(url=endpoint, json=data, headers=headers, timeout=SOCKET_TIMEOUT)
        if (myResponse.ok):
            return myResponse.json()['key']
        else:
            myResponse.raise_for_status()
    except HTTPError as he:
        print_http_error(he)
    except Exception as e:
        print_exception(e)
        #logging.error("Error ...")
        #print(e)
        #traceback.print_exc()
    return None



def post_data(endpoint, token, data):
    response_code = 400
    if not token:
        raise Exception("Token is null")

    headers = {
        "Content-Type": "application/json;charset=utf-8",
        "Authorization": "Token "+token
    }
    try:
        print("-- post to ", endpoint)
        #print("-- data is ", data)
        myResponse = requests.post(url=endpoint, json=data, headers=headers, timeout=SOCKET_TIMEOUT)
        if (myResponse.ok):
            print("-- data posted OK.")
            #print("-- data posted OK. Received: ", myResponse.json())
            return 200, myResponse.json()
        else:
            response_code = myResponse.status_code
            myResponse.raise_for_status()
    except HTTPError as he:
        print_http_error(he)
    except Exception as e:
        print_exception(e)
        #logging.error("Error ...")
        #print(e)
        #traceback.print_exc()
    return response_code, None


def put_data(endpoint, token, data):
    response_code = 400
    if not token:
        raise Exception("Token is null")

    headers = {
        "Content-Type": "application/json;charset=utf-8",
        "Authorization": "Token "+token
    }
    try:
        print("-- put to ", endpoint)
        print("-- data is ", data)
        myResponse = requests.put(url=endpoint, json=data, headers=headers, timeout=SOCKET_TIMEOUT)
        if (myResponse.ok):
            print("-- data put OK. Received: ", myResponse.json())
            return 200, myResponse.json()
        else:
            response_code = myResponse.status_code
            myResponse.raise_for_status()
    except HTTPError as he:
        print_http_error(he)
    except Exception as e:
        print_exception(e)
        #logging.error("Error ...")
        #print(e)
        #traceback.print_exc()
    return response_code, None

def delete_data(endpoint, token, data):
    response_code = 400
    if not token:
        raise Exception("Token is null")

    headers = {
        "Content-Type": "application/json;charset=utf-8",
        "Authorization": "Token "+token
    }
    try:
        print("-- delete to ", endpoint)
        print("-- data is ", data)
        myResponse = requests.delete(url=endpoint, json=data, headers=headers, timeout=SOCKET_TIMEOUT)
        if (myResponse.ok):
            print("-- data delete OK. Received: ", myResponse.json())
            return 200, myResponse.json()
        else:
            response_code = myResponse.status_code
            myResponse.raise_for_status()
    except HTTPError as he:
        print_http_error(he)
    except Exception as e:
        print_exception(e)
        #logging.error("Error ...")
        #print(e)
        #traceback.print_exc()
    return response_code, None


def get_data(endpoint, token, data):
    response_code = 400
    if not token:
        raise Exception("Token is null")

    headers = {
        "Content-Type": "application/json;charset=utf-8",
        "Authorization": "Token "+token
    }
    try:
        print("-- get from ", endpoint)
        if data:
            print("-- data is ", data)
        myResponse = requests.get(url=endpoint, json=data, headers=headers, timeout=SOCKET_TIMEOUT)
        if (myResponse.ok):
            print("-- data GET OK.")
            #print("-- data GET OK. Received: ", myResponse.json())
            return 200, myResponse.json()
        else:
            response_code = myResponse.status_code
            myResponse.raise_for_status()
    except HTTPError as he:
        print_http_error(he)
    except Exception as e:
        print_exception(e)
        #logging.error("Error ...")
        #print(e)
        #traceback.print_exc()
    return response_code, None


