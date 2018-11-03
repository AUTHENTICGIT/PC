import requests

def getUrl(end_cursor):
    variables = {
        "id":"8293195996",
        "include_reel":"false",
        "fetch_mutual":"false",
        "fisrt":24  #12
    }
    variables["after"]=end_cursor
    url = "https://www.instagram.com/graphql/query/?query_hash=56066f031e6239f35a904ac20c9f37d9&variables=" + variables
    return url

def getData():
    cookies = {"sessionid":"IGSC2db717bb62d79ac65d9331bc3459b109b4d579fd94e6810a940d91efd2f0aeaa"}
    url = getUrl()
    r = requests.post(url, cookies=cookies)

def main():
    pass

if __name__ == "__main__":
    main()