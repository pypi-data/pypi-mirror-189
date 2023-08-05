from __future__ import annotations

import argparse
import math
import subprocess
import os
import platform

import privateprefs.core.database as _db


def _save_cli(key: str, value: str, group: None | str) -> None:
    """
    Saves the value for a given key.
    :param key: A unique key to write the value under
    :param value: The value to save into persistent storage
    :param group: The group name to save the key-value pair under
    :return: None
    """
    if group is None:
        group = _db.DEFAULT_GROUP_NAME

    _db.write(key, value, group)
    print(f"saved: '{value}' to group: '{group}'")


def _load_cli(key: str, group: None | str) -> None:
    """
    Loads and returns the value for a given key
    :param key: A key to read the value of
    :type group: The group name to load the key-value pair from
    :return: None
    """
    if group is None:
        group = _db.DEFAULT_GROUP_NAME

    value = _db.read(key, group)
    print(f"loaded value: '{value}'")


def _delete_cli(key: str, group: None | str) -> None:
    """
    Delete a key-value pair for the given key.
    :param key: The key to delete the value of
    type group: The group name to delete the key-value pair from
    :return: None
    """
    print(f"deleted value: '{_db.read(key)}'")
    _db.delete(key, group)


def _delete_group_cli(group: str) -> None:
    """
    Delete all stored key-value pairs in the given group.
    :return: None
    """
    _db.delete_group(group)
    print(f"deleted group: '{group}'")


def _data_cli() -> None:
    """
    Displays a table of all data (saved key-value pairs).
    :return: None
    """
    print_key_value_table()


def _open_cli() -> None:
    """
    Displays a table of all saved key-value pairs.
    :return: None
    """

    did_open_file = _open_file_with_application(_db.PATH_TO_DATA_FILE)
    if did_open_file:
        print()
        print("opened data.ini file in default application")
        print()
    else:
        print()
        print("sorry, could not open the file on you operating system")
        print("you can navigate to the file pate manually and open it at:")
        print(_db.PATH_TO_DATA_FILE)
        print()


def _pre_uninstall_cli() -> None:
    """
    Removes all persistent files and folders created by this package.
    :return: None
    """
    _db.pre_uninstall()
    print()
    print(f"removed all persistent files and folders created by this package")
    print(f"to uninstall this package run:")
    print(f"pip uninstall privateprefs")
    print()


def _privateprefs_cli() -> None:
    print()
    print("Thanks for using Private Prefs!")
    print()
    print("for help run:")
    print("    privateprefs -h")
    print()
    print("or visit:")
    print("    https://github.com/DarrenHaba/privateprefs#readme")
    print()


def print_key_value_table() -> None:
    """
    Prints out a table of all saved data (key-value pairs).
    :return: None
    """
    # CAUTION - ugly code ahead!
    print()
    print(f"key-value data pairs are stored in the data.ini file located at:")
    print(_db.PATH_TO_DATA_FILE)
    print()
    groups = _db.read_groups()

    print("data.ini file contents:")
    for group in groups.keys():
        key_value_pairs = groups[group]
        group_printout = f"GROUP: [{group}]"
        if len(key_value_pairs) > 0:
            max_len_key = max(len(x) for x in key_value_pairs.keys())
            max_len_value = max(len(x) for x in key_value_pairs.values())
            max_len_key = max(max_len_key, 10)
            max_len_value = max(max_len_value, 10)
            is_group_test_longer_the_table = (max_len_key + max_len_value) < len(group_printout)
            if is_group_test_longer_the_table:
                amount_over = len(group_printout) - (max_len_key + max_len_value)
                half_amount_over = math.ceil(amount_over / 2)
                max_len_key += half_amount_over
                max_len_value += half_amount_over

        else:
            max_len_key = 10
            max_len_value = 11
            key_value_pairs["   ...   "] = "    ...   "
            print("- no key-value pairs saved -".lower())

        key_blank = "-" * max_len_key
        value_blank = "-" * max_len_value

        key_header_centered = f'{"KEY":^{max_len_key}s}'
        value_header_centered = f'{"VALUE":^{max_len_value}s}'
        value_group_centered = f'{group_printout:^{max_len_value + max_len_key + 3}s}'
        print(f"+-{key_blank}-+-{value_blank}-+")
        print(f"| {value_group_centered} |")
        print(f"+-{key_blank}-+-{value_blank}-+")
        print(f"| {key_header_centered} | {value_header_centered} |")

        print(f"+-{key_blank}-+-{value_blank}-+")

        for key, val in key_value_pairs.items():
            key = key.ljust(max_len_key)
            val = val.ljust(max_len_value)
            print(f"| {key} | {val} |")

        print(f"+-{key_blank}-+-{value_blank}-+")
        print()


def _open_file_with_application(file_path: str):
    """
    Opens a file using the default application associated with the file type, like double-clicking on
    the file to open it.
    :return: true if the open file command get called, else false
    """
    is_mac = platform.system() == 'Darwin'
    is_windows = platform.system() == 'Windows'
    is_linux = platform.system() == 'Linux'

    if is_mac:
        subprocess.call(('open', file_path))
        return True
    if is_windows:
        os.startfile(file_path)
        return True
    if is_linux:
        subprocess.call(('xdg-open', file_path))
        return True
    return False


def main(argv=None) -> None:
    """
    This main function is the entry point for our CLI in our package.

    In the project.toml file under [project.scripts] is a line code that invokes
    this method. This method instantiate argparse and instantiates sub-commands
    then dynamically calls the function associated with the subcommand been called.
    :param argv: Injected arguments when running unit tests, and None when cli used
    from the command line
    :return: None
    """

    # Instantiate argparse and a subparsers
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subparser')

    # To make argparse sub-parsers easier to deal with, we set up one function per subparsers.

    # The PrivatePrefs sub-parsers.
    # A function called '__cli' will be dynamically called
    # when the '' (privateprefs with no command) command is invoked
    subparsers.add_parser("")

    # The Save sub-parsers.
    # A function called '_save_cli' will be dynamically called when the 'save' command is invoked
    parser_save = subparsers.add_parser("save")
    parser_save.add_argument("key")
    parser_save.add_argument("value")
    parser_save.add_argument("-g", "--group", dest='group')

    # The Load sub-parsers.
    # A function called '_load_cli' will be dynamically called when the 'load' command is invoked
    parser_load = subparsers.add_parser("load")
    parser_load.add_argument("key")
    parser_load.add_argument("-g", "--group", dest='group')

    # The Data sub-parsers.
    # A function called '_data_cli' will be dynamically called when the '_data_cli' command is invoked
    subparsers.add_parser("data")

    # The Open sub-parsers.
    # A function called '_open_cli' will be dynamically called when the 'open' command is invoked
    subparsers.add_parser("open")

    # The Delete sub-parsers.
    # A function called 'delete_' will be dynamically called when the 'delete' command is invoked
    parser_delete = subparsers.add_parser("delete")
    parser_delete.add_argument("key")
    parser_delete.add_argument("-g", "--group", dest="group")

    # The Delete_group sub-parsers.
    # A function called '_delete_group_cli' will be dynamically called when the 'delete_group' command is invoked
    parser_delete_group = subparsers.add_parser("delete_group")
    parser_delete_group.add_argument("group")

    # The Pre_Uninstall sub-parsers.
    # A function called '_pre_uninstall_cli' will be dynamically called when the 'pre_uninstall' command is invoked
    subparsers.add_parser("pre_uninstall")

    # Extract a dict containing the name of the sub processor invoked and its arguments
    kwargs = vars(parser.parse_args(argv))

    # Extract the name of the subcommand being invoked, note we pop/remove the subcommand name,
    # so now kwargs will be just the given arguments without the subcommand in the dict.
    func_name_to_call = kwargs.pop('subparser')  # will be: save, load, delete, etc.

    if func_name_to_call is None:
        #  'privateprefs' was called.
        func_name_to_call = "_privateprefs_cli"
    else:
        # A subcommand was called
        # Make the command name match the corresponding function
        # CLI functions start with an underscore and end with _cli, so we append it here.
        func_name_to_call = f"_{func_name_to_call}_cli"

    # We dynamically call the function from the globals namespace dictionary and pass in cli the arguments.
    globals()[func_name_to_call](**kwargs)


if __name__ == '__main__':
    main()
