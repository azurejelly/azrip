from app import create
from app.utils import dependencies, device
from sys import exit
from dotenv import load_dotenv

load_dotenv()

result = dependencies.check_dependencies()
if result is not None:
    print(f"dependency check failed: {result}")
    print("azrip will now exit.")
    exit(1)

app = create()
device.watch()

if __name__ == '__main__':
    app.run(debug=True)
