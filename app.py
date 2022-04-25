from django.shortcuts import render
from flask import Flask, jsonify, request, render_template
import sqlite3
import database
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recipes')
def recipePage():
    return render_template('recipes.html')

@app.route('/createRecipe/')
def createRecipe():
    return "Hello"