import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileMovedEvent

WATCH_DIR = "non_commit/rename_test"   # Need a search node
SCRIPT = "non_commit/test.py"   # Bash write with the url of the rename

class RenameHandler(FileSystemEventHandler):
    def on_moved(self, event):
        if not isinstance(event, FileMovedEvent):
            return
        old = event.src_path
        new = event.dest_path
        
        subprocess.run(["python3", SCRIPT, old, new])
        
        print(f"renamed: {old} -> {new}")

if __name__ == "__main__":
    obs = Observer()
    obs.schedule(RenameHandler(), str(WATCH_DIR), recursive=False)
    obs.start()
    try:
        obs.join()
    except KeyboardInterrupt:
        obs.stop()
        obs.join()

class State:
    def __init__(self, url:str="https://camhack.org") -> None:
        self.left: list[str] = []
        self.right: list[str] = []
        self.history: list[str] = []
        self.current: str = url
    
    def back(self):
        self.history.append(self.current)
        self.right.append(self.current)
        self.current = self.left.pop()
    
    def forward(self):
        self.history.append(self.current)
        self.left.append(self.current)
        self.current = self.right.pop()
    
    def update(self, url:str):
        self.history.append(self.current)
        self.left.append(self.current)
        self.current = url
        
        """
        NEED TO INTEGRATE CORRECTLY
        - Should have a left and history of recently visited websites and be able to hyperlink the left and right with the latest
        """