"""Minimal example for StepCounter."""

from stepcounter import stepcounter


def main():
 runner = stepcounter({"name": "StepCounter", "dry_run": False})
 result = runner.execute()
 print(result)


if __name__ == "__main__":
 main()