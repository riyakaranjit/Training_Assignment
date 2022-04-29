import json
import requests
from requests.exceptions import SSLError
import time


def make_request(url):
    """This makes a single request to the server to get data from it."""

    try:
        # Accept header tells server what content type your application can handle
        # query = {'lat': '45', 'lon': '180'}
        response = requests.get(url, headers={'Accept': 'application/json'})

        # If response.status_code is not 200, treat it as an error.
        if response.status_code != 200:
            raise RuntimeError(f"HTTP Response Code {response.status_code} received from server.")
        else:
            print(f'Api call {response.status_code} status was successful.')
            json_response = response.json()
            if 'error' in json_response:
                raise RuntimeError(f"API Error Code {json_response['error']} received from server.")
            else:
                print('Key and Values of the response:')
                for key, value in json_response.items():
                    print(f'{key}: {value}')
                return json_response
    except SSLError as ssl_err:
        print(ssl_err)
        return 'Try adding verify=False parameter for get request!'


def request_with_retry(url, backoff_in_seconds=1):
    """This makes a request retry up to MAX_RETRY set above with exponential backoff. Backoff is the number of seconds
    of wait between each retry. """
    attempts = 1
    while True:
        try:
            data = make_request(url)
            return data
        except RuntimeError as err:
            print(err)
            if attempts > MAX_RETRY:
                raise RuntimeError("Maximum number of attempts exceeded, aborting.")

            sleep = backoff_in_seconds * 2 ** (attempts - 1)  # Formula as per retry backoff
            print(f"Retrying request (attempt #{attempts}) in {sleep} seconds...")
            time.sleep(sleep)
            attempts += 1


def main():
    url = 'http://restapi.adequateshop.com/api/Tourist?page=2'
    # url = 'http://api.open-notify.org/iss-pass.json'  # Retry to connect to the server: add params to the requests
    # url = 'https://api.github.com'  # raises SSLError

    try:
        request_with_retry(url=url)
    except RuntimeError as err:
        print(err)
        exit(1)


if __name__ == '__main__':
    MAX_RETRY = 5
    main()
