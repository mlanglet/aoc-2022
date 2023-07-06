use std::{collections::HashMap, fs};

fn main() {
    let content = get_content();
    let value_map_strategy_1 = HashMap::from([
        ("A X", 4),
        ("B X", 1),
        ("C X", 7),
        ("A Y", 8),
        ("B Y", 5),
        ("C Y", 2),
        ("A Z", 3),
        ("B Z", 9),
        ("C Z", 6),
    ]);

    let value_map_strategy_2 = HashMap::from([
        ("A X", 3),
        ("B X", 1),
        ("C X", 2),
        ("A Y", 4),
        ("B Y", 5),
        ("C Y", 6),
        ("A Z", 8),
        ("B Z", 9),
        ("C Z", 7),
    ]);

    println!(
        "The result for strategy one is {}",
        calculate_strategy_score(&content, value_map_strategy_1)
    );
    println!(
        "The result for strategy two is {}",
        calculate_strategy_score(&content, value_map_strategy_2)
    );
}

fn calculate_strategy_score(content: &str, value_map: HashMap<&str, i32>) -> i32 {
    let mut result: i32 = 0;
    for line in content.lines().into_iter() {
        result += value_map.get(line).unwrap();
    }

    result
}

fn get_content() -> String {
    let content = match fs::read_to_string("../../input/day2") {
        Ok(data) => data,
        Err(_) => panic!("Couldn't read the input data"),
    };

    content
}
