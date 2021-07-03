class TestData:
    CHROME_EXECUTABLE_PATH = "drivers\\chromedriver.exe"
    FIREFOX_EXECUTABLE_PATH = "drivers\\geckodriver.exe"

    HOME_URL = "https://www.imdb.com/"

    SIGN_IN_OPTIONS_PAGE_TITLE = "Sign in with IMDb - IMDb"
    SIGN_IN_OPTIONS_PAGE_TITLE_INCORRECT = "Sign in with IMDb"

    CREATE_ACCOUNT_PAGE_TITLE = "IMDb Registration"
    CREATE_ACCOUNT_PAGE_TITLE_INCORRECT = "IMDb Registration_1"

    USER_HOME_PAGE = "IMDb: Ratings, Reviews, and Where to Watch the Best Movies & TV Shows"
    USER_HOME_PAGE_INCORRECT = "IMDb: Ratings, Reviews, and Where to Watch the Best Movies & TV"

    SIGN_IN_PAGE = "IMDb Sign-In"
    SIGN_IN_PAGE_INCORRECT = "IMDb Sing-In"

    USERNAME = "NH"
    EMAIL = "test.0000.imdb@gmail.com"
    PASSWORD = "imdb.0000.test.5555"

    KEYWORDS = ["Avatar", "Jurassic Park", "Joker"]
    NEW_KEYWORDS = ["Friends", "Martian"]

    SORT_TYPES = ["LIST_ORDER", "DATE_ADDED", "NUMBER_OF_RATINGS", "ALPHA", "USER_RATING", "POPULARITY", "YOUR_RATING",
                  "RELEASE_DATE", "RUNTIME"]

    SORTING = {
        "LIST_ORDER": ["Avatar: The Last Airbender", "Joker", "Friends", "The Martian"],
        "ALPHA": ["Avatar: The Last Airbender", "Friends", "Joker", "The Martian"],
        "USER_RATING": ["Avatar: The Last Airbender", "Friends", "Joker", "The Martian"],
        "POPULARITY": ["Friends", "Joker", "Avatar: The Last Airbender", "The Martian"],
        "YOUR_RATING": ["The Martian", "Avatar: The Last Airbender", "Joker", "Friends"],
        "NUMBER_OF_RATINGS": ["Joker", "Friends", "The Martian", "Avatar: The Last Airbender"],
        "RELEASE_DATE": ["Joker", "The Martian", "Avatar: The Last Airbender", "Friends"],
        "RUNTIME": ["The Martian", "Joker", "Avatar: The Last Airbender", "Friends"],
        "DATE_ADDED": ["The Martian", "Friends", "Joker", "Avatar: The Last Airbender"]
    }

    LIST_NAME = "Best"
    LIST_DESCRIPTION = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut " \
                       "labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco " \
                       "laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in" \
                       " voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat" \
                       " non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

    REFINED_LIST = ["Joker", "The Martian"]
