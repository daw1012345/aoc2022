current_path, structure = [], {"/": 0}
for l in open("day7/input.txt", 'r').readlines():
    match l.strip().split(" "):
        case ["$", "cd", "/"]: current_path.clear()
        case ["$", "cd", ".."]:current_path.pop()
        case ["$", "ls"] | ["dir", *_]: pass
        case ["$", "cd", path]:
            current_path.append(path)
            structure["/" if not current_path else "/" + '/'.join(current_path)] = structure["/" if not current_path else "/" + '/'.join(current_path)] if ("/" if not current_path else "/" + '/'.join(current_path)) in structure.keys() else 0
        case [fsize, fname]:
            structure["/" if not current_path else "/" + '/'.join(current_path)] += int(fsize)
            for k in (x for x, _ in structure.items() if ("/" if not current_path else "/" + '/'.join(current_path)).startswith(x) and x != ("/" if not current_path else "/" + '/'.join(current_path))):
                structure[k] += int(fsize)
print(f"Part 1: {sum([x for x in structure.values() if x <= 100000])} Part 2: {min(filter(lambda x: 70000000 - structure['/'] + x >= 30000000 , list(structure.values())))}")