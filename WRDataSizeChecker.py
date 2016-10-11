import os
import re
from os import listdir
from os.path import isfile, join, expandvars, expanduser
from datetime import datetime
import ConfigParser

import shutil

import sys
import platform

from windows_notification import WindowsBalloonTip

TEMPLATE_PREFIX = "WR_support_submission"
SUBMISSIONS = expanduser("~/.wrdatasizechecker")
CURRENT_FOLDER = None
OVERWRITE = False

def config_section_map(config, section):
    config_dict = {}
    options = config.options(section)
    for option in options:
        try:
            config_dict[option] = config.get(section, option)
        except Exception:
            print("exception on {0}!".format(option))
            config_dict[option] = None
    return config_dict


if __name__ == "__main__":
    if len(sys.argv) > 1:
        arguments = sys.argv[1:]
        if "--clean" in arguments or "-c" in arguments:
            OVERWRITE = True

    # determine if application is a script file or frozen exe
    if getattr(sys, 'frozen', False):
        CURRENT_FOLDER = os.path.dirname(sys.executable)
    else:
        CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))
    if not os.path.exists(SUBMISSIONS):
        os.makedirs(SUBMISSIONS)

    if not os.path.exists(SUBMISSIONS + "/config.ini") or OVERWRITE:
        shutil.copyfile(CURRENT_FOLDER + "/default_config.ini", SUBMISSIONS + "/config.ini")


    config = ConfigParser.ConfigParser()
    config.read(SUBMISSIONS + "/config.ini")
    user_config = config_section_map(config, "USER_CONFIG")
    wr_file_locations = config_section_map(config, "WR_FILE_LOCATIONS")
    mb_limit = float(user_config["mb_limit"])

    db_regx = re.compile(r"db\d*.db")
    num_regx = re.compile(r"\d+")
    total = 0
    labels = set()
    sizes = {}

    previous_submission_generations = [f for f in os.listdir(SUBMISSIONS) if f != ".gitkeep"]
    for f in previous_submission_generations:
        if TEMPLATE_PREFIX in f:
            os.remove("{0}/{1}".format(SUBMISSIONS, f))

    if "Windows-XP" not in platform.platform():
        wr_path = str(expandvars(wr_file_locations["wr_path"]))
    else:
        wr_path = wr_file_locations["wr_path_xp"]
    for f in listdir(wr_path):
        if isfile(join(wr_path, f)) and db_regx.match(f) is not None:
            size = os.path.getsize(join(wr_path, f)) / (float(1024) * float(1024))
            label = num_regx.search(f).group(0)
            total += size
            labels.add(label)
            sizes[label] = size

    if total > mb_limit:
        monitored_processes = set()
        used_index = set()
        process_regex = re.compile(r"(?<=Monitoring process).*")
        is_currently_monitored_regex = re.compile(r"\(\d+\)")

        for line in reversed(open(wr_path + wr_file_locations["log_file"]).readlines()):
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
                            "installation: {0}\n\nThanks,\n{1}".format(user_config["key_code"], user_config["name"])
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        with open("{0}/{1}_{2}.txt".format(SUBMISSIONS, TEMPLATE_PREFIX, current_time), "a") as f:
            f.write(message_template)

        w = WindowsBalloonTip()
        w.balloon_tip("WR database exceeded {0}MB limit".format(mb_limit), "Monitored database is currently at {0:.2f}MB".format(total),
                      CURRENT_FOLDER + "/python.ico")
