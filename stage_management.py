def stage_management():
    stageinput = input("What do you want? add/view/update/delete: ").lower()

    print(stageinput)
    if stageinput == "add":
        add()

    elif stageinput == "view":
        view()

    elif stageinput == "update":
        update()

    elif stageinput == "delete":
        delete()

    else:
        print("Please try again. You can only add, view, update or delete.")
        stage_management()

stage_management()