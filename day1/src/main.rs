use std::{fs};
use std::str::FromStr;

fn read_input_file() -> String {
    fs::read_to_string("input.txt")
    .expect("File reading error")
    .parse()
    .expect("Can't parse file into string")
}

fn parse(input: String) -> Vec<i32> {
    let mut input = input
    .split("\n\n")
    .map(|s| s.lines())
    .map(|s| {s.map(|a| i32::from_str(a).unwrap())})
    .map(|s| s.sum::<i32>())
    .collect::<Vec<i32>>();

    input.sort_by(|a,b| b.cmp(a));

    input
}

fn main() {
    let res = parse(read_input_file());
    println!("Part 1: {}", res[0]);
    println!("Part 2: {}", res[0..3].iter().sum::<i32>());

}
