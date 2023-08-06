from random import randrange
from FNLP.Language import Utils, Words
from F import DICT
from FCM.FQ import Q
from FCM.Jarticle import JQ

DASH_MODE = False

COMMAND_DASH = "--"
SUB_SEARCH_COMMANDS = [ "--date", "--source", "--daysBack", "--title", "--url" ]
COMMANDS = { "--search": SUB_SEARCH_COMMANDS }

def parse_commands(mess: str):
    newMess = mess.split(" ")
    commands = {}
    notFirst = False
    directory_command = ""
    input_commands = ""
    count = 0
    lastItem = len(newMess) - 1
    for item in newMess:
        if item.startswith("--"):
            if notFirst:
                commands[directory_command] = input_commands
            directory_command = item
            input_commands = ""
            count += 1
        else:
            input_commands = Utils.combine_args_str(input_commands, item)
            notFirst = True
            count += 1
        if count >= lastItem:
            commands[directory_command] = input_commands
    return commands

def parse_cli_commands(mess: str) -> (str, dict):
    """ apple airpods --date march 22 2022"""
    #matterport --gte March 01 2022 --lte July 22 2022
    tokenized_message = mess.split(" ")
    filter_commands = {}
    directory_command = ""
    lastItem = len(tokenized_message) - 1
    i = 0
    gte = None
    lte = None
    while i < lastItem:
        word = tokenized_message[i]
        if word.startswith("--"):
            # this is a filter
            filter_command = word.replace("--", "")
            input_commands = ""
            for inner_item in tokenized_message[i+1:]:
                if inner_item.startswith("--"):
                    break
                input_commands = Words.combine_words(input_commands, inner_item)
                i += 1

            if filter_command == "pub_date" or filter_command == 'gte' or filter_command == 'lte':
                if filter_command == 'gte':
                    gte = input_commands
                elif filter_command == 'lte':
                    lte = input_commands
                if gte and lte:
                    filter_command = "pub_date"
                    input_commands = JQ.DATE_RANGE_CLI(gte=gte, lte=lte)
                    i += 1
                else:
                    i += 1
                    continue


            filter_commands[filter_command] = input_commands
            continue
        else:
            directory_command = Words.combine_words(directory_command, word)
            i += 1
    if not directory_command:
        directory_command = mess
    return directory_command, filter_commands

parse_cli_commands("matterport --gte March 01 2022 --lte July 22 2022")

def build_query(search_term, filters):
    sq = JQ.SEARCH_ALL(search_term=search_term)
    if not filters:
        return sq
    or_list = [sq]
    for key_filter in filters:
        filter_value = filters[key_filter]
        final_key_filter = key_filter.replace("--", "")
        if final_key_filter == "date":
            temp_qeury = JQ.DATE(filter_value)
        else:
            temp_qeury = Q.BASE(final_key_filter, filter_value)
        or_list.append(temp_qeury)
    final_query = Q.AND(or_list)
    return final_query


if __name__ == '__main__':
    coms = "matterport --date March 22 2022 --source reddit"
    # setest = JQ.SEARCH_ALL("matterport")
    # dtest = {"published_date": "March 22 2022"}
    # stest = {"source": "reddit"}
    # matchStage = AO.MATCH(Q.AND([setest, dtest, stest]))
    # limitStage = AO.LIMIT(100)
    # pipeline = Pipelines.builder(matchStage, limitStage)
    # parsed = parse_cli_commands(coms)
    # searchTerm = LIST.get(0, parsed, False)
    # filters = LIST.get(1, parsed, False)
    # bq = build_query(search_term=searchTerm, filters=filters)

def get_filters(directory_command, commands):
    return DICT.remove_key_value(directory_command, commands)

def get_search_commands():
    phrase = "<search phrase>"
    n = "\n"
    args = []
    args.append(f"{n} Welcome to Tiffany Help Assistant!{n}")
    args.append(f"{n} Ex: --search: Apple Airpods{n}")
    args.append(f"{n} '--FILTER' --date March 22 2022.{n}")
    args.append(f"{n} Ex: --search Apple Airpods --date March 22 2022{n}")
    args.append(f"{n}1) --search: {phrase} {n} -> Search Everything.")
    args.append(f"{n}2) --search --date March 22 2022 {phrase} {n} -> Search Specific Date Only ")
    # args.append(f"{n}3) --search --date March 22 2022 --daysBack 10 {phrase} {n} -> Search Date Range back.")
    # args.append(f"{n}4) --search --source True {phrase} {n} -> Search by Source of Article Only.")
    result = ""
    for arg in args:
        result = Utils.combine_args_str(result, arg)
    return result

def package_results(results):
    saved = []
    packaged_string = f"Found: {len(results)} Articles\n"
    for i in range(5):
        if i > len(results) - 1:
            return packaged_string
        indexPick = randrange(len(results))
        record = results[indexPick]
        title = DICT.get("title", record)
        url = DICT.get("url", record)
        if url in saved:
            continue
        saved.append(url)
        packaged_string += f"\n{i + 1}. {title} \n {url}\n"
    return packaged_string

def get_article_count(db):
    return f"Articles in Database: {db.get_document_count()}"