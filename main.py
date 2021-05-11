#! /usr/bin/env python

import attemdants
import emergency
    

def main():
    t1 = emergency.Emergency()

    t1.insert(
        "1",
        "islam",
        "kard",
        "ibr",
        "type1",
        "100"
    )

    t1.update_by_id(
        "1",
        "bbb",
        "ccc",
        "fff",
        "type2",
        "200"
    )

    
    print(t1.select_by_id("1"))
    
    print(t1.select_all_records())

if __name__ == "__main__":
    main()
