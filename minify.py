import os
import json

def main():
    cur_path = os.path.dirname(__file__)

    # Minify json
    with open("{}/img/comic_data.min.json".format(cur_path), "w") as wf:
        with open("{}/img/comic_data.json".format(cur_path), "r") as rf:
            wf.write(json.dumps(json.load(rf), separators=(',', ':')))

main()
