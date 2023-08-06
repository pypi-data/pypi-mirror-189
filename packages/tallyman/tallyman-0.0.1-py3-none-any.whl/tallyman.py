import csv
import datetime
import os
import shutil

import yaml

from logcfg import logger


def scan_folder(rule_name: str, src_root_path: str, des_root_path: str, words, extensions):
    """

    :param rule_name: rule name
    :param src_root_path: Absolute Path
    :param des_root_path: Absolute Path
    :param words: key words list
    :param extensions: file extension list
    :return:
    """

    logger.debug(f"words:{words}, extensions:{extensions}")

    res = []

    if not os.path.exists(src_root_path):
        return res

    for root, dirs, files in os.walk(src_root_path):
        for filename in files:

            contain_word = False
            contain_ext = False
            base_name, ext_name = os.path.splitext(filename)
            if ext_name in extensions:
                contain_ext = True
            if words:
                for word in words:
                    if str(word) in base_name:
                        contain_word = True
                        break
            else:
                contain_word = True
            if contain_word and contain_ext:
                src_filepath = os.path.join(root, filename)
                des_filepath = os.path.join(des_root_path, filename)
                res.append({"rule": rule_name, "source": src_filepath, "target": des_filepath, "confirm": 1})

    return res


class TallyMan:

    def scan(self, config_filepath: str, output_filename=None) -> str:
        """

        :param config_filepath:
        :param output_filename:
        :return:
        """

        with open(config_filepath, encoding='utf8') as f:
            config = yaml.safe_load(f)

        rows = []

        src_folders = config["scan_root"]
        target_root = config["target_root"]

        for rule in config["rules"]:
            if rule["enabled"]:
                name = rule["name"]

                contains = rule.get("contain", [])
                extension = rule["extension"]
                target_folder = rule["target_folder"]
                target_folder = os.path.join(target_root, target_folder)

                for src_folder in src_folders:
                    logger.info(f"Scanning {src_folder}")
                    files = scan_folder(name, src_folder, target_folder, contains, extension)
                    if files:
                        rows.append(files)

        csv_folder_path = os.path.dirname(config_filepath)
        if not output_filename:
            output_filename = datetime.datetime.today().strftime("%Y%m%d-%H%M%S") + '.csv'
        csv_file_path = os.path.join(csv_folder_path, output_filename)

        fnames = ["rule", "source", "target", "confirm"]
        with open(csv_file_path, 'a+', newline='\n') as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=fnames)
            csv_writer.writeheader()
            for row in rows:
                csv_writer.writerows(row)
        return csv_file_path

    def organize(self, csv_file_path: str):
        """

        :param csv_file_path:
        :return:
        """
        if not os.path.exists(csv_file_path):
            raise FileNotFoundError(f"Can not found {csv_file_path}")

        with open(csv_file_path, 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                if int(row["confirm"]) == 1:
                    src_file_path = row["source"]
                    des_file_path = row["target"]

                    des_folder_path = os.path.dirname(des_file_path)
                    if not os.path.exists(des_folder_path):
                        os.makedirs(des_folder_path)

                    if not os.path.exists(des_file_path):
                        shutil.move(src_file_path, des_file_path)
                        logger.info(f"Moved {src_file_path} to {des_file_path}")
                    else:
                        logger.warning(f"{des_file_path} Existed, Skip")
