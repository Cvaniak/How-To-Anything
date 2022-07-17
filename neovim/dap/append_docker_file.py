import json
import yaml
import os
import sys

app_name = sys.argv[1]

with open("./docker-compose.yml") as file:
    documents_root = yaml.full_load(file)

documents = documents_root["services"][app_name]
documents["ports"].extend(["22:22", "5678:5678"])
documents["volumes"].append(f".:{os.getcwd()}")
documents["security_opt"] = "seccomp:unconfined"
documents["cap_add"] = "SYS_PTRACE"
documents["command"] = "./run-test.sh"

with open("./docker-compose.testing.yml", "w") as file:
    yaml.dump(documents_root, file, sort_keys=False)


with open("./example-dap-launch.json") as file:
    documents_root = json.load(file)
print(documents_root)

path_mappings = {"localRoot": os.getcwd(), "remoteRoot": os.getcwd()}
documents_root["configurations"][0]["pathMappings"].append(path_mappings)

with open("./dap-launch.json", "w") as file:
    json.dump(documents_root, file, sort_keys=False, indent=4)
