import os
import shutil


def organize_folder(folder):
    if not os.path.isdir(folder):
        return None

    count = 0

    for filename in os.listdir(folder):
        source = os.path.join(folder, filename)

        if not os.path.isfile(source):
            continue

        extension = os.path.splitext(filename)[1].lower().replace(".", "")

        if not extension:
            category = "Others"
        else:
            category = extension.upper()

        destination_folder = os.path.join(folder, category)
        os.makedirs(destination_folder, exist_ok=True)

        destination = os.path.join(destination_folder, filename)

        if source != destination:
            shutil.move(source, destination)
            count += 1

    return count
