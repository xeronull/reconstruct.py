# Reconstruct social links to privacy-friendly front-ends via command line

import sys

def reconstruct(url: str) -> str:
    com = ".com/"

    # If com in url
    if com in url:
        instagram = "instagram"
        reddit = "reddit"
        twitter = "twitter"
        youtube = "youtube"
        platform = url.split(com)[0]
        platform_lower = platform.lower()
        subdirectory = url.split(com)[1]
        key = url.split(platform + com)[1]

        # Instagram -> Bibliogram
        # If instagram in platform_lower and "p/" in subdirectory then url is treated as Instagram profile...
        if instagram in platform_lower and "p/" in subdirectory:
            return "https://imginn.com/" + key

        # ...Elif instagram in platform_lower then url is treated as Instagram post
        #elif instagram in platform_lower:
            #return "https://bibliogram.art/u/" + key

        # Reddit -> Teddit
        # Elif reddit in platform_lower then url is treated as Reddit subreddit or post
        elif reddit in platform_lower:
            return "https://teddit.net/" + key

        # Twitter -> Nitter
        # Elif twitter in platform_lower then url is treated as Twitter profile or tweet
        elif twitter in platform_lower:
            return "https://nitter.net/" + key

        # YouTube -> Invidious
        # Elif youtube in platform_lower then url is treated as YouTube channel or video
        elif youtube in platform_lower:
            return "https://invidious.site/" + key

        # Else return empty str
        else:
            return ""

    # Else return empty str
    else:
        return ""

# Driver
for url in sys.argv:
    print(reconstruct(str(url)))
