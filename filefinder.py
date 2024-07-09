file_system = [
    [
        "nothing.txt",
        "dog_pic.png",
        [
            "secret_plan.pdf"
        ]
    ],
    "notion.app",
    "slack.app",
    [
        "fun.txt",
        [
            "meaningless_file.txt",
            "chicken_dinner.txt"
        ],
        "not_fun.txt"
    ],
    "zoom.app"
]

target = "chicken_dinner.txt"

def filefinder(flist, currfile):
    if not flist:
        return "File not found."
    elif flist[0] == currfile:
        return "HOORAH!"
    elif isinstance(flist[0], list):    # Is there another folder we are entering?
        result = filefinder(flist[0], currfile)
        if result == "HOORAH!":
            return "HOORAH!"        # Can't really evaluate asking for "TRUE" because it's not returning TRUE, it returns "HOORAH!"...
    return filefinder(flist[1:], currfile)
    

print(filefinder(file_system, target))
