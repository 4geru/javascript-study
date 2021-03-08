// An attribute to hide warnings for unused code.
// 使用されていないコードよる警告を隠すアトリビュート
#![allow(dead_code)]

enum User {
    Name,
}

enum Status {
    Rich,
    Poor,
}

enum Work {
    Civilian,
    Soldier,
}

fn main() {
    // Explicitly `use` each name so they are available without
    // `use`することで絶対名でなくとも使用可能になる。
    // manual scoping.
    use crate::Status::{Poor, Rich};
    // Automatically `use` each name inside `Work`.
    // `Work`の中の名前をすべて`use`する
    use crate::Work::*;

    use crate::User::Name;

    // Equivalent to `Status::Poor`.
    // `use`しているため、`Status::Poor`と書いていることに等しい
    let status = Poor;
    // Equivalent to `Work::Civilian`.
    // `Work::Civilian`に等しい
    let work = Civilian;

    let name = Name;

    match status {
        // Note the lack of scoping because of the explicit `use` above.
        // `use`しているのでスコープを明示していない
        Rich => println!("The rich have lots of money!"),
        Poor => println!("The poor have no money..."),
    }

    match work {
        // Note again the lack of scoping.
        // こちらも同じ
        Civilian => println!("Civilians work!"),
        Soldier  => println!("Soldiers fight!"),
    }
}
