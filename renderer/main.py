from argparse import ArgumentParser

from render import finder_render

def main():
    parser = ArgumentParser(description="Turns Finder to a web browser.")
    parser.add_argument(
        "url",
        type=str,
        help="The URL to open."
    )
    args = parser.parse_args()
    
    finder_render()

if __name__ == "__main__":
    main()
