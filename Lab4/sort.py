import json

print(
    "Interface Status\n"
    "================================================================================\n"
    "DN                                                 Description           Speed    MTU\n"
    "-------------------------------------------------- --------------------  ------  ------"
)

with open("sample-data.json", "r") as info:
    info = json.load(info)

    for i in info['imdata']:
        print(i["l1PhysIf"]["attributes"]["dn"], "\t",
              i["l1PhysIf"]["attributes"]["descr"], "\t\t\t",
              i["l1PhysIf"]["attributes"]["speed"], "",
              i["l1PhysIf"]["attributes"]["mtu"]
              )