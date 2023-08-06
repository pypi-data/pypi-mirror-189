from FNLP.Regex import Re as Regex
from F import LIST
from F import DICT
from F import LOG
from pyFongo import UserRequest, CommandEngine
from FCM.Jarticle.jProvider import jPro

Log = LOG.Log("SearchArticles")

WELCOME = f"\n{LOG.HEADER}Welcome to pyFongo Command Line!"
PYMONGO_INPUT = f"{LOG.HEADER}MongoDB@pyFongo -> "
ENTER_SEARCH = "Enter Search Term: "
SEARCHING = lambda search_term: f"Searching for: [ {search_term} ]"
SEARCH_OPTIONS = "\nNo More Pages - 2. New Search - 3. Exit - 4. Back/Options\n"
OPTIONS = {"1. Search -> Search Article Database.": "handle_search_input",
           "X. Exit -> Quit pyFongo CLI": "killThySelf"}

db = jPro()

def handle_search_input(user_in, newPage=False, isFirst=False):
    if isFirst:
        request_user_search_query()
        return False
    if newPage and Regex.contains_any(["1", "next", "page"], user_in):
        return True
    if Regex.contains_any(["2", "new", "search"], user_in):
        request_user_search_query()
        return False
    if Regex.contains_any(["3", "exit", "quit"], user_in):
        exit()
    if Regex.contains_any(["4", "back", "options"], user_in):
        return False
    Log.cli("Bad Input. Restarting...")
    restart_search()

def restart_search():
    request_user_search_query()

def request_user_search_query():
    search_input = UserRequest.user_request(ENTER_SEARCH)
    search_commands = CommandEngine.parse_cli_commands(search_input)
    search_term = LIST.get(0, search_commands)
    filters = LIST.get(1, search_commands)
    perform_search(search_term, filters)

def search_loop(records):
    count = len(records)
    Log.cli(f"{count} Articles Found!")
    total_pages = int(count / 10)
    art_count = 1
    current_page = 0
    processing = True

    while processing:
        if current_page > total_pages:
            Log.cli(f"{LOG.HEADER}\nNo More Pages - 2. New Search - 3. Exit - 4. Back/Options")
            user_in = UserRequest.user_request(PYMONGO_INPUT)
            if not handle_search_input(user_in, False):
                return

        # -> Print Results
        Log.cli(f"Page {current_page + 1} of {total_pages}")
        page_records = get_page(records, current_page)
        for i in page_records:
            print_article(art_count, i)
            art_count += 1

        # -> Prepare for next input
        if current_page >= total_pages:
            Log.cli(f"{LOG.HEADER}\nNo More Pages - 2. New Search - 3. Exit - 4. Back/Options")
            user_in = UserRequest.user_request(PYMONGO_INPUT)
            if not handle_search_input(user_in, False):
                return
        else:
            Log.cli(f"{LOG.HEADER}\n1. Next Page - 2. New Search - 3. Exit - 4. Back/Options")
            user_in = UserRequest.user_request(PYMONGO_INPUT)
        if not handle_search_input(user_in, True):
            return
        current_page += 1

def perform_search(search_term, filters):
    Log.i(f"{SEARCHING(search_term=search_term)}")
    records = db.search_cli(search_term=search_term, filters=filters)
    if records:
        search_loop(records)
    else:
        Log.e("No Results Found.")
        request_user_search_query()

def get_page(records, page):
    end_temp = page + 1
    end = end_temp * 10
    start = page * 10
    return records[start:end]

def print_article(i, article):
    print("\n")
    print(f"{i}.", str(DICT.get("title", article)))
    print(f"Category:", str(DICT.get("category", article)))
    print(f"Score:", str(DICT.get("score", article)))
    print(f"URL:", str(DICT.get("url", article)))
    # print("\n")