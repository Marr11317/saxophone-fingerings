saxTransposition = {
    "soprano": 2,
    "alto": 9,
    "tenor": 14,
    "barytone": 21,
}

base_file = "sax_fingerings.qml"

code = ""
with open(base_file + ".template", "r") as file:
    code = file.read()

for key, value in saxTransposition.items():
    with open("../dist/" + key + "_" + base_file, "w") as file:
        file.write(code.replace("$INSTRUMENT$", key).replace(
            "$TRANSPOSITION$", str(value)))
