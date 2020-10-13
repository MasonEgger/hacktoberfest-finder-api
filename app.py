from flask import Flask, jsonify
from github import Github
from github.GithubException import RateLimitExceededException
import os
import time

app = Flask(__name__)


@app.route("/")
def hello_world():
    repos_list = {}
    g = Github(os.getenv("GITHUB_ACCESS_TOKEN", None))
    repos = g.search_repositories(query="topic:hacktoberfest")
    it = iter(repos)
    while True:
        try:
            val = next(it)
        except RateLimitExceededException:
            print("HOLD ON THERE!")
            time.sleep(60)
            print("HERE WE GO!")
        except StopIteration:
            print("KABOOM!")
            break
        print(val)

    return jsonify(repos_list)
