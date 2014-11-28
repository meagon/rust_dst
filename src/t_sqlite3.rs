extern crate time;
extern crate sqlite3;

use time::Timespec;


use sqlite3::{
    DatabaseConnection,
    DatabaseUpdate,
    Query,
    ResultRowAccess,
    SqliteResult,
};

#[deriving(Show)]
struct Person {
    id: i32,
    name: String,
    // time_created: time::Timespec,
    // TODO: data: Option<Vec<u8>>
}

pub fn main() {
    match io() {
        Ok(ppl) => println!("Found people: {}", ppl),
        Err(oops) => panic!(oops)
    }
}

fn io() -> SqliteResult<Vec<Person>> {
    let mut conn = (DatabaseConnection::in_memory());

    try!(conn.exec("CREATE TABLE person (
                 id              SERIAL PRIMARY KEY,
                 name            VARCHAR NOT NULL,
               )"));

    let me = Person {
        id: 0,
        name: "Dan".to_string(),
    //    time_created: time::get_time(),
    };
    {
        let mut tx = try!(conn.prepare("INSERT INTO person (name,) 
                           VALUES ($1, )"));
        let changes = try!(conn.update(&mut tx, &[&me.name, ]));
        assert_eq!(changes, 1);
    }

    let mut stmt = try!(conn.prepare("SELECT id, name FROM person"));

    let mut ppl = vec!();
    try!(stmt.query(
        &[], |row| {
            ppl.push(Person {
                id: row.get("id"),
                name: row.get("name"),
            });
            Ok(())
        }));
    Ok(ppl)
}
