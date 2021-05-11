#! /usr/bin/env python

import attemdants
import emergency
import employees
    

def main():
    t1 = employees.Employees()

    t1.insert(
        "1",
        "islam",
        "kard",
        "ibr",
        "m",
        "post1"
    )

    t1.update_by_id(
        "1",
        "bb",
        "cc",
        "ff",
        "G",
        "post2"
    )

    print(t1.select_by_id("1"))
    t1.remove_by_id("1")
    print(t1.select_all_records())


if __name__ == "__main__":
    main()
