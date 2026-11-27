def student_details(**kwargs):  # **kwargs
    for key, value in kwargs.items():
        print(f"{key}: {value}")


student_details(name="Anu", maths=85, science=90)  # e.g. Anu, 85, 90