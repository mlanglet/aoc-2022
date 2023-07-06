use std::{collections::HashSet, fs, time::Instant};

fn main() {
    let t0 = Instant::now();

    let content = get_content();

    let prio_values: Vec<char> = ('a'..='z')
        .into_iter()
        .chain(('A'..='Z').into_iter())
        .collect();

    println!(
        "The sum of priorities for backpack sorting is {}",
        part_one(&content, &prio_values)
    );

    println!(
        "The sum of priorities for badge authentication is {}",
        part_two(&content, &prio_values)
    );

    println!("The elapsed time is {}", t0.elapsed().as_nanos());
}

fn part_one(content: &str, prio_values: &Vec<char>) -> usize {
    let mut prio_sum = 0;
    for backpack in content.lines().into_iter() {
        let middle: usize = backpack.len() / 2;
        let compartment1: HashSet<char> = backpack[0..middle].chars().collect();
        let compartment2: HashSet<char> = backpack[middle..backpack.len()].chars().collect();
        let mut common_letter = compartment1.intersection(&compartment2);
        prio_sum += get_priority_value(common_letter.nth(0).unwrap(), &prio_values);
    }
    prio_sum
}

fn part_two(content: &str, prio_values: &Vec<char>) -> usize {
    let mut prio_sum = 0;
    let mut items = Vec::new();
    for backpack in content.lines().into_iter() {
        if items.len() == 3 {
            prio_sum += calculate_intersecting_priority_value(&mut items, &prio_values);
        }
        items.push(backpack);
    }
    prio_sum += calculate_intersecting_priority_value(&mut items, &prio_values);

    prio_sum
}

fn calculate_intersecting_priority_value(items: &mut Vec<&str>, prio_values: &Vec<char>) -> usize {
    let set1: HashSet<char> = items.pop().unwrap().chars().collect();
    let set2: HashSet<char> = items.pop().unwrap().chars().collect();
    let set3: HashSet<char> = items.pop().unwrap().chars().collect();
    let common_letters: HashSet<char> = set1.intersection(&set2).cloned().collect();
    let mut common_letters = common_letters.intersection(&set3);

    get_priority_value(common_letters.nth(0).unwrap(), prio_values)
}

fn get_priority_value(letter: &char, values: &Vec<char>) -> usize {
    for (i, v) in values.iter().enumerate() {
        if v == letter {
            return i + 1;
        }
    }
    0
}

fn get_content() -> String {
    let content = match fs::read_to_string("../../input/day3") {
        Ok(data) => data,
        Err(_) => panic!("Couldn't read the input data"),
    };

    content
}
