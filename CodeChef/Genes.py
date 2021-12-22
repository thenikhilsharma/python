t = int(input())
for tc in range(t):
    n = int(input())
    binary = [1,0]
    def addCheck(binary, n, app):
        if len(binary) == n: return binary
        else:
            binary.append(app)
            binaryreverse = binary
            binaryreverse.reverse()
            print(binary, binaryreverse)
            for i in range(len(binary)):
                if binary[i] != binaryreverse[i]:
                    continue
                else:
                    binary[len(binary)-1] = 0
                    return addCheck(binary, n, 1)
            return addCheck(binary, n, 1)
    y = addCheck(binary, n, 1)
    print(y)