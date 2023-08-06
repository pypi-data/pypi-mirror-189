__version__ = '0.1.0'

from requests import post

def getlikers(url):
    def likes(after = ""):
        data = post("https://replit.com/graphql", headers = {
            "X-Requested-With": "replit",
            "Referer": "https://replit.com"
        }, json = {
            "query": """
query Votes($url: String, $after: String) {
    repl(url: $url) {
        ...on Repl {
            posts(count: 100) {
                items {
                    votes(count: 100, after: $after) {
                        items {
                            user {
                                username
                            }
                        }
                        pageInfo {
                            nextCursor
                        }
                    }
                }
            }
        }
    }
}
            """,
            "variables": {
                "url": url,
                "after": after
            }
        }).json()["data"]["repl"]["posts"]["items"][0]["votes"]
        
        return data["items"], data["pageInfo"]["nextCursor"]

    likers = []
    next = ""

    while True:
        users, next = likes(next)
        likers += users
        if not next: break

    return [i["user"]["username"] for i in likers][::-1]