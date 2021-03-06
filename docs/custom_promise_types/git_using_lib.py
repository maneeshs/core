import sys
import os
from cfengine import PromiseModule, ValidationError


class GitPromiseTypeModule(PromiseModule):
    def validate_promise(self, promiser, attributes):
        if not promiser.startswith("/"):
            raise ValidationError(f"File path '{promiser}' must be absolute")
        for name, value in attributes.items():
            if name != "repo":
                raise ValidationError(f"Unknown attribute '{name}' for git promises")
            if name == "repo" and type(value) is not str:
                raise ValidationError(f"'repo' must be string for git promise types")

    def evaluate_promise(self, promiser, attributes):
        if not promiser.startswith("/"):
            raise ValidationError("File path must be absolute")

        folder = promiser
        url = attributes["repo"]

        if os.path.exists(folder):
            self.promise_kept()
            return

        self.log_info(f"Cloning '{url}' -> '{folder}'...")
        os.system(f"git clone {url} {folder} 2>/dev/null")

        if os.path.exists(folder):
            self.log_info(f"Successfully cloned '{url}' -> '{folder}'")
            self.promise_repaired()
        else:
            self.log_error(f"Failed to clone '{url}' -> '{folder}'")
            self.promise_not_kept()


if __name__ == "__main__":
    GitPromiseTypeModule().start()
