#!/usr/bin/python3
"""Module that fetches and processes posts from JSONPlaceholder."""
import csv
import requests


def fetch_and_print_posts():
    """Fetch all posts from JSONPlaceholder and print their titles.

    Prints the response status code, and on success prints the title of
    every post returned by the API.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetch all posts from JSONPlaceholder and save them to posts.csv.

    On a successful request, the posts are structured into a list of
    dictionaries with the keys id, title, and body, and written to a CSV
    file named posts.csv.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        data = [
            {"id": post.get("id"),
             "title": post.get("title"),
             "body": post.get("body")}
            for post in posts
        ]
        fieldnames = ["id", "title", "body"]
        with open("posts.csv", "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
