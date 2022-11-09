import os
from flask import flask
from django.shortcuts import render
from .models import Post
from .forms import CommentForm


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codestar.settings')
    os.environ["DATABASE_URL"] = "Paste in Heroku DATABASE_URL Link"
    os.environ["SECRET_KEY"] = "hemlignyckel1500"


if __name__ == '__main__':
    main()
