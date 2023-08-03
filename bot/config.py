import environ


class Config:

    API_ID = int(environ.get("API_ID", "26305247"))
    API_HASH = environ.get("API_HASH", "20ca7e6687c281e11782856c7efd0ff7")
    BOT_TOKEN = environ.get("BOT_TOKEN", "5857392333:AAFVRsfpEokq1bvGXsgdraFh2lf2Q8MqH20")
    SESSION_NAME = environ.get("SESSION_NAME", "memory")
    LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1001732446845"))
    DATABASE_URL = environ.get("DATABASE_URL", "mongodb+srv://sonukumarkrbbu61:52EO6iqQL1diHODm@db.op4pluq.mongodb.net/?retryWrites=true&w=majority")
    AUTH_USERS = [int(i) for i in environ.get("AUTH_USERS", "5791145987").split(" ")]
    MAX_PROCESSES_PER_USER = int(environ.get("MAX_PROCESSES_PER_USER", 2))
    MAX_TRIM_DURATION = int(environ.get("MAX_TRIM_DURATION", 600))
    TRACK_CHANNEL = int(environ.get("TRACK_CHANNEL", -1001732446845))
    SLOW_SPEED_DELAY = int(environ.get("SLOW_SPEED_DELAY", 5))
    HOST = environ.get("HOST", "")
    TIMEOUT = int(environ.get("TIMEOUT", 60 * 30))
    DEBUG = bool(environ.get("DEBUG"))
    WORKER_COUNT = int(environ.get("WORKER_COUNT", 20))
    IAM_HEADER = environ.get("IAM_HEADER", "")

    COLORS = [
        "white",
        "black",
        "red",
        "blue",
        "green",
        "yellow",
        "orange",
        "purple",
        "brown",
        "gold",
        "silver",
        "pink",
    ]
    FONT_SIZES_NAME = ["Small", "Medium", "Large"]
    FONT_SIZES = [30, 40, 50]
    POSITIONS = [
        "Top Left",
        "Top Center",
        "Top Right",
        "Center Left",
        "Centered",
        "Center Right",
        "Bottom Left",
        "Bottom Center",
        "Bottom Right",
    ]
