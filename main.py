import os
import re
from os import listdir
from os.path import isfile, join
from datetime import datetime

from config import NAME, KEY_CODE, WR_PATH, MB_LIMIT, LOG_FILE
from windows_notification import WindowsBalloonTip

SUBMISSIONS = os.path.dirname(os.path.realpath(__file__)) + "/submissions"

if __name__ == "__main__":
    db_regx = re.compile(r"db\d*.db")
    num_regx = re.compile(r"\d+")
    total = 0
    labels = set()
    sizes = {}

    previous_submission_generations = [f for f in os.listdir(SUBMISSIONS) if f != ".gitkeep"]
    for f in previous_submission_generations:
        os.remove("{0}/{1}".format(SUBMISSIONS, f))

    for f in listdir(WR_PATH):
        if isfile(join(WR_PATH, f)) and db_regx.match(f) is not None:
            size = os.path.getsize(join(WR_PATH, f)) / (float(1024) * float(1024))
            label = num_regx.search(f).group(0)
            total += size
            labels.add(label)
            sizes[label] = size

    if total > MB_LIMIT:
        monitored_processes = set()
        used_index = set()
        process_regex = re.compile(r"(?<=Monitoring process).*")
        is_currently_monitored_regex = re.compile(r"\(\d+\)")

        for line in reversed(open(LOG_FILE).readlines()):
            search = process_regex.search(line)
            if search is not None:
                process = search.group(0)
                label = is_currently_monitored_regex.search(process).group(0).strip("()")
                if label in labels and label not in used_index:
                    monitored_processes.add("db{0}.db".format(label) + "\t->".format(sizes[label]) + process)
                    used_index.add(label)

        message_template = "Good Day Support,\n\nI have a few processes that are being monitored and the WRData " \
                           "folder has become fairly large.\nIs it possible that these processes can be analysed " \
                           "in order to whitelist them if they are deemed safe?\n\n" \
                           "Here is the list of processes in my WRLog.log that are currently monitored:\n"
        for process in monitored_processes:
            message_template += "  - {0}\n".format(process)
        message_template += "\nThis is the keycode for my " \
                            "installation: {0}\n\nThanks,\n{1}".format(KEY_CODE, NAME)
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        with open("{0}/WR_support_submission_{1}.txt".format(SUBMISSIONS, current_time), "a") as f:
            f.write(message_template)

        w = WindowsBalloonTip()
        w.balloon_tip("WRData exceeded {0}MB limit".format(MB_LIMIT), "WRData is currently at {0:.2f}MB".format(total),
                      os.path.dirname(os.path.abspath(__file__)) + "/python.ico")


