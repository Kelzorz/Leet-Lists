from flask import Flask, jsonify
import socket

from LeetLists import LeetLists

app = Flask(__name__)
ll = LeetLists()
wordlist = []
try:
	with open("badwords.txt") as badwords:
		wordlist = badwords.readlines()
except Exception as e:
	print("Unalbe to load wordlist...")
	exit()
for i in range(len(wordlist)):
	wordlist[i] = wordlist[i].strip()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = str(s.getsockname()[0])
s.close()
del s

@app.route("/")
def sixtyNine():
	return "Sex."

@app.route("/leetlists/<string>", methods=["GET"])
def process(string):
	string = str(string)
	return jsonify(ll.check_string(string, wordlist))

if __name__ == "__main__":
	app.run(host=ip, port=6969)