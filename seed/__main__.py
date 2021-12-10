import re

from sqlmodel import Session, select

from nepali_dictionary.common.db import Dictionary, engine


def seed_data(filename):
    with Session(engine) as session:
        PRG = re.compile("(.*\s),\s(.*)\s,(.*)")
        with open(filename, "r") as fp:
            for line in fp.readlines():
                m = PRG.match(line)
                if not m:
                    continue
                word, kind, meaning = m.group(1).strip(), m.group(
                    2).strip(), m.group(3).strip()
                dictWord = Dictionary(word=word, kind=kind, meaning=meaning)
                session.add(dictWord)
            session.commit()

if __name__ == "__main__":
    seed_data("seed/data.csv")
