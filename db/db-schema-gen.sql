--- assumes PostgressSQL DB

CREATE TABLE IF NOT EXISTS MUSHROOMS
          (cap_shape                            TEXT,
          cap_color                             TEXT,
          odor                                  TEXT,
          gill_size                             TEXT,
          gill_color                            TEXT,
          stalk_color_above_ring                TEXT,
          veil_color                            TEXT,
          ring_type                             TEXT,
          spore_print_color                     TEXT,
          population                            TEXT,
          habitat                               TEXT,
          lat                                   REAL,
          lon                                   REAL,
          Time                                  TIME);