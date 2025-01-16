import os

def main():
  print("hello from github actions!")
  token = os.environ.get("AZURE_SECRET_TOKEN")
  if not token:
    raise RuntimeError("AZURE_SECRET_TOKEN is not set")
  print("All good - we found our env")

if __name__ == '__main__':
  main()
