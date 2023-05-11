class RecordReader:

    def __init__(self, description: str) -> None:
        self.description = description

    def __str__(self) -> str:
        return f"{self.__class__}: {self.description}"

    def file_reader(file_name: str) -> dict:

        addr_hash = {}

        f = None
        try:

            f = open(file_name, "r")

            index = 0
            name = ""
            addr = ""
            for each_line in f.readlines():

                if not len(each_line.strip()):  # skip empty record separating linesßßß
                    continue
                else:
                    if index % 2 == 0:
                        name = each_line.strip()
                    elif index % 2 == 1:
                        addr = each_line.strip()

                    # create key/value pair after the addr entry of each record
                    if index % 2 == 1 and name in addr_hash:
                        addr_hash[name].append(addr)
                    elif index % 2 == 1:
                        addr_hash[name] = []
                        addr_hash[name].append(addr)

                    index += 1

            return addr_hash

        except IOError as e:
            print(e)

        finally:
            f.close()


def main() -> None:

    r_obj = RecordReader("Reads Address Records")
    print(r_obj)

    r = RecordReader.file_reader("addr_data/addr_data.txt")
    print(r['\"Joseph Biden\"'])
    print(r['\"Donald Trump\"'])
    print(r['\"Barak Obama\"'])

    for k, v in r.items():
        print(f"{k} => {v}")


if __name__ == '__main__':
    main()
