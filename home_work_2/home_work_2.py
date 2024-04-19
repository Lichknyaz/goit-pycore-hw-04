def get_cats_info(path):
    try:
        with open (path, "r", encoding="utf-8") as fh:
            list_of_cats = []
            for rows in fh.readlines():
                cats_info = {"id": rows.strip().split(",")[0],
                            "name": rows.strip().split(",")[1],
                            "age": rows.strip().split(",")[2]}
                list_of_cats.append(cats_info)
            return list_of_cats
    except FileNotFoundError:
        print("File not found")
        return None
    except Exception as e:
        print (f"Error: {e}")
        return None
print(get_cats_info("home_work_2\cats_file.txt"))