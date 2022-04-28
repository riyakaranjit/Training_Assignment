import requests


def main():
    url = 'http://data.nba.net/prod/v2/2018/teams.json'
    # Accept header tells server what content type your application can handle
    response = requests.get(url, headers={'Accept': 'application/json'})
    json_response = response.json()
    print(json_response)
    # print(json_response['league']['standard'])
    print(response.headers)


if __name__ == '__main__':
    main()
