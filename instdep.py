#!/usr/bin/python
import fileinput
import subprocess

class client:


	def __init__(self, program_name): 
		self.program_name = program_name
		self.repositories = []
		self.args = []

	def add_arg (self, arg):
		self.args.append(arg)

	def add_repo (self, repo):
		self.repositories.append(repo)

	def verbose (self):
		print "list of commands:"
		for repo in self.repositories:
			print [self.program_name] + self.args + [repo]

	def execute(self):
		for repo in self.repositories:
			print [self.program_name] + self.args + [repo]			
			out = subprocess.check_output([self.program_name] + self.args + [repo])
			print out
if __name__ == "__main__":
	lines = []
	clients = []
	first = True

	for line in fileinput.input():

		stripped = line.strip()
		if stripped:
			if not stripped[0] == '#':
				if stripped[0] == '=':
					if first == False:
						clients.append(current_client)
					current_client = client(stripped[1:])
					first = False
				elif stripped[0] == '+':
					current_client.add_arg(stripped[1:])
				else:
					current_client.add_repo(stripped)
	clients.append(current_client)

	for cli in clients:
		cli.execute()
