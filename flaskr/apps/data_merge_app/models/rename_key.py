def rename_sc_data_keys(dict_row: dict[str, str]) -> dict[str, str]:
    rename_dict_row: dict[str, str] = dict()
    for key, value in dict_row.items():
        key = key.replace("q", "sc")
        rename_dict_row[key] = value
    return rename_dict_row
