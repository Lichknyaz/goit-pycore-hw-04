def total_salary(path):
    try:
        with open (path, "r", encoding="utf-8") as fh:
            number_of_emploees = 0
            total_salary = 0
            for rows in fh.readlines():
                # emploees_name = rows.strip().split(",")[0]
                emploees_salary = int(rows.strip().split(",")[1])
                number_of_emploees +=1
                total_salary += emploees_salary
                # print(emploees_name, emploees_salary)
            average_salary = total_salary / number_of_emploees
            return total_salary, round(average_salary, 2)
            # print(f"{total_salary}, {average_salary:.2f}")
    except FileNotFoundError:
        print("File not found")
        return None
    except Exception as e:
        print (f"Error: {e}")
        return None
print(total_salary("home_work_1\salary_file.txt"))