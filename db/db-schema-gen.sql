--- assumes PostgressSQL DB

CREATE TABLE IF NOT EXISTS MUSHROOMS
          (cap_shape                            TEXT,
          cap_color TEXT                        TEXT,
          odor TEXT                             TEXT,
          gill_size TEXT                        TEXT,
          gill_color TEXT                       TEXT,
          stalk_color_above_ring TEXT           TEXT,
          veil_color TEXT                       TEXT,
          ring_type TEXT                        TEXT,
          spore_print_color                     TEXT,
          population                            TEXT,
          habitat                               TEXT,
          lat                                   REAL,
          lon                                   REAL,
          Time                                  TIME);