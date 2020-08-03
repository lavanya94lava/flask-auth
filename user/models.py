from flask import Flask, jsonify

class User:
    def signup(self):
        print("jiiiiii")
        user = {
            "_id":"",
            "name":"",
            "email":"",
            "password":""
        }

        return jsonify(user), 200