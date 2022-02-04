import hashlib

from flask import Flask, request, jsonify
import boto3
from boto3.dynamodb.conditions import Key

app = Flask(__name__)

@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "GET":
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table("academia-backend")

        email = request.args.get("email")

        item_retrieved = table.get_item(Key={"PK": f"USERS#{email}", "SK": "#PROFILE"})

        if "Item" in item_retrieved.keys():
            return jsonify(item_retrieved), 200

        return jsonify({"error": "item not found"}), 404

    elif request.method == "POST":
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table("academia-backend")

        data = request.json

        table.put_item(
            Item={
                "PK": f"USERS#{data['email']}",
                "SK": "#PROFILE",
                "username": data["username"],
                "password": hashlib.sha512(data["password"].encode()).hexdigest(),
            }
        )

        item_created = table.get_item(Key={"PK": f"USERS#{data['email']}", "SK": "#PROFILE"})

        return jsonify(item_created), 201

@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table("academia-backend")

        data = request.json

        item_retrieved = table.get_item(Key={"PK": f"USERS#{data['email']}", "SK": "#PROFILE"})

        if "Item" not in item_retrieved.keys():
            return jsonify({"login": None}), 401

        password = hashlib.sha512(data["password"].encode()).hexdigest()

        if "password" in item_retrieved["Item"] and password == item_retrieved["Item"]["password"]:
            return jsonify({"login": True}), 200

        return jsonify({"login": False}), 403
